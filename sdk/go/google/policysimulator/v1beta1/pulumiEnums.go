// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1beta1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The logs to use as input for the Replay.
type GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource string

const (
	// An unspecified log source. If the log source is unspecified, the Replay defaults to using `RECENT_ACCESSES`.
	GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceLogSourceUnspecified = GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource("LOG_SOURCE_UNSPECIFIED")
	// All access logs from the last 90 days. These logs may not include logs from the most recent 7 days.
	GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceRecentAccesses = GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource("RECENT_ACCESSES")
)

func (GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource) ElementType() reflect.Type {
	return reflect.TypeOf((*GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource)(nil)).Elem()
}

func (e GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource) ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput() GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput {
	return pulumi.ToOutput(e).(GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput)
}

func (e GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource) ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutputWithContext(ctx context.Context) GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput {
	return pulumi.ToOutputWithContext(ctx, e).(GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput)
}

func (e GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource) ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput() GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput {
	return e.ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutputWithContext(context.Background())
}

func (e GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource) ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutputWithContext(ctx context.Context) GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput {
	return GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource(e).ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutputWithContext(ctx).ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutputWithContext(ctx)
}

func (e GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput struct{ *pulumi.OutputState }

func (GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource)(nil)).Elem()
}

func (o GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput) ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput() GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput {
	return o
}

func (o GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput) ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutputWithContext(ctx context.Context) GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput {
	return o
}

func (o GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput) ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput() GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput {
	return o.ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutputWithContext(context.Background())
}

func (o GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput) ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutputWithContext(ctx context.Context) GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource) *GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource {
		return &v
	}).(GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput)
}

func (o GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput struct{ *pulumi.OutputState }

func (GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource)(nil)).Elem()
}

func (o GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput) ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput() GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput {
	return o
}

func (o GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput) ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutputWithContext(ctx context.Context) GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput {
	return o
}

func (o GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput) Elem() GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput {
	return o.ApplyT(func(v *GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource) GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource {
		if v != nil {
			return *v
		}
		var ret GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource
		return ret
	}).(GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput)
}

func (o GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceInput is an input type that accepts values of the GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource enum
// A concrete instance of `GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceInput` can be one of the following:
//
//	GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceLogSourceUnspecified
//	GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceRecentAccesses
type GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceInput interface {
	pulumi.Input

	ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput() GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput
	ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutputWithContext(context.Context) GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput
}

var googleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrType = reflect.TypeOf((**GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource)(nil)).Elem()

type GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrInput interface {
	pulumi.Input

	ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput() GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput
	ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutputWithContext(context.Context) GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput
}

type googleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtr string

func GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtr(v string) GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrInput {
	return (*googleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtr)(&v)
}

func (*googleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtr) ElementType() reflect.Type {
	return googleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrType
}

func (in *googleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtr) ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput() GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput {
	return pulumi.ToOutput(in).(GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput)
}

func (in *googleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtr) ToGoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutputWithContext(ctx context.Context) GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput)
}

// The log type that this config enables.
type GoogleIamV1AuditLogConfigLogType string

const (
	// Default case. Should never be this.
	GoogleIamV1AuditLogConfigLogTypeLogTypeUnspecified = GoogleIamV1AuditLogConfigLogType("LOG_TYPE_UNSPECIFIED")
	// Admin reads. Example: CloudIAM getIamPolicy
	GoogleIamV1AuditLogConfigLogTypeAdminRead = GoogleIamV1AuditLogConfigLogType("ADMIN_READ")
	// Data writes. Example: CloudSQL Users create
	GoogleIamV1AuditLogConfigLogTypeDataWrite = GoogleIamV1AuditLogConfigLogType("DATA_WRITE")
	// Data reads. Example: CloudSQL Users list
	GoogleIamV1AuditLogConfigLogTypeDataRead = GoogleIamV1AuditLogConfigLogType("DATA_READ")
)

func (GoogleIamV1AuditLogConfigLogType) ElementType() reflect.Type {
	return reflect.TypeOf((*GoogleIamV1AuditLogConfigLogType)(nil)).Elem()
}

