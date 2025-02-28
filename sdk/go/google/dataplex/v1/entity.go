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

// Create a metadata entity.
// Auto-naming is currently not supported for this resource.
type Entity struct {
	pulumi.CustomResourceState

	// Identifies the access mechanism to the entity. Not user settable.
	Access GoogleCloudDataplexV1StorageAccessResponseOutput `pulumi:"access"`
	// Immutable. The ID of the asset associated with the storage location containing the entity data. The entity must be with in the same zone with the asset.
	Asset pulumi.StringOutput `pulumi:"asset"`
	// The name of the associated Data Catalog entry.
	CatalogEntry pulumi.StringOutput `pulumi:"catalogEntry"`
	// Metadata stores that the entity is compatible with.
	Compatibility GoogleCloudDataplexV1EntityCompatibilityStatusResponseOutput `pulumi:"compatibility"`
	// The time when the entity was created.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// Immutable. The storage path of the entity data. For Cloud Storage data, this is the fully-qualified path to the entity, such as gs://bucket/path/to/data. For BigQuery data, this is the name of the table resource, such as projects/project_id/datasets/dataset_id/tables/table_id.
	DataPath pulumi.StringOutput `pulumi:"dataPath"`
	// Optional. The set of items within the data path constituting the data in the entity, represented as a glob path. Example: gs://bucket/path/to/data/**/*.csv.
	DataPathPattern pulumi.StringOutput `pulumi:"dataPathPattern"`
	// Optional. User friendly longer description text. Must be shorter than or equal to 1024 characters.
	Description pulumi.StringOutput `pulumi:"description"`
	// Optional. Display name must be shorter than or equal to 256 characters.
	DisplayName pulumi.StringOutput `pulumi:"displayName"`
	// Optional. The etag associated with the entity, which can be retrieved with a GetEntity request. Required for update and delete requests.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// Identifies the storage format of the entity data. It does not apply to entities with data stored in BigQuery.
	Format   GoogleCloudDataplexV1StorageFormatResponseOutput `pulumi:"format"`
	LakeId   pulumi.StringOutput                              `pulumi:"lakeId"`
	Location pulumi.StringOutput                              `pulumi:"location"`
	// The resource name of the entity, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/entities/{id}.
	Name    pulumi.StringOutput `pulumi:"name"`
	Project pulumi.StringOutput `pulumi:"project"`
	// The description of the data structure and layout. The schema is not included in list responses. It is only included in SCHEMA and FULL entity views of a GetEntity response.
	Schema GoogleCloudDataplexV1SchemaResponseOutput `pulumi:"schema"`
	// Immutable. Identifies the storage system of the entity data.
	System pulumi.StringOutput `pulumi:"system"`
	// Immutable. The type of entity.
	Type pulumi.StringOutput `pulumi:"type"`
	// System generated unique ID for the Entity. This ID will be different if the Entity is deleted and re-created with the same name.
	Uid pulumi.StringOutput `pulumi:"uid"`
	// The time when the entity was last updated.
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
	Zone       pulumi.StringOutput `pulumi:"zone"`
}

