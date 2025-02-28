// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Creates a new model.
 */
export class Model extends pulumi.CustomResource {
    /**
     * Get an existing Model resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Model {
        return new Model(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:retail/v2:Model';

    /**
     * Returns true if the given object is an instance of Model.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Model {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Model.__pulumiType;
    }

    public readonly catalogId!: pulumi.Output<string>;
    /**
     * Timestamp the Recommendation Model was created at.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * The state of data requirements for this model: `DATA_OK` and `DATA_ERROR`. Recommendation model cannot be trained if the data is in `DATA_ERROR` state. Recommendation model can have `DATA_ERROR` state even if serving state is `ACTIVE`: models were trained successfully before, but cannot be refreshed because model no longer has sufficient data for training.
     */
    public /*out*/ readonly dataState!: pulumi.Output<string>;
    /**
     * The display name of the model. Should be human readable, used to display Recommendation Models in the Retail Cloud Console Dashboard. UTF-8 encoded string with limit of 1024 characters.
     */
    public readonly displayName!: pulumi.Output<string>;
    /**
     * Optional. Whether to run a dry run to validate the request (without actually creating the model).
     */
    public readonly dryRun!: pulumi.Output<boolean | undefined>;
    /**
     * Optional. If `RECOMMENDATIONS_FILTERING_ENABLED`, recommendation filtering by attributes is enabled for the model.
     */
    public readonly filteringOption!: pulumi.Output<string>;
    /**
     * The timestamp when the latest successful tune finished.
     */
    public /*out*/ readonly lastTuneTime!: pulumi.Output<string>;
    public readonly location!: pulumi.Output<string>;
    /**
     * Optional. Additional model features config.
     */
    public readonly modelFeaturesConfig!: pulumi.Output<outputs.retail.v2.GoogleCloudRetailV2ModelModelFeaturesConfigResponse>;
    /**
     * The fully qualified resource name of the model. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}` catalog_id has char limit of 50. recommendation_model_id has char limit of 40.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Optional. The optimization objective e.g. `cvr`. Currently supported values: `ctr`, `cvr`, `revenue-per-order`. If not specified, we choose default based on model type. Default depends on type of recommendation: `recommended-for-you` => `ctr` `others-you-may-like` => `ctr` `frequently-bought-together` => `revenue_per_order` This field together with optimization_objective describe model metadata to use to control model training and serving. See https://cloud.google.com/retail/docs/models for more details on what the model metadata control and which combination of parameters are valid. For invalid combinations of parameters (e.g. type = `frequently-bought-together` and optimization_objective = `ctr`), you receive an error 400 if you try to create/update a recommendation with this set of knobs.
     */
    public readonly optimizationObjective!: pulumi.Output<string>;
    /**
     * Optional. The state of periodic tuning. The period we use is 3 months - to do a one-off tune earlier use the `TuneModel` method. Default value is `PERIODIC_TUNING_ENABLED`.
     */
    public readonly periodicTuningState!: pulumi.Output<string>;
    public readonly project!: pulumi.Output<string>;
    /**
     * The list of valid serving configs associated with the PageOptimizationConfig.
     */
    public /*out*/ readonly servingConfigLists!: pulumi.Output<outputs.retail.v2.GoogleCloudRetailV2ModelServingConfigListResponse[]>;
    /**
     * The serving state of the model: `ACTIVE`, `NOT_ACTIVE`.
     */
    public /*out*/ readonly servingState!: pulumi.Output<string>;
    /**
     * Optional. The training state that the model is in (e.g. `TRAINING` or `PAUSED`). Since part of the cost of running the service is frequency of training - this can be used to determine when to train model in order to control cost. If not specified: the default value for `CreateModel` method is `TRAINING`. The default value for `UpdateModel` method is to keep the state the same as before.
     */
    public readonly trainingState!: pulumi.Output<string>;
    /**
     * The tune operation associated with the model. Can be used to determine if there is an ongoing tune for this recommendation. Empty field implies no tune is goig on.
     */
    public /*out*/ readonly tuningOperation!: pulumi.Output<string>;
    /**
     * The type of model e.g. `home-page`. Currently supported values: `recommended-for-you`, `others-you-may-like`, `frequently-bought-together`, `page-optimization`, `similar-items`, `buy-it-again`, `on-sale-items`, and `recently-viewed`(readonly value). This field together with optimization_objective describe model metadata to use to control model training and serving. See https://cloud.google.com/retail/docs/models for more details on what the model metadata control and which combination of parameters are valid. For invalid combinations of parameters (e.g. type = `frequently-bought-together` and optimization_objective = `ctr`), you receive an error 400 if you try to create/update a recommendation with this set of knobs.
     */
    public readonly type!: pulumi.Output<string>;
    /**
     * Timestamp the Recommendation Model was last updated. E.g. if a Recommendation Model was paused - this would be the time the pause was initiated.
     */
    public /*out*/ readonly updateTime!: pulumi.Output<string>;

