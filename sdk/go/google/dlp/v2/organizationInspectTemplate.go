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

// Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates to learn more.
// Auto-naming is currently not supported for this resource.
type OrganizationInspectTemplate struct {
	pulumi.CustomResourceState

	// The creation timestamp of an inspectTemplate.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// Short description (max 256 chars).
	Description pulumi.StringOutput `pulumi:"description"`
	// Display name (max 256 chars).
	DisplayName pulumi.StringOutput `pulumi:"displayName"`
	// The core content of the template. Configuration of the scanning process.
	InspectConfig GooglePrivacyDlpV2InspectConfigResponseOutput `pulumi:"inspectConfig"`
	Location      pulumi.StringOutput                           `pulumi:"location"`
	// The template name. The template will have one of the following formats: `projects/PROJECT_ID/inspectTemplates/TEMPLATE_ID` OR `organizations/ORGANIZATION_ID/inspectTemplates/TEMPLATE_ID`;
	Name           pulumi.StringOutput `pulumi:"name"`
	OrganizationId pulumi.StringOutput `pulumi:"organizationId"`
	// The last update timestamp of an inspectTemplate.
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
}

// NewOrganizationInspectTemplate registers a new resource with the given unique name, arguments, and options.
func NewOrganizationInspectTemplate(ctx *pulumi.Context,
	name string, args *OrganizationInspectTemplateArgs, opts ...pulumi.ResourceOption) (*OrganizationInspectTemplate, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.OrganizationId == nil {
		return nil, errors.New("invalid value for required argument 'OrganizationId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"location",
		"organizationId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource OrganizationInspectTemplate
	err := ctx.RegisterResource("google-native:dlp/v2:OrganizationInspectTemplate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOrganizationInspectTemplate gets an existing OrganizationInspectTemplate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOrganizationInspectTemplate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OrganizationInspectTemplateState, opts ...pulumi.ResourceOption) (*OrganizationInspectTemplate, error) {
	var resource OrganizationInspectTemplate
	err := ctx.ReadResource("google-native:dlp/v2:OrganizationInspectTemplate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering OrganizationInspectTemplate resources.
type organizationInspectTemplateState struct {
}

type OrganizationInspectTemplateState struct {
}

func (OrganizationInspectTemplateState) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationInspectTemplateState)(nil)).Elem()
}

type organizationInspectTemplateArgs struct {
	// Short description (max 256 chars).
	Description *string `pulumi:"description"`
	// Display name (max 256 chars).
	DisplayName *string `pulumi:"displayName"`
	// The core content of the template. Configuration of the scanning process.
	InspectConfig *GooglePrivacyDlpV2InspectConfig `pulumi:"inspectConfig"`
	// Deprecated. This field has no effect.
	//
	// Deprecated: Deprecated. This field has no effect.
	Location       *string `pulumi:"location"`
	OrganizationId string  `pulumi:"organizationId"`
	// The template id can contain uppercase and lowercase letters, numbers, and hyphens; that is, it must match the regular expression: `[a-zA-Z\d-_]+`. The maximum length is 100 characters. Can be empty to allow the system to generate one.
	TemplateId *string `pulumi:"templateId"`
}

// The set of arguments for constructing a OrganizationInspectTemplate resource.
type OrganizationInspectTemplateArgs struct {
	// Short description (max 256 chars).
	Description pulumi.StringPtrInput
	// Display name (max 256 chars).
	DisplayName pulumi.StringPtrInput
	// The core content of the template. Configuration of the scanning process.
	InspectConfig GooglePrivacyDlpV2InspectConfigPtrInput
	// Deprecated. This field has no effect.
	//
	// Deprecated: Deprecated. This field has no effect.
	Location       pulumi.StringPtrInput
	OrganizationId pulumi.StringInput
	// The template id can contain uppercase and lowercase letters, numbers, and hyphens; that is, it must match the regular expression: `[a-zA-Z\d-_]+`. The maximum length is 100 characters. Can be empty to allow the system to generate one.
	TemplateId pulumi.StringPtrInput
}

func (OrganizationInspectTemplateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationInspectTemplateArgs)(nil)).Elem()
}

type OrganizationInspectTemplateInput interface {
	pulumi.Input

	ToOrganizationInspectTemplateOutput() OrganizationInspectTemplateOutput
	ToOrganizationInspectTemplateOutputWithContext(ctx context.Context) OrganizationInspectTemplateOutput
}

func (*OrganizationInspectTemplate) ElementType() reflect.Type {
	return reflect.TypeOf((**OrganizationInspectTemplate)(nil)).Elem()
}

func (i *OrganizationInspectTemplate) ToOrganizationInspectTemplateOutput() OrganizationInspectTemplateOutput {
	return i.ToOrganizationInspectTemplateOutputWithContext(context.Background())
}

func (i *OrganizationInspectTemplate) ToOrganizationInspectTemplateOutputWithContext(ctx context.Context) OrganizationInspectTemplateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrganizationInspectTemplateOutput)
}

type OrganizationInspectTemplateOutput struct{ *pulumi.OutputState }

func (OrganizationInspectTemplateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**OrganizationInspectTemplate)(nil)).Elem()
}

func (o OrganizationInspectTemplateOutput) ToOrganizationInspectTemplateOutput() OrganizationInspectTemplateOutput {
	return o
}

func (o OrganizationInspectTemplateOutput) ToOrganizationInspectTemplateOutputWithContext(ctx context.Context) OrganizationInspectTemplateOutput {
	return o
}

// The creation timestamp of an inspectTemplate.
func (o OrganizationInspectTemplateOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *OrganizationInspectTemplate) pulumi.StringOutput { return v.CreateTime }).(pulumi.StringOutput)
}

// Short description (max 256 chars).
func (o OrganizationInspectTemplateOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *OrganizationInspectTemplate) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// Display name (max 256 chars).
func (o OrganizationInspectTemplateOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v *OrganizationInspectTemplate) pulumi.StringOutput { return v.DisplayName }).(pulumi.StringOutput)
}

// The core content of the template. Configuration of the scanning process.
func (o OrganizationInspectTemplateOutput) InspectConfig() GooglePrivacyDlpV2InspectConfigResponseOutput {
	return o.ApplyT(func(v *OrganizationInspectTemplate) GooglePrivacyDlpV2InspectConfigResponseOutput {
		return v.InspectConfig
	}).(GooglePrivacyDlpV2InspectConfigResponseOutput)
}

func (o OrganizationInspectTemplateOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *OrganizationInspectTemplate) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

// The template name. The template will have one of the following formats: `projects/PROJECT_ID/inspectTemplates/TEMPLATE_ID` OR `organizations/ORGANIZATION_ID/inspectTemplates/TEMPLATE_ID`;
func (o OrganizationInspectTemplateOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *OrganizationInspectTemplate) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o OrganizationInspectTemplateOutput) OrganizationId() pulumi.StringOutput {
	return o.ApplyT(func(v *OrganizationInspectTemplate) pulumi.StringOutput { return v.OrganizationId }).(pulumi.StringOutput)
}

// The last update timestamp of an inspectTemplate.
func (o OrganizationInspectTemplateOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *OrganizationInspectTemplate) pulumi.StringOutput { return v.UpdateTime }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OrganizationInspectTemplateInput)(nil)).Elem(), &OrganizationInspectTemplate{})
	pulumi.RegisterOutputType(OrganizationInspectTemplateOutput{})
}
