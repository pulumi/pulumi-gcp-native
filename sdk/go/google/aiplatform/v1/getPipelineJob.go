// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Gets a PipelineJob.
func LookupPipelineJob(ctx *pulumi.Context, args *LookupPipelineJobArgs, opts ...pulumi.InvokeOption) (*LookupPipelineJobResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupPipelineJobResult
	err := ctx.Invoke("google-native:aiplatform/v1:getPipelineJob", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupPipelineJobArgs struct {
	Location      string  `pulumi:"location"`
	PipelineJobId string  `pulumi:"pipelineJobId"`
	Project       *string `pulumi:"project"`
}

type LookupPipelineJobResult struct {
	// Pipeline creation time.
	CreateTime string `pulumi:"createTime"`
	// The display name of the Pipeline. The name can be up to 128 characters long and can consist of any UTF-8 characters.
	DisplayName string `pulumi:"displayName"`
	// Customer-managed encryption key spec for a pipelineJob. If set, this PipelineJob and all of its sub-resources will be secured by this key.
	EncryptionSpec GoogleCloudAiplatformV1EncryptionSpecResponse `pulumi:"encryptionSpec"`
	// Pipeline end time.
	EndTime string `pulumi:"endTime"`
	// The error that occurred during pipeline execution. Only populated when the pipeline's state is FAILED or CANCELLED.
	Error GoogleRpcStatusResponse `pulumi:"error"`
	// The details of pipeline run. Not available in the list view.
	JobDetail GoogleCloudAiplatformV1PipelineJobDetailResponse `pulumi:"jobDetail"`
	// The labels with user-defined metadata to organize PipelineJob. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. Note there is some reserved label key for Vertex AI Pipelines. - `vertex-ai-pipelines-run-billing-id`, user set value will get overrided.
	Labels map[string]string `pulumi:"labels"`
	// The resource name of the PipelineJob.
	Name string `pulumi:"name"`
	// The full name of the Compute Engine [network](/compute/docs/networks-and-firewalls#networks) to which the Pipeline Job's workload should be peered. For example, `projects/12345/global/networks/myVPC`. [Format](/compute/docs/reference/rest/v1/networks/insert) is of the form `projects/{project}/global/networks/{network}`. Where {project} is a project number, as in `12345`, and {network} is a network name. Private services access must already be configured for the network. Pipeline job will apply the network configuration to the Google Cloud resources being launched, if applied, such as Vertex AI Training or Dataflow job. If left unspecified, the workload is not peered with any network.
	Network string `pulumi:"network"`
	// The spec of the pipeline.
	PipelineSpec map[string]interface{} `pulumi:"pipelineSpec"`
	// A list of names for the reserved ip ranges under the VPC network that can be used for this Pipeline Job's workload. If set, we will deploy the Pipeline Job's workload within the provided ip ranges. Otherwise, the job will be deployed to any ip ranges under the provided VPC network. Example: ['vertex-ai-ip-range'].
	ReservedIpRanges []string `pulumi:"reservedIpRanges"`
	// Runtime config of the pipeline.
	RuntimeConfig GoogleCloudAiplatformV1PipelineJobRuntimeConfigResponse `pulumi:"runtimeConfig"`
	// The schedule resource name. Only returned if the Pipeline is created by Schedule API.
	ScheduleName string `pulumi:"scheduleName"`
	// The service account that the pipeline workload runs as. If not specified, the Compute Engine default service account in the project will be used. See https://cloud.google.com/compute/docs/access/service-accounts#default_service_account Users starting the pipeline must have the `iam.serviceAccounts.actAs` permission on this service account.
	ServiceAccount string `pulumi:"serviceAccount"`
	// Pipeline start time.
	StartTime string `pulumi:"startTime"`
	// The detailed state of the job.
	State string `pulumi:"state"`
	// Pipeline template metadata. Will fill up fields if PipelineJob.template_uri is from supported template registry.
	TemplateMetadata GoogleCloudAiplatformV1PipelineTemplateMetadataResponse `pulumi:"templateMetadata"`
	// A template uri from where the PipelineJob.pipeline_spec, if empty, will be downloaded. Currently, only uri from Vertex Template Registry & Gallery is supported. Reference to https://cloud.google.com/vertex-ai/docs/pipelines/create-pipeline-template.
	TemplateUri string `pulumi:"templateUri"`
	// Timestamp when this PipelineJob was most recently updated.
	UpdateTime string `pulumi:"updateTime"`
}

func LookupPipelineJobOutput(ctx *pulumi.Context, args LookupPipelineJobOutputArgs, opts ...pulumi.InvokeOption) LookupPipelineJobResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupPipelineJobResult, error) {
			args := v.(LookupPipelineJobArgs)
			r, err := LookupPipelineJob(ctx, &args, opts...)
			var s LookupPipelineJobResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupPipelineJobResultOutput)
}

