// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1beta1

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates a `CustomDomain`.
// Auto-naming is currently not supported for this resource.
type CustomDomain struct {
	pulumi.CustomResourceState

	// Annotations you can add to leave both human- and machine-readable metadata about your `CustomDomain`.
	Annotations pulumi.StringMapOutput `pulumi:"annotations"`
	// The SSL certificate Hosting has for this custom domain's domain name. For new custom domains, this often represents Hosting's intent to create a certificate, rather than an actual cert. Check the `state` field for more.
	Cert CertificateResponseOutput `pulumi:"cert"`
	// A field that lets you specify which SSL certificate type Hosting creates for your domain name. Spark plan custom domains only have access to the `GROUPED` cert type, while Blaze plan domains can select any option.
	CertPreference pulumi.StringOutput `pulumi:"certPreference"`
	// The custom domain's create time.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// Required. The ID of the `CustomDomain`, which is the domain name you'd like to use with Firebase Hosting.
	CustomDomainId pulumi.StringOutput `pulumi:"customDomainId"`
	// The time the `CustomDomain` was deleted; null for custom domains that haven't been deleted. Deleted custom domains persist for approximately 30 days, after which time Hosting removes them completely. To restore a deleted custom domain, make an `UndeleteCustomDomain` request.
	DeleteTime pulumi.StringOutput `pulumi:"deleteTime"`
	// A string that represents the current state of the `CustomDomain` and allows you to confirm its initial state in requests that would modify it. Use the tag to ensure consistency when making `UpdateCustomDomain`, `DeleteCustomDomain`, and `UndeleteCustomDomain` requests.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// The minimum time before a soft-deleted `CustomDomain` is completely removed from Hosting; null for custom domains that haven't been deleted.
	ExpireTime pulumi.StringOutput `pulumi:"expireTime"`
	// The `HostState` of the domain name this `CustomDomain` refers to.
	HostState pulumi.StringOutput `pulumi:"hostState"`
	// A set of errors Hosting systems encountered when trying to establish Hosting's ability to serve secure content for your domain name. Resolve these issues to ensure your `CustomDomain` behaves properly.
	Issues StatusResponseArrayOutput `pulumi:"issues"`
	// Labels used for extra metadata and/or filtering.
	Labels pulumi.StringMapOutput `pulumi:"labels"`
	// The fully-qualified name of the `CustomDomain`.
	Name pulumi.StringOutput `pulumi:"name"`
	// The `OwnershipState` of the domain name this `CustomDomain` refers to.
	OwnershipState pulumi.StringOutput `pulumi:"ownershipState"`
	Project        pulumi.StringOutput `pulumi:"project"`
	// A field that, if true, indicates that Hosting's systems are attmepting to make the custom domain's state match your preferred state. This is most frequently `true` when initially provisioning a `CustomDomain` after a `CreateCustomDomain` request or when creating a new SSL certificate to match an updated `cert_preference` after an `UpdateCustomDomain` request.
	Reconciling pulumi.BoolOutput `pulumi:"reconciling"`
	// A domain name that this `CustomDomain` should direct traffic towards. If specified, Hosting will respond to requests against this custom domain with an HTTP 301 code, and route traffic to the specified `redirect_target` instead.
	RedirectTarget pulumi.StringOutput `pulumi:"redirectTarget"`
	// A set of updates you should make to the domain name's DNS records to let Hosting serve secure content on its behalf.
	RequiredDnsUpdates DnsUpdatesResponseOutput `pulumi:"requiredDnsUpdates"`
	SiteId             pulumi.StringOutput      `pulumi:"siteId"`
	// The last time the `CustomDomain` was updated.
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
}

