// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v2

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views.
// Auto-naming is currently not supported for this resource.
type OrganizationBucketView struct {
	pulumi.CustomResourceState

	BucketId pulumi.StringOutput `pulumi:"bucketId"`
	// The creation timestamp of the view.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// Describes this view.
	Description pulumi.StringOutput `pulumi:"description"`
	// Filter that restricts which log entries in a bucket are visible in this view.Filters are restricted to be a logical AND of ==/!= of any of the following: originating project/folder/organization/billing account. resource type log idFor example:SOURCE("projects/myproject") AND resource.type = "gce_instance" AND LOG_ID("stdout")
	Filter   pulumi.StringOutput `pulumi:"filter"`
	Location pulumi.StringOutput `pulumi:"location"`
	// The resource name of the view.For example:projects/my-project/locations/global/buckets/my-bucket/views/my-view
	Name           pulumi.StringOutput `pulumi:"name"`
	OrganizationId pulumi.StringOutput `pulumi:"organizationId"`
	// The last update timestamp of the view.
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
	// Required. A client-assigned identifier such as "my-view". Identifiers are limited to 100 characters and can include only letters, digits, underscores, hyphens, and periods.
	ViewId pulumi.StringOutput `pulumi:"viewId"`
}

// NewOrganizationBucketView registers a new resource with the given unique name, arguments, and options.
func NewOrganizationBucketView(ctx *pulumi.Context,
	name string, args *OrganizationBucketViewArgs, opts ...pulumi.ResourceOption) (*OrganizationBucketView, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.BucketId == nil {
		return nil, errors.New("invalid value for required argument 'BucketId'")
	}
	if args.OrganizationId == nil {
		return nil, errors.New("invalid value for required argument 'OrganizationId'")
	}
	if args.ViewId == nil {
		return nil, errors.New("invalid value for required argument 'ViewId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"bucketId",
		"location",
		"organizationId",
		"viewId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource OrganizationBucketView
	err := ctx.RegisterResource("google-native:logging/v2:OrganizationBucketView", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOrganizationBucketView gets an existing OrganizationBucketView resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOrganizationBucketView(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OrganizationBucketViewState, opts ...pulumi.ResourceOption) (*OrganizationBucketView, error) {
	var resource OrganizationBucketView
	err := ctx.ReadResource("google-native:logging/v2:OrganizationBucketView", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering OrganizationBucketView resources.
type organizationBucketViewState struct {
}

type OrganizationBucketViewState struct {
}

func (OrganizationBucketViewState) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationBucketViewState)(nil)).Elem()
}

type organizationBucketViewArgs struct {
	BucketId string `pulumi:"bucketId"`
	// Describes this view.
	Description *string `pulumi:"description"`
	// Filter that restricts which log entries in a bucket are visible in this view.Filters are restricted to be a logical AND of ==/!= of any of the following: originating project/folder/organization/billing account. resource type log idFor example:SOURCE("projects/myproject") AND resource.type = "gce_instance" AND LOG_ID("stdout")
	Filter   *string `pulumi:"filter"`
	Location *string `pulumi:"location"`
	// The resource name of the view.For example:projects/my-project/locations/global/buckets/my-bucket/views/my-view
	Name           *string `pulumi:"name"`
	OrganizationId string  `pulumi:"organizationId"`
	// Required. A client-assigned identifier such as "my-view". Identifiers are limited to 100 characters and can include only letters, digits, underscores, hyphens, and periods.
	ViewId string `pulumi:"viewId"`
}

// The set of arguments for constructing a OrganizationBucketView resource.
type OrganizationBucketViewArgs struct {
	BucketId pulumi.StringInput
	// Describes this view.
	Description pulumi.StringPtrInput
	// Filter that restricts which log entries in a bucket are visible in this view.Filters are restricted to be a logical AND of ==/!= of any of the following: originating project/folder/organization/billing account. resource type log idFor example:SOURCE("projects/myproject") AND resource.type = "gce_instance" AND LOG_ID("stdout")
	Filter   pulumi.StringPtrInput
	Location pulumi.StringPtrInput
	// The resource name of the view.For example:projects/my-project/locations/global/buckets/my-bucket/views/my-view
	Name           pulumi.StringPtrInput
	OrganizationId pulumi.StringInput
	// Required. A client-assigned identifier such as "my-view". Identifiers are limited to 100 characters and can include only letters, digits, underscores, hyphens, and periods.
	ViewId pulumi.StringInput
}

func (OrganizationBucketViewArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationBucketViewArgs)(nil)).Elem()
}

type OrganizationBucketViewInput interface {
	pulumi.Input

	ToOrganizationBucketViewOutput() OrganizationBucketViewOutput
	ToOrganizationBucketViewOutputWithContext(ctx context.Context) OrganizationBucketViewOutput
}

func (*OrganizationBucketView) ElementType() reflect.Type {
	return reflect.TypeOf((**OrganizationBucketView)(nil)).Elem()
}

func (i *OrganizationBucketView) ToOrganizationBucketViewOutput() OrganizationBucketViewOutput {
	return i.ToOrganizationBucketViewOutputWithContext(context.Background())
}

func (i *OrganizationBucketView) ToOrganizationBucketViewOutputWithContext(ctx context.Context) OrganizationBucketViewOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrganizationBucketViewOutput)
}

