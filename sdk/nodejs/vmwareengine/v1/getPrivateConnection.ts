// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Retrieves a `PrivateConnection` resource by its resource name. The resource contains details of the private connection, such as connected network, routing mode and state.
 */
export function getPrivateConnection(args: GetPrivateConnectionArgs, opts?: pulumi.InvokeOptions): Promise<GetPrivateConnectionResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:vmwareengine/v1:getPrivateConnection", {
        "location": args.location,
        "privateConnectionId": args.privateConnectionId,
        "project": args.project,
    }, opts);
}

export interface GetPrivateConnectionArgs {
    location: string;
    privateConnectionId: string;
    project?: string;
}

export interface GetPrivateConnectionResult {
    /**
     * Creation time of this resource.
     */
    readonly createTime: string;
    /**
     * Optional. User-provided description for this private connection.
     */
    readonly description: string;
    /**
     * The resource name of the private connection. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1/privateConnections/my-connection`
     */
    readonly name: string;
    /**
     * VPC network peering id between given network VPC and VMwareEngineNetwork.
     */
    readonly peeringId: string;
    /**
     * Peering state between service network and VMware Engine network.
     */
    readonly peeringState: string;
    /**
     * Optional. Routing Mode. Default value is set to GLOBAL. For type = PRIVATE_SERVICE_ACCESS, this field can be set to GLOBAL or REGIONAL, for other types only GLOBAL is supported.
     */
    readonly routingMode: string;
    /**
     * Service network to create private connection. Specify the name in the following form: `projects/{project}/global/networks/{network_id}` For type = PRIVATE_SERVICE_ACCESS, this field represents servicenetworking VPC, e.g. projects/project-tp/global/networks/servicenetworking. For type = NETAPP_CLOUD_VOLUME, this field represents NetApp service VPC, e.g. projects/project-tp/global/networks/netapp-tenant-vpc. For type = DELL_POWERSCALE, this field represent Dell service VPC, e.g. projects/project-tp/global/networks/dell-tenant-vpc. For type= THIRD_PARTY_SERVICE, this field could represent a consumer VPC or any other producer VPC to which the VMware Engine Network needs to be connected, e.g. projects/project/global/networks/vpc.
     */
    readonly serviceNetwork: string;
    /**
     * State of the private connection.
     */
    readonly state: string;
    /**
     * Private connection type.
     */
    readonly type: string;
    /**
     * System-generated unique identifier for the resource.
     */
    readonly uid: string;
    /**
     * Last update time of this resource.
     */
    readonly updateTime: string;
    /**
     * The relative resource name of Legacy VMware Engine network. Specify the name in the following form: `projects/{project}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}` where `{project}`, `{location}` will be same as specified in private connection resource name and `{vmware_engine_network_id}` will be in the form of `{location}`-default e.g. projects/project/locations/us-central1/vmwareEngineNetworks/us-central1-default.
     */
    readonly vmwareEngineNetwork: string;
    /**
     * The canonical name of the VMware Engine network in the form: `projects/{project_number}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}`
     */
    readonly vmwareEngineNetworkCanonical: string;
}
/**
 * Retrieves a `PrivateConnection` resource by its resource name. The resource contains details of the private connection, such as connected network, routing mode and state.
 */
export function getPrivateConnectionOutput(args: GetPrivateConnectionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPrivateConnectionResult> {
    return pulumi.output(args).apply((a: any) => getPrivateConnection(a, opts))
}

export interface GetPrivateConnectionOutputArgs {
    location: pulumi.Input<string>;
    privateConnectionId: pulumi.Input<string>;
    project?: pulumi.Input<string>;
}
