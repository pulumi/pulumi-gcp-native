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

// Creates an Execution associated with a MetadataStore.
// Auto-naming is currently not supported for this resource.
type Execution struct {
	pulumi.CustomResourceState

	// Timestamp when this Execution was created.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// Description of the Execution
	Description pulumi.StringOutput `pulumi:"description"`
	// User provided display name of the Execution. May be up to 128 Unicode characters.
	DisplayName pulumi.StringOutput `pulumi:"displayName"`
	// An eTag used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// The {execution} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}` If not provided, the Execution's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all Executions in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting Execution.)
	ExecutionId pulumi.StringPtrOutput `pulumi:"executionId"`
	// The labels with user-defined metadata to organize your Executions. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Execution (System labels are excluded).
	Labels   pulumi.StringMapOutput `pulumi:"labels"`
	Location pulumi.StringOutput    `pulumi:"location"`
	// Properties of the Execution. Top level metadata keys' heading and trailing spaces will be trimmed. The size of this field should not exceed 200KB.
	Metadata        pulumi.MapOutput    `pulumi:"metadata"`
	MetadataStoreId pulumi.StringOutput `pulumi:"metadataStoreId"`
	// The resource name of the Execution.
	Name    pulumi.StringOutput `pulumi:"name"`
	Project pulumi.StringOutput `pulumi:"project"`
	// The title of the schema describing the metadata. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store.
	SchemaTitle pulumi.StringOutput `pulumi:"schemaTitle"`
	// The version of the schema in `schema_title` to use. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store.
	SchemaVersion pulumi.StringOutput `pulumi:"schemaVersion"`
	// The state of this Execution. This is a property of the Execution, and does not imply or capture any ongoing process. This property is managed by clients (such as Vertex AI Pipelines) and the system does not prescribe or check the validity of state transitions.
	State pulumi.StringOutput `pulumi:"state"`
	// Timestamp when this Execution was last updated.
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
}

// NewExecution registers a new resource with the given unique name, arguments, and options.
func NewExecution(ctx *pulumi.Context,
	name string, args *ExecutionArgs, opts ...pulumi.ResourceOption) (*Execution, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.MetadataStoreId == nil {
		return nil, errors.New("invalid value for required argument 'MetadataStoreId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"location",
		"metadataStoreId",
		"project",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Execution
	err := ctx.RegisterResource("google-native:aiplatform/v1:Execution", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetExecution gets an existing Execution resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetExecution(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ExecutionState, opts ...pulumi.ResourceOption) (*Execution, error) {
	var resource Execution
	err := ctx.ReadResource("google-native:aiplatform/v1:Execution", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Execution resources.
type executionState struct {
}

type ExecutionState struct {
}

func (ExecutionState) ElementType() reflect.Type {
	return reflect.TypeOf((*executionState)(nil)).Elem()
}

type executionArgs struct {
	// Description of the Execution
	Description *string `pulumi:"description"`
	// User provided display name of the Execution. May be up to 128 Unicode characters.
	DisplayName *string `pulumi:"displayName"`
	// An eTag used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
	Etag *string `pulumi:"etag"`
	// The {execution} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}` If not provided, the Execution's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all Executions in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting Execution.)
	ExecutionId *string `pulumi:"executionId"`
	// The labels with user-defined metadata to organize your Executions. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Execution (System labels are excluded).
	Labels   map[string]string `pulumi:"labels"`
	Location *string           `pulumi:"location"`
	// Properties of the Execution. Top level metadata keys' heading and trailing spaces will be trimmed. The size of this field should not exceed 200KB.
	Metadata        map[string]interface{} `pulumi:"metadata"`
	MetadataStoreId string                 `pulumi:"metadataStoreId"`
	Project         *string                `pulumi:"project"`
	// The title of the schema describing the metadata. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store.
	SchemaTitle *string `pulumi:"schemaTitle"`
	// The version of the schema in `schema_title` to use. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store.
	SchemaVersion *string `pulumi:"schemaVersion"`
	// The state of this Execution. This is a property of the Execution, and does not imply or capture any ongoing process. This property is managed by clients (such as Vertex AI Pipelines) and the system does not prescribe or check the validity of state transitions.
	State *ExecutionStateEnum `pulumi:"state"`
}

// The set of arguments for constructing a Execution resource.
type ExecutionArgs struct {
	// Description of the Execution
	Description pulumi.StringPtrInput
	// User provided display name of the Execution. May be up to 128 Unicode characters.
	DisplayName pulumi.StringPtrInput
	// An eTag used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
	Etag pulumi.StringPtrInput
	// The {execution} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}` If not provided, the Execution's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all Executions in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting Execution.)
	ExecutionId pulumi.StringPtrInput
	// The labels with user-defined metadata to organize your Executions. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Execution (System labels are excluded).
	Labels   pulumi.StringMapInput
	Location pulumi.StringPtrInput
	// Properties of the Execution. Top level metadata keys' heading and trailing spaces will be trimmed. The size of this field should not exceed 200KB.
	Metadata        pulumi.MapInput
	MetadataStoreId pulumi.StringInput
	Project         pulumi.StringPtrInput
	// The title of the schema describing the metadata. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store.
	SchemaTitle pulumi.StringPtrInput
	// The version of the schema in `schema_title` to use. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store.
	SchemaVersion pulumi.StringPtrInput
	// The state of this Execution. This is a property of the Execution, and does not imply or capture any ongoing process. This property is managed by clients (such as Vertex AI Pipelines) and the system does not prescribe or check the validity of state transitions.
	State ExecutionStateEnumPtrInput
}

func (ExecutionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*executionArgs)(nil)).Elem()
}

type ExecutionInput interface {
	pulumi.Input

	ToExecutionOutput() ExecutionOutput
	ToExecutionOutputWithContext(ctx context.Context) ExecutionOutput
}

func (*Execution) ElementType() reflect.Type {
	return reflect.TypeOf((**Execution)(nil)).Elem()
}

func (i *Execution) ToExecutionOutput() ExecutionOutput {
	return i.ToExecutionOutputWithContext(context.Background())
}

func (i *Execution) ToExecutionOutputWithContext(ctx context.Context) ExecutionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ExecutionOutput)
}

type ExecutionOutput struct{ *pulumi.OutputState }

func (ExecutionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Execution)(nil)).Elem()
}

