// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Required. Type of fade animation: `FADE_IN` or `FADE_OUT`.
type AnimationFadeFadeType string

const (
	// The fade type is not specified.
	AnimationFadeFadeTypeFadeTypeUnspecified = AnimationFadeFadeType("FADE_TYPE_UNSPECIFIED")
	// Fade the overlay object into view.
	AnimationFadeFadeTypeFadeIn = AnimationFadeFadeType("FADE_IN")
	// Fade the overlay object out of view.
	AnimationFadeFadeTypeFadeOut = AnimationFadeFadeType("FADE_OUT")
)

func (AnimationFadeFadeType) ElementType() reflect.Type {
	return reflect.TypeOf((*AnimationFadeFadeType)(nil)).Elem()
}

func (e AnimationFadeFadeType) ToAnimationFadeFadeTypeOutput() AnimationFadeFadeTypeOutput {
	return pulumi.ToOutput(e).(AnimationFadeFadeTypeOutput)
}

func (e AnimationFadeFadeType) ToAnimationFadeFadeTypeOutputWithContext(ctx context.Context) AnimationFadeFadeTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(AnimationFadeFadeTypeOutput)
}

func (e AnimationFadeFadeType) ToAnimationFadeFadeTypePtrOutput() AnimationFadeFadeTypePtrOutput {
	return e.ToAnimationFadeFadeTypePtrOutputWithContext(context.Background())
}

func (e AnimationFadeFadeType) ToAnimationFadeFadeTypePtrOutputWithContext(ctx context.Context) AnimationFadeFadeTypePtrOutput {
	return AnimationFadeFadeType(e).ToAnimationFadeFadeTypeOutputWithContext(ctx).ToAnimationFadeFadeTypePtrOutputWithContext(ctx)
}

func (e AnimationFadeFadeType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e AnimationFadeFadeType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e AnimationFadeFadeType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e AnimationFadeFadeType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type AnimationFadeFadeTypeOutput struct{ *pulumi.OutputState }

func (AnimationFadeFadeTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AnimationFadeFadeType)(nil)).Elem()
}

func (o AnimationFadeFadeTypeOutput) ToAnimationFadeFadeTypeOutput() AnimationFadeFadeTypeOutput {
	return o
}

func (o AnimationFadeFadeTypeOutput) ToAnimationFadeFadeTypeOutputWithContext(ctx context.Context) AnimationFadeFadeTypeOutput {
	return o
}

func (o AnimationFadeFadeTypeOutput) ToAnimationFadeFadeTypePtrOutput() AnimationFadeFadeTypePtrOutput {
	return o.ToAnimationFadeFadeTypePtrOutputWithContext(context.Background())
}

func (o AnimationFadeFadeTypeOutput) ToAnimationFadeFadeTypePtrOutputWithContext(ctx context.Context) AnimationFadeFadeTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v AnimationFadeFadeType) *AnimationFadeFadeType {
		return &v
	}).(AnimationFadeFadeTypePtrOutput)
}

func (o AnimationFadeFadeTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o AnimationFadeFadeTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AnimationFadeFadeType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o AnimationFadeFadeTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AnimationFadeFadeTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AnimationFadeFadeType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type AnimationFadeFadeTypePtrOutput struct{ *pulumi.OutputState }

func (AnimationFadeFadeTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AnimationFadeFadeType)(nil)).Elem()
}

func (o AnimationFadeFadeTypePtrOutput) ToAnimationFadeFadeTypePtrOutput() AnimationFadeFadeTypePtrOutput {
	return o
}

func (o AnimationFadeFadeTypePtrOutput) ToAnimationFadeFadeTypePtrOutputWithContext(ctx context.Context) AnimationFadeFadeTypePtrOutput {
	return o
}

func (o AnimationFadeFadeTypePtrOutput) Elem() AnimationFadeFadeTypeOutput {
	return o.ApplyT(func(v *AnimationFadeFadeType) AnimationFadeFadeType {
		if v != nil {
			return *v
		}
		var ret AnimationFadeFadeType
		return ret
	}).(AnimationFadeFadeTypeOutput)
}

