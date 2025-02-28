// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Retrieves a 'ManagementDnsZoneBinding' resource by its resource name.
 */
export function getManagementDnsZoneBinding(args: GetManagementDnsZoneBindingArgs, opts?: pulumi.InvokeOptions): Promise<GetManagementDnsZoneBindingResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:vmwareengine/v1:getManagementDnsZoneBinding", {
        "location": args.location,
        "managementDnsZoneBindingId": args.managementDnsZoneBindingId,
        "privateCloudId": args.privateCloudId,
        "project": args.project,
    }, opts);
}

export interface GetManagementDnsZoneBindingArgs {
    location: string;
    managementDnsZoneBindingId: string;
    privateCloudId: string;
    project?: string;
}

export interface GetManagementDnsZoneBindingResult {
    /**
     * Creation time of this resource.
     */
    readonly createTime: string;
    /**
     * User-provided description for this resource.
     */
    readonly description: string;
    /**
     * The resource name of this binding. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/managementDnsZoneBindings/my-management-dns-zone-binding`
     */
    readonly name: string;
    /**
     * The state of the resource.
     */
    readonly state: string;
    /**
     * System-generated unique identifier for the resource.
     */
    readonly uid: string;
    /**
     * Last update time of this resource.
     */
    readonly updateTime: string;
    /**
     * Network to bind is a VMware Engine network. Specify the name in the following form for VMware engine network: `projects/{project}/locations/global/vmwareEngineNetworks/{vmware_engine_network_id}`. `{project}` can either be a project number or a project ID.
     */
    readonly vmwareEngineNetwork: string;
    /**
     * Network to bind is a standard consumer VPC. Specify the name in the following form for consumer VPC network: `projects/{project}/global/networks/{network_id}`. `{project}` can either be a project number or a project ID.
     */
    readonly vpcNetwork: string;
}
/**
 * Retrieves a 'ManagementDnsZoneBinding' resource by its resource name.
 */
export function getManagementDnsZoneBindingOutput(args: GetManagementDnsZoneBindingOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetManagementDnsZoneBindingResult> {
    return pulumi.output(args).apply((a: any) => getManagementDnsZoneBinding(a, opts))
}

export interface GetManagementDnsZoneBindingOutputArgs {
    location: pulumi.Input<string>;
    managementDnsZoneBindingId: pulumi.Input<string>;
    privateCloudId: pulumi.Input<string>;
    project?: pulumi.Input<string>;
}