    /**
     * Create a Model resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ModelArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.catalogId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'catalogId'");
            }
            if ((!args || args.displayName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'displayName'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            resourceInputs["catalogId"] = args ? args.catalogId : undefined;
            resourceInputs["displayName"] = args ? args.displayName : undefined;
            resourceInputs["dryRun"] = args ? args.dryRun : undefined;
            resourceInputs["filteringOption"] = args ? args.filteringOption : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["modelFeaturesConfig"] = args ? args.modelFeaturesConfig : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["optimizationObjective"] = args ? args.optimizationObjective : undefined;
            resourceInputs["periodicTuningState"] = args ? args.periodicTuningState : undefined;
            resourceInputs["project"] = args ? args.project : undefined;
            resourceInputs["trainingState"] = args ? args.trainingState : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["dataState"] = undefined /*out*/;
            resourceInputs["lastTuneTime"] = undefined /*out*/;
            resourceInputs["servingConfigLists"] = undefined /*out*/;
            resourceInputs["servingState"] = undefined /*out*/;
            resourceInputs["tuningOperation"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        } else {
            resourceInputs["catalogId"] = undefined /*out*/;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["dataState"] = undefined /*out*/;
            resourceInputs["displayName"] = undefined /*out*/;
            resourceInputs["dryRun"] = undefined /*out*/;
            resourceInputs["filteringOption"] = undefined /*out*/;
            resourceInputs["lastTuneTime"] = undefined /*out*/;
            resourceInputs["location"] = undefined /*out*/;
            resourceInputs["modelFeaturesConfig"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["optimizationObjective"] = undefined /*out*/;
            resourceInputs["periodicTuningState"] = undefined /*out*/;
            resourceInputs["project"] = undefined /*out*/;
            resourceInputs["servingConfigLists"] = undefined /*out*/;
            resourceInputs["servingState"] = undefined /*out*/;
            resourceInputs["trainingState"] = undefined /*out*/;
            resourceInputs["tuningOperation"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["catalogId", "location", "project"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Model.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Model resource.
 */
export interface ModelArgs {
    catalogId: pulumi.Input<string>;
    /**
     * The display name of the model. Should be human readable, used to display Recommendation Models in the Retail Cloud Console Dashboard. UTF-8 encoded string with limit of 1024 characters.
     */
    displayName: pulumi.Input<string>;
    /**
     * Optional. Whether to run a dry run to validate the request (without actually creating the model).
     */
    dryRun?: pulumi.Input<boolean>;
    /**
     * Optional. If `RECOMMENDATIONS_FILTERING_ENABLED`, recommendation filtering by attributes is enabled for the model.
     */
    filteringOption?: pulumi.Input<enums.retail.v2.ModelFilteringOption>;
    location?: pulumi.Input<string>;
    /**
     * Optional. Additional model features config.
     */
    modelFeaturesConfig?: pulumi.Input<inputs.retail.v2.GoogleCloudRetailV2ModelModelFeaturesConfigArgs>;
    /**
     * The fully qualified resource name of the model. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}` catalog_id has char limit of 50. recommendation_model_id has char limit of 40.
     */
    name?: pulumi.Input<string>;
    /**
     * Optional. The optimization objective e.g. `cvr`. Currently supported values: `ctr`, `cvr`, `revenue-per-order`. If not specified, we choose default based on model type. Default depends on type of recommendation: `recommended-for-you` => `ctr` `others-you-may-like` => `ctr` `frequently-bought-together` => `revenue_per_order` This field together with optimization_objective describe model metadata to use to control model training and serving. See https://cloud.google.com/retail/docs/models for more details on what the model metadata control and which combination of parameters are valid. For invalid combinations of parameters (e.g. type = `frequently-bought-together` and optimization_objective = `ctr`), you receive an error 400 if you try to create/update a recommendation with this set of knobs.
     */
    optimizationObjective?: pulumi.Input<string>;
    /**
     * Optional. The state of periodic tuning. The period we use is 3 months - to do a one-off tune earlier use the `TuneModel` method. Default value is `PERIODIC_TUNING_ENABLED`.
     */
    periodicTuningState?: pulumi.Input<enums.retail.v2.ModelPeriodicTuningState>;
    project?: pulumi.Input<string>;
    /**
     * Optional. The training state that the model is in (e.g. `TRAINING` or `PAUSED`). Since part of the cost of running the service is frequency of training - this can be used to determine when to train model in order to control cost. If not specified: the default value for `CreateModel` method is `TRAINING`. The default value for `UpdateModel` method is to keep the state the same as before.
     */
    trainingState?: pulumi.Input<enums.retail.v2.ModelTrainingState>;
    /**
     * The type of model e.g. `home-page`. Currently supported values: `recommended-for-you`, `others-you-may-like`, `frequently-bought-together`, `page-optimization`, `similar-items`, `buy-it-again`, `on-sale-items`, and `recently-viewed`(readonly value). This field together with optimization_objective describe model metadata to use to control model training and serving. See https://cloud.google.com/retail/docs/models for more details on what the model metadata control and which combination of parameters are valid. For invalid combinations of parameters (e.g. type = `frequently-bought-together` and optimization_objective = `ctr`), you receive an error 400 if you try to create/update a recommendation with this set of knobs.
     */
    type: pulumi.Input<string>;
}