func (o AnimationFadeFadeTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AnimationFadeFadeTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *AnimationFadeFadeType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// AnimationFadeFadeTypeInput is an input type that accepts values of the AnimationFadeFadeType enum
// A concrete instance of `AnimationFadeFadeTypeInput` can be one of the following:
//
//	AnimationFadeFadeTypeFadeTypeUnspecified
//	AnimationFadeFadeTypeFadeIn
//	AnimationFadeFadeTypeFadeOut
type AnimationFadeFadeTypeInput interface {
	pulumi.Input

	ToAnimationFadeFadeTypeOutput() AnimationFadeFadeTypeOutput
	ToAnimationFadeFadeTypeOutputWithContext(context.Context) AnimationFadeFadeTypeOutput
}

var animationFadeFadeTypePtrType = reflect.TypeOf((**AnimationFadeFadeType)(nil)).Elem()

type AnimationFadeFadeTypePtrInput interface {
	pulumi.Input

	ToAnimationFadeFadeTypePtrOutput() AnimationFadeFadeTypePtrOutput
	ToAnimationFadeFadeTypePtrOutputWithContext(context.Context) AnimationFadeFadeTypePtrOutput
}

type animationFadeFadeTypePtr string

func AnimationFadeFadeTypePtr(v string) AnimationFadeFadeTypePtrInput {
	return (*animationFadeFadeTypePtr)(&v)
}

func (*animationFadeFadeTypePtr) ElementType() reflect.Type {
	return animationFadeFadeTypePtrType
}

func (in *animationFadeFadeTypePtr) ToAnimationFadeFadeTypePtrOutput() AnimationFadeFadeTypePtrOutput {
	return pulumi.ToOutput(in).(AnimationFadeFadeTypePtrOutput)
}

func (in *animationFadeFadeTypePtr) ToAnimationFadeFadeTypePtrOutputWithContext(ctx context.Context) AnimationFadeFadeTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(AnimationFadeFadeTypePtrOutput)
}

// The segment reference scheme for a `DASH` manifest. The default is `SEGMENT_LIST`.
type DashConfigSegmentReferenceScheme string

const (
	// The segment reference scheme is not specified.
	DashConfigSegmentReferenceSchemeSegmentReferenceSchemeUnspecified = DashConfigSegmentReferenceScheme("SEGMENT_REFERENCE_SCHEME_UNSPECIFIED")
	// Explicitly lists the URLs of media files for each segment. For example, if SegmentSettings.individual_segments is `true`, then the manifest contains fields similar to the following: ``` xml ...  ```
	DashConfigSegmentReferenceSchemeSegmentList = DashConfigSegmentReferenceScheme("SEGMENT_LIST")
	// SegmentSettings.individual_segments must be set to `true` to use this segment reference scheme. Uses the DASH specification `` tag to determine the URLs of media files for each segment. For example: ``` xml ...  ```
	DashConfigSegmentReferenceSchemeSegmentTemplateNumber = DashConfigSegmentReferenceScheme("SEGMENT_TEMPLATE_NUMBER")
)

func (DashConfigSegmentReferenceScheme) ElementType() reflect.Type {
	return reflect.TypeOf((*DashConfigSegmentReferenceScheme)(nil)).Elem()
}

func (e DashConfigSegmentReferenceScheme) ToDashConfigSegmentReferenceSchemeOutput() DashConfigSegmentReferenceSchemeOutput {
	return pulumi.ToOutput(e).(DashConfigSegmentReferenceSchemeOutput)
}

func (e DashConfigSegmentReferenceScheme) ToDashConfigSegmentReferenceSchemeOutputWithContext(ctx context.Context) DashConfigSegmentReferenceSchemeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(DashConfigSegmentReferenceSchemeOutput)
}

func (e DashConfigSegmentReferenceScheme) ToDashConfigSegmentReferenceSchemePtrOutput() DashConfigSegmentReferenceSchemePtrOutput {
	return e.ToDashConfigSegmentReferenceSchemePtrOutputWithContext(context.Background())
}

func (e DashConfigSegmentReferenceScheme) ToDashConfigSegmentReferenceSchemePtrOutputWithContext(ctx context.Context) DashConfigSegmentReferenceSchemePtrOutput {
	return DashConfigSegmentReferenceScheme(e).ToDashConfigSegmentReferenceSchemeOutputWithContext(ctx).ToDashConfigSegmentReferenceSchemePtrOutputWithContext(ctx)
}

