// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Create a session template synchronously.
type SessionTemplate struct {
	pulumi.CustomResourceState

	// The time when the template was created.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// The email address of the user who created the template.
	Creator pulumi.StringOutput `pulumi:"creator"`
	// Optional. Brief description of the template.
	Description pulumi.StringOutput `pulumi:"description"`
	// Optional. Environment configuration for session execution.
	EnvironmentConfig EnvironmentConfigResponseOutput `pulumi:"environmentConfig"`
	// Optional. Jupyter session config.
	JupyterSession JupyterConfigResponseOutput `pulumi:"jupyterSession"`
	// Optional. Labels to associate with sessions created using this template. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values can be empty, but, if present, must contain 1 to 63 characters and conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a session.
	Labels   pulumi.StringMapOutput `pulumi:"labels"`
	Location pulumi.StringOutput    `pulumi:"location"`
	// The resource name of the session template.
	Name    pulumi.StringOutput `pulumi:"name"`
	Project pulumi.StringOutput `pulumi:"project"`
	// Optional. Runtime configuration for session execution.
	RuntimeConfig RuntimeConfigResponseOutput `pulumi:"runtimeConfig"`
	// The time the template was last updated.
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
	// A session template UUID (Unique Universal Identifier). The service generates this value when it creates the session template.
	Uuid pulumi.StringOutput `pulumi:"uuid"`
}

// NewSessionTemplate registers a new resource with the given unique name, arguments, and options.
func NewSessionTemplate(ctx *pulumi.Context,
	name string, args *SessionTemplateArgs, opts ...pulumi.ResourceOption) (*SessionTemplate, error) {
	if args == nil {
		args = &SessionTemplateArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"location",
		"project",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource SessionTemplate
	err := ctx.RegisterResource("google-native:dataproc/v1:SessionTemplate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSessionTemplate gets an existing SessionTemplate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSessionTemplate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SessionTemplateState, opts ...pulumi.ResourceOption) (*SessionTemplate, error) {
	var resource SessionTemplate
	err := ctx.ReadResource("google-native:dataproc/v1:SessionTemplate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SessionTemplate resources.
type sessionTemplateState struct {
}

type SessionTemplateState struct {
}

func (SessionTemplateState) ElementType() reflect.Type {
	return reflect.TypeOf((*sessionTemplateState)(nil)).Elem()
}

type sessionTemplateArgs struct {
	// Optional. Brief description of the template.
	Description *string `pulumi:"description"`
	// Optional. Environment configuration for session execution.
	EnvironmentConfig *EnvironmentConfig `pulumi:"environmentConfig"`
	// Optional. Jupyter session config.
	JupyterSession *JupyterConfig `pulumi:"jupyterSession"`
	// Optional. Labels to associate with sessions created using this template. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values can be empty, but, if present, must contain 1 to 63 characters and conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a session.
	Labels   map[string]string `pulumi:"labels"`
	Location *string           `pulumi:"location"`
	// The resource name of the session template.
	Name    *string `pulumi:"name"`
	Project *string `pulumi:"project"`
	// Optional. Runtime configuration for session execution.
	RuntimeConfig *RuntimeConfig `pulumi:"runtimeConfig"`
}

// The set of arguments for constructing a SessionTemplate resource.
type SessionTemplateArgs struct {
	// Optional. Brief description of the template.
	Description pulumi.StringPtrInput
	// Optional. Environment configuration for session execution.
	EnvironmentConfig EnvironmentConfigPtrInput
	// Optional. Jupyter session config.
	JupyterSession JupyterConfigPtrInput
	// Optional. Labels to associate with sessions created using this template. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values can be empty, but, if present, must contain 1 to 63 characters and conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a session.
	Labels   pulumi.StringMapInput
	Location pulumi.StringPtrInput
	// The resource name of the session template.
	Name    pulumi.StringPtrInput
	Project pulumi.StringPtrInput
	// Optional. Runtime configuration for session execution.
	RuntimeConfig RuntimeConfigPtrInput
}

func (SessionTemplateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*sessionTemplateArgs)(nil)).Elem()
}

type SessionTemplateInput interface {
	pulumi.Input

	ToSessionTemplateOutput() SessionTemplateOutput
	ToSessionTemplateOutputWithContext(ctx context.Context) SessionTemplateOutput
}

func (*SessionTemplate) ElementType() reflect.Type {
	return reflect.TypeOf((**SessionTemplate)(nil)).Elem()
}

func (i *SessionTemplate) ToSessionTemplateOutput() SessionTemplateOutput {
	return i.ToSessionTemplateOutputWithContext(context.Background())
}

func (i *SessionTemplate) ToSessionTemplateOutputWithContext(ctx context.Context) SessionTemplateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SessionTemplateOutput)
}

