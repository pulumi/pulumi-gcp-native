// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const EntryType = {
    /**
     * Default unknown type.
     */
    EntryTypeUnspecified: "ENTRY_TYPE_UNSPECIFIED",
    /**
     * The entry type that has a GoogleSQL schema, including logical views.
     */
    Table: "TABLE",
    /**
     * The type of models. For more information, see [Supported models in BigQuery ML](/bigquery/docs/bqml-introduction#supported_models).
     */
    Model: "MODEL",
    /**
     * An entry type for streaming entries. For example, a Pub/Sub topic.
     */
    DataStream: "DATA_STREAM",
    /**
     * An entry type for a set of files or objects. For example, a Cloud Storage fileset.
     */
    Fileset: "FILESET",
    /**
     * A group of servers that work together. For example, a Kafka cluster.
     */
    Cluster: "CLUSTER",
    /**
     * A database.
     */
    Database: "DATABASE",
    /**
     * Connection to a data source. For example, a BigQuery connection.
     */
    DataSourceConnection: "DATA_SOURCE_CONNECTION",
    /**
     * Routine, for example, a BigQuery routine.
     */
    Routine: "ROUTINE",
    /**
     * A Dataplex lake.
     */
    Lake: "LAKE",
    /**
     * A Dataplex zone.
     */
    Zone: "ZONE",
    /**
     * A service, for example, a Dataproc Metastore service.
     */
    Service: "SERVICE",
    /**
     * Schema within a relational database.
     */
    DatabaseSchema: "DATABASE_SCHEMA",
    /**
     * A Dashboard, for example from Looker.
     */
    Dashboard: "DASHBOARD",
    /**
     * A Looker Explore. For more information, see [Looker Explore API] (https://developers.looker.com/api/explorer/4.0/methods/LookmlModel/lookml_model_explore).
     */
    Explore: "EXPLORE",
    /**
     * A Looker Look. For more information, see [Looker Look API] (https://developers.looker.com/api/explorer/4.0/methods/Look).
     */
    Look: "LOOK",
} as const;

/**
 * The type of the entry. For details, see [`EntryType`](#entrytype).
 */
export type EntryType = (typeof EntryType)[keyof typeof EntryType];

export const GoogleCloudDatacatalogV1ColumnSchemaHighestIndexingType = {
    /**
     * Unspecified.
     */
    IndexingTypeUnspecified: "INDEXING_TYPE_UNSPECIFIED",
    /**
     * Column not a part of an index.
     */
    IndexingTypeNone: "INDEXING_TYPE_NONE",
    /**
     * Column Part of non unique index.
     */
    IndexingTypeNonUnique: "INDEXING_TYPE_NON_UNIQUE",
    /**
     * Column part of unique index.
     */
    IndexingTypeUnique: "INDEXING_TYPE_UNIQUE",
    /**
     * Column part of the primary key.
     */
    IndexingTypePrimaryKey: "INDEXING_TYPE_PRIMARY_KEY",
} as const;

/**
 * Optional. Most important inclusion of this column.
 */
export type GoogleCloudDatacatalogV1ColumnSchemaHighestIndexingType = (typeof GoogleCloudDatacatalogV1ColumnSchemaHighestIndexingType)[keyof typeof GoogleCloudDatacatalogV1ColumnSchemaHighestIndexingType];

export const GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecType = {
    /**
     * Unspecified.
     */
    LookerColumnTypeUnspecified: "LOOKER_COLUMN_TYPE_UNSPECIFIED",
    /**
     * Dimension.
     */
    Dimension: "DIMENSION",
    /**
     * Dimension group - parent for Dimension.
     */
    DimensionGroup: "DIMENSION_GROUP",
    /**
     * Filter.
     */
    Filter: "FILTER",
    /**
     * Measure.
     */
    Measure: "MEASURE",
    /**
     * Parameter.
     */
    Parameter: "PARAMETER",
} as const;

/**
 * Looker specific column type of this column.
 */
export type GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecType = (typeof GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecType)[keyof typeof GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecType];

export const GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecViewType = {
    /**
     * Default unknown view type.
     */
    ViewTypeUnspecified: "VIEW_TYPE_UNSPECIFIED",
    /**
     * Standard view.
     */
    StandardView: "STANDARD_VIEW",
    /**
     * Materialized view.
     */
    MaterializedView: "MATERIALIZED_VIEW",
} as const;

/**
 * Type of this view.
 */
export type GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecViewType = (typeof GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecViewType)[keyof typeof GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecViewType];

export const GoogleCloudDatacatalogV1DatabaseTableSpecType = {
    /**
     * Default unknown table type.
     */
    TableTypeUnspecified: "TABLE_TYPE_UNSPECIFIED",
    /**
     * Native table.
     */
    Native: "NATIVE",
    /**
     * External table.
     */
    External: "EXTERNAL",
} as const;

/**
 * Type of this table.
 */
export type GoogleCloudDatacatalogV1DatabaseTableSpecType = (typeof GoogleCloudDatacatalogV1DatabaseTableSpecType)[keyof typeof GoogleCloudDatacatalogV1DatabaseTableSpecType];

export const GoogleCloudDatacatalogV1FieldTypePrimitiveType = {
    /**
     * The default invalid value for a type.
     */
    PrimitiveTypeUnspecified: "PRIMITIVE_TYPE_UNSPECIFIED",
    /**
     * A double precision number.
     */
    Double: "DOUBLE",
    /**
     * An UTF-8 string.
     */
    String: "STRING",
    /**
     * A boolean value.
     */
    Bool: "BOOL",
    /**
     * A timestamp.
     */
    Timestamp: "TIMESTAMP",
    /**
     * A Richtext description.
     */
    Richtext: "RICHTEXT",
} as const;

