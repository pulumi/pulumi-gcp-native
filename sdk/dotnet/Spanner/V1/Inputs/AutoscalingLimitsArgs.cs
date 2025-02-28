// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Spanner.V1.Inputs
{

    /// <summary>
    /// The autoscaling limits for the instance. Users can define the minimum and maximum compute capacity allocated to the instance, and the autoscaler will only scale within that range. Users can either use nodes or processing units to specify the limits, but should use the same unit to set both the min_limit and max_limit.
    /// </summary>
    public sealed class AutoscalingLimitsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Maximum number of nodes allocated to the instance. If set, this number should be greater than or equal to min_nodes.
        /// </summary>
        [Input("maxNodes")]
        public Input<int>? MaxNodes { get; set; }

        /// <summary>
        /// Maximum number of processing units allocated to the instance. If set, this number should be multiples of 1000 and be greater than or equal to min_processing_units.
        /// </summary>
        [Input("maxProcessingUnits")]
        public Input<int>? MaxProcessingUnits { get; set; }

        /// <summary>
        /// Minimum number of nodes allocated to the instance. If set, this number should be greater than or equal to 1.
        /// </summary>
        [Input("minNodes")]
        public Input<int>? MinNodes { get; set; }

        /// <summary>
        /// Minimum number of processing units allocated to the instance. If set, this number should be multiples of 1000.
        /// </summary>
        [Input("minProcessingUnits")]
        public Input<int>? MinProcessingUnits { get; set; }

        public AutoscalingLimitsArgs()
        {
        }
        public static new AutoscalingLimitsArgs Empty => new AutoscalingLimitsArgs();
    }
}
