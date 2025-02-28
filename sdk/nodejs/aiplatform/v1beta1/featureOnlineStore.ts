// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Creates a new FeatureOnlineStore in a given project and location.
 * Auto-naming is currently not supported for this resource.
 */
export class FeatureOnlineStore extends pulumi.CustomResource {
    /**
     * Get an existing FeatureOnlineStore resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): FeatureOnlineStore {
        return new FeatureOnlineStore(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:aiplatform/v1beta1:FeatureOnlineStore';

    /**
     * Returns true if the given object is an instance of FeatureOnlineStore.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is FeatureOnlineStore {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === FeatureOnlineStore.__pulumiType;
    }

    /**
     * Contains settings for the Cloud Bigtable instance that will be created to serve featureValues for all FeatureViews under this FeatureOnlineStore.
     */
    public readonly bigtable!: pulumi.Output<outputs.aiplatform.v1beta1.GoogleCloudAiplatformV1beta1FeatureOnlineStoreBigtableResponse>;
    /**
     * Timestamp when this FeatureOnlineStore was created.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * Optional. The dedicated serving endpoint for this FeatureOnlineStore, which is different from common Vertex service endpoint.
     */
    public readonly dedicatedServingEndpoint!: pulumi.Output<outputs.aiplatform.v1beta1.GoogleCloudAiplatformV1beta1FeatureOnlineStoreDedicatedServingEndpointResponse>;
    /**
     * Optional. The settings for embedding management in FeatureOnlineStore.
     */
    public readonly embeddingManagement!: pulumi.Output<outputs.aiplatform.v1beta1.GoogleCloudAiplatformV1beta1FeatureOnlineStoreEmbeddingManagementResponse>;
    /**
     * Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
     */
    public readonly etag!: pulumi.Output<string>;
    /**
     * Required. The ID to use for this FeatureOnlineStore, which will become the final component of the FeatureOnlineStore's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.
     */
    public readonly featureOnlineStoreId!: pulumi.Output<string>;
    /**
     * Optional. The labels with user-defined metadata to organize your FeatureOnlineStore. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one FeatureOnlineStore(System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.
     */
    public readonly labels!: pulumi.Output<{[key: string]: string}>;
    public readonly location!: pulumi.Output<string>;
    /**
     * Name of the FeatureOnlineStore. Format: `projects/{project}/locations/{location}/featureOnlineStores/{featureOnlineStore}`
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * Contains settings for the Optimized store that will be created to serve featureValues for all FeatureViews under this FeatureOnlineStore. When choose Optimized storage type, need to set PrivateServiceConnectConfig.enable_private_service_connect to use private endpoint. Otherwise will use public endpoint by default.
     */
    public readonly optimized!: pulumi.Output<outputs.aiplatform.v1beta1.GoogleCloudAiplatformV1beta1FeatureOnlineStoreOptimizedResponse>;
    public readonly project!: pulumi.Output<string>;
    /**
     * State of the featureOnlineStore.
     */
    public /*out*/ readonly state!: pulumi.Output<string>;
    /**
     * Timestamp when this FeatureOnlineStore was last updated.
     */
    public /*out*/ readonly updateTime!: pulumi.Output<string>;

    /**
     * Create a FeatureOnlineStore resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FeatureOnlineStoreArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.featureOnlineStoreId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'featureOnlineStoreId'");
            }
            resourceInputs["bigtable"] = args ? args.bigtable : undefined;
            resourceInputs["dedicatedServingEndpoint"] = args ? args.dedicatedServingEndpoint : undefined;
            resourceInputs["embeddingManagement"] = args ? args.embeddingManagement : undefined;
            resourceInputs["etag"] = args ? args.etag : undefined;
            resourceInputs["featureOnlineStoreId"] = args ? args.featureOnlineStoreId : undefined;
            resourceInputs["labels"] = args ? args.labels : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["optimized"] = args ? args.optimized : undefined;
            resourceInputs["project"] = args ? args.project : undefined;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        } else {
            resourceInputs["bigtable"] = undefined /*out*/;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["dedicatedServingEndpoint"] = undefined /*out*/;
            resourceInputs["embeddingManagement"] = undefined /*out*/;
            resourceInputs["etag"] = undefined /*out*/;
            resourceInputs["featureOnlineStoreId"] = undefined /*out*/;
            resourceInputs["labels"] = undefined /*out*/;
            resourceInputs["location"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["optimized"] = undefined /*out*/;
            resourceInputs["project"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["featureOnlineStoreId", "location", "project"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(FeatureOnlineStore.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a FeatureOnlineStore resource.
 */
export interface FeatureOnlineStoreArgs {
    /**
     * Contains settings for the Cloud Bigtable instance that will be created to serve featureValues for all FeatureViews under this FeatureOnlineStore.
     */
    bigtable?: pulumi.Input<inputs.aiplatform.v1beta1.GoogleCloudAiplatformV1beta1FeatureOnlineStoreBigtableArgs>;
    /**
     * Optional. The dedicated serving endpoint for this FeatureOnlineStore, which is different from common Vertex service endpoint.
     */
    dedicatedServingEndpoint?: pulumi.Input<inputs.aiplatform.v1beta1.GoogleCloudAiplatformV1beta1FeatureOnlineStoreDedicatedServingEndpointArgs>;
    /**
     * Optional. The settings for embedding management in FeatureOnlineStore.
     */
    embeddingManagement?: pulumi.Input<inputs.aiplatform.v1beta1.GoogleCloudAiplatformV1beta1FeatureOnlineStoreEmbeddingManagementArgs>;
    /**
     * Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
     */
    etag?: pulumi.Input<string>;
    /**
     * Required. The ID to use for this FeatureOnlineStore, which will become the final component of the FeatureOnlineStore's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.
     */
    featureOnlineStoreId: pulumi.Input<string>;
    /**
     * Optional. The labels with user-defined metadata to organize your FeatureOnlineStore. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one FeatureOnlineStore(System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.
     */
    labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    location?: pulumi.Input<string>;
    /**
     * Contains settings for the Optimized store that will be created to serve featureValues for all FeatureViews under this FeatureOnlineStore. When choose Optimized storage type, need to set PrivateServiceConnectConfig.enable_private_service_connect to use private endpoint. Otherwise will use public endpoint by default.
     */
    optimized?: pulumi.Input<inputs.aiplatform.v1beta1.GoogleCloudAiplatformV1beta1FeatureOnlineStoreOptimizedArgs>;
    project?: pulumi.Input<string>;
}
