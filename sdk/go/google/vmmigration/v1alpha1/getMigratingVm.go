// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1alpha1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Gets details of a single MigratingVm.
func LookupMigratingVm(ctx *pulumi.Context, args *LookupMigratingVmArgs, opts ...pulumi.InvokeOption) (*LookupMigratingVmResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupMigratingVmResult
	err := ctx.Invoke("google-native:vmmigration/v1alpha1:getMigratingVm", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupMigratingVmArgs struct {
	Location      string  `pulumi:"location"`
	MigratingVmId string  `pulumi:"migratingVmId"`
	Project       *string `pulumi:"project"`
	SourceId      string  `pulumi:"sourceId"`
	View          *string `pulumi:"view"`
}

type LookupMigratingVmResult struct {
	// Details of the VM from an AWS source.
	AwsSourceVmDetails AwsSourceVmDetailsResponse `pulumi:"awsSourceVmDetails"`
	// Details of the VM from an Azure source.
	AzureSourceVmDetails AzureSourceVmDetailsResponse `pulumi:"azureSourceVmDetails"`
	// Details of the target Persistent Disks in Compute Engine.
	ComputeEngineDisksTargetDefaults ComputeEngineDisksTargetDefaultsResponse `pulumi:"computeEngineDisksTargetDefaults"`
	// Details of the target VM in Compute Engine.
	ComputeEngineTargetDefaults ComputeEngineTargetDefaultsResponse `pulumi:"computeEngineTargetDefaults"`
	// Details of the VM in Compute Engine. Deprecated: Use compute_engine_target_defaults instead.
	//
	// Deprecated: Details of the VM in Compute Engine. Deprecated: Use compute_engine_target_defaults instead.
	ComputeEngineVmDefaults TargetVMDetailsResponse `pulumi:"computeEngineVmDefaults"`
	// The time the migrating VM was created (this refers to this resource and not to the time it was installed in the source).
	CreateTime string `pulumi:"createTime"`
	// Details of the current running replication cycle.
	CurrentSyncInfo ReplicationCycleResponse `pulumi:"currentSyncInfo"`
	// Provides details of future CutoverJobs of a MigratingVm. Set to empty when cutover forecast is unavailable.
	CutoverForecast CutoverForecastResponse `pulumi:"cutoverForecast"`
	// The description attached to the migrating VM by the user.
	Description string `pulumi:"description"`
	// The display name attached to the MigratingVm by the user.
	DisplayName string `pulumi:"displayName"`
	// Provides details on the state of the Migrating VM in case of an error in replication.
	Error StatusResponse `pulumi:"error"`
	// The group this migrating vm is included in, if any. The group is represented by the full path of the appropriate Group resource.
	Group string `pulumi:"group"`
	// The labels of the migrating VM.
	Labels map[string]string `pulumi:"labels"`
	// Details of the last replication cycle. This will be updated whenever a replication cycle is finished and is not to be confused with last_sync which is only updated on successful replication cycles.
	LastReplicationCycle ReplicationCycleResponse `pulumi:"lastReplicationCycle"`
	// The most updated snapshot created time in the source that finished replication.
	LastSync ReplicationSyncResponse `pulumi:"lastSync"`
	// The identifier of the MigratingVm.
	Name string `pulumi:"name"`
	// The replication schedule policy.
	Policy SchedulePolicyResponse `pulumi:"policy"`
	// The recent clone jobs performed on the migrating VM. This field holds the vm's last completed clone job and the vm's running clone job, if one exists. Note: To have this field populated you need to explicitly request it via the "view" parameter of the Get/List request.
	RecentCloneJobs []CloneJobResponse `pulumi:"recentCloneJobs"`
	// The recent cutover jobs performed on the migrating VM. This field holds the vm's last completed cutover job and the vm's running cutover job, if one exists. Note: To have this field populated you need to explicitly request it via the "view" parameter of the Get/List request.
	RecentCutoverJobs []CutoverJobResponse `pulumi:"recentCutoverJobs"`
	// The unique ID of the VM in the source. The VM's name in vSphere can be changed, so this is not the VM's name but rather its moRef id. This id is of the form vm-.
	SourceVmId string `pulumi:"sourceVmId"`
	// State of the MigratingVm.
	State string `pulumi:"state"`
	// The last time the migrating VM state was updated.
	StateTime string `pulumi:"stateTime"`
	// The default configuration of the target VM that will be created in Google Cloud as a result of the migration. Deprecated: Use compute_engine_target_defaults instead.
	//
	// Deprecated: The default configuration of the target VM that will be created in Google Cloud as a result of the migration. Deprecated: Use compute_engine_target_defaults instead.
	TargetDefaults TargetVMDetailsResponse `pulumi:"targetDefaults"`
	// The last time the migrating VM resource was updated.
	UpdateTime string `pulumi:"updateTime"`
	// Details of the VM from a Vmware source.
	VmwareSourceVmDetails VmwareSourceVmDetailsResponse `pulumi:"vmwareSourceVmDetails"`
}

func LookupMigratingVmOutput(ctx *pulumi.Context, args LookupMigratingVmOutputArgs, opts ...pulumi.InvokeOption) LookupMigratingVmResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupMigratingVmResult, error) {
			args := v.(LookupMigratingVmArgs)
			r, err := LookupMigratingVm(ctx, &args, opts...)
			var s LookupMigratingVmResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupMigratingVmResultOutput)
}