// NewEntity registers a new resource with the given unique name, arguments, and options.
func NewEntity(ctx *pulumi.Context,
	name string, args *EntityArgs, opts ...pulumi.ResourceOption) (*Entity, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Asset == nil {
		return nil, errors.New("invalid value for required argument 'Asset'")
	}
	if args.DataPath == nil {
		return nil, errors.New("invalid value for required argument 'DataPath'")
	}
	if args.Format == nil {
		return nil, errors.New("invalid value for required argument 'Format'")
	}
	if args.Id == nil {
		return nil, errors.New("invalid value for required argument 'Id'")
	}
	if args.LakeId == nil {
		return nil, errors.New("invalid value for required argument 'LakeId'")
	}
	if args.Schema == nil {
		return nil, errors.New("invalid value for required argument 'Schema'")
	}
	if args.System == nil {
		return nil, errors.New("invalid value for required argument 'System'")
	}
	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"lakeId",
		"location",
		"project",
		"zone",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Entity
	err := ctx.RegisterResource("google-native:dataplex/v1:Entity", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEntity gets an existing Entity resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEntity(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EntityState, opts ...pulumi.ResourceOption) (*Entity, error) {
	var resource Entity
	err := ctx.ReadResource("google-native:dataplex/v1:Entity", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Entity resources.
type entityState struct {
}

type EntityState struct {
}

func (EntityState) ElementType() reflect.Type {
	return reflect.TypeOf((*entityState)(nil)).Elem()
}

type entityArgs struct {
	// Immutable. The ID of the asset associated with the storage location containing the entity data. The entity must be with in the same zone with the asset.
	Asset string `pulumi:"asset"`
	// Immutable. The storage path of the entity data. For Cloud Storage data, this is the fully-qualified path to the entity, such as gs://bucket/path/to/data. For BigQuery data, this is the name of the table resource, such as projects/project_id/datasets/dataset_id/tables/table_id.
	DataPath string `pulumi:"dataPath"`
	// Optional. The set of items within the data path constituting the data in the entity, represented as a glob path. Example: gs://bucket/path/to/data/**/*.csv.
	DataPathPattern *string `pulumi:"dataPathPattern"`
	// Optional. User friendly longer description text. Must be shorter than or equal to 1024 characters.
	Description *string `pulumi:"description"`
	// Optional. Display name must be shorter than or equal to 256 characters.
	DisplayName *string `pulumi:"displayName"`
	// Optional. The etag associated with the entity, which can be retrieved with a GetEntity request. Required for update and delete requests.
	Etag *string `pulumi:"etag"`
	// Identifies the storage format of the entity data. It does not apply to entities with data stored in BigQuery.
	Format GoogleCloudDataplexV1StorageFormat `pulumi:"format"`
	// A user-provided entity ID. It is mutable, and will be used as the published table name. Specifying a new ID in an update entity request will override the existing value. The ID must contain only letters (a-z, A-Z), numbers (0-9), and underscores, and consist of 256 or fewer characters.
	Id       string  `pulumi:"id"`
	LakeId   string  `pulumi:"lakeId"`
	Location *string `pulumi:"location"`
	Project  *string `pulumi:"project"`
	// The description of the data structure and layout. The schema is not included in list responses. It is only included in SCHEMA and FULL entity views of a GetEntity response.
	Schema GoogleCloudDataplexV1Schema `pulumi:"schema"`
	// Immutable. Identifies the storage system of the entity data.
	System EntitySystem `pulumi:"system"`
	// Immutable. The type of entity.
	Type EntityType `pulumi:"type"`
	Zone *string    `pulumi:"zone"`
}

// The set of arguments for constructing a Entity resource.
type EntityArgs struct {
	// Immutable. The ID of the asset associated with the storage location containing the entity data. The entity must be with in the same zone with the asset.
	Asset pulumi.StringInput
	// Immutable. The storage path of the entity data. For Cloud Storage data, this is the fully-qualified path to the entity, such as gs://bucket/path/to/data. For BigQuery data, this is the name of the table resource, such as projects/project_id/datasets/dataset_id/tables/table_id.
	DataPath pulumi.StringInput
	// Optional. The set of items within the data path constituting the data in the entity, represented as a glob path. Example: gs://bucket/path/to/data/**/*.csv.
	DataPathPattern pulumi.StringPtrInput
	// Optional. User friendly longer description text. Must be shorter than or equal to 1024 characters.
	Description pulumi.StringPtrInput
	// Optional. Display name must be shorter than or equal to 256 characters.
	DisplayName pulumi.StringPtrInput
	// Optional. The etag associated with the entity, which can be retrieved with a GetEntity request. Required for update and delete requests.
	Etag pulumi.StringPtrInput
	// Identifies the storage format of the entity data. It does not apply to entities with data stored in BigQuery.
	Format GoogleCloudDataplexV1StorageFormatInput
	// A user-provided entity ID. It is mutable, and will be used as the published table name. Specifying a new ID in an update entity request will override the existing value. The ID must contain only letters (a-z, A-Z), numbers (0-9), and underscores, and consist of 256 or fewer characters.
	Id       pulumi.StringInput
	LakeId   pulumi.StringInput
	Location pulumi.StringPtrInput
	Project  pulumi.StringPtrInput
	// The description of the data structure and layout. The schema is not included in list responses. It is only included in SCHEMA and FULL entity views of a GetEntity response.
	Schema GoogleCloudDataplexV1SchemaInput
	// Immutable. Identifies the storage system of the entity data.
	System EntitySystemInput
	// Immutable. The type of entity.
	Type EntityTypeInput
	Zone pulumi.StringPtrInput
}

func (EntityArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*entityArgs)(nil)).Elem()
}

type EntityInput interface {
	pulumi.Input

	ToEntityOutput() EntityOutput
	ToEntityOutputWithContext(ctx context.Context) EntityOutput
}

func (*Entity) ElementType() reflect.Type {
	return reflect.TypeOf((**Entity)(nil)).Elem()
}

func (i *Entity) ToEntityOutput() EntityOutput {
	return i.ToEntityOutputWithContext(context.Background())
}

func (i *Entity) ToEntityOutputWithContext(ctx context.Context) EntityOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EntityOutput)
}