type OrganizationBucketViewOutput struct{ *pulumi.OutputState }

func (OrganizationBucketViewOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**OrganizationBucketView)(nil)).Elem()
}

func (o OrganizationBucketViewOutput) ToOrganizationBucketViewOutput() OrganizationBucketViewOutput {
	return o
}

func (o OrganizationBucketViewOutput) ToOrganizationBucketViewOutputWithContext(ctx context.Context) OrganizationBucketViewOutput {
	return o
}

func (o OrganizationBucketViewOutput) BucketId() pulumi.StringOutput {
	return o.ApplyT(func(v *OrganizationBucketView) pulumi.StringOutput { return v.BucketId }).(pulumi.StringOutput)
}

// The creation timestamp of the view.
func (o OrganizationBucketViewOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *OrganizationBucketView) pulumi.StringOutput { return v.CreateTime }).(pulumi.StringOutput)
}

// Describes this view.
func (o OrganizationBucketViewOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *OrganizationBucketView) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// Filter that restricts which log entries in a bucket are visible in this view.Filters are restricted to be a logical AND of ==/!= of any of the following: originating project/folder/organization/billing account. resource type log idFor example:SOURCE("projects/myproject") AND resource.type = "gce_instance" AND LOG_ID("stdout")
func (o OrganizationBucketViewOutput) Filter() pulumi.StringOutput {
	return o.ApplyT(func(v *OrganizationBucketView) pulumi.StringOutput { return v.Filter }).(pulumi.StringOutput)
}

func (o OrganizationBucketViewOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *OrganizationBucketView) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

// The resource name of the view.For example:projects/my-project/locations/global/buckets/my-bucket/views/my-view
func (o OrganizationBucketViewOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *OrganizationBucketView) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o OrganizationBucketViewOutput) OrganizationId() pulumi.StringOutput {
	return o.ApplyT(func(v *OrganizationBucketView) pulumi.StringOutput { return v.OrganizationId }).(pulumi.StringOutput)
}

// The last update timestamp of the view.
func (o OrganizationBucketViewOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *OrganizationBucketView) pulumi.StringOutput { return v.UpdateTime }).(pulumi.StringOutput)
}

// Required. A client-assigned identifier such as "my-view". Identifiers are limited to 100 characters and can include only letters, digits, underscores, hyphens, and periods.
func (o OrganizationBucketViewOutput) ViewId() pulumi.StringOutput {
	return o.ApplyT(func(v *OrganizationBucketView) pulumi.StringOutput { return v.ViewId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OrganizationBucketViewInput)(nil)).Elem(), &OrganizationBucketView{})
	pulumi.RegisterOutputType(OrganizationBucketViewOutput{})
}