type LookupMigratingVmOutputArgs struct {
	Location      pulumi.StringInput    `pulumi:"location"`
	MigratingVmId pulumi.StringInput    `pulumi:"migratingVmId"`
	Project       pulumi.StringPtrInput `pulumi:"project"`
	SourceId      pulumi.StringInput    `pulumi:"sourceId"`
	View          pulumi.StringPtrInput `pulumi:"view"`
}

func (LookupMigratingVmOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMigratingVmArgs)(nil)).Elem()
}

type LookupMigratingVmResultOutput struct{ *pulumi.OutputState }

func (LookupMigratingVmResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMigratingVmResult)(nil)).Elem()
}

func (o LookupMigratingVmResultOutput) ToLookupMigratingVmResultOutput() LookupMigratingVmResultOutput {
	return o
}

func (o LookupMigratingVmResultOutput) ToLookupMigratingVmResultOutputWithContext(ctx context.Context) LookupMigratingVmResultOutput {
	return o
}

// Details of the VM from an AWS source.
func (o LookupMigratingVmResultOutput) AwsSourceVmDetails() AwsSourceVmDetailsResponseOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) AwsSourceVmDetailsResponse { return v.AwsSourceVmDetails }).(AwsSourceVmDetailsResponseOutput)
}

// Details of the VM from an Azure source.
func (o LookupMigratingVmResultOutput) AzureSourceVmDetails() AzureSourceVmDetailsResponseOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) AzureSourceVmDetailsResponse { return v.AzureSourceVmDetails }).(AzureSourceVmDetailsResponseOutput)
}

// Details of the target Persistent Disks in Compute Engine.
func (o LookupMigratingVmResultOutput) ComputeEngineDisksTargetDefaults() ComputeEngineDisksTargetDefaultsResponseOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) ComputeEngineDisksTargetDefaultsResponse {
		return v.ComputeEngineDisksTargetDefaults
	}).(ComputeEngineDisksTargetDefaultsResponseOutput)
}

// Details of the target VM in Compute Engine.
func (o LookupMigratingVmResultOutput) ComputeEngineTargetDefaults() ComputeEngineTargetDefaultsResponseOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) ComputeEngineTargetDefaultsResponse {
		return v.ComputeEngineTargetDefaults
	}).(ComputeEngineTargetDefaultsResponseOutput)
}

// Details of the VM in Compute Engine. Deprecated: Use compute_engine_target_defaults instead.
//
// Deprecated: Details of the VM in Compute Engine. Deprecated: Use compute_engine_target_defaults instead.
func (o LookupMigratingVmResultOutput) ComputeEngineVmDefaults() TargetVMDetailsResponseOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) TargetVMDetailsResponse { return v.ComputeEngineVmDefaults }).(TargetVMDetailsResponseOutput)
}

// The time the migrating VM was created (this refers to this resource and not to the time it was installed in the source).
func (o LookupMigratingVmResultOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) string { return v.CreateTime }).(pulumi.StringOutput)
}

// Details of the current running replication cycle.
func (o LookupMigratingVmResultOutput) CurrentSyncInfo() ReplicationCycleResponseOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) ReplicationCycleResponse { return v.CurrentSyncInfo }).(ReplicationCycleResponseOutput)
}

// Provides details of future CutoverJobs of a MigratingVm. Set to empty when cutover forecast is unavailable.
func (o LookupMigratingVmResultOutput) CutoverForecast() CutoverForecastResponseOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) CutoverForecastResponse { return v.CutoverForecast }).(CutoverForecastResponseOutput)
}

