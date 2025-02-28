// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.VMwareEngine.V1
{
    public static class GetCluster
    {
        /// <summary>
        /// Retrieves a `Cluster` resource by its resource name.
        /// </summary>
        public static Task<GetClusterResult> InvokeAsync(GetClusterArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetClusterResult>("google-native:vmwareengine/v1:getCluster", args ?? new GetClusterArgs(), options.WithDefaults());

        /// <summary>
        /// Retrieves a `Cluster` resource by its resource name.
        /// </summary>
        public static Output<GetClusterResult> Invoke(GetClusterInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetClusterResult>("google-native:vmwareengine/v1:getCluster", args ?? new GetClusterInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetClusterArgs : global::Pulumi.InvokeArgs
    {
        [Input("clusterId", required: true)]
        public string ClusterId { get; set; } = null!;

        [Input("location", required: true)]
        public string Location { get; set; } = null!;

        [Input("privateCloudId", required: true)]
        public string PrivateCloudId { get; set; } = null!;

        [Input("project")]
        public string? Project { get; set; }

        public GetClusterArgs()
        {
        }
        public static new GetClusterArgs Empty => new GetClusterArgs();
    }

    public sealed class GetClusterInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        [Input("privateCloudId", required: true)]
        public Input<string> PrivateCloudId { get; set; } = null!;

        [Input("project")]
        public Input<string>? Project { get; set; }

        public GetClusterInvokeArgs()
        {
        }
        public static new GetClusterInvokeArgs Empty => new GetClusterInvokeArgs();
    }


    [OutputType]
    public sealed class GetClusterResult
    {
        /// <summary>
        /// Creation time of this resource.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// True if the cluster is a management cluster; false otherwise. There can only be one management cluster in a private cloud and it has to be the first one.
        /// </summary>
        public readonly bool Management;
        /// <summary>
        /// The resource name of this cluster. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster`
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The map of cluster node types in this cluster, where the key is canonical identifier of the node type (corresponds to the `NodeType`).
        /// </summary>
        public readonly ImmutableDictionary<string, Outputs.NodeTypeConfigResponse> NodeTypeConfigs;
        /// <summary>
        /// State of the resource.
        /// </summary>
        public readonly string State;
        /// <summary>
        /// Optional. Configuration of a stretched cluster. Required for clusters that belong to a STRETCHED private cloud.
        /// </summary>
        public readonly Outputs.StretchedClusterConfigResponse StretchedClusterConfig;
        /// <summary>
        /// System-generated unique identifier for the resource.
        /// </summary>
        public readonly string Uid;
        /// <summary>
        /// Last update time of this resource.
        /// </summary>
        public readonly string UpdateTime;

        [OutputConstructor]
        private GetClusterResult(
            string createTime,

            bool management,

            string name,

            ImmutableDictionary<string, Outputs.NodeTypeConfigResponse> nodeTypeConfigs,

            string state,

            Outputs.StretchedClusterConfigResponse stretchedClusterConfig,

            string uid,

            string updateTime)
        {
            CreateTime = createTime;
            Management = management;
            Name = name;
            NodeTypeConfigs = nodeTypeConfigs;
            State = state;
            StretchedClusterConfig = stretchedClusterConfig;
            Uid = uid;
            UpdateTime = updateTime;
        }
    }
}