type LookupPipelineJobOutputArgs struct {
	Location      pulumi.StringInput    `pulumi:"location"`
	PipelineJobId pulumi.StringInput    `pulumi:"pipelineJobId"`
	Project       pulumi.StringPtrInput `pulumi:"project"`
}

func (LookupPipelineJobOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPipelineJobArgs)(nil)).Elem()
}

type LookupPipelineJobResultOutput struct{ *pulumi.OutputState }

func (LookupPipelineJobResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPipelineJobResult)(nil)).Elem()
}

func (o LookupPipelineJobResultOutput) ToLookupPipelineJobResultOutput() LookupPipelineJobResultOutput {
	return o
}

func (o LookupPipelineJobResultOutput) ToLookupPipelineJobResultOutputWithContext(ctx context.Context) LookupPipelineJobResultOutput {
	return o
}

// Pipeline creation time.
func (o LookupPipelineJobResultOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPipelineJobResult) string { return v.CreateTime }).(pulumi.StringOutput)
}

// The display name of the Pipeline. The name can be up to 128 characters long and can consist of any UTF-8 characters.
func (o LookupPipelineJobResultOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPipelineJobResult) string { return v.DisplayName }).(pulumi.StringOutput)
}

// Customer-managed encryption key spec for a pipelineJob. If set, this PipelineJob and all of its sub-resources will be secured by this key.
func (o LookupPipelineJobResultOutput) EncryptionSpec() GoogleCloudAiplatformV1EncryptionSpecResponseOutput {
	return o.ApplyT(func(v LookupPipelineJobResult) GoogleCloudAiplatformV1EncryptionSpecResponse { return v.EncryptionSpec }).(GoogleCloudAiplatformV1EncryptionSpecResponseOutput)
}

// Pipeline end time.
func (o LookupPipelineJobResultOutput) EndTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPipelineJobResult) string { return v.EndTime }).(pulumi.StringOutput)
}

// The error that occurred during pipeline execution. Only populated when the pipeline's state is FAILED or CANCELLED.
func (o LookupPipelineJobResultOutput) Error() GoogleRpcStatusResponseOutput {
	return o.ApplyT(func(v LookupPipelineJobResult) GoogleRpcStatusResponse { return v.Error }).(GoogleRpcStatusResponseOutput)
}

// The details of pipeline run. Not available in the list view.
func (o LookupPipelineJobResultOutput) JobDetail() GoogleCloudAiplatformV1PipelineJobDetailResponseOutput {
	return o.ApplyT(func(v LookupPipelineJobResult) GoogleCloudAiplatformV1PipelineJobDetailResponse { return v.JobDetail }).(GoogleCloudAiplatformV1PipelineJobDetailResponseOutput)
}

// The labels with user-defined metadata to organize PipelineJob. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. Note there is some reserved label key for Vertex AI Pipelines. - `vertex-ai-pipelines-run-billing-id`, user set value will get overrided.
func (o LookupPipelineJobResultOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupPipelineJobResult) map[string]string { return v.Labels }).(pulumi.StringMapOutput)
}

// The resource name of the PipelineJob.
func (o LookupPipelineJobResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPipelineJobResult) string { return v.Name }).(pulumi.StringOutput)
}

