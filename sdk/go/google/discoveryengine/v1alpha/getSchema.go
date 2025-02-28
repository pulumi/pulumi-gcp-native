// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1alpha

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Gets a Schema.
func LookupSchema(ctx *pulumi.Context, args *LookupSchemaArgs, opts ...pulumi.InvokeOption) (*LookupSchemaResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupSchemaResult
	err := ctx.Invoke("google-native:discoveryengine/v1alpha:getSchema", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupSchemaArgs struct {
	CollectionId string  `pulumi:"collectionId"`
	DataStoreId  string  `pulumi:"dataStoreId"`
	Location     string  `pulumi:"location"`
	Project      *string `pulumi:"project"`
	SchemaId     string  `pulumi:"schemaId"`
}

type LookupSchemaResult struct {
	// Configurations for fields of the schema.
	FieldConfigs []GoogleCloudDiscoveryengineV1alphaFieldConfigResponse `pulumi:"fieldConfigs"`
	// The JSON representation of the schema.
	JsonSchema string `pulumi:"jsonSchema"`
	// Immutable. The full resource name of the schema, in the format of `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/schemas/{schema}`. This field must be a UTF-8 encoded string with a length limit of 1024 characters.
	Name string `pulumi:"name"`
	// The structured representation of the schema.
	StructSchema map[string]interface{} `pulumi:"structSchema"`
}

func LookupSchemaOutput(ctx *pulumi.Context, args LookupSchemaOutputArgs, opts ...pulumi.InvokeOption) LookupSchemaResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSchemaResult, error) {
			args := v.(LookupSchemaArgs)
			r, err := LookupSchema(ctx, &args, opts...)
			var s LookupSchemaResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupSchemaResultOutput)
}

type LookupSchemaOutputArgs struct {
	CollectionId pulumi.StringInput    `pulumi:"collectionId"`
	DataStoreId  pulumi.StringInput    `pulumi:"dataStoreId"`
	Location     pulumi.StringInput    `pulumi:"location"`
	Project      pulumi.StringPtrInput `pulumi:"project"`
	SchemaId     pulumi.StringInput    `pulumi:"schemaId"`
}

func (LookupSchemaOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSchemaArgs)(nil)).Elem()
}

type LookupSchemaResultOutput struct{ *pulumi.OutputState }

func (LookupSchemaResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSchemaResult)(nil)).Elem()
}

func (o LookupSchemaResultOutput) ToLookupSchemaResultOutput() LookupSchemaResultOutput {
	return o
}

func (o LookupSchemaResultOutput) ToLookupSchemaResultOutputWithContext(ctx context.Context) LookupSchemaResultOutput {
	return o
}

// Configurations for fields of the schema.
func (o LookupSchemaResultOutput) FieldConfigs() GoogleCloudDiscoveryengineV1alphaFieldConfigResponseArrayOutput {
	return o.ApplyT(func(v LookupSchemaResult) []GoogleCloudDiscoveryengineV1alphaFieldConfigResponse {
		return v.FieldConfigs
	}).(GoogleCloudDiscoveryengineV1alphaFieldConfigResponseArrayOutput)
}

// The JSON representation of the schema.
func (o LookupSchemaResultOutput) JsonSchema() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSchemaResult) string { return v.JsonSchema }).(pulumi.StringOutput)
}

// Immutable. The full resource name of the schema, in the format of `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/schemas/{schema}`. This field must be a UTF-8 encoded string with a length limit of 1024 characters.
func (o LookupSchemaResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSchemaResult) string { return v.Name }).(pulumi.StringOutput)
}

// The structured representation of the schema.
func (o LookupSchemaResultOutput) StructSchema() pulumi.MapOutput {
	return o.ApplyT(func(v LookupSchemaResult) map[string]interface{} { return v.StructSchema }).(pulumi.MapOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSchemaResultOutput{})
}
