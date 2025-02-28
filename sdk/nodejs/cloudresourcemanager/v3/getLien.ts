// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Retrieve a Lien by `name`. Callers of this method will require permission on the `parent` resource. For example, a Lien with a `parent` of `projects/1234` requires permission `resourcemanager.projects.get`
 */
export function getLien(args: GetLienArgs, opts?: pulumi.InvokeOptions): Promise<GetLienResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:cloudresourcemanager/v3:getLien", {
        "lienId": args.lienId,
    }, opts);
}

export interface GetLienArgs {
    lienId: string;
}

export interface GetLienResult {
    /**
     * The creation time of this Lien.
     */
    readonly createTime: string;
    /**
     * A system-generated unique identifier for this Lien. Example: `liens/1234abcd`
     */
    readonly name: string;
    /**
     * A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically. Maximum length of 200 characters. Example: 'compute.googleapis.com'
     */
    readonly origin: string;
    /**
     * A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens are supported. Example: `projects/1234`
     */
    readonly parent: string;
    /**
     * Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200 characters. Example: 'Holds production API key'
     */
    readonly reason: string;
    /**
     * The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM permission. The server will validate the permissions against those for which Liens are supported. An empty list is meaningless and will be rejected. Example: ['resourcemanager.projects.delete']
     */
    readonly restrictions: string[];
}
/**
 * Retrieve a Lien by `name`. Callers of this method will require permission on the `parent` resource. For example, a Lien with a `parent` of `projects/1234` requires permission `resourcemanager.projects.get`
 */
export function getLienOutput(args: GetLienOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetLienResult> {
    return pulumi.output(args).apply((a: any) => getLien(a, opts))
}

export interface GetLienOutputArgs {
    lienId: pulumi.Input<string>;
}
