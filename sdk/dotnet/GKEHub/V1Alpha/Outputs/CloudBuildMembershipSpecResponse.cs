// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.GKEHub.V1Alpha.Outputs
{

    /// <summary>
    /// **Cloud Build**: Configurations for each Cloud Build enabled cluster.
    /// </summary>
    [OutputType]
    public sealed class CloudBuildMembershipSpecResponse
    {
        /// <summary>
        /// Whether it is allowed to run the privileged builds on the cluster or not.
        /// </summary>
        public readonly string SecurityPolicy;
        /// <summary>
        /// Version of the cloud build software on the cluster.
        /// </summary>
        public readonly string Version;

        [OutputConstructor]
        private CloudBuildMembershipSpecResponse(
            string securityPolicy,

            string version)
        {
            SecurityPolicy = securityPolicy;
            Version = version;
        }
    }
}
