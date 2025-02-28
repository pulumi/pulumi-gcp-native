// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dataproc.V1.Outputs
{

    /// <summary>
    /// Shielded Instance Config for clusters using Compute Engine Shielded VMs (https://cloud.google.com/security/shielded-cloud/shielded-vm).
    /// </summary>
    [OutputType]
    public sealed class ShieldedInstanceConfigResponse
    {
        /// <summary>
        /// Optional. Defines whether instances have integrity monitoring enabled.
        /// </summary>
        public readonly bool EnableIntegrityMonitoring;
        /// <summary>
        /// Optional. Defines whether instances have Secure Boot enabled.
        /// </summary>
        public readonly bool EnableSecureBoot;
        /// <summary>
        /// Optional. Defines whether instances have the vTPM enabled.
        /// </summary>
        public readonly bool EnableVtpm;

        [OutputConstructor]
        private ShieldedInstanceConfigResponse(
            bool enableIntegrityMonitoring,

            bool enableSecureBoot,

            bool enableVtpm)
        {
            EnableIntegrityMonitoring = enableIntegrityMonitoring;
            EnableSecureBoot = enableSecureBoot;
            EnableVtpm = enableVtpm;
        }
    }
}
