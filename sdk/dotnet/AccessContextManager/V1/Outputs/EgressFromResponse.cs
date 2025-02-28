// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.AccessContextManager.V1.Outputs
{

    /// <summary>
    /// Defines the conditions under which an EgressPolicy matches a request. Conditions based on information about the source of the request. Note that if the destination of the request is also protected by a ServicePerimeter, then that ServicePerimeter must have an IngressPolicy which allows access in order for this request to succeed.
    /// </summary>
    [OutputType]
    public sealed class EgressFromResponse
    {
        /// <summary>
        /// A list of identities that are allowed access through this [EgressPolicy]. Should be in the format of email address. The email address should represent individual user or service account only.
        /// </summary>
        public readonly ImmutableArray<string> Identities;
        /// <summary>
        /// Specifies the type of identities that are allowed access to outside the perimeter. If left unspecified, then members of `identities` field will be allowed access.
        /// </summary>
        public readonly string IdentityType;
        /// <summary>
        /// Whether to enforce traffic restrictions based on `sources` field. If the `sources` fields is non-empty, then this field must be set to `SOURCE_RESTRICTION_ENABLED`.
        /// </summary>
        public readonly string SourceRestriction;
        /// <summary>
        /// Sources that this EgressPolicy authorizes access from. If this field is not empty, then `source_restriction` must be set to `SOURCE_RESTRICTION_ENABLED`.
        /// </summary>
        public readonly ImmutableArray<Outputs.EgressSourceResponse> Sources;

        [OutputConstructor]
        private EgressFromResponse(
            ImmutableArray<string> identities,

            string identityType,

            string sourceRestriction,

            ImmutableArray<Outputs.EgressSourceResponse> sources)
        {
            Identities = identities;
            IdentityType = identityType;
            SourceRestriction = sourceRestriction;
            Sources = sources;
        }
    }
}
