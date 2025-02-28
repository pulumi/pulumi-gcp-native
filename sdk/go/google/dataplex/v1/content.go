// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Create a content.
// Auto-naming is currently not supported for this resource.
type Content struct {
	pulumi.CustomResourceState

	// Content creation time.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// Content data in string format.
	DataText pulumi.StringOutput `pulumi:"dataText"`
	// Optional. Description of the content.
	Description pulumi.StringOutput `pulumi:"description"`
	// Optional. User defined labels for the content.
	Labels   pulumi.StringMapOutput `pulumi:"labels"`
	LakeId   pulumi.StringOutput    `pulumi:"lakeId"`
	Location pulumi.StringOutput    `pulumi:"location"`
	// The relative resource name of the content, of the form: projects/{project_id}/locations/{location_id}/lakes/{lake_id}/content/{content_id}
	Name pulumi.StringOutput `pulumi:"name"`
	// Notebook related configurations.
	Notebook GoogleCloudDataplexV1ContentNotebookResponseOutput `pulumi:"notebook"`
	// The path for the Content file, represented as directory structure. Unique within a lake. Limited to alphanumerics, hyphens, underscores, dots and slashes.
	Path    pulumi.StringOutput `pulumi:"path"`
	Project pulumi.StringOutput `pulumi:"project"`
	// Sql Script related configurations.
	SqlScript GoogleCloudDataplexV1ContentSqlScriptResponseOutput `pulumi:"sqlScript"`
	// System generated globally unique ID for the content. This ID will be different if the content is deleted and re-created with the same name.
	Uid pulumi.StringOutput `pulumi:"uid"`
	// The time when the content was last updated.
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
}

// NewContent registers a new resource with the given unique name, arguments, and options.
func NewContent(ctx *pulumi.Context,
	name string, args *ContentArgs, opts ...pulumi.ResourceOption) (*Content, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DataText == nil {
		return nil, errors.New("invalid value for required argument 'DataText'")
	}
	if args.LakeId == nil {
		return nil, errors.New("invalid value for required argument 'LakeId'")
	}
	if args.Path == nil {
		return nil, errors.New("invalid value for required argument 'Path'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"lakeId",
		"location",
		"project",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Content
	err := ctx.RegisterResource("google-native:dataplex/v1:Content", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetContent gets an existing Content resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetContent(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ContentState, opts ...pulumi.ResourceOption) (*Content, error) {
	var resource Content
	err := ctx.ReadResource("google-native:dataplex/v1:Content", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Content resources.
type contentState struct {
}

type ContentState struct {
}

func (ContentState) ElementType() reflect.Type {
	return reflect.TypeOf((*contentState)(nil)).Elem()
}

type contentArgs struct {
	// Content data in string format.
	DataText string `pulumi:"dataText"`
	// Optional. Description of the content.
	Description *string `pulumi:"description"`
	// Optional. User defined labels for the content.
	Labels   map[string]string `pulumi:"labels"`
	LakeId   string            `pulumi:"lakeId"`
	Location *string           `pulumi:"location"`
	// Notebook related configurations.
	Notebook *GoogleCloudDataplexV1ContentNotebook `pulumi:"notebook"`
	// The path for the Content file, represented as directory structure. Unique within a lake. Limited to alphanumerics, hyphens, underscores, dots and slashes.
	Path    string  `pulumi:"path"`
	Project *string `pulumi:"project"`
	// Sql Script related configurations.
	SqlScript *GoogleCloudDataplexV1ContentSqlScript `pulumi:"sqlScript"`
}

// The set of arguments for constructing a Content resource.
type ContentArgs struct {
	// Content data in string format.
	DataText pulumi.StringInput
	// Optional. Description of the content.
	Description pulumi.StringPtrInput
	// Optional. User defined labels for the content.
	Labels   pulumi.StringMapInput
	LakeId   pulumi.StringInput
	Location pulumi.StringPtrInput
	// Notebook related configurations.
	Notebook GoogleCloudDataplexV1ContentNotebookPtrInput
	// The path for the Content file, represented as directory structure. Unique within a lake. Limited to alphanumerics, hyphens, underscores, dots and slashes.
	Path    pulumi.StringInput
	Project pulumi.StringPtrInput
	// Sql Script related configurations.
	SqlScript GoogleCloudDataplexV1ContentSqlScriptPtrInput
}

func (ContentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*contentArgs)(nil)).Elem()
}

type ContentInput interface {
	pulumi.Input

	ToContentOutput() ContentOutput
	ToContentOutputWithContext(ctx context.Context) ContentOutput
}

func (*Content) ElementType() reflect.Type {
	return reflect.TypeOf((**Content)(nil)).Elem()
}

func (i *Content) ToContentOutput() ContentOutput {
	return i.ToContentOutputWithContext(context.Background())
}

func (i *Content) ToContentOutputWithContext(ctx context.Context) ContentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ContentOutput)
}

type ContentOutput struct{ *pulumi.OutputState }

func (ContentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Content)(nil)).Elem()
}