func (e GoogleIamV1AuditLogConfigLogType) ToGoogleIamV1AuditLogConfigLogTypeOutput() GoogleIamV1AuditLogConfigLogTypeOutput {
	return pulumi.ToOutput(e).(GoogleIamV1AuditLogConfigLogTypeOutput)
}

func (e GoogleIamV1AuditLogConfigLogType) ToGoogleIamV1AuditLogConfigLogTypeOutputWithContext(ctx context.Context) GoogleIamV1AuditLogConfigLogTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(GoogleIamV1AuditLogConfigLogTypeOutput)
}

func (e GoogleIamV1AuditLogConfigLogType) ToGoogleIamV1AuditLogConfigLogTypePtrOutput() GoogleIamV1AuditLogConfigLogTypePtrOutput {
	return e.ToGoogleIamV1AuditLogConfigLogTypePtrOutputWithContext(context.Background())
}

func (e GoogleIamV1AuditLogConfigLogType) ToGoogleIamV1AuditLogConfigLogTypePtrOutputWithContext(ctx context.Context) GoogleIamV1AuditLogConfigLogTypePtrOutput {
	return GoogleIamV1AuditLogConfigLogType(e).ToGoogleIamV1AuditLogConfigLogTypeOutputWithContext(ctx).ToGoogleIamV1AuditLogConfigLogTypePtrOutputWithContext(ctx)
}

func (e GoogleIamV1AuditLogConfigLogType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e GoogleIamV1AuditLogConfigLogType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e GoogleIamV1AuditLogConfigLogType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e GoogleIamV1AuditLogConfigLogType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type GoogleIamV1AuditLogConfigLogTypeOutput struct{ *pulumi.OutputState }

func (GoogleIamV1AuditLogConfigLogTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GoogleIamV1AuditLogConfigLogType)(nil)).Elem()
}

func (o GoogleIamV1AuditLogConfigLogTypeOutput) ToGoogleIamV1AuditLogConfigLogTypeOutput() GoogleIamV1AuditLogConfigLogTypeOutput {
	return o
}

func (o GoogleIamV1AuditLogConfigLogTypeOutput) ToGoogleIamV1AuditLogConfigLogTypeOutputWithContext(ctx context.Context) GoogleIamV1AuditLogConfigLogTypeOutput {
	return o
}

func (o GoogleIamV1AuditLogConfigLogTypeOutput) ToGoogleIamV1AuditLogConfigLogTypePtrOutput() GoogleIamV1AuditLogConfigLogTypePtrOutput {
	return o.ToGoogleIamV1AuditLogConfigLogTypePtrOutputWithContext(context.Background())
}

func (o GoogleIamV1AuditLogConfigLogTypeOutput) ToGoogleIamV1AuditLogConfigLogTypePtrOutputWithContext(ctx context.Context) GoogleIamV1AuditLogConfigLogTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v GoogleIamV1AuditLogConfigLogType) *GoogleIamV1AuditLogConfigLogType {
		return &v
	}).(GoogleIamV1AuditLogConfigLogTypePtrOutput)
}

func (o GoogleIamV1AuditLogConfigLogTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o GoogleIamV1AuditLogConfigLogTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e GoogleIamV1AuditLogConfigLogType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o GoogleIamV1AuditLogConfigLogTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o GoogleIamV1AuditLogConfigLogTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e GoogleIamV1AuditLogConfigLogType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type GoogleIamV1AuditLogConfigLogTypePtrOutput struct{ *pulumi.OutputState }

func (GoogleIamV1AuditLogConfigLogTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**GoogleIamV1AuditLogConfigLogType)(nil)).Elem()
}

func (o GoogleIamV1AuditLogConfigLogTypePtrOutput) ToGoogleIamV1AuditLogConfigLogTypePtrOutput() GoogleIamV1AuditLogConfigLogTypePtrOutput {
	return o
}

func (o GoogleIamV1AuditLogConfigLogTypePtrOutput) ToGoogleIamV1AuditLogConfigLogTypePtrOutputWithContext(ctx context.Context) GoogleIamV1AuditLogConfigLogTypePtrOutput {
	return o
}