// NewCustomDomain registers a new resource with the given unique name, arguments, and options.
func NewCustomDomain(ctx *pulumi.Context,
	name string, args *CustomDomainArgs, opts ...pulumi.ResourceOption) (*CustomDomain, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CustomDomainId == nil {
		return nil, errors.New("invalid value for required argument 'CustomDomainId'")
	}
	if args.SiteId == nil {
		return nil, errors.New("invalid value for required argument 'SiteId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"customDomainId",
		"project",
		"siteId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource CustomDomain
	err := ctx.RegisterResource("google-native:firebasehosting/v1beta1:CustomDomain", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCustomDomain gets an existing CustomDomain resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCustomDomain(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CustomDomainState, opts ...pulumi.ResourceOption) (*CustomDomain, error) {
	var resource CustomDomain
	err := ctx.ReadResource("google-native:firebasehosting/v1beta1:CustomDomain", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CustomDomain resources.
type customDomainState struct {
}

type CustomDomainState struct {
}

func (CustomDomainState) ElementType() reflect.Type {
	return reflect.TypeOf((*customDomainState)(nil)).Elem()
}

type customDomainArgs struct {
	// Annotations you can add to leave both human- and machine-readable metadata about your `CustomDomain`.
	Annotations map[string]string `pulumi:"annotations"`
	// A field that lets you specify which SSL certificate type Hosting creates for your domain name. Spark plan custom domains only have access to the `GROUPED` cert type, while Blaze plan domains can select any option.
	CertPreference *CustomDomainCertPreference `pulumi:"certPreference"`
	// Required. The ID of the `CustomDomain`, which is the domain name you'd like to use with Firebase Hosting.
	CustomDomainId string `pulumi:"customDomainId"`
	// Labels used for extra metadata and/or filtering.
	Labels  map[string]string `pulumi:"labels"`
	Project *string           `pulumi:"project"`
	// A domain name that this `CustomDomain` should direct traffic towards. If specified, Hosting will respond to requests against this custom domain with an HTTP 301 code, and route traffic to the specified `redirect_target` instead.
	RedirectTarget *string `pulumi:"redirectTarget"`
	SiteId         string  `pulumi:"siteId"`
}

// The set of arguments for constructing a CustomDomain resource.
type CustomDomainArgs struct {
	// Annotations you can add to leave both human- and machine-readable metadata about your `CustomDomain`.
	Annotations pulumi.StringMapInput
	// A field that lets you specify which SSL certificate type Hosting creates for your domain name. Spark plan custom domains only have access to the `GROUPED` cert type, while Blaze plan domains can select any option.
	CertPreference CustomDomainCertPreferencePtrInput
	// Required. The ID of the `CustomDomain`, which is the domain name you'd like to use with Firebase Hosting.
	CustomDomainId pulumi.StringInput
	// Labels used for extra metadata and/or filtering.
	Labels  pulumi.StringMapInput
	Project pulumi.StringPtrInput
	// A domain name that this `CustomDomain` should direct traffic towards. If specified, Hosting will respond to requests against this custom domain with an HTTP 301 code, and route traffic to the specified `redirect_target` instead.
	RedirectTarget pulumi.StringPtrInput
	SiteId         pulumi.StringInput
}

func (CustomDomainArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*customDomainArgs)(nil)).Elem()
}

type CustomDomainInput interface {
	pulumi.Input

	ToCustomDomainOutput() CustomDomainOutput
	ToCustomDomainOutputWithContext(ctx context.Context) CustomDomainOutput
}

func (*CustomDomain) ElementType() reflect.Type {
	return reflect.TypeOf((**CustomDomain)(nil)).Elem()
}

func (i *CustomDomain) ToCustomDomainOutput() CustomDomainOutput {
	return i.ToCustomDomainOutputWithContext(context.Background())
}

func (i *CustomDomain) ToCustomDomainOutputWithContext(ctx context.Context) CustomDomainOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CustomDomainOutput)
}

type CustomDomainOutput struct{ *pulumi.OutputState }

func (CustomDomainOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CustomDomain)(nil)).Elem()
}

func (o CustomDomainOutput) ToCustomDomainOutput() CustomDomainOutput {
	return o
}

func (o CustomDomainOutput) ToCustomDomainOutputWithContext(ctx context.Context) CustomDomainOutput {
	return o
}

// Annotations you can add to leave both human- and machine-readable metadata about your `CustomDomain`.
func (o CustomDomainOutput) Annotations() pulumi.StringMapOutput {
	return o.ApplyT(func(v *CustomDomain) pulumi.StringMapOutput { return v.Annotations }).(pulumi.StringMapOutput)
}

// The SSL certificate Hosting has for this custom domain's domain name. For new custom domains, this often represents Hosting's intent to create a certificate, rather than an actual cert. Check the `state` field for more.
func (o CustomDomainOutput) Cert() CertificateResponseOutput {
	return o.ApplyT(func(v *CustomDomain) CertificateResponseOutput { return v.Cert }).(CertificateResponseOutput)
}

// A field that lets you specify which SSL certificate type Hosting creates for your domain name. Spark plan custom domains only have access to the `GROUPED` cert type, while Blaze plan domains can select any option.
func (o CustomDomainOutput) CertPreference() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomDomain) pulumi.StringOutput { return v.CertPreference }).(pulumi.StringOutput)
}

