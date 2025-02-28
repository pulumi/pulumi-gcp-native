// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.GKEHub.V1.Outputs
{

    /// <summary>
    /// DefaultClusterConfig describes the default cluster configurations to be applied to all clusters born-in-fleet.
    /// </summary>
    [OutputType]
    public sealed class DefaultClusterConfigResponse
    {
        /// <summary>
        /// Optional. Enable/Disable binary authorization features for the cluster.
        /// </summary>
        public readonly Outputs.BinaryAuthorizationConfigResponse BinaryAuthorizationConfig;
        /// <summary>
        /// Enable/Disable Security Posture features for the cluster.
        /// </summary>
        public readonly Outputs.SecurityPostureConfigResponse SecurityPostureConfig;

        [OutputConstructor]
        private DefaultClusterConfigResponse(
            Outputs.BinaryAuthorizationConfigResponse binaryAuthorizationConfig,

            Outputs.SecurityPostureConfigResponse securityPostureConfig)
        {
            BinaryAuthorizationConfig = binaryAuthorizationConfig;
            SecurityPostureConfig = securityPostureConfig;
        }
    }
}