type SessionTemplateOutput struct{ *pulumi.OutputState }

func (SessionTemplateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SessionTemplate)(nil)).Elem()
}

func (o SessionTemplateOutput) ToSessionTemplateOutput() SessionTemplateOutput {
	return o
}

func (o SessionTemplateOutput) ToSessionTemplateOutputWithContext(ctx context.Context) SessionTemplateOutput {
	return o
}

// The time when the template was created.
func (o SessionTemplateOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *SessionTemplate) pulumi.StringOutput { return v.CreateTime }).(pulumi.StringOutput)
}

// The email address of the user who created the template.
func (o SessionTemplateOutput) Creator() pulumi.StringOutput {
	return o.ApplyT(func(v *SessionTemplate) pulumi.StringOutput { return v.Creator }).(pulumi.StringOutput)
}

// Optional. Brief description of the template.
func (o SessionTemplateOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *SessionTemplate) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// Optional. Environment configuration for session execution.
func (o SessionTemplateOutput) EnvironmentConfig() EnvironmentConfigResponseOutput {
	return o.ApplyT(func(v *SessionTemplate) EnvironmentConfigResponseOutput { return v.EnvironmentConfig }).(EnvironmentConfigResponseOutput)
}

// Optional. Jupyter session config.
func (o SessionTemplateOutput) JupyterSession() JupyterConfigResponseOutput {
	return o.ApplyT(func(v *SessionTemplate) JupyterConfigResponseOutput { return v.JupyterSession }).(JupyterConfigResponseOutput)
}

// Optional. Labels to associate with sessions created using this template. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values can be empty, but, if present, must contain 1 to 63 characters and conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a session.
func (o SessionTemplateOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v *SessionTemplate) pulumi.StringMapOutput { return v.Labels }).(pulumi.StringMapOutput)
}

func (o SessionTemplateOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *SessionTemplate) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

// The resource name of the session template.
func (o SessionTemplateOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *SessionTemplate) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o SessionTemplateOutput) Project() pulumi.StringOutput {
	return o.ApplyT(func(v *SessionTemplate) pulumi.StringOutput { return v.Project }).(pulumi.StringOutput)
}

// Optional. Runtime configuration for session execution.
func (o SessionTemplateOutput) RuntimeConfig() RuntimeConfigResponseOutput {
	return o.ApplyT(func(v *SessionTemplate) RuntimeConfigResponseOutput { return v.RuntimeConfig }).(RuntimeConfigResponseOutput)
}

// The time the template was last updated.
func (o SessionTemplateOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *SessionTemplate) pulumi.StringOutput { return v.UpdateTime }).(pulumi.StringOutput)
}

// A session template UUID (Unique Universal Identifier). The service generates this value when it creates the session template.
func (o SessionTemplateOutput) Uuid() pulumi.StringOutput {
	return o.ApplyT(func(v *SessionTemplate) pulumi.StringOutput { return v.Uuid }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SessionTemplateInput)(nil)).Elem(), &SessionTemplate{})
	pulumi.RegisterOutputType(SessionTemplateOutput{})
}