// The custom domain's create time.
func (o CustomDomainOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomDomain) pulumi.StringOutput { return v.CreateTime }).(pulumi.StringOutput)
}

// Required. The ID of the `CustomDomain`, which is the domain name you'd like to use with Firebase Hosting.
func (o CustomDomainOutput) CustomDomainId() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomDomain) pulumi.StringOutput { return v.CustomDomainId }).(pulumi.StringOutput)
}

// The time the `CustomDomain` was deleted; null for custom domains that haven't been deleted. Deleted custom domains persist for approximately 30 days, after which time Hosting removes them completely. To restore a deleted custom domain, make an `UndeleteCustomDomain` request.
func (o CustomDomainOutput) DeleteTime() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomDomain) pulumi.StringOutput { return v.DeleteTime }).(pulumi.StringOutput)
}

// A string that represents the current state of the `CustomDomain` and allows you to confirm its initial state in requests that would modify it. Use the tag to ensure consistency when making `UpdateCustomDomain`, `DeleteCustomDomain`, and `UndeleteCustomDomain` requests.
func (o CustomDomainOutput) Etag() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomDomain) pulumi.StringOutput { return v.Etag }).(pulumi.StringOutput)
}

// The minimum time before a soft-deleted `CustomDomain` is completely removed from Hosting; null for custom domains that haven't been deleted.
func (o CustomDomainOutput) ExpireTime() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomDomain) pulumi.StringOutput { return v.ExpireTime }).(pulumi.StringOutput)
}

// The `HostState` of the domain name this `CustomDomain` refers to.
func (o CustomDomainOutput) HostState() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomDomain) pulumi.StringOutput { return v.HostState }).(pulumi.StringOutput)
}

// A set of errors Hosting systems encountered when trying to establish Hosting's ability to serve secure content for your domain name. Resolve these issues to ensure your `CustomDomain` behaves properly.
func (o CustomDomainOutput) Issues() StatusResponseArrayOutput {
	return o.ApplyT(func(v *CustomDomain) StatusResponseArrayOutput { return v.Issues }).(StatusResponseArrayOutput)
}

// Labels used for extra metadata and/or filtering.
func (o CustomDomainOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v *CustomDomain) pulumi.StringMapOutput { return v.Labels }).(pulumi.StringMapOutput)
}

// The fully-qualified name of the `CustomDomain`.
func (o CustomDomainOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomDomain) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The `OwnershipState` of the domain name this `CustomDomain` refers to.
func (o CustomDomainOutput) OwnershipState() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomDomain) pulumi.StringOutput { return v.OwnershipState }).(pulumi.StringOutput)
}

func (o CustomDomainOutput) Project() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomDomain) pulumi.StringOutput { return v.Project }).(pulumi.StringOutput)
}

// A field that, if true, indicates that Hosting's systems are attmepting to make the custom domain's state match your preferred state. This is most frequently `true` when initially provisioning a `CustomDomain` after a `CreateCustomDomain` request or when creating a new SSL certificate to match an updated `cert_preference` after an `UpdateCustomDomain` request.
func (o CustomDomainOutput) Reconciling() pulumi.BoolOutput {
	return o.ApplyT(func(v *CustomDomain) pulumi.BoolOutput { return v.Reconciling }).(pulumi.BoolOutput)
}

// A domain name that this `CustomDomain` should direct traffic towards. If specified, Hosting will respond to requests against this custom domain with an HTTP 301 code, and route traffic to the specified `redirect_target` instead.
func (o CustomDomainOutput) RedirectTarget() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomDomain) pulumi.StringOutput { return v.RedirectTarget }).(pulumi.StringOutput)
}

// A set of updates you should make to the domain name's DNS records to let Hosting serve secure content on its behalf.
func (o CustomDomainOutput) RequiredDnsUpdates() DnsUpdatesResponseOutput {
	return o.ApplyT(func(v *CustomDomain) DnsUpdatesResponseOutput { return v.RequiredDnsUpdates }).(DnsUpdatesResponseOutput)
}

func (o CustomDomainOutput) SiteId() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomDomain) pulumi.StringOutput { return v.SiteId }).(pulumi.StringOutput)
}

// The last time the `CustomDomain` was updated.
func (o CustomDomainOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomDomain) pulumi.StringOutput { return v.UpdateTime }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CustomDomainInput)(nil)).Elem(), &CustomDomain{})
	pulumi.RegisterOutputType(CustomDomainOutput{})
}
