// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.VMwareEngine.V1
{
    /// <summary>
    /// Creates a new network policy in a given VMware Engine network of a project and location (region). A new network policy cannot be created if another network policy already exists in the same scope.
    /// Auto-naming is currently not supported for this resource.
    /// </summary>
    [GoogleNativeResourceType("google-native:vmwareengine/v1:NetworkPolicy")]
    public partial class NetworkPolicy : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Creation time of this resource.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// Optional. User-provided description for this network policy.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// IP address range in CIDR notation used to create internet access and external IP access. An RFC 1918 CIDR block, with a "/26" prefix, is required. The range cannot overlap with any prefixes either in the consumer VPC network or in use by the private clouds attached to that VPC network.
        /// </summary>
        [Output("edgeServicesCidr")]
        public Output<string> EdgeServicesCidr { get; private set; } = null!;

        /// <summary>
        /// Network service that allows External IP addresses to be assigned to VMware workloads. This service can only be enabled when `internet_access` is also enabled.
        /// </summary>
        [Output("externalIp")]
        public Output<Outputs.NetworkServiceResponse> ExternalIp { get; private set; } = null!;

        /// <summary>
        /// Network service that allows VMware workloads to access the internet.
        /// </summary>
        [Output("internetAccess")]
        public Output<Outputs.NetworkServiceResponse> InternetAccess { get; private set; } = null!;

        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// The resource name of this network policy. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1/networkPolicies/my-network-policy`
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Required. The user-provided identifier of the network policy to be created. This identifier must be unique within parent `projects/{my-project}/locations/{us-central1}/networkPolicies` and becomes the final token in the name URI. The identifier must meet the following requirements: * Only contains 1-63 alphanumeric characters and hyphens * Begins with an alphabetical character * Ends with a non-hyphen character * Not formatted as a UUID * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)
        /// </summary>
        [Output("networkPolicyId")]
        public Output<string> NetworkPolicyId { get; private set; } = null!;

        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        /// </summary>
        [Output("requestId")]
        public Output<string?> RequestId { get; private set; } = null!;

        /// <summary>
        /// System-generated unique identifier for the resource.
        /// </summary>
        [Output("uid")]
        public Output<string> Uid { get; private set; } = null!;

        /// <summary>
        /// Last update time of this resource.
        /// </summary>
        [Output("updateTime")]
        public Output<string> UpdateTime { get; private set; } = null!;

        /// <summary>
        /// Optional. The relative resource name of the VMware Engine network. Specify the name in the following form: `projects/{project}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}` where `{project}` can either be a project number or a project ID.
        /// </summary>
        [Output("vmwareEngineNetwork")]
        public Output<string> VmwareEngineNetwork { get; private set; } = null!;

        /// <summary>
        /// The canonical name of the VMware Engine network in the form: `projects/{project_number}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}`
        /// </summary>
        [Output("vmwareEngineNetworkCanonical")]
        public Output<string> VmwareEngineNetworkCanonical { get; private set; } = null!;


        /// <summary>
        /// Create a NetworkPolicy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NetworkPolicy(string name, NetworkPolicyArgs args, CustomResourceOptions? options = null)
            : base("google-native:vmwareengine/v1:NetworkPolicy", name, args ?? new NetworkPolicyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private NetworkPolicy(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-native:vmwareengine/v1:NetworkPolicy", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "location",
                    "networkPolicyId",
                    "project",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing NetworkPolicy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static NetworkPolicy Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new NetworkPolicy(name, id, options);
        }
    }

    public sealed class NetworkPolicyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. User-provided description for this network policy.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// IP address range in CIDR notation used to create internet access and external IP access. An RFC 1918 CIDR block, with a "/26" prefix, is required. The range cannot overlap with any prefixes either in the consumer VPC network or in use by the private clouds attached to that VPC network.
        /// </summary>
        [Input("edgeServicesCidr", required: true)]
        public Input<string> EdgeServicesCidr { get; set; } = null!;

        /// <summary>
        /// Network service that allows External IP addresses to be assigned to VMware workloads. This service can only be enabled when `internet_access` is also enabled.
        /// </summary>
        [Input("externalIp")]
        public Input<Inputs.NetworkServiceArgs>? ExternalIp { get; set; }

        /// <summary>
        /// Network service that allows VMware workloads to access the internet.
        /// </summary>
        [Input("internetAccess")]
        public Input<Inputs.NetworkServiceArgs>? InternetAccess { get; set; }

        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Required. The user-provided identifier of the network policy to be created. This identifier must be unique within parent `projects/{my-project}/locations/{us-central1}/networkPolicies` and becomes the final token in the name URI. The identifier must meet the following requirements: * Only contains 1-63 alphanumeric characters and hyphens * Begins with an alphabetical character * Ends with a non-hyphen character * Not formatted as a UUID * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)
        /// </summary>
        [Input("networkPolicyId", required: true)]
        public Input<string> NetworkPolicyId { get; set; } = null!;

        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        /// </summary>
        [Input("requestId")]
        public Input<string>? RequestId { get; set; }

        /// <summary>
        /// Optional. The relative resource name of the VMware Engine network. Specify the name in the following form: `projects/{project}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}` where `{project}` can either be a project number or a project ID.
        /// </summary>
        [Input("vmwareEngineNetwork")]
        public Input<string>? VmwareEngineNetwork { get; set; }

        public NetworkPolicyArgs()
        {
        }
        public static new NetworkPolicyArgs Empty => new NetworkPolicyArgs();
    }
}
