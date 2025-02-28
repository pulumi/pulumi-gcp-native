// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.BigtableAdmin.V2.Inputs
{

    /// <summary>
    /// Configuration for a cluster.
    /// </summary>
    public sealed class ClusterConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Autoscaling configuration for this cluster.
        /// </summary>
        [Input("clusterAutoscalingConfig")]
        public Input<Inputs.ClusterAutoscalingConfigArgs>? ClusterAutoscalingConfig { get; set; }

        public ClusterConfigArgs()
        {
        }
        public static new ClusterConfigArgs Empty => new ClusterConfigArgs();
    }
}
