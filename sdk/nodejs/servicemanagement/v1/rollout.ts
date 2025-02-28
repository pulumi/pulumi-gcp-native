// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Creates a new service configuration rollout. Based on rollout, the Google Service Management will roll out the service configurations to different backend services. For example, the logging configuration will be pushed to Google Cloud Logging. Please note that any previous pending and running Rollouts and associated Operations will be automatically cancelled so that the latest Rollout will not be blocked by previous Rollouts. Only the 100 most recent (in any state) and the last 10 successful (if not already part of the set of 100 most recent) rollouts are kept for each service. The rest will be deleted eventually. Operation
 * Auto-naming is currently not supported for this resource.
 * Note - this resource's API doesn't support deletion. When deleted, the resource will persist
 * on Google Cloud even though it will be deleted from Pulumi state.
 */
export class Rollout extends pulumi.CustomResource {
    /**
     * Get an existing Rollout resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Rollout {
        return new Rollout(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:servicemanagement/v1:Rollout';

    /**
     * Returns true if the given object is an instance of Rollout.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Rollout {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Rollout.__pulumiType;
    }

    /**
     * Creation time of the rollout. Readonly.
     */
    public readonly createTime!: pulumi.Output<string>;
    /**
     * The user who created the Rollout. Readonly.
     */
    public readonly createdBy!: pulumi.Output<string>;
    /**
     * The strategy associated with a rollout to delete a `ManagedService`. Readonly.
     */
    public readonly deleteServiceStrategy!: pulumi.Output<outputs.servicemanagement.v1.DeleteServiceStrategyResponse>;
    /**
     * Optional. Unique identifier of this Rollout. Must be no longer than 63 characters and only lower case letters, digits, '.', '_' and '-' are allowed. If not specified by client, the server will generate one. The generated id will have the form of , where "date" is the create date in ISO 8601 format. "revision number" is a monotonically increasing positive number that is reset every day for each service. An example of the generated rollout_id is '2016-02-16r1'
     */
    public readonly rolloutId!: pulumi.Output<string>;
    public readonly serviceName!: pulumi.Output<string>;
    /**
     * The status of this rollout. Readonly. In case of a failed rollout, the system will automatically rollback to the current Rollout version. Readonly.
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * Google Service Control selects service configurations based on traffic percentage.
     */
    public readonly trafficPercentStrategy!: pulumi.Output<outputs.servicemanagement.v1.TrafficPercentStrategyResponse>;

    /**
     * Create a Rollout resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RolloutArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.serviceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceName'");
            }
            resourceInputs["createTime"] = args ? args.createTime : undefined;
            resourceInputs["createdBy"] = args ? args.createdBy : undefined;
            resourceInputs["deleteServiceStrategy"] = args ? args.deleteServiceStrategy : undefined;
            resourceInputs["rolloutId"] = args ? args.rolloutId : undefined;
            resourceInputs["serviceName"] = args ? args.serviceName : undefined;
            resourceInputs["trafficPercentStrategy"] = args ? args.trafficPercentStrategy : undefined;
            resourceInputs["status"] = undefined /*out*/;
        } else {
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["createdBy"] = undefined /*out*/;
            resourceInputs["deleteServiceStrategy"] = undefined /*out*/;
            resourceInputs["rolloutId"] = undefined /*out*/;
            resourceInputs["serviceName"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["trafficPercentStrategy"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["serviceName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Rollout.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Rollout resource.
 */
export interface RolloutArgs {
    /**
     * Creation time of the rollout. Readonly.
     */
    createTime?: pulumi.Input<string>;
    /**
     * The user who created the Rollout. Readonly.
     */
    createdBy?: pulumi.Input<string>;
    /**
     * The strategy associated with a rollout to delete a `ManagedService`. Readonly.
     */
    deleteServiceStrategy?: pulumi.Input<inputs.servicemanagement.v1.DeleteServiceStrategyArgs>;
    /**
     * Optional. Unique identifier of this Rollout. Must be no longer than 63 characters and only lower case letters, digits, '.', '_' and '-' are allowed. If not specified by client, the server will generate one. The generated id will have the form of , where "date" is the create date in ISO 8601 format. "revision number" is a monotonically increasing positive number that is reset every day for each service. An example of the generated rollout_id is '2016-02-16r1'
     */
    rolloutId?: pulumi.Input<string>;
    /**
     * The name of the service associated with this Rollout.
     */
    serviceName: pulumi.Input<string>;
    /**
     * Google Service Control selects service configurations based on traffic percentage.
     */
    trafficPercentStrategy?: pulumi.Input<inputs.servicemanagement.v1.TrafficPercentStrategyArgs>;
}