func (o ContentOutput) ToContentOutput() ContentOutput {
	return o
}

func (o ContentOutput) ToContentOutputWithContext(ctx context.Context) ContentOutput {
	return o
}

// Content creation time.
func (o ContentOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Content) pulumi.StringOutput { return v.CreateTime }).(pulumi.StringOutput)
}

// Content data in string format.
func (o ContentOutput) DataText() pulumi.StringOutput {
	return o.ApplyT(func(v *Content) pulumi.StringOutput { return v.DataText }).(pulumi.StringOutput)
}

// Optional. Description of the content.
func (o ContentOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *Content) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// Optional. User defined labels for the content.
func (o ContentOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Content) pulumi.StringMapOutput { return v.Labels }).(pulumi.StringMapOutput)
}

func (o ContentOutput) LakeId() pulumi.StringOutput {
	return o.ApplyT(func(v *Content) pulumi.StringOutput { return v.LakeId }).(pulumi.StringOutput)
}

func (o ContentOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *Content) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

// The relative resource name of the content, of the form: projects/{project_id}/locations/{location_id}/lakes/{lake_id}/content/{content_id}
func (o ContentOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Content) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Notebook related configurations.
func (o ContentOutput) Notebook() GoogleCloudDataplexV1ContentNotebookResponseOutput {
	return o.ApplyT(func(v *Content) GoogleCloudDataplexV1ContentNotebookResponseOutput { return v.Notebook }).(GoogleCloudDataplexV1ContentNotebookResponseOutput)
}

// The path for the Content file, represented as directory structure. Unique within a lake. Limited to alphanumerics, hyphens, underscores, dots and slashes.
func (o ContentOutput) Path() pulumi.StringOutput {
	return o.ApplyT(func(v *Content) pulumi.StringOutput { return v.Path }).(pulumi.StringOutput)
}

func (o ContentOutput) Project() pulumi.StringOutput {
	return o.ApplyT(func(v *Content) pulumi.StringOutput { return v.Project }).(pulumi.StringOutput)
}

// Sql Script related configurations.
func (o ContentOutput) SqlScript() GoogleCloudDataplexV1ContentSqlScriptResponseOutput {
	return o.ApplyT(func(v *Content) GoogleCloudDataplexV1ContentSqlScriptResponseOutput { return v.SqlScript }).(GoogleCloudDataplexV1ContentSqlScriptResponseOutput)
}

// System generated globally unique ID for the content. This ID will be different if the content is deleted and re-created with the same name.
func (o ContentOutput) Uid() pulumi.StringOutput {
	return o.ApplyT(func(v *Content) pulumi.StringOutput { return v.Uid }).(pulumi.StringOutput)
}

// The time when the content was last updated.
func (o ContentOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Content) pulumi.StringOutput { return v.UpdateTime }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ContentInput)(nil)).Elem(), &Content{})
	pulumi.RegisterOutputType(ContentOutput{})
}
