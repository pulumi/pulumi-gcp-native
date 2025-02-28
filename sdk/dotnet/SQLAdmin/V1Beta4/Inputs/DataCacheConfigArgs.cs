// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.SQLAdmin.V1Beta4.Inputs
{

    /// <summary>
    /// Data cache configurations.
    /// </summary>
    public sealed class DataCacheConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether data cache is enabled for the instance.
        /// </summary>
        [Input("dataCacheEnabled")]
        public Input<bool>? DataCacheEnabled { get; set; }

        public DataCacheConfigArgs()
        {
        }
        public static new DataCacheConfigArgs Empty => new DataCacheConfigArgs();
    }
}
