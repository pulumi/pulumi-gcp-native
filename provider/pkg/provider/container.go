// Copyright 2016-2022, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package provider

import (
	"context"
	"fmt"
	"time"

	"github.com/pulumi/pulumi/pkg/v3/codegen"

	"github.com/jpillora/backoff"
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi-google-native/provider/pkg/resources"
	"github.com/pulumi/pulumi/sdk/v3/go/common/diag"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/contract"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/logging"
)

type nodepoolMutations struct {
	updateHandlers map[string]nodepoolUpdateHandlerFunc
}

func (n nodepoolMutations) mutablePropertyPaths() []string {
	return codegen.SortedKeys(n.updateHandlers)
}

func (n nodepoolMutations) update(
	providerInstance *googleCloudProvider,
	urn resource.URN,
	label string,
	res *resources.CloudAPIResource,
	inputs resource.PropertyMap,
	oldState resource.PropertyMap,
) (appliedInputs resource.PropertyMap, resp map[string]interface{}, err error) {
	// TODO wait for the cluster to be in resting state

	// Extract old inputs from the `__inputs` field of the old state.
	oldInputs := parseCheckpointObject(oldState)
	// Delete the auto-injected __autonamed tag in old and new inputs to avoid spurious diffs.
	if v, ok := oldInputs[autonamed]; ok && v.IsBool() {
		delete(oldInputs, autonamed)
	}

	if v, ok := inputs[autonamed]; ok && v.IsBool() {
		delete(inputs, autonamed)
	}

	diff := oldInputs.Diff(inputs)
	batchedInputs := resource.NewObjectProperty(oldInputs)

	if diff == nil {
		logging.V(9).Infof("[%s] no diff found in update!", label)
	} else {
		// Calculate the detailed diff object containing information about replacements.
		detailedDiff := calculateDetailedDiff(res, providerInstance.resourceMap.Types, diff)
		logging.V(9).Infof("[%s] detailedDiff: %+v", label, detailedDiff)
		logging.V(9).Infof("[%s] updateNodepool oldState: %+v", label, oldState)

		for _, key := range updateOrder {
			updateHandler, ok := n.updateHandlers[key]
			if !ok {
				logging.V(9).Infof("[%s] No handler found for field: %q", label, key)
				// TODO This should be an error once all the targetted mutations are in place!
				continue
			}
			logging.V(9).Infof("[%s] Invoking update for field: %q", label, key)
			for k := range detailedDiff {
				logging.V(9).Infof("[%s] processing diff on field: %q", label, k)
				var diffPropPath, propPath resource.PropertyPath
				diffPropPath, err = resource.ParsePropertyPath(k)
				if err != nil {
					err = fmt.Errorf("failed to parse property path: %q: %w", k, err)
					break
				}
				propPath, err = resource.ParsePropertyPath(key)
				if err != nil {
					err = fmt.Errorf("failed to parse property path: %q: %w", k, err)
					break
				}
				if propPath.Contains(diffPropPath) {
					_ = providerInstance.host.LogStatus(context.Background(), diag.Info, urn,
						fmt.Sprintf("Performing update for field: %q", key))
					logging.V(9).Infof("[%s] processing diff for %q with handler for %q",
						label, diffPropPath.String(), propPath.String())
					logging.V(9).Infof("[%s] waiting for nodepool to reach resting state", label)
					_, err = waitForNodepoolRestingState(providerInstance, urn, res, inputs, oldState)
					if err != nil {
						break
					}
					newVal, _ := diffPropPath.Get(resource.NewObjectProperty(inputs))
					logging.V(9).Infof("[%s] calling update handler", label)
					err = updateHandler(providerInstance, urn, label, res, inputs, oldState)
					if err != nil {
						logging.V(9).Infof("[%s] failure updating: %+v", label, err)
						break
					}
					batchedInputs, ok = diffPropPath.Add(batchedInputs, newVal)
					if !ok {
						err = fmt.Errorf("failed to record update at field: %q", k)
						break
					}
				}
			}
			if err != nil {
				break
			}
		}
	}
	appliedInputs = batchedInputs.ObjectValue()
	uri, readErr := res.Read.Endpoint.URI(inputs.Mappable(), oldState.Mappable())
	if readErr != nil {
		return nil, nil, readErr
	}
	resp, err2 := readNodepoolStatus(providerInstance, uri)
	if err2 != nil {
		logging.V(9).Infof("[%s] Failed to read nodepool status: %v", label, err2)
		return nil, nil, fmt.Errorf("failed to retrieve nodepool status: %v. Previous error: %w", err2, err)
	}

	return appliedInputs, resp, err
}

