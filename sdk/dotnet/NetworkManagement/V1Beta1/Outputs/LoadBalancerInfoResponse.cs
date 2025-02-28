// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.NetworkManagement.V1Beta1.Outputs
{

    /// <summary>
    /// For display only. Metadata associated with a load balancer.
    /// </summary>
    [OutputType]
    public sealed class LoadBalancerInfoResponse
    {
        /// <summary>
        /// Type of load balancer's backend configuration.
        /// </summary>
        public readonly string BackendType;
        /// <summary>
        /// Backend configuration URI.
        /// </summary>
        public readonly string BackendUri;
        /// <summary>
        /// Information for the loadbalancer backends.
        /// </summary>
        public readonly ImmutableArray<Outputs.LoadBalancerBackendResponse> Backends;
        /// <summary>
        /// URI of the health check for the load balancer. Deprecated and no longer populated as different load balancer backends might have different health checks.
        /// </summary>
        public readonly string HealthCheckUri;
        /// <summary>
        /// Type of the load balancer.
        /// </summary>
        public readonly string LoadBalancerType;

        [OutputConstructor]
        private LoadBalancerInfoResponse(
            string backendType,

            string backendUri,

            ImmutableArray<Outputs.LoadBalancerBackendResponse> backends,

            string healthCheckUri,

            string loadBalancerType)
        {
            BackendType = backendType;
            BackendUri = backendUri;
            Backends = backends;
            HealthCheckUri = healthCheckUri;
            LoadBalancerType = loadBalancerType;
        }
    }
}
