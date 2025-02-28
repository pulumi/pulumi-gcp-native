// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Gets metadata for a given Secret.
 */
export function getSecret(args: GetSecretArgs, opts?: pulumi.InvokeOptions): Promise<GetSecretResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:secretmanager/v1beta1:getSecret", {
        "project": args.project,
        "secretId": args.secretId,
    }, opts);
}

export interface GetSecretArgs {
    project?: string;
    secretId: string;
}

export interface GetSecretResult {
    /**
     * The time at which the Secret was created.
     */
    readonly createTime: string;
    /**
     * The labels assigned to this Secret. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `\p{Ll}\p{Lo}{0,62}` Label values must be between 0 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}` No more than 64 labels can be assigned to a given resource.
     */
    readonly labels: {[key: string]: string};
    /**
     * The resource name of the Secret in the format `projects/*&#47;secrets/*`.
     */
    readonly name: string;
    /**
     * Immutable. The replication policy of the secret data attached to the Secret. The replication policy cannot be changed after the Secret has been created.
     */
    readonly replication: outputs.secretmanager.v1beta1.ReplicationResponse;
}
/**
 * Gets metadata for a given Secret.
 */
export function getSecretOutput(args: GetSecretOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSecretResult> {
    return pulumi.output(args).apply((a: any) => getSecret(a, opts))
}

export interface GetSecretOutputArgs {
    project?: pulumi.Input<string>;
    secretId: pulumi.Input<string>;
}
