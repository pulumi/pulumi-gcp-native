// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Translate.V3.Inputs
{

    /// <summary>
    /// Represents a single entry for an unidirectional glossary.
    /// </summary>
    public sealed class GlossaryTermsPairArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The source term is the term that will get match in the text,
        /// </summary>
        [Input("sourceTerm")]
        public Input<Inputs.GlossaryTermArgs>? SourceTerm { get; set; }

        /// <summary>
        /// The term that will replace the match source term.
        /// </summary>
        [Input("targetTerm")]
        public Input<Inputs.GlossaryTermArgs>? TargetTerm { get; set; }

        public GlossaryTermsPairArgs()
        {
        }
        public static new GlossaryTermsPairArgs Empty => new GlossaryTermsPairArgs();
    }
}
