// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.WebSecurityScanner.V1Beta.Outputs
{

    /// <summary>
    /// Describes authentication configuration when Web-Security-Scanner service account is added in Identity-Aware-Proxy (IAP) access policies.
    /// </summary>
    [OutputType]
    public sealed class IapTestServiceAccountInfoResponse
    {
        /// <summary>
        /// Describes OAuth2 Client ID of resources protected by Identity-Aware-Proxy(IAP).
        /// </summary>
        public readonly string TargetAudienceClientId;

        [OutputConstructor]
        private IapTestServiceAccountInfoResponse(string targetAudienceClientId)
        {
            TargetAudienceClientId = targetAudienceClientId;
        }
    }
}
