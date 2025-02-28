# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['EndpointArgs', 'Endpoint']

@pulumi.input_type
class EndpointArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 enable_private_service_connect: Optional[pulumi.Input[bool]] = None,
                 encryption_spec: Optional[pulumi.Input['GoogleCloudAiplatformV1beta1EncryptionSpecArgs']] = None,
                 endpoint_id: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 predict_request_response_logging_config: Optional[pulumi.Input['GoogleCloudAiplatformV1beta1PredictRequestResponseLoggingConfigArgs']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 traffic_split: Optional[pulumi.Input[Mapping[str, pulumi.Input[int]]]] = None):
        """
        The set of arguments for constructing a Endpoint resource.
        :param pulumi.Input[str] display_name: The display name of the Endpoint. The name can be up to 128 characters long and can consist of any UTF-8 characters.
        :param pulumi.Input[str] description: The description of the Endpoint.
        :param pulumi.Input[bool] enable_private_service_connect: Deprecated: If true, expose the Endpoint via private service connect. Only one of the fields, network or enable_private_service_connect, can be set.
        :param pulumi.Input['GoogleCloudAiplatformV1beta1EncryptionSpecArgs'] encryption_spec: Customer-managed encryption key spec for an Endpoint. If set, this Endpoint and all sub-resources of this Endpoint will be secured by this key.
        :param pulumi.Input[str] endpoint_id: Immutable. The ID to use for endpoint, which will become the final component of the endpoint resource name. If not provided, Vertex AI will generate a value for this ID. If the first character is a letter, this value may be up to 63 characters, and valid characters are `[a-z0-9-]`. The last character must be a letter or number. If the first character is a number, this value may be up to 9 characters, and valid characters are `[0-9]` with no leading zeros. When using HTTP/JSON, this field is populated based on a query string argument, such as `?endpoint_id=12345`. This is the fallback for fields that are not included in either the URI or the body.
        :param pulumi.Input[str] etag: Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels with user-defined metadata to organize your Endpoints. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
        :param pulumi.Input[str] network: Optional. The full name of the Google Compute Engine [network](https://cloud.google.com//compute/docs/networks-and-firewalls#networks) to which the Endpoint should be peered. Private services access must already be configured for the network. If left unspecified, the Endpoint is not peered with any network. Only one of the fields, network or enable_private_service_connect, can be set. [Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/{project}/global/networks/{network}`. Where `{project}` is a project number, as in `12345`, and `{network}` is network name.
        :param pulumi.Input['GoogleCloudAiplatformV1beta1PredictRequestResponseLoggingConfigArgs'] predict_request_response_logging_config: Configures the request-response logging for online prediction.
        :param pulumi.Input[Mapping[str, pulumi.Input[int]]] traffic_split: A map from a DeployedModel's ID to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel. If a DeployedModel's ID is not listed in this map, then it receives no traffic. The traffic percentage values must add up to 100, or map must be empty if the Endpoint is to not accept any traffic at a moment.
        """
        pulumi.set(__self__, "display_name", display_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enable_private_service_connect is not None:
            warnings.warn("""Deprecated: If true, expose the Endpoint via private service connect. Only one of the fields, network or enable_private_service_connect, can be set.""", DeprecationWarning)
            pulumi.log.warn("""enable_private_service_connect is deprecated: Deprecated: If true, expose the Endpoint via private service connect. Only one of the fields, network or enable_private_service_connect, can be set.""")
        if enable_private_service_connect is not None:
            pulumi.set(__self__, "enable_private_service_connect", enable_private_service_connect)
        if encryption_spec is not None:
            pulumi.set(__self__, "encryption_spec", encryption_spec)
        if endpoint_id is not None:
            pulumi.set(__self__, "endpoint_id", endpoint_id)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if network is not None:
            pulumi.set(__self__, "network", network)
        if predict_request_response_logging_config is not None:
            pulumi.set(__self__, "predict_request_response_logging_config", predict_request_response_logging_config)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if traffic_split is not None:
            pulumi.set(__self__, "traffic_split", traffic_split)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The display name of the Endpoint. The name can be up to 128 characters long and can consist of any UTF-8 characters.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Endpoint.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="enablePrivateServiceConnect")
    @_utilities.deprecated("""Deprecated: If true, expose the Endpoint via private service connect. Only one of the fields, network or enable_private_service_connect, can be set.""")
    def enable_private_service_connect(self) -> Optional[pulumi.Input[bool]]:
        """
        Deprecated: If true, expose the Endpoint via private service connect. Only one of the fields, network or enable_private_service_connect, can be set.
        """
        return pulumi.get(self, "enable_private_service_connect")

    @enable_private_service_connect.setter
    def enable_private_service_connect(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_private_service_connect", value)

    @property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(self) -> Optional[pulumi.Input['GoogleCloudAiplatformV1beta1EncryptionSpecArgs']]:
        """
        Customer-managed encryption key spec for an Endpoint. If set, this Endpoint and all sub-resources of this Endpoint will be secured by this key.
        """
        return pulumi.get(self, "encryption_spec")

    @encryption_spec.setter
    def encryption_spec(self, value: Optional[pulumi.Input['GoogleCloudAiplatformV1beta1EncryptionSpecArgs']]):
        pulumi.set(self, "encryption_spec", value)

    @property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. The ID to use for endpoint, which will become the final component of the endpoint resource name. If not provided, Vertex AI will generate a value for this ID. If the first character is a letter, this value may be up to 63 characters, and valid characters are `[a-z0-9-]`. The last character must be a letter or number. If the first character is a number, this value may be up to 9 characters, and valid characters are `[0-9]` with no leading zeros. When using HTTP/JSON, this field is populated based on a query string argument, such as `?endpoint_id=12345`. This is the fallback for fields that are not included in either the URI or the body.
        """
        return pulumi.get(self, "endpoint_id")

    @endpoint_id.setter
    def endpoint_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_id", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The labels with user-defined metadata to organize your Endpoints. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The full name of the Google Compute Engine [network](https://cloud.google.com//compute/docs/networks-and-firewalls#networks) to which the Endpoint should be peered. Private services access must already be configured for the network. If left unspecified, the Endpoint is not peered with any network. Only one of the fields, network or enable_private_service_connect, can be set. [Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/{project}/global/networks/{network}`. Where `{project}` is a project number, as in `12345`, and `{network}` is network name.
        """
        return pulumi.get(self, "network")

    @network.setter
    def network(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network", value)

    @property
    @pulumi.getter(name="predictRequestResponseLoggingConfig")
    def predict_request_response_logging_config(self) -> Optional[pulumi.Input['GoogleCloudAiplatformV1beta1PredictRequestResponseLoggingConfigArgs']]:
        """
        Configures the request-response logging for online prediction.
        """
        return pulumi.get(self, "predict_request_response_logging_config")

    @predict_request_response_logging_config.setter
    def predict_request_response_logging_config(self, value: Optional[pulumi.Input['GoogleCloudAiplatformV1beta1PredictRequestResponseLoggingConfigArgs']]):
        pulumi.set(self, "predict_request_response_logging_config", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="trafficSplit")
    def traffic_split(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[int]]]]:
        """
        A map from a DeployedModel's ID to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel. If a DeployedModel's ID is not listed in this map, then it receives no traffic. The traffic percentage values must add up to 100, or map must be empty if the Endpoint is to not accept any traffic at a moment.
        """
        return pulumi.get(self, "traffic_split")

    @traffic_split.setter
    def traffic_split(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[int]]]]):
        pulumi.set(self, "traffic_split", value)


class Endpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enable_private_service_connect: Optional[pulumi.Input[bool]] = None,
                 encryption_spec: Optional[pulumi.Input[pulumi.InputType['GoogleCloudAiplatformV1beta1EncryptionSpecArgs']]] = None,
                 endpoint_id: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 predict_request_response_logging_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudAiplatformV1beta1PredictRequestResponseLoggingConfigArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 traffic_split: Optional[pulumi.Input[Mapping[str, pulumi.Input[int]]]] = None,
                 __props__=None):
        """
        Creates an Endpoint.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the Endpoint.
        :param pulumi.Input[str] display_name: The display name of the Endpoint. The name can be up to 128 characters long and can consist of any UTF-8 characters.
        :param pulumi.Input[bool] enable_private_service_connect: Deprecated: If true, expose the Endpoint via private service connect. Only one of the fields, network or enable_private_service_connect, can be set.
        :param pulumi.Input[pulumi.InputType['GoogleCloudAiplatformV1beta1EncryptionSpecArgs']] encryption_spec: Customer-managed encryption key spec for an Endpoint. If set, this Endpoint and all sub-resources of this Endpoint will be secured by this key.
        :param pulumi.Input[str] endpoint_id: Immutable. The ID to use for endpoint, which will become the final component of the endpoint resource name. If not provided, Vertex AI will generate a value for this ID. If the first character is a letter, this value may be up to 63 characters, and valid characters are `[a-z0-9-]`. The last character must be a letter or number. If the first character is a number, this value may be up to 9 characters, and valid characters are `[0-9]` with no leading zeros. When using HTTP/JSON, this field is populated based on a query string argument, such as `?endpoint_id=12345`. This is the fallback for fields that are not included in either the URI or the body.
        :param pulumi.Input[str] etag: Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels with user-defined metadata to organize your Endpoints. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
        :param pulumi.Input[str] network: Optional. The full name of the Google Compute Engine [network](https://cloud.google.com//compute/docs/networks-and-firewalls#networks) to which the Endpoint should be peered. Private services access must already be configured for the network. If left unspecified, the Endpoint is not peered with any network. Only one of the fields, network or enable_private_service_connect, can be set. [Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/{project}/global/networks/{network}`. Where `{project}` is a project number, as in `12345`, and `{network}` is network name.
        :param pulumi.Input[pulumi.InputType['GoogleCloudAiplatformV1beta1PredictRequestResponseLoggingConfigArgs']] predict_request_response_logging_config: Configures the request-response logging for online prediction.
        :param pulumi.Input[Mapping[str, pulumi.Input[int]]] traffic_split: A map from a DeployedModel's ID to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel. If a DeployedModel's ID is not listed in this map, then it receives no traffic. The traffic percentage values must add up to 100, or map must be empty if the Endpoint is to not accept any traffic at a moment.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an Endpoint.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param EndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enable_private_service_connect: Optional[pulumi.Input[bool]] = None,
                 encryption_spec: Optional[pulumi.Input[pulumi.InputType['GoogleCloudAiplatformV1beta1EncryptionSpecArgs']]] = None,
                 endpoint_id: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 predict_request_response_logging_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudAiplatformV1beta1PredictRequestResponseLoggingConfigArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 traffic_split: Optional[pulumi.Input[Mapping[str, pulumi.Input[int]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EndpointArgs.__new__(EndpointArgs)

            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["enable_private_service_connect"] = enable_private_service_connect
            __props__.__dict__["encryption_spec"] = encryption_spec
            __props__.__dict__["endpoint_id"] = endpoint_id
            __props__.__dict__["etag"] = etag
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["network"] = network
            __props__.__dict__["predict_request_response_logging_config"] = predict_request_response_logging_config
            __props__.__dict__["project"] = project
            __props__.__dict__["traffic_split"] = traffic_split
            __props__.__dict__["create_time"] = None
            __props__.__dict__["deployed_models"] = None
            __props__.__dict__["model_deployment_monitoring_job"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["location", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Endpoint, __self__).__init__(
            'google-native:aiplatform/v1beta1:Endpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Endpoint':
        """
        Get an existing Endpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EndpointArgs.__new__(EndpointArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["deployed_models"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["enable_private_service_connect"] = None
        __props__.__dict__["encryption_spec"] = None
        __props__.__dict__["endpoint_id"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["model_deployment_monitoring_job"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network"] = None
        __props__.__dict__["predict_request_response_logging_config"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["traffic_split"] = None
        __props__.__dict__["update_time"] = None
        return Endpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Timestamp when this Endpoint was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="deployedModels")
    def deployed_models(self) -> pulumi.Output[Sequence['outputs.GoogleCloudAiplatformV1beta1DeployedModelResponse']]:
        """
        The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively.
        """
        return pulumi.get(self, "deployed_models")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the Endpoint.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The display name of the Endpoint. The name can be up to 128 characters long and can consist of any UTF-8 characters.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="enablePrivateServiceConnect")
    @_utilities.deprecated("""Deprecated: If true, expose the Endpoint via private service connect. Only one of the fields, network or enable_private_service_connect, can be set.""")
    def enable_private_service_connect(self) -> pulumi.Output[bool]:
        """
        Deprecated: If true, expose the Endpoint via private service connect. Only one of the fields, network or enable_private_service_connect, can be set.
        """
        return pulumi.get(self, "enable_private_service_connect")

    @property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(self) -> pulumi.Output['outputs.GoogleCloudAiplatformV1beta1EncryptionSpecResponse']:
        """
        Customer-managed encryption key spec for an Endpoint. If set, this Endpoint and all sub-resources of this Endpoint will be secured by this key.
        """
        return pulumi.get(self, "encryption_spec")

    @property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> pulumi.Output[Optional[str]]:
        """
        Immutable. The ID to use for endpoint, which will become the final component of the endpoint resource name. If not provided, Vertex AI will generate a value for this ID. If the first character is a letter, this value may be up to 63 characters, and valid characters are `[a-z0-9-]`. The last character must be a letter or number. If the first character is a number, this value may be up to 9 characters, and valid characters are `[0-9]` with no leading zeros. When using HTTP/JSON, this field is populated based on a query string argument, such as `?endpoint_id=12345`. This is the fallback for fields that are not included in either the URI or the body.
        """
        return pulumi.get(self, "endpoint_id")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The labels with user-defined metadata to organize your Endpoints. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="modelDeploymentMonitoringJob")
    def model_deployment_monitoring_job(self) -> pulumi.Output[str]:
        """
        Resource name of the Model Monitoring job associated with this Endpoint if monitoring is enabled by JobService.CreateModelDeploymentMonitoringJob. Format: `projects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}`
        """
        return pulumi.get(self, "model_deployment_monitoring_job")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the Endpoint.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output[str]:
        """
        Optional. The full name of the Google Compute Engine [network](https://cloud.google.com//compute/docs/networks-and-firewalls#networks) to which the Endpoint should be peered. Private services access must already be configured for the network. If left unspecified, the Endpoint is not peered with any network. Only one of the fields, network or enable_private_service_connect, can be set. [Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/{project}/global/networks/{network}`. Where `{project}` is a project number, as in `12345`, and `{network}` is network name.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="predictRequestResponseLoggingConfig")
    def predict_request_response_logging_config(self) -> pulumi.Output['outputs.GoogleCloudAiplatformV1beta1PredictRequestResponseLoggingConfigResponse']:
        """
        Configures the request-response logging for online prediction.
        """
        return pulumi.get(self, "predict_request_response_logging_config")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="trafficSplit")
    def traffic_split(self) -> pulumi.Output[Mapping[str, int]]:
        """
        A map from a DeployedModel's ID to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel. If a DeployedModel's ID is not listed in this map, then it receives no traffic. The traffic percentage values must add up to 100, or map must be empty if the Endpoint is to not accept any traffic at a moment.
        """
        return pulumi.get(self, "traffic_split")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Timestamp when this Endpoint was last updated.
        """
        return pulumi.get(self, "update_time")

