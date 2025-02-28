// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.BinaryAuthorization.V1.Outputs
{

    /// <summary>
    /// A conjunction of policy checks, scoped to a particular namespace or Kubernetes service account. In order for evaluation of a `CheckSet` to return "allowed" for a given image in a given Pod, one of the following conditions must be satisfied: * The image is explicitly exempted by an entry in `image_allowlist`, OR * ALL of the `checks` evaluate to "allowed".
    /// </summary>
    [OutputType]
    public sealed class CheckSetResponse
    {
        /// <summary>
        /// Optional. The checks to apply. The ultimate result of evaluating the check set will be "allow" if and only if every check in `checks` evaluates to "allow". If `checks` is empty, the default behavior is "always allow".
        /// </summary>
        public readonly ImmutableArray<Outputs.CheckResponse> Checks;
        /// <summary>
        /// Optional. A user-provided name for this `CheckSet`. This field has no effect on the policy evaluation behavior except to improve readability of messages in evaluation results.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// Optional. Images exempted from this `CheckSet`. If any of the patterns match the image being evaluated, no checks in the `CheckSet` will be evaluated.
        /// </summary>
        public readonly Outputs.ImageAllowlistResponse ImageAllowlist;
        /// <summary>
        /// Optional. The scope to which this `CheckSet` applies. If unset or an empty string (the default), applies to all namespaces and service accounts. See the `Scope` message documentation for details on scoping rules.
        /// </summary>
        public readonly Outputs.ScopeResponse Scope;

        [OutputConstructor]
        private CheckSetResponse(
            ImmutableArray<Outputs.CheckResponse> checks,

            string displayName,

            Outputs.ImageAllowlistResponse imageAllowlist,

            Outputs.ScopeResponse scope)
        {
            Checks = checks;
            DisplayName = displayName;
            ImageAllowlist = imageAllowlist;
            Scope = scope;
        }
    }
}
