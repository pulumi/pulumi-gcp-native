// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1beta1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Gets a HyperparameterTuningJob
func LookupHyperparameterTuningJob(ctx *pulumi.Context, args *LookupHyperparameterTuningJobArgs, opts ...pulumi.InvokeOption) (*LookupHyperparameterTuningJobResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupHyperparameterTuningJobResult
	err := ctx.Invoke("google-native:aiplatform/v1beta1:getHyperparameterTuningJob", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupHyperparameterTuningJobArgs struct {
	HyperparameterTuningJobId string  `pulumi:"hyperparameterTuningJobId"`
	Location                  string  `pulumi:"location"`
	Project                   *string `pulumi:"project"`
}

type LookupHyperparameterTuningJobResult struct {
	// Time when the HyperparameterTuningJob was created.
	CreateTime string `pulumi:"createTime"`
	// The display name of the HyperparameterTuningJob. The name can be up to 128 characters long and can consist of any UTF-8 characters.
	DisplayName string `pulumi:"displayName"`
	// Customer-managed encryption key options for a HyperparameterTuningJob. If this is set, then all resources created by the HyperparameterTuningJob will be encrypted with the provided encryption key.
	EncryptionSpec GoogleCloudAiplatformV1beta1EncryptionSpecResponse `pulumi:"encryptionSpec"`
	// Time when the HyperparameterTuningJob entered any of the following states: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`.
	EndTime string `pulumi:"endTime"`
	// Only populated when job's state is JOB_STATE_FAILED or JOB_STATE_CANCELLED.
	Error GoogleRpcStatusResponse `pulumi:"error"`
	// The labels with user-defined metadata to organize HyperparameterTuningJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
	Labels map[string]string `pulumi:"labels"`
	// The number of failed Trials that need to be seen before failing the HyperparameterTuningJob. If set to 0, Vertex AI decides how many Trials must fail before the whole job fails.
	MaxFailedTrialCount int `pulumi:"maxFailedTrialCount"`
	// The desired total number of Trials.
	MaxTrialCount int `pulumi:"maxTrialCount"`
	// Resource name of the HyperparameterTuningJob.
	Name string `pulumi:"name"`
	// The desired number of Trials to run in parallel.
	ParallelTrialCount int `pulumi:"parallelTrialCount"`
	// Time when the HyperparameterTuningJob for the first time entered the `JOB_STATE_RUNNING` state.
	StartTime string `pulumi:"startTime"`
	// The detailed state of the job.
	State string `pulumi:"state"`
	// Study configuration of the HyperparameterTuningJob.
	StudySpec GoogleCloudAiplatformV1beta1StudySpecResponse `pulumi:"studySpec"`
	// The spec of a trial job. The same spec applies to the CustomJobs created in all the trials.
	TrialJobSpec GoogleCloudAiplatformV1beta1CustomJobSpecResponse `pulumi:"trialJobSpec"`
	// Trials of the HyperparameterTuningJob.
	Trials []GoogleCloudAiplatformV1beta1TrialResponse `pulumi:"trials"`
	// Time when the HyperparameterTuningJob was most recently updated.
	UpdateTime string `pulumi:"updateTime"`
}

func LookupHyperparameterTuningJobOutput(ctx *pulumi.Context, args LookupHyperparameterTuningJobOutputArgs, opts ...pulumi.InvokeOption) LookupHyperparameterTuningJobResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupHyperparameterTuningJobResult, error) {
			args := v.(LookupHyperparameterTuningJobArgs)
			r, err := LookupHyperparameterTuningJob(ctx, &args, opts...)
			var s LookupHyperparameterTuningJobResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupHyperparameterTuningJobResultOutput)
}

type LookupHyperparameterTuningJobOutputArgs struct {
	HyperparameterTuningJobId pulumi.StringInput    `pulumi:"hyperparameterTuningJobId"`
	Location                  pulumi.StringInput    `pulumi:"location"`
	Project                   pulumi.StringPtrInput `pulumi:"project"`
}

func (LookupHyperparameterTuningJobOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupHyperparameterTuningJobArgs)(nil)).Elem()
}

type LookupHyperparameterTuningJobResultOutput struct{ *pulumi.OutputState }

func (LookupHyperparameterTuningJobResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupHyperparameterTuningJobResult)(nil)).Elem()
}

func (o LookupHyperparameterTuningJobResultOutput) ToLookupHyperparameterTuningJobResultOutput() LookupHyperparameterTuningJobResultOutput {
	return o
}

func (o LookupHyperparameterTuningJobResultOutput) ToLookupHyperparameterTuningJobResultOutputWithContext(ctx context.Context) LookupHyperparameterTuningJobResultOutput {
	return o
}

// Time when the HyperparameterTuningJob was created.
func (o LookupHyperparameterTuningJobResultOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHyperparameterTuningJobResult) string { return v.CreateTime }).(pulumi.StringOutput)
}

