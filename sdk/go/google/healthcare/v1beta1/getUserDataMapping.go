// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1beta1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Gets the specified User data mapping.
func LookupUserDataMapping(ctx *pulumi.Context, args *LookupUserDataMappingArgs, opts ...pulumi.InvokeOption) (*LookupUserDataMappingResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupUserDataMappingResult
	err := ctx.Invoke("google-native:healthcare/v1beta1:getUserDataMapping", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupUserDataMappingArgs struct {
	ConsentStoreId    string  `pulumi:"consentStoreId"`
	DatasetId         string  `pulumi:"datasetId"`
	Location          string  `pulumi:"location"`
	Project           *string `pulumi:"project"`
	UserDataMappingId string  `pulumi:"userDataMappingId"`
}

type LookupUserDataMappingResult struct {
	// Indicates the time when this mapping was archived.
	ArchiveTime string `pulumi:"archiveTime"`
	// Indicates whether this mapping is archived.
	Archived bool `pulumi:"archived"`
	// A unique identifier for the mapped resource.
	DataId string `pulumi:"dataId"`
	// Resource name of the User data mapping, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/userDataMappings/{user_data_mapping_id}`.
	Name string `pulumi:"name"`
	// Attributes of the resource. Only explicitly set attributes are displayed here. Attribute definitions with defaults set implicitly apply to these User data mappings. Attributes listed here must be single valued, that is, exactly one value is specified for the field "values" in each Attribute.
	ResourceAttributes []AttributeResponse `pulumi:"resourceAttributes"`
	// User's UUID provided by the client.
	UserId string `pulumi:"userId"`
}

func LookupUserDataMappingOutput(ctx *pulumi.Context, args LookupUserDataMappingOutputArgs, opts ...pulumi.InvokeOption) LookupUserDataMappingResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupUserDataMappingResult, error) {
			args := v.(LookupUserDataMappingArgs)
			r, err := LookupUserDataMapping(ctx, &args, opts...)
			var s LookupUserDataMappingResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupUserDataMappingResultOutput)
}

type LookupUserDataMappingOutputArgs struct {
	ConsentStoreId    pulumi.StringInput    `pulumi:"consentStoreId"`
	DatasetId         pulumi.StringInput    `pulumi:"datasetId"`
	Location          pulumi.StringInput    `pulumi:"location"`
	Project           pulumi.StringPtrInput `pulumi:"project"`
	UserDataMappingId pulumi.StringInput    `pulumi:"userDataMappingId"`
}

func (LookupUserDataMappingOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupUserDataMappingArgs)(nil)).Elem()
}

type LookupUserDataMappingResultOutput struct{ *pulumi.OutputState }

func (LookupUserDataMappingResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupUserDataMappingResult)(nil)).Elem()
}

func (o LookupUserDataMappingResultOutput) ToLookupUserDataMappingResultOutput() LookupUserDataMappingResultOutput {
	return o
}

func (o LookupUserDataMappingResultOutput) ToLookupUserDataMappingResultOutputWithContext(ctx context.Context) LookupUserDataMappingResultOutput {
	return o
}

// Indicates the time when this mapping was archived.
func (o LookupUserDataMappingResultOutput) ArchiveTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupUserDataMappingResult) string { return v.ArchiveTime }).(pulumi.StringOutput)
}

// Indicates whether this mapping is archived.
func (o LookupUserDataMappingResultOutput) Archived() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupUserDataMappingResult) bool { return v.Archived }).(pulumi.BoolOutput)
}

// A unique identifier for the mapped resource.
func (o LookupUserDataMappingResultOutput) DataId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupUserDataMappingResult) string { return v.DataId }).(pulumi.StringOutput)
}

// Resource name of the User data mapping, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/userDataMappings/{user_data_mapping_id}`.
func (o LookupUserDataMappingResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupUserDataMappingResult) string { return v.Name }).(pulumi.StringOutput)
}

// Attributes of the resource. Only explicitly set attributes are displayed here. Attribute definitions with defaults set implicitly apply to these User data mappings. Attributes listed here must be single valued, that is, exactly one value is specified for the field "values" in each Attribute.
func (o LookupUserDataMappingResultOutput) ResourceAttributes() AttributeResponseArrayOutput {
	return o.ApplyT(func(v LookupUserDataMappingResult) []AttributeResponse { return v.ResourceAttributes }).(AttributeResponseArrayOutput)
}

// User's UUID provided by the client.
func (o LookupUserDataMappingResultOutput) UserId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupUserDataMappingResult) string { return v.UserId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupUserDataMappingResultOutput{})
}
