// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.ContainerAnalysis.V1Beta1.Outputs
{

    /// <summary>
    /// Specifies details on how to handle (and presumably, fix) a vulnerability.
    /// </summary>
    [OutputType]
    public sealed class RemediationResponse
    {
        /// <summary>
        /// Contains a comprehensive human-readable discussion of the remediation.
        /// </summary>
        public readonly string Details;
        /// <summary>
        /// The type of remediation that can be applied.
        /// </summary>
        public readonly string RemediationType;
        /// <summary>
        /// Contains the URL where to obtain the remediation.
        /// </summary>
        public readonly Outputs.RelatedUrlResponse RemediationUri;

        [OutputConstructor]
        private RemediationResponse(
            string details,

            string remediationType,

            Outputs.RelatedUrlResponse remediationUri)
        {
            Details = details;
            RemediationType = remediationType;
            RemediationUri = remediationUri;
        }
    }
}
