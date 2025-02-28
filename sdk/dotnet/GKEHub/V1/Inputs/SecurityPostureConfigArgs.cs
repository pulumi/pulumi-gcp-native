// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.GKEHub.V1.Inputs
{

    /// <summary>
    /// SecurityPostureConfig defines the flags needed to enable/disable features for the Security Posture API.
    /// </summary>
    public sealed class SecurityPostureConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Sets which mode to use for Security Posture features.
        /// </summary>
        [Input("mode")]
        public Input<Pulumi.GoogleNative.GKEHub.V1.SecurityPostureConfigMode>? Mode { get; set; }

        /// <summary>
        /// Sets which mode to use for vulnerability scanning.
        /// </summary>
        [Input("vulnerabilityMode")]
        public Input<Pulumi.GoogleNative.GKEHub.V1.SecurityPostureConfigVulnerabilityMode>? VulnerabilityMode { get; set; }

        public SecurityPostureConfigArgs()
        {
        }
        public static new SecurityPostureConfigArgs Empty => new SecurityPostureConfigArgs();
    }
}