func (e DashConfigSegmentReferenceScheme) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e DashConfigSegmentReferenceScheme) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e DashConfigSegmentReferenceScheme) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e DashConfigSegmentReferenceScheme) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type DashConfigSegmentReferenceSchemeOutput struct{ *pulumi.OutputState }

func (DashConfigSegmentReferenceSchemeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DashConfigSegmentReferenceScheme)(nil)).Elem()
}

func (o DashConfigSegmentReferenceSchemeOutput) ToDashConfigSegmentReferenceSchemeOutput() DashConfigSegmentReferenceSchemeOutput {
	return o
}

func (o DashConfigSegmentReferenceSchemeOutput) ToDashConfigSegmentReferenceSchemeOutputWithContext(ctx context.Context) DashConfigSegmentReferenceSchemeOutput {
	return o
}

func (o DashConfigSegmentReferenceSchemeOutput) ToDashConfigSegmentReferenceSchemePtrOutput() DashConfigSegmentReferenceSchemePtrOutput {
	return o.ToDashConfigSegmentReferenceSchemePtrOutputWithContext(context.Background())
}

func (o DashConfigSegmentReferenceSchemeOutput) ToDashConfigSegmentReferenceSchemePtrOutputWithContext(ctx context.Context) DashConfigSegmentReferenceSchemePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v DashConfigSegmentReferenceScheme) *DashConfigSegmentReferenceScheme {
		return &v
	}).(DashConfigSegmentReferenceSchemePtrOutput)
}

func (o DashConfigSegmentReferenceSchemeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o DashConfigSegmentReferenceSchemeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DashConfigSegmentReferenceScheme) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o DashConfigSegmentReferenceSchemeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DashConfigSegmentReferenceSchemeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DashConfigSegmentReferenceScheme) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type DashConfigSegmentReferenceSchemePtrOutput struct{ *pulumi.OutputState }

func (DashConfigSegmentReferenceSchemePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DashConfigSegmentReferenceScheme)(nil)).Elem()
}

func (o DashConfigSegmentReferenceSchemePtrOutput) ToDashConfigSegmentReferenceSchemePtrOutput() DashConfigSegmentReferenceSchemePtrOutput {
	return o
}

func (o DashConfigSegmentReferenceSchemePtrOutput) ToDashConfigSegmentReferenceSchemePtrOutputWithContext(ctx context.Context) DashConfigSegmentReferenceSchemePtrOutput {
	return o
}

func (o DashConfigSegmentReferenceSchemePtrOutput) Elem() DashConfigSegmentReferenceSchemeOutput {
	return o.ApplyT(func(v *DashConfigSegmentReferenceScheme) DashConfigSegmentReferenceScheme {
		if v != nil {
			return *v
		}
		var ret DashConfigSegmentReferenceScheme
		return ret
	}).(DashConfigSegmentReferenceSchemeOutput)
}

func (o DashConfigSegmentReferenceSchemePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DashConfigSegmentReferenceSchemePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *DashConfigSegmentReferenceScheme) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// DashConfigSegmentReferenceSchemeInput is an input type that accepts values of the DashConfigSegmentReferenceScheme enum
// A concrete instance of `DashConfigSegmentReferenceSchemeInput` can be one of the following:
//
//	DashConfigSegmentReferenceSchemeSegmentReferenceSchemeUnspecified
//	DashConfigSegmentReferenceSchemeSegmentList
//	DashConfigSegmentReferenceSchemeSegmentTemplateNumber
type DashConfigSegmentReferenceSchemeInput interface {
	pulumi.Input

	ToDashConfigSegmentReferenceSchemeOutput() DashConfigSegmentReferenceSchemeOutput
	ToDashConfigSegmentReferenceSchemeOutputWithContext(context.Context) DashConfigSegmentReferenceSchemeOutput
}

var dashConfigSegmentReferenceSchemePtrType = reflect.TypeOf((**DashConfigSegmentReferenceScheme)(nil)).Elem()

type DashConfigSegmentReferenceSchemePtrInput interface {
	pulumi.Input

	ToDashConfigSegmentReferenceSchemePtrOutput() DashConfigSegmentReferenceSchemePtrOutput
	ToDashConfigSegmentReferenceSchemePtrOutputWithContext(context.Context) DashConfigSegmentReferenceSchemePtrOutput
}

type dashConfigSegmentReferenceSchemePtr string

