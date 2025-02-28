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
    /// Configuration for Hierarchy Controller
    /// </summary>
    [OutputType]
    public sealed class ConfigManagementHierarchyControllerConfigResponse
    {
        /// <summary>
        /// Whether hierarchical resource quota is enabled in this cluster.
        /// </summary>
        public readonly bool EnableHierarchicalResourceQuota;
        /// <summary>
        /// Whether pod tree labels are enabled in this cluster.
        /// </summary>
        public readonly bool EnablePodTreeLabels;
        /// <summary>
        /// Whether Hierarchy Controller is enabled in this cluster.
        /// </summary>
        public readonly bool Enabled;

        [OutputConstructor]
        private ConfigManagementHierarchyControllerConfigResponse(
            bool enableHierarchicalResourceQuota,

            bool enablePodTreeLabels,

            bool enabled)
        {
            EnableHierarchicalResourceQuota = enableHierarchicalResourceQuota;
            EnablePodTreeLabels = enablePodTreeLabels;
            Enabled = enabled;
        }
    }
}