type nodepoolUpdateHandlerFunc func(
	p *googleCloudProvider,
	urn resource.URN,
	label string,
	res *resources.CloudAPIResource,
	newInputs,
	oldState resource.PropertyMap,
) error

var emptyObjVal = resource.NewObjectProperty(resource.NewPropertyMapFromMap(nil))
var emptyArrayVal = resource.NewArrayProperty([]resource.PropertyValue{})

type propValueIfMissingFunc func(oldState resource.PropertyMap, propPath resource.PropertyPath) resource.PropertyValue

func extractFromDefaults(valIfMissing resource.PropertyValue) propValueIfMissingFunc {
	return func(oldState resource.PropertyMap, propPath resource.PropertyPath) resource.PropertyValue {
		defaults := parseDefaultsObject(oldState)
		if val, ok := propPath.Get(resource.NewObjectProperty(defaults)); ok {
			return val
		}
		return valIfMissing
	}
}

func defaultValue(defVal resource.PropertyValue) propValueIfMissingFunc {
	return func(_ resource.PropertyMap, _ resource.PropertyPath) resource.PropertyValue {
		return defVal
	}
}

// Following an ordering here that the terraform provider performs updates in.
// We have a lot more mutations defined than the terraform providers does though.
var updateOrder = []string{
	"autoscaling",
	"config.imageType",
	"config.workloadMetadataConfig",
	"config.kubeletConfig",
	"config.linuxNodeConfig",
	"config.confidentialNodes",
	"config.gcfsConfig",
	"config.gvnic",
	"config.labels",
	"config.tags",
	"config.taints",
	"networkConfig",
	"initialNodeCount",
	"management",
	"version",
	"locations",
	"upgradeSettings"}

func mustParsePropertyPath(pattern string) resource.PropertyPath {
	pp, err := resource.ParsePropertyPath(pattern)
	contract.AssertNoError(err)
	return pp
}

func readNodepoolStatus(
	p *googleCloudProvider,
	uri string,
) (map[string]interface{}, error) {
	// Read the current state of the resource from the API.
	newState, err := retryRequest(p.client, "GET", uri, "", nil)
	if err != nil {
		return nil, fmt.Errorf("error fetching nodepool status: %w", err)
	}
	return newState, nil
}

func waitForNodepoolRestingState(
	p *googleCloudProvider,
	urn resource.URN,
	res *resources.CloudAPIResource,
	inputs,
	oldState resource.PropertyMap,
) (map[string]interface{}, error) {
	ctx, cancelFunc := context.WithTimeout(context.Background(), 15*time.Minute)
	defer cancelFunc()
	retryPolicy := backoff.Backoff{
		Min:    1 * time.Second,
		Max:    15 * time.Second,
		Factor: 1.5,
		Jitter: true,
	}

	uri, err := res.Read.Endpoint.URI(inputs.Mappable(), oldState.Mappable())
	if err != nil {
		return nil, err
	}

	for {
		resp, err := readNodepoolStatus(p, uri)
		if err != nil {
			return nil, err
		}

		status, hasStatus := resp["status"].(string)
		if hasStatus && isNodepoolInRestingStatus(status) {
			return resp, nil
		} else {
			_ = p.host.LogStatus(context.Background(), diag.Info, urn,
				fmt.Sprintf("Waiting for nodepool to reach resting state. "+
					"Current status: %q", status))
		}
		select {
		case <-time.After(retryPolicy.Duration()):
		case <-ctx.Done():
			return nil, fmt.Errorf("timeout polling for nodepool resting state: %q", uri)
		}
	}

}

func isNodepoolInRestingStatus(status string) bool {
	switch status {
	case "RUNNING", "RUNNING_WITH_ERROR", "ERROR":
		return true
	}
	return false
}