func (o ExecutionOutput) ToExecutionOutput() ExecutionOutput {
	return o
}

func (o ExecutionOutput) ToExecutionOutputWithContext(ctx context.Context) ExecutionOutput {
	return o
}

// Timestamp when this Execution was created.
func (o ExecutionOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Execution) pulumi.StringOutput { return v.CreateTime }).(pulumi.StringOutput)
}

// Description of the Execution
func (o ExecutionOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *Execution) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// User provided display name of the Execution. May be up to 128 Unicode characters.
func (o ExecutionOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v *Execution) pulumi.StringOutput { return v.DisplayName }).(pulumi.StringOutput)
}

// An eTag used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
func (o ExecutionOutput) Etag() pulumi.StringOutput {
	return o.ApplyT(func(v *Execution) pulumi.StringOutput { return v.Etag }).(pulumi.StringOutput)
}

// The {execution} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}` If not provided, the Execution's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/a-z-/`. Must be unique across all Executions in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting Execution.)
func (o ExecutionOutput) ExecutionId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Execution) pulumi.StringPtrOutput { return v.ExecutionId }).(pulumi.StringPtrOutput)
}

// The labels with user-defined metadata to organize your Executions. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Execution (System labels are excluded).
func (o ExecutionOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Execution) pulumi.StringMapOutput { return v.Labels }).(pulumi.StringMapOutput)
}

func (o ExecutionOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *Execution) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

// Properties of the Execution. Top level metadata keys' heading and trailing spaces will be trimmed. The size of this field should not exceed 200KB.
func (o ExecutionOutput) Metadata() pulumi.MapOutput {
	return o.ApplyT(func(v *Execution) pulumi.MapOutput { return v.Metadata }).(pulumi.MapOutput)
}

func (o ExecutionOutput) MetadataStoreId() pulumi.StringOutput {
	return o.ApplyT(func(v *Execution) pulumi.StringOutput { return v.MetadataStoreId }).(pulumi.StringOutput)
}

// The resource name of the Execution.
func (o ExecutionOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Execution) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o ExecutionOutput) Project() pulumi.StringOutput {
	return o.ApplyT(func(v *Execution) pulumi.StringOutput { return v.Project }).(pulumi.StringOutput)
}

// The title of the schema describing the metadata. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store.
func (o ExecutionOutput) SchemaTitle() pulumi.StringOutput {
	return o.ApplyT(func(v *Execution) pulumi.StringOutput { return v.SchemaTitle }).(pulumi.StringOutput)
}

// The version of the schema in `schema_title` to use. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store.
func (o ExecutionOutput) SchemaVersion() pulumi.StringOutput {
	return o.ApplyT(func(v *Execution) pulumi.StringOutput { return v.SchemaVersion }).(pulumi.StringOutput)
}

// The state of this Execution. This is a property of the Execution, and does not imply or capture any ongoing process. This property is managed by clients (such as Vertex AI Pipelines) and the system does not prescribe or check the validity of state transitions.
func (o ExecutionOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v *Execution) pulumi.StringOutput { return v.State }).(pulumi.StringOutput)
}

// Timestamp when this Execution was last updated.
func (o ExecutionOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Execution) pulumi.StringOutput { return v.UpdateTime }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ExecutionInput)(nil)).Elem(), &Execution{})
	pulumi.RegisterOutputType(ExecutionOutput{})
}
