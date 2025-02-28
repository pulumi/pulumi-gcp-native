// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.BigtableAdmin.V2.Inputs
{

    /// <summary>
    /// A GcRule which deletes cells matching any of the given rules.
    /// </summary>
    public sealed class UnionArgs : global::Pulumi.ResourceArgs
    {
        [Input("rules")]
        private InputList<Inputs.GcRuleArgs>? _rules;

        /// <summary>
        /// Delete cells which would be deleted by any element of `rules`.
        /// </summary>
        public InputList<Inputs.GcRuleArgs> Rules
        {
            get => _rules ?? (_rules = new InputList<Inputs.GcRuleArgs>());
            set => _rules = value;
        }

        public UnionArgs()
        {
        }
        public static new UnionArgs Empty => new UnionArgs();
    }
}