// The display name of the HyperparameterTuningJob. The name can be up to 128 characters long and can consist of any UTF-8 characters.
func (o LookupHyperparameterTuningJobResultOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHyperparameterTuningJobResult) string { return v.DisplayName }).(pulumi.StringOutput)
}

// Customer-managed encryption key options for a HyperparameterTuningJob. If this is set, then all resources created by the HyperparameterTuningJob will be encrypted with the provided encryption key.
func (o LookupHyperparameterTuningJobResultOutput) EncryptionSpec() GoogleCloudAiplatformV1beta1EncryptionSpecResponseOutput {
	return o.ApplyT(func(v LookupHyperparameterTuningJobResult) GoogleCloudAiplatformV1beta1EncryptionSpecResponse {
		return v.EncryptionSpec
	}).(GoogleCloudAiplatformV1beta1EncryptionSpecResponseOutput)
}

// Time when the HyperparameterTuningJob entered any of the following states: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`.
func (o LookupHyperparameterTuningJobResultOutput) EndTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHyperparameterTuningJobResult) string { return v.EndTime }).(pulumi.StringOutput)
}

// Only populated when job's state is JOB_STATE_FAILED or JOB_STATE_CANCELLED.
func (o LookupHyperparameterTuningJobResultOutput) Error() GoogleRpcStatusResponseOutput {
	return o.ApplyT(func(v LookupHyperparameterTuningJobResult) GoogleRpcStatusResponse { return v.Error }).(GoogleRpcStatusResponseOutput)
}

// The labels with user-defined metadata to organize HyperparameterTuningJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
func (o LookupHyperparameterTuningJobResultOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupHyperparameterTuningJobResult) map[string]string { return v.Labels }).(pulumi.StringMapOutput)
}

// The number of failed Trials that need to be seen before failing the HyperparameterTuningJob. If set to 0, Vertex AI decides how many Trials must fail before the whole job fails.
func (o LookupHyperparameterTuningJobResultOutput) MaxFailedTrialCount() pulumi.IntOutput {
	return o.ApplyT(func(v LookupHyperparameterTuningJobResult) int { return v.MaxFailedTrialCount }).(pulumi.IntOutput)
}

// The desired total number of Trials.
func (o LookupHyperparameterTuningJobResultOutput) MaxTrialCount() pulumi.IntOutput {
	return o.ApplyT(func(v LookupHyperparameterTuningJobResult) int { return v.MaxTrialCount }).(pulumi.IntOutput)
}

// Resource name of the HyperparameterTuningJob.
func (o LookupHyperparameterTuningJobResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHyperparameterTuningJobResult) string { return v.Name }).(pulumi.StringOutput)
}

// The desired number of Trials to run in parallel.
func (o LookupHyperparameterTuningJobResultOutput) ParallelTrialCount() pulumi.IntOutput {
	return o.ApplyT(func(v LookupHyperparameterTuningJobResult) int { return v.ParallelTrialCount }).(pulumi.IntOutput)
}

// Time when the HyperparameterTuningJob for the first time entered the `JOB_STATE_RUNNING` state.
func (o LookupHyperparameterTuningJobResultOutput) StartTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHyperparameterTuningJobResult) string { return v.StartTime }).(pulumi.StringOutput)
}

// The detailed state of the job.
func (o LookupHyperparameterTuningJobResultOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHyperparameterTuningJobResult) string { return v.State }).(pulumi.StringOutput)
}

// Study configuration of the HyperparameterTuningJob.
func (o LookupHyperparameterTuningJobResultOutput) StudySpec() GoogleCloudAiplatformV1beta1StudySpecResponseOutput {
	return o.ApplyT(func(v LookupHyperparameterTuningJobResult) GoogleCloudAiplatformV1beta1StudySpecResponse {
		return v.StudySpec
	}).(GoogleCloudAiplatformV1beta1StudySpecResponseOutput)
}

// The spec of a trial job. The same spec applies to the CustomJobs created in all the trials.
func (o LookupHyperparameterTuningJobResultOutput) TrialJobSpec() GoogleCloudAiplatformV1beta1CustomJobSpecResponseOutput {
	return o.ApplyT(func(v LookupHyperparameterTuningJobResult) GoogleCloudAiplatformV1beta1CustomJobSpecResponse {
		return v.TrialJobSpec
	}).(GoogleCloudAiplatformV1beta1CustomJobSpecResponseOutput)
}

// Trials of the HyperparameterTuningJob.
func (o LookupHyperparameterTuningJobResultOutput) Trials() GoogleCloudAiplatformV1beta1TrialResponseArrayOutput {
	return o.ApplyT(func(v LookupHyperparameterTuningJobResult) []GoogleCloudAiplatformV1beta1TrialResponse {
		return v.Trials
	}).(GoogleCloudAiplatformV1beta1TrialResponseArrayOutput)
}

// Time when the HyperparameterTuningJob was most recently updated.
func (o LookupHyperparameterTuningJobResultOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHyperparameterTuningJobResult) string { return v.UpdateTime }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupHyperparameterTuningJobResultOutput{})
}
