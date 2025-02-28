// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Gets a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more.
func LookupOrganizationsDeidentifyTemplate(ctx *pulumi.Context, args *LookupOrganizationsDeidentifyTemplateArgs, opts ...pulumi.InvokeOption) (*LookupOrganizationsDeidentifyTemplateResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupOrganizationsDeidentifyTemplateResult
	err := ctx.Invoke("google-native:dlp/v2:getOrganizationsDeidentifyTemplate", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupOrganizationsDeidentifyTemplateArgs struct {
	DeidentifyTemplateId string `pulumi:"deidentifyTemplateId"`
	Location             string `pulumi:"location"`
	OrganizationId       string `pulumi:"organizationId"`
}

type LookupOrganizationsDeidentifyTemplateResult struct {
	// The creation timestamp of an inspectTemplate.
	CreateTime string `pulumi:"createTime"`
	// The core content of the template.
	DeidentifyConfig GooglePrivacyDlpV2DeidentifyConfigResponse `pulumi:"deidentifyConfig"`
	// Short description (max 256 chars).
	Description string `pulumi:"description"`
	// Display name (max 256 chars).
	DisplayName string `pulumi:"displayName"`
	// The template name. The template will have one of the following formats: `projects/PROJECT_ID/deidentifyTemplates/TEMPLATE_ID` OR `organizations/ORGANIZATION_ID/deidentifyTemplates/TEMPLATE_ID`
	Name string `pulumi:"name"`
	// The last update timestamp of an inspectTemplate.
	UpdateTime string `pulumi:"updateTime"`
}

func LookupOrganizationsDeidentifyTemplateOutput(ctx *pulumi.Context, args LookupOrganizationsDeidentifyTemplateOutputArgs, opts ...pulumi.InvokeOption) LookupOrganizationsDeidentifyTemplateResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupOrganizationsDeidentifyTemplateResult, error) {
			args := v.(LookupOrganizationsDeidentifyTemplateArgs)
			r, err := LookupOrganizationsDeidentifyTemplate(ctx, &args, opts...)
			var s LookupOrganizationsDeidentifyTemplateResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupOrganizationsDeidentifyTemplateResultOutput)
}

type LookupOrganizationsDeidentifyTemplateOutputArgs struct {
	DeidentifyTemplateId pulumi.StringInput `pulumi:"deidentifyTemplateId"`
	Location             pulumi.StringInput `pulumi:"location"`
	OrganizationId       pulumi.StringInput `pulumi:"organizationId"`
}

func (LookupOrganizationsDeidentifyTemplateOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupOrganizationsDeidentifyTemplateArgs)(nil)).Elem()
}

type LookupOrganizationsDeidentifyTemplateResultOutput struct{ *pulumi.OutputState }

func (LookupOrganizationsDeidentifyTemplateResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupOrganizationsDeidentifyTemplateResult)(nil)).Elem()
}

func (o LookupOrganizationsDeidentifyTemplateResultOutput) ToLookupOrganizationsDeidentifyTemplateResultOutput() LookupOrganizationsDeidentifyTemplateResultOutput {
	return o
}

func (o LookupOrganizationsDeidentifyTemplateResultOutput) ToLookupOrganizationsDeidentifyTemplateResultOutputWithContext(ctx context.Context) LookupOrganizationsDeidentifyTemplateResultOutput {
	return o
}

// The creation timestamp of an inspectTemplate.
func (o LookupOrganizationsDeidentifyTemplateResultOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupOrganizationsDeidentifyTemplateResult) string { return v.CreateTime }).(pulumi.StringOutput)
}

// The core content of the template.
func (o LookupOrganizationsDeidentifyTemplateResultOutput) DeidentifyConfig() GooglePrivacyDlpV2DeidentifyConfigResponseOutput {
	return o.ApplyT(func(v LookupOrganizationsDeidentifyTemplateResult) GooglePrivacyDlpV2DeidentifyConfigResponse {
		return v.DeidentifyConfig
	}).(GooglePrivacyDlpV2DeidentifyConfigResponseOutput)
}

// Short description (max 256 chars).
func (o LookupOrganizationsDeidentifyTemplateResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupOrganizationsDeidentifyTemplateResult) string { return v.Description }).(pulumi.StringOutput)
}

// Display name (max 256 chars).
func (o LookupOrganizationsDeidentifyTemplateResultOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupOrganizationsDeidentifyTemplateResult) string { return v.DisplayName }).(pulumi.StringOutput)
}

// The template name. The template will have one of the following formats: `projects/PROJECT_ID/deidentifyTemplates/TEMPLATE_ID` OR `organizations/ORGANIZATION_ID/deidentifyTemplates/TEMPLATE_ID`
func (o LookupOrganizationsDeidentifyTemplateResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupOrganizationsDeidentifyTemplateResult) string { return v.Name }).(pulumi.StringOutput)
}

// The last update timestamp of an inspectTemplate.
func (o LookupOrganizationsDeidentifyTemplateResultOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupOrganizationsDeidentifyTemplateResult) string { return v.UpdateTime }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupOrganizationsDeidentifyTemplateResultOutput{})
}