/**
 * Primitive types, such as string, boolean, etc.
 */
export type GoogleCloudDatacatalogV1FieldTypePrimitiveType = (typeof GoogleCloudDatacatalogV1FieldTypePrimitiveType)[keyof typeof GoogleCloudDatacatalogV1FieldTypePrimitiveType];

export const GoogleCloudDatacatalogV1RoutineSpecArgumentMode = {
    /**
     * Unspecified mode.
     */
    ModeUnspecified: "MODE_UNSPECIFIED",
    /**
     * The argument is input-only.
     */
    In: "IN",
    /**
     * The argument is output-only.
     */
    Out: "OUT",
    /**
     * The argument is both an input and an output.
     */
    Inout: "INOUT",
} as const;

/**
 * Specifies whether the argument is input or output.
 */
export type GoogleCloudDatacatalogV1RoutineSpecArgumentMode = (typeof GoogleCloudDatacatalogV1RoutineSpecArgumentMode)[keyof typeof GoogleCloudDatacatalogV1RoutineSpecArgumentMode];

export const GoogleCloudDatacatalogV1RoutineSpecRoutineType = {
    /**
     * Unspecified type.
     */
    RoutineTypeUnspecified: "ROUTINE_TYPE_UNSPECIFIED",
    /**
     * Non-builtin permanent scalar function.
     */
    ScalarFunction: "SCALAR_FUNCTION",
    /**
     * Stored procedure.
     */
    Procedure: "PROCEDURE",
} as const;

/**
 * The type of the routine.
 */
export type GoogleCloudDatacatalogV1RoutineSpecRoutineType = (typeof GoogleCloudDatacatalogV1RoutineSpecRoutineType)[keyof typeof GoogleCloudDatacatalogV1RoutineSpecRoutineType];

export const GoogleCloudDatacatalogV1VertexDatasetSpecDataType = {
    /**
     * Should not be used.
     */
    DataTypeUnspecified: "DATA_TYPE_UNSPECIFIED",
    /**
     * Structured data dataset.
     */
    Table: "TABLE",
    /**
     * Image dataset which supports ImageClassification, ImageObjectDetection and ImageSegmentation problems.
     */
    Image: "IMAGE",
    /**
     * Document dataset which supports TextClassification, TextExtraction and TextSentiment problems.
     */
    Text: "TEXT",
    /**
     * Video dataset which supports VideoClassification, VideoObjectTracking and VideoActionRecognition problems.
     */
    Video: "VIDEO",
    /**
     * Conversation dataset which supports conversation problems.
     */
    Conversation: "CONVERSATION",
    /**
     * TimeSeries dataset.
     */
    TimeSeries: "TIME_SERIES",
    /**
     * Document dataset which supports DocumentAnnotation problems.
     */
    Document: "DOCUMENT",
    /**
     * TextToSpeech dataset which supports TextToSpeech problems.
     */
    TextToSpeech: "TEXT_TO_SPEECH",
    /**
     * Translation dataset which supports Translation problems.
     */
    Translation: "TRANSLATION",
    /**
     * Store Vision dataset which is used for HITL integration.
     */
    StoreVision: "STORE_VISION",
    /**
     * Enterprise Knowledge Graph dataset which is used for HITL labeling integration.
     */
    EnterpriseKnowledgeGraph: "ENTERPRISE_KNOWLEDGE_GRAPH",
    /**
     * Text prompt dataset which supports Large Language Models.
     */
    TextPrompt: "TEXT_PROMPT",
} as const;

/**
 * Type of the dataset.
 */
export type GoogleCloudDatacatalogV1VertexDatasetSpecDataType = (typeof GoogleCloudDatacatalogV1VertexDatasetSpecDataType)[keyof typeof GoogleCloudDatacatalogV1VertexDatasetSpecDataType];

export const GoogleCloudDatacatalogV1VertexModelSourceInfoSourceType = {
    /**
     * Should not be used.
     */
    ModelSourceTypeUnspecified: "MODEL_SOURCE_TYPE_UNSPECIFIED",
    /**
     * The Model is uploaded by automl training pipeline.
     */
    Automl: "AUTOML",
    /**
     * The Model is uploaded by user or custom training pipeline.
     */
    Custom: "CUSTOM",
    /**
     * The Model is registered and sync'ed from BigQuery ML.
     */
    Bqml: "BQML",
    /**
     * The Model is saved or tuned from Model Garden.
     */
    ModelGarden: "MODEL_GARDEN",
} as const;

/**
 * Type of the model source.
 */
export type GoogleCloudDatacatalogV1VertexModelSourceInfoSourceType = (typeof GoogleCloudDatacatalogV1VertexModelSourceInfoSourceType)[keyof typeof GoogleCloudDatacatalogV1VertexModelSourceInfoSourceType];

export const TaxonomyActivatedPolicyTypesItem = {
    /**
     * Unspecified policy type.
     */
    PolicyTypeUnspecified: "POLICY_TYPE_UNSPECIFIED",
    /**
     * Fine-grained access control policy that enables access control on tagged sub-resources.
     */
    FineGrainedAccessControl: "FINE_GRAINED_ACCESS_CONTROL",
} as const;

export type TaxonomyActivatedPolicyTypesItem = (typeof TaxonomyActivatedPolicyTypesItem)[keyof typeof TaxonomyActivatedPolicyTypesItem];
