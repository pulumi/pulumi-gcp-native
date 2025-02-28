// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.ContainerAnalysis.V1Beta1.Inputs
{

    /// <summary>
    /// The occurrence representing an SBOM reference as applied to a specific resource. The occurrence follows the DSSE specification. See https://github.com/secure-systems-lab/dsse/blob/master/envelope.md for more details.
    /// </summary>
    public sealed class SBOMReferenceOccurrenceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The actual payload that contains the SBOM reference data.
        /// </summary>
        [Input("payload")]
        public Input<Inputs.SbomReferenceIntotoPayloadArgs>? Payload { get; set; }

        /// <summary>
        /// The kind of payload that SbomReferenceIntotoPayload takes. Since it's in the intoto format, this value is expected to be 'application/vnd.in-toto+json'.
        /// </summary>
        [Input("payloadType")]
        public Input<string>? PayloadType { get; set; }

        [Input("signatures")]
        private InputList<Inputs.EnvelopeSignatureArgs>? _signatures;

        /// <summary>
        /// The signatures over the payload.
        /// </summary>
        public InputList<Inputs.EnvelopeSignatureArgs> Signatures
        {
            get => _signatures ?? (_signatures = new InputList<Inputs.EnvelopeSignatureArgs>());
            set => _signatures = value;
        }

        public SBOMReferenceOccurrenceArgs()
        {
        }
        public static new SBOMReferenceOccurrenceArgs Empty => new SBOMReferenceOccurrenceArgs();
    }
}
