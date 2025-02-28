// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.GKEHub.V1Beta1.Outputs
{

    /// <summary>
    /// MonitoringConfig informs Fleet-based applications/services/UIs how the metrics for the underlying cluster is reported to cloud monitoring services. It can be set from empty to non-empty, but can't be mutated directly to prevent accidentally breaking the constinousty of metrics.
    /// </summary>
    [OutputType]
    public sealed class MonitoringConfigResponse
    {
        /// <summary>
        /// Optional. Cluster name used to report metrics. For Anthos on VMWare/Baremetal/MultiCloud clusters, it would be in format {cluster_type}/{cluster_name}, e.g., "awsClusters/cluster_1".
        /// </summary>
        public readonly string Cluster;
        /// <summary>
        /// Optional. For GKE and Multicloud clusters, this is the UUID of the cluster resource. For VMWare and Baremetal clusters, this is the kube-system UID.
        /// </summary>
        public readonly string ClusterHash;
        /// <summary>
        /// Optional. Kubernetes system metrics, if available, are written to this prefix. This defaults to kubernetes.io for GKE, and kubernetes.io/anthos for Anthos eventually. Noted: Anthos MultiCloud will have kubernetes.io prefix today but will migration to be under kubernetes.io/anthos.
        /// </summary>
        public readonly string KubernetesMetricsPrefix;
        /// <summary>
        /// Optional. Location used to report Metrics
        /// </summary>
        public readonly string Location;
        /// <summary>
        /// Optional. Project used to report Metrics
        /// </summary>
        public readonly string Project;

        [OutputConstructor]
        private MonitoringConfigResponse(
            string cluster,

            string clusterHash,

            string kubernetesMetricsPrefix,

            string location,

            string project)
        {
            Cluster = cluster;
            ClusterHash = clusterHash;
            KubernetesMetricsPrefix = kubernetesMetricsPrefix;
            Location = location;
            Project = project;
        }
    }
}
