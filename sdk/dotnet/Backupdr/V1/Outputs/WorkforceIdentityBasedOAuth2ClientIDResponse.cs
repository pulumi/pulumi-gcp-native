// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Backupdr.V1.Outputs
{

    /// <summary>
    /// OAuth Client ID depending on the Workforce Identity i.e. either 1p or 3p,
    /// </summary>
    [OutputType]
    public sealed class WorkforceIdentityBasedOAuth2ClientIDResponse
    {
        /// <summary>
        /// First party OAuth Client ID for Google Identities.
        /// </summary>
        public readonly string FirstPartyOauth2ClientId;
        /// <summary>
        /// Third party OAuth Client ID for External Identity Providers.
        /// </summary>
        public readonly string ThirdPartyOauth2ClientId;

        [OutputConstructor]
        private WorkforceIdentityBasedOAuth2ClientIDResponse(
            string firstPartyOauth2ClientId,

            string thirdPartyOauth2ClientId)
        {
            FirstPartyOauth2ClientId = firstPartyOauth2ClientId;
            ThirdPartyOauth2ClientId = thirdPartyOauth2ClientId;
        }
    }
}
