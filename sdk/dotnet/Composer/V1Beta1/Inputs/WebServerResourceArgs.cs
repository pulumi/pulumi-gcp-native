// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Composer.V1Beta1.Inputs
{

    /// <summary>
    /// Configuration for resources used by Airflow web server.
    /// </summary>
    public sealed class WebServerResourceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. CPU request and limit for Airflow web server.
        /// </summary>
        [Input("cpu")]
        public Input<double>? Cpu { get; set; }

        /// <summary>
        /// Optional. Memory (GB) request and limit for Airflow web server.
        /// </summary>
        [Input("memoryGb")]
        public Input<double>? MemoryGb { get; set; }

        /// <summary>
        /// Optional. Storage (GB) request and limit for Airflow web server.
        /// </summary>
        [Input("storageGb")]
        public Input<double>? StorageGb { get; set; }

        public WebServerResourceArgs()
        {
        }
        public static new WebServerResourceArgs Empty => new WebServerResourceArgs();
    }
}
