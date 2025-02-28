// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Gkeonprem.V1.Inputs
{

    /// <summary>
    /// BareMetalAdminWorkloadNodeConfig specifies the workload node configurations.
    /// </summary>
    public sealed class BareMetalAdminWorkloadNodeConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The maximum number of pods a node can run. The size of the CIDR range assigned to the node will be derived from this parameter. By default 110 Pods are created per Node. Upper bound is 250 for both HA and non-HA admin cluster. Lower bound is 64 for non-HA admin cluster and 32 for HA admin cluster.
        /// </summary>
        [Input("maxPodsPerNode")]
        public Input<string>? MaxPodsPerNode { get; set; }

        public BareMetalAdminWorkloadNodeConfigArgs()
        {
        }
        public static new BareMetalAdminWorkloadNodeConfigArgs Empty => new BareMetalAdminWorkloadNodeConfigArgs();
    }
}
