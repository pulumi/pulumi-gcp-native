// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Creates a catalog item.
 * Auto-naming is currently not supported for this resource.
 */
export class CatalogItem extends pulumi.CustomResource {
    /**
     * Get an existing CatalogItem resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): CatalogItem {
        return new CatalogItem(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:recommendationengine/v1beta1:CatalogItem';

    /**
     * Returns true if the given object is an instance of CatalogItem.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CatalogItem {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CatalogItem.__pulumiType;
    }

    public readonly catalogId!: pulumi.Output<string>;
    /**
     * Catalog item categories. This field is repeated for supporting one catalog item belonging to several parallel category hierarchies. For example, if a shoes product belongs to both ["Shoes & Accessories" -> "Shoes"] and ["Sports & Fitness" -> "Athletic Clothing" -> "Shoes"], it could be represented as: "categoryHierarchies": [ { "categories": ["Shoes & Accessories", "Shoes"]}, { "categories": ["Sports & Fitness", "Athletic Clothing", "Shoes"] } ]
     */
    public readonly categoryHierarchies!: pulumi.Output<outputs.recommendationengine.v1beta1.GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchyResponse[]>;
    /**
     * Optional. Catalog item description. UTF-8 encoded string with a length limit of 5 KiB.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * Optional. Highly encouraged. Extra catalog item attributes to be included in the recommendation model. For example, for retail products, this could include the store name, vendor, style, color, etc. These are very strong signals for recommendation model, thus we highly recommend providing the item attributes here.
     */
    public readonly itemAttributes!: pulumi.Output<outputs.recommendationengine.v1beta1.GoogleCloudRecommendationengineV1beta1FeatureMapResponse>;
    /**
     * Optional. Variant group identifier for prediction results. UTF-8 encoded string with a length limit of 128 bytes. This field must be enabled before it can be used. [Learn more](/recommendations-ai/docs/catalog#item-group-id).
     */
    public readonly itemGroupId!: pulumi.Output<string>;
    /**
     * Optional. Deprecated. The model automatically detects the text language. Your catalog can include text in different languages, but duplicating catalog items to provide text in multiple languages can result in degraded model performance.
     *
     * @deprecated Optional. Deprecated. The model automatically detects the text language. Your catalog can include text in different languages, but duplicating catalog items to provide text in multiple languages can result in degraded model performance.
     */
    public readonly languageCode!: pulumi.Output<string>;
    public readonly location!: pulumi.Output<string>;
    /**
     * Optional. Metadata specific to retail products.
     */
    public readonly productMetadata!: pulumi.Output<outputs.recommendationengine.v1beta1.GoogleCloudRecommendationengineV1beta1ProductCatalogItemResponse>;
    public readonly project!: pulumi.Output<string>;
    /**
     * Optional. Filtering tags associated with the catalog item. Each tag should be a UTF-8 encoded string with a length limit of 1 KiB. This tag can be used for filtering recommendation results by passing the tag as part of the predict request filter.
     */
    public readonly tags!: pulumi.Output<string[]>;
    /**
     * Catalog item title. UTF-8 encoded string with a length limit of 1 KiB.
     */
    public readonly title!: pulumi.Output<string>;

    /**
     * Create a CatalogItem resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CatalogItemArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.catalogId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'catalogId'");
            }
            if ((!args || args.categoryHierarchies === undefined) && !opts.urn) {
                throw new Error("Missing required property 'categoryHierarchies'");
            }
            if ((!args || args.id === undefined) && !opts.urn) {
                throw new Error("Missing required property 'id'");
            }
            if ((!args || args.title === undefined) && !opts.urn) {
                throw new Error("Missing required property 'title'");
            }
            resourceInputs["catalogId"] = args ? args.catalogId : undefined;
            resourceInputs["categoryHierarchies"] = args ? args.categoryHierarchies : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["id"] = args ? args.id : undefined;
            resourceInputs["itemAttributes"] = args ? args.itemAttributes : undefined;
            resourceInputs["itemGroupId"] = args ? args.itemGroupId : undefined;
            resourceInputs["languageCode"] = args ? args.languageCode : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["productMetadata"] = args ? args.productMetadata : undefined;
            resourceInputs["project"] = args ? args.project : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["title"] = args ? args.title : undefined;
        } else {
            resourceInputs["catalogId"] = undefined /*out*/;
            resourceInputs["categoryHierarchies"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["itemAttributes"] = undefined /*out*/;
            resourceInputs["itemGroupId"] = undefined /*out*/;
            resourceInputs["languageCode"] = undefined /*out*/;
            resourceInputs["location"] = undefined /*out*/;
            resourceInputs["productMetadata"] = undefined /*out*/;
            resourceInputs["project"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["title"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["catalogId", "location", "project"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(CatalogItem.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a CatalogItem resource.
 */
export interface CatalogItemArgs {
    catalogId: pulumi.Input<string>;
    /**
     * Catalog item categories. This field is repeated for supporting one catalog item belonging to several parallel category hierarchies. For example, if a shoes product belongs to both ["Shoes & Accessories" -> "Shoes"] and ["Sports & Fitness" -> "Athletic Clothing" -> "Shoes"], it could be represented as: "categoryHierarchies": [ { "categories": ["Shoes & Accessories", "Shoes"]}, { "categories": ["Sports & Fitness", "Athletic Clothing", "Shoes"] } ]
     */
    categoryHierarchies: pulumi.Input<pulumi.Input<inputs.recommendationengine.v1beta1.GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchyArgs>[]>;
    /**
     * Optional. Catalog item description. UTF-8 encoded string with a length limit of 5 KiB.
     */
    description?: pulumi.Input<string>;
    /**
     * Catalog item identifier. UTF-8 encoded string with a length limit of 128 bytes. This id must be unique among all catalog items within the same catalog. It should also be used when logging user events in order for the user events to be joined with the Catalog.
     */
    id: pulumi.Input<string>;
    /**
     * Optional. Highly encouraged. Extra catalog item attributes to be included in the recommendation model. For example, for retail products, this could include the store name, vendor, style, color, etc. These are very strong signals for recommendation model, thus we highly recommend providing the item attributes here.
     */
    itemAttributes?: pulumi.Input<inputs.recommendationengine.v1beta1.GoogleCloudRecommendationengineV1beta1FeatureMapArgs>;
    /**
     * Optional. Variant group identifier for prediction results. UTF-8 encoded string with a length limit of 128 bytes. This field must be enabled before it can be used. [Learn more](/recommendations-ai/docs/catalog#item-group-id).
     */
    itemGroupId?: pulumi.Input<string>;
    /**
     * Optional. Deprecated. The model automatically detects the text language. Your catalog can include text in different languages, but duplicating catalog items to provide text in multiple languages can result in degraded model performance.
     *
     * @deprecated Optional. Deprecated. The model automatically detects the text language. Your catalog can include text in different languages, but duplicating catalog items to provide text in multiple languages can result in degraded model performance.
     */
    languageCode?: pulumi.Input<string>;
    location?: pulumi.Input<string>;
    /**
     * Optional. Metadata specific to retail products.
     */
    productMetadata?: pulumi.Input<inputs.recommendationengine.v1beta1.GoogleCloudRecommendationengineV1beta1ProductCatalogItemArgs>;
    project?: pulumi.Input<string>;
    /**
     * Optional. Filtering tags associated with the catalog item. Each tag should be a UTF-8 encoded string with a length limit of 1 KiB. This tag can be used for filtering recommendation results by passing the tag as part of the predict request filter.
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Catalog item title. UTF-8 encoded string with a length limit of 1 KiB.
     */
    title: pulumi.Input<string>;
}
