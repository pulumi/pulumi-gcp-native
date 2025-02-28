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
    /// Justification provides the justification when the state of the assessment if NOT_AFFECTED.
    /// </summary>
    public sealed class JustificationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Additional details on why this justification was chosen.
        /// </summary>
        [Input("details")]
        public Input<string>? Details { get; set; }

        /// <summary>
        /// The justification type for this vulnerability.
        /// </summary>
        [Input("justificationType")]
        public Input<Pulumi.GoogleNative.ContainerAnalysis.V1Beta1.JustificationJustificationType>? JustificationType { get; set; }

        public JustificationArgs()
        {
        }
        public static new JustificationArgs Empty => new JustificationArgs();
    }
}
