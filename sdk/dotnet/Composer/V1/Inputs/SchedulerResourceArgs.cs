// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Composer.V1.Inputs
{

    /// <summary>
    /// Configuration for resources used by Airflow schedulers.
    /// </summary>
    public sealed class SchedulerResourceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. The number of schedulers.
        /// </summary>
        [Input("count")]
        public Input<int>? Count { get; set; }

        /// <summary>
        /// Optional. CPU request and limit for a single Airflow scheduler replica.
        /// </summary>
        [Input("cpu")]
        public Input<double>? Cpu { get; set; }

        /// <summary>
        /// Optional. Memory (GB) request and limit for a single Airflow scheduler replica.
        /// </summary>
        [Input("memoryGb")]
        public Input<double>? MemoryGb { get; set; }

        /// <summary>
        /// Optional. Storage (GB) request and limit for a single Airflow scheduler replica.
        /// </summary>
        [Input("storageGb")]
        public Input<double>? StorageGb { get; set; }

        public SchedulerResourceArgs()
        {
        }
        public static new SchedulerResourceArgs Empty => new SchedulerResourceArgs();
    }
}