// The full name of the Compute Engine [network](/compute/docs/networks-and-firewalls#networks) to which the Pipeline Job's workload should be peered. For example, `projects/12345/global/networks/myVPC`. [Format](/compute/docs/reference/rest/v1/networks/insert) is of the form `projects/{project}/global/networks/{network}`. Where {project} is a project number, as in `12345`, and {network} is a network name. Private services access must already be configured for the network. Pipeline job will apply the network configuration to the Google Cloud resources being launched, if applied, such as Vertex AI Training or Dataflow job. If left unspecified, the workload is not peered with any network.
func (o LookupPipelineJobResultOutput) Network() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPipelineJobResult) string { return v.Network }).(pulumi.StringOutput)
}

// The spec of the pipeline.
func (o LookupPipelineJobResultOutput) PipelineSpec() pulumi.MapOutput {
	return o.ApplyT(func(v LookupPipelineJobResult) map[string]interface{} { return v.PipelineSpec }).(pulumi.MapOutput)
}

// A list of names for the reserved ip ranges under the VPC network that can be used for this Pipeline Job's workload. If set, we will deploy the Pipeline Job's workload within the provided ip ranges. Otherwise, the job will be deployed to any ip ranges under the provided VPC network. Example: ['vertex-ai-ip-range'].
func (o LookupPipelineJobResultOutput) ReservedIpRanges() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupPipelineJobResult) []string { return v.ReservedIpRanges }).(pulumi.StringArrayOutput)
}

// Runtime config of the pipeline.
func (o LookupPipelineJobResultOutput) RuntimeConfig() GoogleCloudAiplatformV1PipelineJobRuntimeConfigResponseOutput {
	return o.ApplyT(func(v LookupPipelineJobResult) GoogleCloudAiplatformV1PipelineJobRuntimeConfigResponse {
		return v.RuntimeConfig
	}).(GoogleCloudAiplatformV1PipelineJobRuntimeConfigResponseOutput)
}

// The schedule resource name. Only returned if the Pipeline is created by Schedule API.
func (o LookupPipelineJobResultOutput) ScheduleName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPipelineJobResult) string { return v.ScheduleName }).(pulumi.StringOutput)
}

// The service account that the pipeline workload runs as. If not specified, the Compute Engine default service account in the project will be used. See https://cloud.google.com/compute/docs/access/service-accounts#default_service_account Users starting the pipeline must have the `iam.serviceAccounts.actAs` permission on this service account.
func (o LookupPipelineJobResultOutput) ServiceAccount() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPipelineJobResult) string { return v.ServiceAccount }).(pulumi.StringOutput)
}

// Pipeline start time.
func (o LookupPipelineJobResultOutput) StartTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPipelineJobResult) string { return v.StartTime }).(pulumi.StringOutput)
}

// The detailed state of the job.
func (o LookupPipelineJobResultOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPipelineJobResult) string { return v.State }).(pulumi.StringOutput)
}

// Pipeline template metadata. Will fill up fields if PipelineJob.template_uri is from supported template registry.
func (o LookupPipelineJobResultOutput) TemplateMetadata() GoogleCloudAiplatformV1PipelineTemplateMetadataResponseOutput {
	return o.ApplyT(func(v LookupPipelineJobResult) GoogleCloudAiplatformV1PipelineTemplateMetadataResponse {
		return v.TemplateMetadata
	}).(GoogleCloudAiplatformV1PipelineTemplateMetadataResponseOutput)
}

// A template uri from where the PipelineJob.pipeline_spec, if empty, will be downloaded. Currently, only uri from Vertex Template Registry & Gallery is supported. Reference to https://cloud.google.com/vertex-ai/docs/pipelines/create-pipeline-template.
func (o LookupPipelineJobResultOutput) TemplateUri() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPipelineJobResult) string { return v.TemplateUri }).(pulumi.StringOutput)
}

// Timestamp when this PipelineJob was most recently updated.
func (o LookupPipelineJobResultOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPipelineJobResult) string { return v.UpdateTime }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupPipelineJobResultOutput{})
}
