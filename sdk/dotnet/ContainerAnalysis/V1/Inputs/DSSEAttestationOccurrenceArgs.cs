// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.ContainerAnalysis.V1.Inputs
{

    /// <summary>
    /// Deprecated. Prefer to use a regular Occurrence, and populate the Envelope at the top level of the Occurrence.
    /// </summary>
    public sealed class DSSEAttestationOccurrenceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// If doing something security critical, make sure to verify the signatures in this metadata.
        /// </summary>
        [Input("envelope")]
        public Input<Inputs.EnvelopeArgs>? Envelope { get; set; }

        [Input("statement")]
        public Input<Inputs.InTotoStatementArgs>? Statement { get; set; }

        public DSSEAttestationOccurrenceArgs()
        {
        }
        public static new DSSEAttestationOccurrenceArgs Empty => new DSSEAttestationOccurrenceArgs();
    }
}
