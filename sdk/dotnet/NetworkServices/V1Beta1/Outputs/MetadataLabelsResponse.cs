// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.NetworkServices.V1Beta1.Outputs
{

    /// <summary>
    /// Defines a name-pair value for a single label.
    /// </summary>
    [OutputType]
    public sealed class MetadataLabelsResponse
    {
        /// <summary>
        /// Label name presented as key in xDS Node Metadata.
        /// </summary>
        public readonly string LabelName;
        /// <summary>
        /// Label value presented as value corresponding to the above key, in xDS Node Metadata.
        /// </summary>
        public readonly string LabelValue;

        [OutputConstructor]
        private MetadataLabelsResponse(
            string labelName,

            string labelValue)
        {
            LabelName = labelName;
            LabelValue = labelValue;
        }
    }
}
