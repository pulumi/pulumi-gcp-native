// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Gets information about an instance.
 */
export function getInstance(args: GetInstanceArgs, opts?: pulumi.InvokeOptions): Promise<GetInstanceResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:bigtableadmin/v2:getInstance", {
        "instanceId": args.instanceId,
        "project": args.project,
    }, opts);
}

export interface GetInstanceArgs {
    instanceId: string;
    project?: string;
}

export interface GetInstanceResult {
    /**
     * A commit timestamp representing when this Instance was created. For instances created before this field was added (August 2021), this value is `seconds: 0, nanos: 1`.
     */
    readonly createTime: string;
    /**
     * The descriptive name for this instance as it appears in UIs. Can be changed at any time, but should be kept globally unique to avoid confusion.
     */
    readonly displayName: string;
    /**
     * Labels are a flexible and lightweight mechanism for organizing cloud resources into groups that reflect a customer's organizational needs and deployment strategies. They can be used to filter resources and aggregate metrics. * Label keys must be between 1 and 63 characters long and must conform to the regular expression: `\p{Ll}\p{Lo}{0,62}`. * Label values must be between 0 and 63 characters long and must conform to the regular expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}`. * No more than 64 labels can be associated with a given resource. * Keys and values must both be under 128 bytes.
     */
    readonly labels: {[key: string]: string};
    /**
     * The unique name of the instance. Values are of the form `projects/{project}/instances/a-z+[a-z0-9]`.
     */
    readonly name: string;
    /**
     * Reserved for future use.
     */
    readonly satisfiesPzs: boolean;
    /**
     * The current state of the instance.
     */
    readonly state: string;
    /**
     * The type of the instance. Defaults to `PRODUCTION`.
     */
    readonly type: string;
}
/**
 * Gets information about an instance.
 */
export function getInstanceOutput(args: GetInstanceOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetInstanceResult> {
    return pulumi.output(args).apply((a: any) => getInstance(a, opts))
}

export interface GetInstanceOutputArgs {
    instanceId: pulumi.Input<string>;
    project?: pulumi.Input<string>;
}
