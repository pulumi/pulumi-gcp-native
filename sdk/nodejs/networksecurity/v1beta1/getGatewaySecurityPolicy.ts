// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Gets details of a single GatewaySecurityPolicy.
 */
export function getGatewaySecurityPolicy(args: GetGatewaySecurityPolicyArgs, opts?: pulumi.InvokeOptions): Promise<GetGatewaySecurityPolicyResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:networksecurity/v1beta1:getGatewaySecurityPolicy", {
        "gatewaySecurityPolicyId": args.gatewaySecurityPolicyId,
        "location": args.location,
        "project": args.project,
    }, opts);
}

export interface GetGatewaySecurityPolicyArgs {
    gatewaySecurityPolicyId: string;
    location: string;
    project?: string;
}

export interface GetGatewaySecurityPolicyResult {
    /**
     * The timestamp when the resource was created.
     */
    readonly createTime: string;
    /**
     * Optional. Free-text description of the resource.
     */
    readonly description: string;
    /**
     * Name of the resource. Name is of the form projects/{project}/locations/{location}/gatewaySecurityPolicies/{gateway_security_policy} gateway_security_policy should match the pattern:(^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$).
     */
    readonly name: string;
    /**
     * Optional. Name of a TLS Inspection Policy resource that defines how TLS inspection will be performed for any rule(s) which enables it.
     */
    readonly tlsInspectionPolicy: string;
    /**
     * The timestamp when the resource was updated.
     */
    readonly updateTime: string;
}
/**
 * Gets details of a single GatewaySecurityPolicy.
 */
export function getGatewaySecurityPolicyOutput(args: GetGatewaySecurityPolicyOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetGatewaySecurityPolicyResult> {
    return pulumi.output(args).apply((a: any) => getGatewaySecurityPolicy(a, opts))
}

export interface GetGatewaySecurityPolicyOutputArgs {
    gatewaySecurityPolicyId: pulumi.Input<string>;
    location: pulumi.Input<string>;
    project?: pulumi.Input<string>;
}