func DashConfigSegmentReferenceSchemePtr(v string) DashConfigSegmentReferenceSchemePtrInput {
	return (*dashConfigSegmentReferenceSchemePtr)(&v)
}

func (*dashConfigSegmentReferenceSchemePtr) ElementType() reflect.Type {
	return dashConfigSegmentReferenceSchemePtrType
}

func (in *dashConfigSegmentReferenceSchemePtr) ToDashConfigSegmentReferenceSchemePtrOutput() DashConfigSegmentReferenceSchemePtrOutput {
	return pulumi.ToOutput(in).(DashConfigSegmentReferenceSchemePtrOutput)
}

func (in *dashConfigSegmentReferenceSchemePtr) ToDashConfigSegmentReferenceSchemePtrOutputWithContext(ctx context.Context) DashConfigSegmentReferenceSchemePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(DashConfigSegmentReferenceSchemePtrOutput)
}

// The processing mode of the job. The default is `PROCESSING_MODE_INTERACTIVE`.
type JobMode string

const (
	// The job processing mode is not specified.
	JobModeProcessingModeUnspecified = JobMode("PROCESSING_MODE_UNSPECIFIED")
	// The job processing mode is interactive mode. Interactive job will either be ran or rejected if quota does not allow for it.
	JobModeProcessingModeInteractive = JobMode("PROCESSING_MODE_INTERACTIVE")
	// The job processing mode is batch mode. Batch mode allows queuing of jobs.
	JobModeProcessingModeBatch = JobMode("PROCESSING_MODE_BATCH")
)

func (JobMode) ElementType() reflect.Type {
	return reflect.TypeOf((*JobMode)(nil)).Elem()
}

func (e JobMode) ToJobModeOutput() JobModeOutput {
	return pulumi.ToOutput(e).(JobModeOutput)
}

func (e JobMode) ToJobModeOutputWithContext(ctx context.Context) JobModeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(JobModeOutput)
}

func (e JobMode) ToJobModePtrOutput() JobModePtrOutput {
	return e.ToJobModePtrOutputWithContext(context.Background())
}

func (e JobMode) ToJobModePtrOutputWithContext(ctx context.Context) JobModePtrOutput {
	return JobMode(e).ToJobModeOutputWithContext(ctx).ToJobModePtrOutputWithContext(ctx)
}

func (e JobMode) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e JobMode) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e JobMode) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e JobMode) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type JobModeOutput struct{ *pulumi.OutputState }

func (JobModeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*JobMode)(nil)).Elem()
}

func (o JobModeOutput) ToJobModeOutput() JobModeOutput {
	return o
}

func (o JobModeOutput) ToJobModeOutputWithContext(ctx context.Context) JobModeOutput {
	return o
}

func (o JobModeOutput) ToJobModePtrOutput() JobModePtrOutput {
	return o.ToJobModePtrOutputWithContext(context.Background())
}

func (o JobModeOutput) ToJobModePtrOutputWithContext(ctx context.Context) JobModePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v JobMode) *JobMode {
		return &v
	}).(JobModePtrOutput)
}

func (o JobModeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o JobModeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e JobMode) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o JobModeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o JobModeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e JobMode) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type JobModePtrOutput struct{ *pulumi.OutputState }

func (JobModePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**JobMode)(nil)).Elem()
}

func (o JobModePtrOutput) ToJobModePtrOutput() JobModePtrOutput {
	return o
}

func (o JobModePtrOutput) ToJobModePtrOutputWithContext(ctx context.Context) JobModePtrOutput {
	return o
}

func (o JobModePtrOutput) Elem() JobModeOutput {
	return o.ApplyT(func(v *JobMode) JobMode {
		if v != nil {
			return *v
		}
		var ret JobMode
		return ret
	}).(JobModeOutput)
}

func (o JobModePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o JobModePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *JobMode) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// JobModeInput is an input type that accepts values of the JobMode enum
// A concrete instance of `JobModeInput` can be one of the following:
//
//	JobModeProcessingModeUnspecified
//	JobModeProcessingModeInteractive
//	JobModeProcessingModeBatch
type JobModeInput interface {
	pulumi.Input

	ToJobModeOutput() JobModeOutput
	ToJobModeOutputWithContext(context.Context) JobModeOutput
}

