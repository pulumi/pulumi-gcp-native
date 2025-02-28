// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Creates a ServingConfig. A maximum of 100 ServingConfigs are allowed in a Catalog, otherwise a FAILED_PRECONDITION error is returned.
 * Auto-naming is currently not supported for this resource.
 */
export class ServingConfig extends pulumi.CustomResource {
    /**
     * Get an existing ServingConfig resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ServingConfig {
        return new ServingConfig(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:retail/v2:ServingConfig';

    /**
     * Returns true if the given object is an instance of ServingConfig.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ServingConfig {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ServingConfig.__pulumiType;
    }

    /**
     * Condition boost specifications. If a product matches multiple conditions in the specifications, boost scores from these specifications are all applied and combined in a non-linear way. Maximum number of specifications is 100. Notice that if both ServingConfig.boost_control_ids and SearchRequest.boost_spec are set, the boost conditions from both places are evaluated. If a search request matches multiple boost conditions, the final boost score is equal to the sum of the boost scores from all matched boost conditions. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    public readonly boostControlIds!: pulumi.Output<string[]>;
    public readonly catalogId!: pulumi.Output<string>;
    /**
     * The human readable serving config display name. Used in Retail UI. This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.
     */
    public readonly displayName!: pulumi.Output<string>;
    /**
     * How much diversity to use in recommendation model results e.g. `medium-diversity` or `high-diversity`. Currently supported values: * `no-diversity` * `low-diversity` * `medium-diversity` * `high-diversity` * `auto-diversity` If not specified, we choose default based on recommendation model type. Default value: `no-diversity`. Can only be set if solution_types is SOLUTION_TYPE_RECOMMENDATION.
     */
    public readonly diversityLevel!: pulumi.Output<string>;
    /**
     * What kind of diversity to use - data driven or rule based. If unset, the server behavior defaults to RULE_BASED_DIVERSITY.
     */
    public readonly diversityType!: pulumi.Output<string>;
    /**
     * Condition do not associate specifications. If multiple do not associate conditions match, all matching do not associate controls in the list will execute. - Order does not matter. - Maximum number of specifications is 100. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    public readonly doNotAssociateControlIds!: pulumi.Output<string[]>;
    /**
     * The specification for dynamically generated facets. Notice that only textual facets can be dynamically generated. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    public readonly dynamicFacetSpec!: pulumi.Output<outputs.retail.v2.GoogleCloudRetailV2SearchRequestDynamicFacetSpecResponse>;
    /**
     * Whether to add additional category filters on the `similar-items` model. If not specified, we enable it by default. Allowed values are: * `no-category-match`: No additional filtering of original results from the model and the customer's filters. * `relaxed-category-match`: Only keep results with categories that match at least one item categories in the PredictRequests's context item. * If customer also sends filters in the PredictRequest, then the results will satisfy both conditions (user given and category match). Can only be set if solution_types is SOLUTION_TYPE_RECOMMENDATION.
     */
    public readonly enableCategoryFilterLevel!: pulumi.Output<string>;
    /**
     * Facet specifications for faceted search. If empty, no facets are returned. The ids refer to the ids of Control resources with only the Facet control set. These controls are assumed to be in the same Catalog as the ServingConfig. A maximum of 100 values are allowed. Otherwise, an INVALID_ARGUMENT error is returned. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    public readonly facetControlIds!: pulumi.Output<string[]>;
    /**
     * Condition filter specifications. If a product matches multiple conditions in the specifications, filters from these specifications are all applied and combined via the AND operator. Maximum number of specifications is 100. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    public readonly filterControlIds!: pulumi.Output<string[]>;
    /**
     * Condition ignore specifications. If multiple ignore conditions match, all matching ignore controls in the list will execute. - Order does not matter. - Maximum number of specifications is 100. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    public readonly ignoreControlIds!: pulumi.Output<string[]>;
    public readonly location!: pulumi.Output<string>;
    /**
     * The id of the model in the same Catalog to use at serving time. Currently only RecommendationModels are supported: https://cloud.google.com/retail/recommendations-ai/docs/create-models Can be changed but only to a compatible model (e.g. others-you-may-like CTR to others-you-may-like CVR). Required when solution_types is SOLUTION_TYPE_RECOMMENDATION.
     */
    public readonly modelId!: pulumi.Output<string>;
    /**
     * Immutable. Fully qualified name `projects/*&#47;locations/global/catalogs/*&#47;servingConfig/*`
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Condition oneway synonyms specifications. If multiple oneway synonyms conditions match, all matching oneway synonyms controls in the list will execute. Order of controls in the list will not matter. Maximum number of specifications is 100. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    public readonly onewaySynonymsControlIds!: pulumi.Output<string[]>;
    /**
     * The specification for personalization spec. Can only be set if solution_types is SOLUTION_TYPE_SEARCH. Notice that if both ServingConfig.personalization_spec and SearchRequest.personalization_spec are set. SearchRequest.personalization_spec will override ServingConfig.personalization_spec.
     */
    public readonly personalizationSpec!: pulumi.Output<outputs.retail.v2.GoogleCloudRetailV2SearchRequestPersonalizationSpecResponse>;
    /**
     * How much price ranking we want in serving results. Price reranking causes product items with a similar recommendation probability to be ordered by price, with the highest-priced items first. This setting could result in a decrease in click-through and conversion rates. Allowed values are: * `no-price-reranking` * `low-price-reranking` * `medium-price-reranking` * `high-price-reranking` If not specified, we choose default based on model type. Default value: `no-price-reranking`. Can only be set if solution_types is SOLUTION_TYPE_RECOMMENDATION.
     */
    public readonly priceRerankingLevel!: pulumi.Output<string>;
    public readonly project!: pulumi.Output<string>;
    /**
     * Condition redirect specifications. Only the first triggered redirect action is applied, even if multiple apply. Maximum number of specifications is 1000. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    public readonly redirectControlIds!: pulumi.Output<string[]>;
    /**
     * Condition replacement specifications. - Applied according to the order in the list. - A previously replaced term can not be re-replaced. - Maximum number of specifications is 100. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    public readonly replacementControlIds!: pulumi.Output<string[]>;
    /**
     * Required. The ID to use for the ServingConfig, which will become the final component of the ServingConfig's resource name. This value should be 4-63 characters, and valid characters are /a-z-_/.
     */
    public readonly servingConfigId!: pulumi.Output<string>;
    /**
     * Immutable. Specifies the solution types that a serving config can be associated with. Currently we support setting only one type of solution.
     */
    public readonly solutionTypes!: pulumi.Output<string[]>;
    /**
     * Condition synonyms specifications. If multiple syonyms conditions match, all matching synonyms control in the list will execute. Order of controls in the list will not matter. Maximum number of specifications is 100. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    public readonly twowaySynonymsControlIds!: pulumi.Output<string[]>;

    /**
     * Create a ServingConfig resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ServingConfigArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.catalogId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'catalogId'");
            }
            if ((!args || args.displayName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'displayName'");
            }
            if ((!args || args.servingConfigId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'servingConfigId'");
            }
            if ((!args || args.solutionTypes === undefined) && !opts.urn) {
                throw new Error("Missing required property 'solutionTypes'");
            }
            resourceInputs["boostControlIds"] = args ? args.boostControlIds : undefined;
            resourceInputs["catalogId"] = args ? args.catalogId : undefined;
            resourceInputs["displayName"] = args ? args.displayName : undefined;
            resourceInputs["diversityLevel"] = args ? args.diversityLevel : undefined;
            resourceInputs["diversityType"] = args ? args.diversityType : undefined;
            resourceInputs["doNotAssociateControlIds"] = args ? args.doNotAssociateControlIds : undefined;
            resourceInputs["dynamicFacetSpec"] = args ? args.dynamicFacetSpec : undefined;
            resourceInputs["enableCategoryFilterLevel"] = args ? args.enableCategoryFilterLevel : undefined;
            resourceInputs["facetControlIds"] = args ? args.facetControlIds : undefined;
            resourceInputs["filterControlIds"] = args ? args.filterControlIds : undefined;
            resourceInputs["ignoreControlIds"] = args ? args.ignoreControlIds : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["modelId"] = args ? args.modelId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["onewaySynonymsControlIds"] = args ? args.onewaySynonymsControlIds : undefined;
            resourceInputs["personalizationSpec"] = args ? args.personalizationSpec : undefined;
            resourceInputs["priceRerankingLevel"] = args ? args.priceRerankingLevel : undefined;
            resourceInputs["project"] = args ? args.project : undefined;
            resourceInputs["redirectControlIds"] = args ? args.redirectControlIds : undefined;
            resourceInputs["replacementControlIds"] = args ? args.replacementControlIds : undefined;
            resourceInputs["servingConfigId"] = args ? args.servingConfigId : undefined;
            resourceInputs["solutionTypes"] = args ? args.solutionTypes : undefined;
            resourceInputs["twowaySynonymsControlIds"] = args ? args.twowaySynonymsControlIds : undefined;
        } else {
            resourceInputs["boostControlIds"] = undefined /*out*/;
            resourceInputs["catalogId"] = undefined /*out*/;
            resourceInputs["displayName"] = undefined /*out*/;
            resourceInputs["diversityLevel"] = undefined /*out*/;
            resourceInputs["diversityType"] = undefined /*out*/;
            resourceInputs["doNotAssociateControlIds"] = undefined /*out*/;
            resourceInputs["dynamicFacetSpec"] = undefined /*out*/;
            resourceInputs["enableCategoryFilterLevel"] = undefined /*out*/;
            resourceInputs["facetControlIds"] = undefined /*out*/;
            resourceInputs["filterControlIds"] = undefined /*out*/;
            resourceInputs["ignoreControlIds"] = undefined /*out*/;
            resourceInputs["location"] = undefined /*out*/;
            resourceInputs["modelId"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["onewaySynonymsControlIds"] = undefined /*out*/;
            resourceInputs["personalizationSpec"] = undefined /*out*/;
            resourceInputs["priceRerankingLevel"] = undefined /*out*/;
            resourceInputs["project"] = undefined /*out*/;
            resourceInputs["redirectControlIds"] = undefined /*out*/;
            resourceInputs["replacementControlIds"] = undefined /*out*/;
            resourceInputs["servingConfigId"] = undefined /*out*/;
            resourceInputs["solutionTypes"] = undefined /*out*/;
            resourceInputs["twowaySynonymsControlIds"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["catalogId", "location", "project", "servingConfigId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ServingConfig.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ServingConfig resource.
 */
export interface ServingConfigArgs {
    /**
     * Condition boost specifications. If a product matches multiple conditions in the specifications, boost scores from these specifications are all applied and combined in a non-linear way. Maximum number of specifications is 100. Notice that if both ServingConfig.boost_control_ids and SearchRequest.boost_spec are set, the boost conditions from both places are evaluated. If a search request matches multiple boost conditions, the final boost score is equal to the sum of the boost scores from all matched boost conditions. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    boostControlIds?: pulumi.Input<pulumi.Input<string>[]>;
    catalogId: pulumi.Input<string>;
    /**
     * The human readable serving config display name. Used in Retail UI. This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.
     */
    displayName: pulumi.Input<string>;
    /**
     * How much diversity to use in recommendation model results e.g. `medium-diversity` or `high-diversity`. Currently supported values: * `no-diversity` * `low-diversity` * `medium-diversity` * `high-diversity` * `auto-diversity` If not specified, we choose default based on recommendation model type. Default value: `no-diversity`. Can only be set if solution_types is SOLUTION_TYPE_RECOMMENDATION.
     */
    diversityLevel?: pulumi.Input<string>;
    /**
     * What kind of diversity to use - data driven or rule based. If unset, the server behavior defaults to RULE_BASED_DIVERSITY.
     */
    diversityType?: pulumi.Input<enums.retail.v2.ServingConfigDiversityType>;
    /**
     * Condition do not associate specifications. If multiple do not associate conditions match, all matching do not associate controls in the list will execute. - Order does not matter. - Maximum number of specifications is 100. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    doNotAssociateControlIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The specification for dynamically generated facets. Notice that only textual facets can be dynamically generated. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    dynamicFacetSpec?: pulumi.Input<inputs.retail.v2.GoogleCloudRetailV2SearchRequestDynamicFacetSpecArgs>;
    /**
     * Whether to add additional category filters on the `similar-items` model. If not specified, we enable it by default. Allowed values are: * `no-category-match`: No additional filtering of original results from the model and the customer's filters. * `relaxed-category-match`: Only keep results with categories that match at least one item categories in the PredictRequests's context item. * If customer also sends filters in the PredictRequest, then the results will satisfy both conditions (user given and category match). Can only be set if solution_types is SOLUTION_TYPE_RECOMMENDATION.
     */
    enableCategoryFilterLevel?: pulumi.Input<string>;
    /**
     * Facet specifications for faceted search. If empty, no facets are returned. The ids refer to the ids of Control resources with only the Facet control set. These controls are assumed to be in the same Catalog as the ServingConfig. A maximum of 100 values are allowed. Otherwise, an INVALID_ARGUMENT error is returned. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    facetControlIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Condition filter specifications. If a product matches multiple conditions in the specifications, filters from these specifications are all applied and combined via the AND operator. Maximum number of specifications is 100. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    filterControlIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Condition ignore specifications. If multiple ignore conditions match, all matching ignore controls in the list will execute. - Order does not matter. - Maximum number of specifications is 100. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    ignoreControlIds?: pulumi.Input<pulumi.Input<string>[]>;
    location?: pulumi.Input<string>;
    /**
     * The id of the model in the same Catalog to use at serving time. Currently only RecommendationModels are supported: https://cloud.google.com/retail/recommendations-ai/docs/create-models Can be changed but only to a compatible model (e.g. others-you-may-like CTR to others-you-may-like CVR). Required when solution_types is SOLUTION_TYPE_RECOMMENDATION.
     */
    modelId?: pulumi.Input<string>;
    /**
     * Immutable. Fully qualified name `projects/*&#47;locations/global/catalogs/*&#47;servingConfig/*`
     */
    name?: pulumi.Input<string>;
    /**
     * Condition oneway synonyms specifications. If multiple oneway synonyms conditions match, all matching oneway synonyms controls in the list will execute. Order of controls in the list will not matter. Maximum number of specifications is 100. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    onewaySynonymsControlIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The specification for personalization spec. Can only be set if solution_types is SOLUTION_TYPE_SEARCH. Notice that if both ServingConfig.personalization_spec and SearchRequest.personalization_spec are set. SearchRequest.personalization_spec will override ServingConfig.personalization_spec.
     */
    personalizationSpec?: pulumi.Input<inputs.retail.v2.GoogleCloudRetailV2SearchRequestPersonalizationSpecArgs>;
    /**
     * How much price ranking we want in serving results. Price reranking causes product items with a similar recommendation probability to be ordered by price, with the highest-priced items first. This setting could result in a decrease in click-through and conversion rates. Allowed values are: * `no-price-reranking` * `low-price-reranking` * `medium-price-reranking` * `high-price-reranking` If not specified, we choose default based on model type. Default value: `no-price-reranking`. Can only be set if solution_types is SOLUTION_TYPE_RECOMMENDATION.
     */
    priceRerankingLevel?: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    /**
     * Condition redirect specifications. Only the first triggered redirect action is applied, even if multiple apply. Maximum number of specifications is 1000. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    redirectControlIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Condition replacement specifications. - Applied according to the order in the list. - A previously replaced term can not be re-replaced. - Maximum number of specifications is 100. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    replacementControlIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Required. The ID to use for the ServingConfig, which will become the final component of the ServingConfig's resource name. This value should be 4-63 characters, and valid characters are /a-z-_/.
     */
    servingConfigId: pulumi.Input<string>;
    /**
     * Immutable. Specifies the solution types that a serving config can be associated with. Currently we support setting only one type of solution.
     */
    solutionTypes: pulumi.Input<pulumi.Input<enums.retail.v2.ServingConfigSolutionTypesItem>[]>;
    /**
     * Condition synonyms specifications. If multiple syonyms conditions match, all matching synonyms control in the list will execute. Order of controls in the list will not matter. Maximum number of specifications is 100. Can only be set if solution_types is SOLUTION_TYPE_SEARCH.
     */
    twowaySynonymsControlIds?: pulumi.Input<pulumi.Input<string>[]>;
}