// The description attached to the migrating VM by the user.
func (o LookupMigratingVmResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) string { return v.Description }).(pulumi.StringOutput)
}

// The display name attached to the MigratingVm by the user.
func (o LookupMigratingVmResultOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) string { return v.DisplayName }).(pulumi.StringOutput)
}

// Provides details on the state of the Migrating VM in case of an error in replication.
func (o LookupMigratingVmResultOutput) Error() StatusResponseOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) StatusResponse { return v.Error }).(StatusResponseOutput)
}

// The group this migrating vm is included in, if any. The group is represented by the full path of the appropriate Group resource.
func (o LookupMigratingVmResultOutput) Group() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) string { return v.Group }).(pulumi.StringOutput)
}

// The labels of the migrating VM.
func (o LookupMigratingVmResultOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) map[string]string { return v.Labels }).(pulumi.StringMapOutput)
}

// Details of the last replication cycle. This will be updated whenever a replication cycle is finished and is not to be confused with last_sync which is only updated on successful replication cycles.
func (o LookupMigratingVmResultOutput) LastReplicationCycle() ReplicationCycleResponseOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) ReplicationCycleResponse { return v.LastReplicationCycle }).(ReplicationCycleResponseOutput)
}

// The most updated snapshot created time in the source that finished replication.
func (o LookupMigratingVmResultOutput) LastSync() ReplicationSyncResponseOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) ReplicationSyncResponse { return v.LastSync }).(ReplicationSyncResponseOutput)
}

// The identifier of the MigratingVm.
func (o LookupMigratingVmResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) string { return v.Name }).(pulumi.StringOutput)
}

// The replication schedule policy.
func (o LookupMigratingVmResultOutput) Policy() SchedulePolicyResponseOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) SchedulePolicyResponse { return v.Policy }).(SchedulePolicyResponseOutput)
}

// The recent clone jobs performed on the migrating VM. This field holds the vm's last completed clone job and the vm's running clone job, if one exists. Note: To have this field populated you need to explicitly request it via the "view" parameter of the Get/List request.
func (o LookupMigratingVmResultOutput) RecentCloneJobs() CloneJobResponseArrayOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) []CloneJobResponse { return v.RecentCloneJobs }).(CloneJobResponseArrayOutput)
}

// The recent cutover jobs performed on the migrating VM. This field holds the vm's last completed cutover job and the vm's running cutover job, if one exists. Note: To have this field populated you need to explicitly request it via the "view" parameter of the Get/List request.
func (o LookupMigratingVmResultOutput) RecentCutoverJobs() CutoverJobResponseArrayOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) []CutoverJobResponse { return v.RecentCutoverJobs }).(CutoverJobResponseArrayOutput)
}

// The unique ID of the VM in the source. The VM's name in vSphere can be changed, so this is not the VM's name but rather its moRef id. This id is of the form vm-.
func (o LookupMigratingVmResultOutput) SourceVmId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) string { return v.SourceVmId }).(pulumi.StringOutput)
}

// State of the MigratingVm.
func (o LookupMigratingVmResultOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) string { return v.State }).(pulumi.StringOutput)
}

// The last time the migrating VM state was updated.
func (o LookupMigratingVmResultOutput) StateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) string { return v.StateTime }).(pulumi.StringOutput)
}

// The default configuration of the target VM that will be created in Google Cloud as a result of the migration. Deprecated: Use compute_engine_target_defaults instead.
//
// Deprecated: The default configuration of the target VM that will be created in Google Cloud as a result of the migration. Deprecated: Use compute_engine_target_defaults instead.
func (o LookupMigratingVmResultOutput) TargetDefaults() TargetVMDetailsResponseOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) TargetVMDetailsResponse { return v.TargetDefaults }).(TargetVMDetailsResponseOutput)
}

// The last time the migrating VM resource was updated.
func (o LookupMigratingVmResultOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) string { return v.UpdateTime }).(pulumi.StringOutput)
}

// Details of the VM from a Vmware source.
func (o LookupMigratingVmResultOutput) VmwareSourceVmDetails() VmwareSourceVmDetailsResponseOutput {
	return o.ApplyT(func(v LookupMigratingVmResult) VmwareSourceVmDetailsResponse { return v.VmwareSourceVmDetails }).(VmwareSourceVmDetailsResponseOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupMigratingVmResultOutput{})
}