var jobModePtrType = reflect.TypeOf((**JobMode)(nil)).Elem()

type JobModePtrInput interface {
	pulumi.Input

	ToJobModePtrOutput() JobModePtrOutput
	ToJobModePtrOutputWithContext(context.Context) JobModePtrOutput
}

type jobModePtr string

func JobModePtr(v string) JobModePtrInput {
	return (*jobModePtr)(&v)
}

func (*jobModePtr) ElementType() reflect.Type {
	return jobModePtrType
}

func (in *jobModePtr) ToJobModePtrOutput() JobModePtrOutput {
	return pulumi.ToOutput(in).(JobModePtrOutput)
}

func (in *jobModePtr) ToJobModePtrOutputWithContext(ctx context.Context) JobModePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(JobModePtrOutput)
}

// Optional. The optimization strategy of the job. The default is `AUTODETECT`.
type JobOptimization string

const (
	// The optimization strategy is not specified.
	JobOptimizationOptimizationStrategyUnspecified = JobOptimization("OPTIMIZATION_STRATEGY_UNSPECIFIED")
	// Prioritize job processing speed.
	JobOptimizationAutodetect = JobOptimization("AUTODETECT")
	// Disable all optimizations.
	JobOptimizationDisabled = JobOptimization("DISABLED")
)

func (JobOptimization) ElementType() reflect.Type {
	return reflect.TypeOf((*JobOptimization)(nil)).Elem()
}

func (e JobOptimization) ToJobOptimizationOutput() JobOptimizationOutput {
	return pulumi.ToOutput(e).(JobOptimizationOutput)
}

func (e JobOptimization) ToJobOptimizationOutputWithContext(ctx context.Context) JobOptimizationOutput {
	return pulumi.ToOutputWithContext(ctx, e).(JobOptimizationOutput)
}

func (e JobOptimization) ToJobOptimizationPtrOutput() JobOptimizationPtrOutput {
	return e.ToJobOptimizationPtrOutputWithContext(context.Background())
}

func (e JobOptimization) ToJobOptimizationPtrOutputWithContext(ctx context.Context) JobOptimizationPtrOutput {
	return JobOptimization(e).ToJobOptimizationOutputWithContext(ctx).ToJobOptimizationPtrOutputWithContext(ctx)
}

func (e JobOptimization) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e JobOptimization) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e JobOptimization) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e JobOptimization) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type JobOptimizationOutput struct{ *pulumi.OutputState }

func (JobOptimizationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*JobOptimization)(nil)).Elem()
}

func (o JobOptimizationOutput) ToJobOptimizationOutput() JobOptimizationOutput {
	return o
}

func (o JobOptimizationOutput) ToJobOptimizationOutputWithContext(ctx context.Context) JobOptimizationOutput {
	return o
}

func (o JobOptimizationOutput) ToJobOptimizationPtrOutput() JobOptimizationPtrOutput {
	return o.ToJobOptimizationPtrOutputWithContext(context.Background())
}

func (o JobOptimizationOutput) ToJobOptimizationPtrOutputWithContext(ctx context.Context) JobOptimizationPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v JobOptimization) *JobOptimization {
		return &v
	}).(JobOptimizationPtrOutput)
}

func (o JobOptimizationOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o JobOptimizationOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e JobOptimization) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o JobOptimizationOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o JobOptimizationOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e JobOptimization) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type JobOptimizationPtrOutput struct{ *pulumi.OutputState }

func (JobOptimizationPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**JobOptimization)(nil)).Elem()
}

func (o JobOptimizationPtrOutput) ToJobOptimizationPtrOutput() JobOptimizationPtrOutput {
	return o
}

func (o JobOptimizationPtrOutput) ToJobOptimizationPtrOutputWithContext(ctx context.Context) JobOptimizationPtrOutput {
	return o
}

func (o JobOptimizationPtrOutput) Elem() JobOptimizationOutput {
	return o.ApplyT(func(v *JobOptimization) JobOptimization {
		if v != nil {
			return *v
		}
		var ret JobOptimization
		return ret
	}).(JobOptimizationOutput)
}