func (o GoogleIamV1AuditLogConfigLogTypePtrOutput) Elem() GoogleIamV1AuditLogConfigLogTypeOutput {
	return o.ApplyT(func(v *GoogleIamV1AuditLogConfigLogType) GoogleIamV1AuditLogConfigLogType {
		if v != nil {
			return *v
		}
		var ret GoogleIamV1AuditLogConfigLogType
		return ret
	}).(GoogleIamV1AuditLogConfigLogTypeOutput)
}

func (o GoogleIamV1AuditLogConfigLogTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o GoogleIamV1AuditLogConfigLogTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *GoogleIamV1AuditLogConfigLogType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// GoogleIamV1AuditLogConfigLogTypeInput is an input type that accepts values of the GoogleIamV1AuditLogConfigLogType enum
// A concrete instance of `GoogleIamV1AuditLogConfigLogTypeInput` can be one of the following:
//
//	GoogleIamV1AuditLogConfigLogTypeLogTypeUnspecified
//	GoogleIamV1AuditLogConfigLogTypeAdminRead
//	GoogleIamV1AuditLogConfigLogTypeDataWrite
//	GoogleIamV1AuditLogConfigLogTypeDataRead
type GoogleIamV1AuditLogConfigLogTypeInput interface {
	pulumi.Input

	ToGoogleIamV1AuditLogConfigLogTypeOutput() GoogleIamV1AuditLogConfigLogTypeOutput
	ToGoogleIamV1AuditLogConfigLogTypeOutputWithContext(context.Context) GoogleIamV1AuditLogConfigLogTypeOutput
}

var googleIamV1AuditLogConfigLogTypePtrType = reflect.TypeOf((**GoogleIamV1AuditLogConfigLogType)(nil)).Elem()

type GoogleIamV1AuditLogConfigLogTypePtrInput interface {
	pulumi.Input

	ToGoogleIamV1AuditLogConfigLogTypePtrOutput() GoogleIamV1AuditLogConfigLogTypePtrOutput
	ToGoogleIamV1AuditLogConfigLogTypePtrOutputWithContext(context.Context) GoogleIamV1AuditLogConfigLogTypePtrOutput
}

type googleIamV1AuditLogConfigLogTypePtr string

func GoogleIamV1AuditLogConfigLogTypePtr(v string) GoogleIamV1AuditLogConfigLogTypePtrInput {
	return (*googleIamV1AuditLogConfigLogTypePtr)(&v)
}

func (*googleIamV1AuditLogConfigLogTypePtr) ElementType() reflect.Type {
	return googleIamV1AuditLogConfigLogTypePtrType
}

func (in *googleIamV1AuditLogConfigLogTypePtr) ToGoogleIamV1AuditLogConfigLogTypePtrOutput() GoogleIamV1AuditLogConfigLogTypePtrOutput {
	return pulumi.ToOutput(in).(GoogleIamV1AuditLogConfigLogTypePtrOutput)
}

func (in *googleIamV1AuditLogConfigLogTypePtr) ToGoogleIamV1AuditLogConfigLogTypePtrOutputWithContext(ctx context.Context) GoogleIamV1AuditLogConfigLogTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(GoogleIamV1AuditLogConfigLogTypePtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceInput)(nil)).Elem(), GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource("LOG_SOURCE_UNSPECIFIED"))
	pulumi.RegisterInputType(reflect.TypeOf((*GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrInput)(nil)).Elem(), GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSource("LOG_SOURCE_UNSPECIFIED"))
	pulumi.RegisterInputType(reflect.TypeOf((*GoogleIamV1AuditLogConfigLogTypeInput)(nil)).Elem(), GoogleIamV1AuditLogConfigLogType("LOG_TYPE_UNSPECIFIED"))
	pulumi.RegisterInputType(reflect.TypeOf((*GoogleIamV1AuditLogConfigLogTypePtrInput)(nil)).Elem(), GoogleIamV1AuditLogConfigLogType("LOG_TYPE_UNSPECIFIED"))
	pulumi.RegisterOutputType(GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourceOutput{})
	pulumi.RegisterOutputType(GoogleCloudPolicysimulatorV1beta1ReplayConfigLogSourcePtrOutput{})
	pulumi.RegisterOutputType(GoogleIamV1AuditLogConfigLogTypeOutput{})
	pulumi.RegisterOutputType(GoogleIamV1AuditLogConfigLogTypePtrOutput{})
}
