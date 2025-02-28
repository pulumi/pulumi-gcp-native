// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.IdentityToolkit.V2.Outputs
{

    /// <summary>
    /// TotpMFAProviderConfig represents the TOTP based MFA provider.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudIdentitytoolkitAdminV2TotpMfaProviderConfigResponse
    {
        /// <summary>
        /// The allowed number of adjacent intervals that will be used for verification to avoid clock skew.
        /// </summary>
        public readonly int AdjacentIntervals;

        [OutputConstructor]
        private GoogleCloudIdentitytoolkitAdminV2TotpMfaProviderConfigResponse(int adjacentIntervals)
        {
            AdjacentIntervals = adjacentIntervals;
        }
    }
}
