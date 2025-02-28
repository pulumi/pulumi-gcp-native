// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Container.V1Beta1.Inputs
{

    /// <summary>
    /// Specifies options for controlling advanced machine features.
    /// </summary>
    public sealed class AdvancedMachineFeaturesArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The number of threads per physical core. To disable simultaneous multithreading (SMT) set this to 1. If unset, the maximum number of threads supported per core by the underlying processor is assumed.
        /// </summary>
        [Input("threadsPerCore")]
        public Input<string>? ThreadsPerCore { get; set; }

        public AdvancedMachineFeaturesArgs()
        {
        }
        public static new AdvancedMachineFeaturesArgs Empty => new AdvancedMachineFeaturesArgs();
    }
}