func (o JobOptimizationPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o JobOptimizationPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *JobOptimization) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// JobOptimizationInput is an input type that accepts values of the JobOptimization enum
// A concrete instance of `JobOptimizationInput` can be one of the following:
//
//	JobOptimizationOptimizationStrategyUnspecified
//	JobOptimizationAutodetect
//	JobOptimizationDisabled
type JobOptimizationInput interface {
	pulumi.Input

	ToJobOptimizationOutput() JobOptimizationOutput
	ToJobOptimizationOutputWithContext(context.Context) JobOptimizationOutput
}

var jobOptimizationPtrType = reflect.TypeOf((**JobOptimization)(nil)).Elem()

type JobOptimizationPtrInput interface {
	pulumi.Input

	ToJobOptimizationPtrOutput() JobOptimizationPtrOutput
	ToJobOptimizationPtrOutputWithContext(context.Context) JobOptimizationPtrOutput
}

type jobOptimizationPtr string

func JobOptimizationPtr(v string) JobOptimizationPtrInput {
	return (*jobOptimizationPtr)(&v)
}

func (*jobOptimizationPtr) ElementType() reflect.Type {
	return jobOptimizationPtrType
}

func (in *jobOptimizationPtr) ToJobOptimizationPtrOutput() JobOptimizationPtrOutput {
	return pulumi.ToOutput(in).(JobOptimizationPtrOutput)
}

func (in *jobOptimizationPtr) ToJobOptimizationPtrOutputWithContext(ctx context.Context) JobOptimizationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(JobOptimizationPtrOutput)
}

// Required. Type of the manifest.
type ManifestType string

const (
	// The manifest type is not specified.
	ManifestTypeManifestTypeUnspecified = ManifestType("MANIFEST_TYPE_UNSPECIFIED")
	// Create an HLS manifest. The corresponding file extension is `.m3u8`.
	ManifestTypeHls = ManifestType("HLS")
	// Create an MPEG-DASH manifest. The corresponding file extension is `.mpd`.
	ManifestTypeDash = ManifestType("DASH")
)

func (ManifestType) ElementType() reflect.Type {
	return reflect.TypeOf((*ManifestType)(nil)).Elem()
}

func (e ManifestType) ToManifestTypeOutput() ManifestTypeOutput {
	return pulumi.ToOutput(e).(ManifestTypeOutput)
}

func (e ManifestType) ToManifestTypeOutputWithContext(ctx context.Context) ManifestTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(ManifestTypeOutput)
}

func (e ManifestType) ToManifestTypePtrOutput() ManifestTypePtrOutput {
	return e.ToManifestTypePtrOutputWithContext(context.Background())
}

func (e ManifestType) ToManifestTypePtrOutputWithContext(ctx context.Context) ManifestTypePtrOutput {
	return ManifestType(e).ToManifestTypeOutputWithContext(ctx).ToManifestTypePtrOutputWithContext(ctx)
}

func (e ManifestType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e ManifestType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e ManifestType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e ManifestType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type ManifestTypeOutput struct{ *pulumi.OutputState }

func (ManifestTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ManifestType)(nil)).Elem()
}

func (o ManifestTypeOutput) ToManifestTypeOutput() ManifestTypeOutput {
	return o
}

func (o ManifestTypeOutput) ToManifestTypeOutputWithContext(ctx context.Context) ManifestTypeOutput {
	return o
}

func (o ManifestTypeOutput) ToManifestTypePtrOutput() ManifestTypePtrOutput {
	return o.ToManifestTypePtrOutputWithContext(context.Background())
}

func (o ManifestTypeOutput) ToManifestTypePtrOutputWithContext(ctx context.Context) ManifestTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ManifestType) *ManifestType {
		return &v
	}).(ManifestTypePtrOutput)
}

func (o ManifestTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o ManifestTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ManifestType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o ManifestTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ManifestTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ManifestType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type ManifestTypePtrOutput struct{ *pulumi.OutputState }

func (ManifestTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ManifestType)(nil)).Elem()
}

func (o ManifestTypePtrOutput) ToManifestTypePtrOutput() ManifestTypePtrOutput {
	return o
}

func (o ManifestTypePtrOutput) ToManifestTypePtrOutputWithContext(ctx context.Context) ManifestTypePtrOutput {
	return o
}

func (o ManifestTypePtrOutput) Elem() ManifestTypeOutput {
	return o.ApplyT(func(v *ManifestType) ManifestType {
		if v != nil {
			return *v
		}
		var ret ManifestType
		return ret
	}).(ManifestTypeOutput)
}

