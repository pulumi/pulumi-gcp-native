// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1Beta1.Outputs
{

    /// <summary>
    /// Used to set up the auth on the DeployedIndex's private endpoint.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudAiplatformV1beta1DeployedIndexAuthConfigResponse
    {
        /// <summary>
        /// Defines the authentication provider that the DeployedIndex uses.
        /// </summary>
        public readonly Outputs.GoogleCloudAiplatformV1beta1DeployedIndexAuthConfigAuthProviderResponse AuthProvider;

        [OutputConstructor]
        private GoogleCloudAiplatformV1beta1DeployedIndexAuthConfigResponse(Outputs.GoogleCloudAiplatformV1beta1DeployedIndexAuthConfigAuthProviderResponse authProvider)
        {
            AuthProvider = authProvider;
        }
    }
}