type EntityOutput struct{ *pulumi.OutputState }

func (EntityOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Entity)(nil)).Elem()
}

func (o EntityOutput) ToEntityOutput() EntityOutput {
	return o
}

func (o EntityOutput) ToEntityOutputWithContext(ctx context.Context) EntityOutput {
	return o
}

// Identifies the access mechanism to the entity. Not user settable.
func (o EntityOutput) Access() GoogleCloudDataplexV1StorageAccessResponseOutput {
	return o.ApplyT(func(v *Entity) GoogleCloudDataplexV1StorageAccessResponseOutput { return v.Access }).(GoogleCloudDataplexV1StorageAccessResponseOutput)
}

// Immutable. The ID of the asset associated with the storage location containing the entity data. The entity must be with in the same zone with the asset.
func (o EntityOutput) Asset() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.Asset }).(pulumi.StringOutput)
}

// The name of the associated Data Catalog entry.
func (o EntityOutput) CatalogEntry() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.CatalogEntry }).(pulumi.StringOutput)
}

// Metadata stores that the entity is compatible with.
func (o EntityOutput) Compatibility() GoogleCloudDataplexV1EntityCompatibilityStatusResponseOutput {
	return o.ApplyT(func(v *Entity) GoogleCloudDataplexV1EntityCompatibilityStatusResponseOutput { return v.Compatibility }).(GoogleCloudDataplexV1EntityCompatibilityStatusResponseOutput)
}

// The time when the entity was created.
func (o EntityOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.CreateTime }).(pulumi.StringOutput)
}

// Immutable. The storage path of the entity data. For Cloud Storage data, this is the fully-qualified path to the entity, such as gs://bucket/path/to/data. For BigQuery data, this is the name of the table resource, such as projects/project_id/datasets/dataset_id/tables/table_id.
func (o EntityOutput) DataPath() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.DataPath }).(pulumi.StringOutput)
}

// Optional. The set of items within the data path constituting the data in the entity, represented as a glob path. Example: gs://bucket/path/to/data/**/*.csv.
func (o EntityOutput) DataPathPattern() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.DataPathPattern }).(pulumi.StringOutput)
}

// Optional. User friendly longer description text. Must be shorter than or equal to 1024 characters.
func (o EntityOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// Optional. Display name must be shorter than or equal to 256 characters.
func (o EntityOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.DisplayName }).(pulumi.StringOutput)
}

// Optional. The etag associated with the entity, which can be retrieved with a GetEntity request. Required for update and delete requests.
func (o EntityOutput) Etag() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.Etag }).(pulumi.StringOutput)
}

// Identifies the storage format of the entity data. It does not apply to entities with data stored in BigQuery.
func (o EntityOutput) Format() GoogleCloudDataplexV1StorageFormatResponseOutput {
	return o.ApplyT(func(v *Entity) GoogleCloudDataplexV1StorageFormatResponseOutput { return v.Format }).(GoogleCloudDataplexV1StorageFormatResponseOutput)
}

func (o EntityOutput) LakeId() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.LakeId }).(pulumi.StringOutput)
}

func (o EntityOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

// The resource name of the entity, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/entities/{id}.
func (o EntityOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o EntityOutput) Project() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.Project }).(pulumi.StringOutput)
}

// The description of the data structure and layout. The schema is not included in list responses. It is only included in SCHEMA and FULL entity views of a GetEntity response.
func (o EntityOutput) Schema() GoogleCloudDataplexV1SchemaResponseOutput {
	return o.ApplyT(func(v *Entity) GoogleCloudDataplexV1SchemaResponseOutput { return v.Schema }).(GoogleCloudDataplexV1SchemaResponseOutput)
}

// Immutable. Identifies the storage system of the entity data.
func (o EntityOutput) System() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.System }).(pulumi.StringOutput)
}

// Immutable. The type of entity.
func (o EntityOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

// System generated unique ID for the Entity. This ID will be different if the Entity is deleted and re-created with the same name.
func (o EntityOutput) Uid() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.Uid }).(pulumi.StringOutput)
}

// The time when the entity was last updated.
func (o EntityOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.UpdateTime }).(pulumi.StringOutput)
}

func (o EntityOutput) Zone() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.Zone }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EntityInput)(nil)).Elem(), &Entity{})
	pulumi.RegisterOutputType(EntityOutput{})
}
