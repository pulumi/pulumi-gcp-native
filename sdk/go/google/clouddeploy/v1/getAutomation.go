// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Gets details of a single Automation.
func LookupAutomation(ctx *pulumi.Context, args *LookupAutomationArgs, opts ...pulumi.InvokeOption) (*LookupAutomationResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupAutomationResult
	err := ctx.Invoke("google-native:clouddeploy/v1:getAutomation", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupAutomationArgs struct {
	AutomationId       string  `pulumi:"automationId"`
	DeliveryPipelineId string  `pulumi:"deliveryPipelineId"`
	Location           string  `pulumi:"location"`
	Project            *string `pulumi:"project"`
}

type LookupAutomationResult struct {
	// Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. Annotations must meet the following constraints: * Annotations are key/value pairs. * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (`/`). * The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between. * The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots(`.`), not longer than 253 characters in total, followed by a slash (`/`). See https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#syntax-and-character-set for more details.
	Annotations map[string]string `pulumi:"annotations"`
	// Time at which the automation was created.
	CreateTime string `pulumi:"createTime"`
	// Optional. Description of the `Automation`. Max length is 255 characters.
	Description string `pulumi:"description"`
	// Optional. The weak etag of the `Automation` resource. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.
	Etag string `pulumi:"etag"`
	// Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 63 characters.
	Labels map[string]string `pulumi:"labels"`
	// Name of the `Automation`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{delivery_pipeline}/automations/{automation}`.
	Name string `pulumi:"name"`
	// List of Automation rules associated with the Automation resource. Must have at least one rule and limited to 250 rules per Delivery Pipeline. Note: the order of the rules here is not the same as the order of execution.
	Rules []AutomationRuleResponse `pulumi:"rules"`
	// Selected resources to which the automation will be applied.
	Selector AutomationResourceSelectorResponse `pulumi:"selector"`
	// Email address of the user-managed IAM service account that creates Cloud Deploy release and rollout resources.
	ServiceAccount string `pulumi:"serviceAccount"`
	// Optional. When Suspended, automation is deactivated from execution.
	Suspended bool `pulumi:"suspended"`
	// Unique identifier of the `Automation`.
	Uid string `pulumi:"uid"`
	// Time at which the automation was updated.
	UpdateTime string `pulumi:"updateTime"`
}

func LookupAutomationOutput(ctx *pulumi.Context, args LookupAutomationOutputArgs, opts ...pulumi.InvokeOption) LookupAutomationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupAutomationResult, error) {
			args := v.(LookupAutomationArgs)
			r, err := LookupAutomation(ctx, &args, opts...)
			var s LookupAutomationResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupAutomationResultOutput)
}

type LookupAutomationOutputArgs struct {
	AutomationId       pulumi.StringInput    `pulumi:"automationId"`
	DeliveryPipelineId pulumi.StringInput    `pulumi:"deliveryPipelineId"`
	Location           pulumi.StringInput    `pulumi:"location"`
	Project            pulumi.StringPtrInput `pulumi:"project"`
}

func (LookupAutomationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAutomationArgs)(nil)).Elem()
}

type LookupAutomationResultOutput struct{ *pulumi.OutputState }

func (LookupAutomationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAutomationResult)(nil)).Elem()
}

func (o LookupAutomationResultOutput) ToLookupAutomationResultOutput() LookupAutomationResultOutput {
	return o
}

func (o LookupAutomationResultOutput) ToLookupAutomationResultOutputWithContext(ctx context.Context) LookupAutomationResultOutput {
	return o
}

// Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. Annotations must meet the following constraints: * Annotations are key/value pairs. * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (`/`). * The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between. * The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots(`.`), not longer than 253 characters in total, followed by a slash (`/`). See https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#syntax-and-character-set for more details.
func (o LookupAutomationResultOutput) Annotations() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupAutomationResult) map[string]string { return v.Annotations }).(pulumi.StringMapOutput)
}

// Time at which the automation was created.
func (o LookupAutomationResultOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAutomationResult) string { return v.CreateTime }).(pulumi.StringOutput)
}

// Optional. Description of the `Automation`. Max length is 255 characters.
func (o LookupAutomationResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAutomationResult) string { return v.Description }).(pulumi.StringOutput)
}

// Optional. The weak etag of the `Automation` resource. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.
func (o LookupAutomationResultOutput) Etag() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAutomationResult) string { return v.Etag }).(pulumi.StringOutput)
}

// Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 63 characters.
func (o LookupAutomationResultOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupAutomationResult) map[string]string { return v.Labels }).(pulumi.StringMapOutput)
}

// Name of the `Automation`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{delivery_pipeline}/automations/{automation}`.
func (o LookupAutomationResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAutomationResult) string { return v.Name }).(pulumi.StringOutput)
}

// List of Automation rules associated with the Automation resource. Must have at least one rule and limited to 250 rules per Delivery Pipeline. Note: the order of the rules here is not the same as the order of execution.
func (o LookupAutomationResultOutput) Rules() AutomationRuleResponseArrayOutput {
	return o.ApplyT(func(v LookupAutomationResult) []AutomationRuleResponse { return v.Rules }).(AutomationRuleResponseArrayOutput)
}

// Selected resources to which the automation will be applied.
func (o LookupAutomationResultOutput) Selector() AutomationResourceSelectorResponseOutput {
	return o.ApplyT(func(v LookupAutomationResult) AutomationResourceSelectorResponse { return v.Selector }).(AutomationResourceSelectorResponseOutput)
}

// Email address of the user-managed IAM service account that creates Cloud Deploy release and rollout resources.
func (o LookupAutomationResultOutput) ServiceAccount() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAutomationResult) string { return v.ServiceAccount }).(pulumi.StringOutput)
}

// Optional. When Suspended, automation is deactivated from execution.
func (o LookupAutomationResultOutput) Suspended() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupAutomationResult) bool { return v.Suspended }).(pulumi.BoolOutput)
}

// Unique identifier of the `Automation`.
func (o LookupAutomationResultOutput) Uid() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAutomationResult) string { return v.Uid }).(pulumi.StringOutput)
}

// Time at which the automation was updated.
func (o LookupAutomationResultOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAutomationResult) string { return v.UpdateTime }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupAutomationResultOutput{})
}