func (o ManifestTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ManifestTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *ManifestType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// ManifestTypeInput is an input type that accepts values of the ManifestType enum
// A concrete instance of `ManifestTypeInput` can be one of the following:
//
//	ManifestTypeManifestTypeUnspecified
//	ManifestTypeHls
//	ManifestTypeDash
type ManifestTypeInput interface {
	pulumi.Input

	ToManifestTypeOutput() ManifestTypeOutput
	ToManifestTypeOutputWithContext(context.Context) ManifestTypeOutput
}

var manifestTypePtrType = reflect.TypeOf((**ManifestType)(nil)).Elem()

type ManifestTypePtrInput interface {
	pulumi.Input

	ToManifestTypePtrOutput() ManifestTypePtrOutput
	ToManifestTypePtrOutputWithContext(context.Context) ManifestTypePtrOutput
}

type manifestTypePtr string

func ManifestTypePtr(v string) ManifestTypePtrInput {
	return (*manifestTypePtr)(&v)
}

func (*manifestTypePtr) ElementType() reflect.Type {
	return manifestTypePtrType
}

func (in *manifestTypePtr) ToManifestTypePtrOutput() ManifestTypePtrOutput {
	return pulumi.ToOutput(in).(ManifestTypePtrOutput)
}

func (in *manifestTypePtr) ToManifestTypePtrOutputWithContext(ctx context.Context) ManifestTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(ManifestTypePtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AnimationFadeFadeTypeInput)(nil)).Elem(), AnimationFadeFadeType("FADE_TYPE_UNSPECIFIED"))
	pulumi.RegisterInputType(reflect.TypeOf((*AnimationFadeFadeTypePtrInput)(nil)).Elem(), AnimationFadeFadeType("FADE_TYPE_UNSPECIFIED"))
	pulumi.RegisterInputType(reflect.TypeOf((*DashConfigSegmentReferenceSchemeInput)(nil)).Elem(), DashConfigSegmentReferenceScheme("SEGMENT_REFERENCE_SCHEME_UNSPECIFIED"))
	pulumi.RegisterInputType(reflect.TypeOf((*DashConfigSegmentReferenceSchemePtrInput)(nil)).Elem(), DashConfigSegmentReferenceScheme("SEGMENT_REFERENCE_SCHEME_UNSPECIFIED"))
	pulumi.RegisterInputType(reflect.TypeOf((*JobModeInput)(nil)).Elem(), JobMode("PROCESSING_MODE_UNSPECIFIED"))
	pulumi.RegisterInputType(reflect.TypeOf((*JobModePtrInput)(nil)).Elem(), JobMode("PROCESSING_MODE_UNSPECIFIED"))
	pulumi.RegisterInputType(reflect.TypeOf((*JobOptimizationInput)(nil)).Elem(), JobOptimization("OPTIMIZATION_STRATEGY_UNSPECIFIED"))
	pulumi.RegisterInputType(reflect.TypeOf((*JobOptimizationPtrInput)(nil)).Elem(), JobOptimization("OPTIMIZATION_STRATEGY_UNSPECIFIED"))
	pulumi.RegisterInputType(reflect.TypeOf((*ManifestTypeInput)(nil)).Elem(), ManifestType("MANIFEST_TYPE_UNSPECIFIED"))
	pulumi.RegisterInputType(reflect.TypeOf((*ManifestTypePtrInput)(nil)).Elem(), ManifestType("MANIFEST_TYPE_UNSPECIFIED"))
	pulumi.RegisterOutputType(AnimationFadeFadeTypeOutput{})
	pulumi.RegisterOutputType(AnimationFadeFadeTypePtrOutput{})
	pulumi.RegisterOutputType(DashConfigSegmentReferenceSchemeOutput{})
	pulumi.RegisterOutputType(DashConfigSegmentReferenceSchemePtrOutput{})
	pulumi.RegisterOutputType(JobModeOutput{})
	pulumi.RegisterOutputType(JobModePtrOutput{})
	pulumi.RegisterOutputType(JobOptimizationOutput{})
	pulumi.RegisterOutputType(JobOptimizationPtrOutput{})
	pulumi.RegisterOutputType(ManifestTypeOutput{})
	pulumi.RegisterOutputType(ManifestTypePtrOutput{})
}
