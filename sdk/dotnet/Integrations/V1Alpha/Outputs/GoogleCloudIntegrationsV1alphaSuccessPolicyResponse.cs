// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Integrations.V1Alpha.Outputs
{

    /// <summary>
    /// Policy that dictates the behavior for the task after it completes successfully.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudIntegrationsV1alphaSuccessPolicyResponse
    {
        /// <summary>
        /// State to which the execution snapshot status will be set if the task succeeds.
        /// </summary>
        public readonly string FinalState;

        [OutputConstructor]
        private GoogleCloudIntegrationsV1alphaSuccessPolicyResponse(string finalState)
        {
            FinalState = finalState;
        }
    }
}