func updateNodePoolMapping(
	diffPropPath resource.PropertyPath,
	apiFieldName string,
	defaultIfMissing propValueIfMissingFunc,
	operationSuffix string,
	httpMethod string,
) nodepoolUpdateHandlerFunc {
	return func(p *googleCloudProvider,
		urn resource.URN,
		label string,
		res *resources.CloudAPIResource,
		newInputs,
		oldState resource.PropertyMap) error {
		endpoint := resources.CloudAPIEndpoint{
			Template: fmt.Sprintf(`https://container.googleapis.com/v1/`+
				`projects/{projectsId}/locations/{locationsId}/clusters/{clustersId}/nodePools/{nodePoolsId}%s`, operationSuffix),
			Values: append(res.Create.Endpoint.Values,
				resources.CloudAPIResourceParam{
					Name:    "nodePoolsId",
					SdkName: "name",
					Kind:    "path",
				}),
		}
		uri, err := endpoint.URI(newInputs.Mappable(), oldState.Mappable())
		if err != nil {
			return err
		}

		// If key is omitted, use default.
		_, ok := diffPropPath.Get(resource.NewObjectProperty(newInputs))
		if !ok {
			updated, _ := diffPropPath.Add(resource.NewObjectProperty(newInputs), defaultIfMissing(oldState, diffPropPath))
			newInputs = updated.ObjectValue()
		}

		body := p.prepareAPIInputs(newInputs, oldState, map[string]resources.CloudAPIProperty{
			apiFieldName: {SdkName: diffPropPath.String()},
		})
		op, err := retryRequest(p.client, httpMethod, uri, "", body)
		if err != nil {
			return fmt.Errorf("error sending request: %s: %q %+v", err, uri, body)
		}

		_, err = p.waitForResourceOpCompletion(urn, res.Update.CloudAPIOperation, op)
		if err != nil {
			return errors.Wrapf(err, "waiting for completion")
		}
		return nil
	}
}

func updateNodePoolConfig(diffPropPath, targetPropPath resource.PropertyPath,
	defaultIfMissing propValueIfMissingFunc) nodepoolUpdateHandlerFunc {
	return func(p *googleCloudProvider,
		urn resource.URN,
		label string,
		res *resources.CloudAPIResource,
		newInputs,
		oldState resource.PropertyMap) error {
		logging.V(9).Infof("[%s] updateNodePoolConfig called for property path: %q", label, diffPropPath.String())
		endpoint := resources.CloudAPIEndpoint{
			Template: `https://container.googleapis.com/v1/projects/{projectsId}/locations/{locationsId}/clusters/{clustersId}/nodePools/{nodePoolsId}`,
			Values: append(res.Create.Endpoint.Values,
				resources.CloudAPIResourceParam{
					Name:    "nodePoolsId",
					SdkName: "name",
					Kind:    "path",
				}),
		}
		uri, err := endpoint.URI(newInputs.Mappable(), oldState.Mappable())
		if err != nil {
			return err
		}
		// Get the new config object to copy the value for fieldName from
		newConfigField, ok := diffPropPath.Get(resource.NewObjectProperty(newInputs))
		if !ok {
			logging.V(9).Infof("[%s] no update found at path: %q. Assuming the field is deleted.", label,
				diffPropPath.String())
			newConfigField = defaultIfMissing(oldState, diffPropPath)
		}
		// Overwrite the config object where the one value for fieldName has been updated.
		newConfig := resource.NewObjectProperty(resource.NewPropertyMapFromMap(nil))
		if targetPropPath == nil {
			targetPropPath = diffPropPath
		}
		// Now updatedConfigField essentially is a config object with just one field - `fieldName`
		updatedConfigField, ok := targetPropPath.Add(newConfig, newConfigField)
		if !ok {
			return fmt.Errorf("failed to inject node config at property path: %q", targetPropPath.String())
		}
		logging.V(9).Infof("[%s] staged property value: %+v", label, updatedConfigField.ObjectValue().Mappable())
		body := p.prepareAPIInputs(updatedConfigField.ObjectValue(), oldState, map[string]resources.CloudAPIProperty{
			"config": {Flatten: true},
		})
		logging.V(9).Infof("[%s] nodepool config update request body: %v", label, body)
		op, err := retryRequest(p.client, "PUT", uri, "", body)
		if err != nil {
			return fmt.Errorf("error sending request: %s: %q %+v", err, uri, body)
		}

		_, err = p.waitForResourceOpCompletion(urn, res.Update.CloudAPIOperation, op)
		if err != nil {
			return errors.Wrapf(err, "waiting for completion")
		}
		return nil
	}
}
