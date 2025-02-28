// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.AppEngine.V1.Outputs
{

    /// <summary>
    /// Automatic scaling is based on request rate, response latencies, and other application metrics.
    /// </summary>
    [OutputType]
    public sealed class AutomaticScalingResponse
    {
        /// <summary>
        /// The time period that the Autoscaler (https://cloud.google.com/compute/docs/autoscaler/) should wait before it starts collecting information from a new instance. This prevents the autoscaler from collecting information when the instance is initializing, during which the collected usage would not be reliable. Only applicable in the App Engine flexible environment.
        /// </summary>
        public readonly string CoolDownPeriod;
        /// <summary>
        /// Target scaling by CPU usage.
        /// </summary>
        public readonly Outputs.CpuUtilizationResponse CpuUtilization;
        /// <summary>
        /// Target scaling by disk usage.
        /// </summary>
        public readonly Outputs.DiskUtilizationResponse DiskUtilization;
        /// <summary>
        /// Number of concurrent requests an automatic scaling instance can accept before the scheduler spawns a new instance.Defaults to a runtime-specific value.
        /// </summary>
        public readonly int MaxConcurrentRequests;
        /// <summary>
        /// Maximum number of idle instances that should be maintained for this version.
        /// </summary>
        public readonly int MaxIdleInstances;
        /// <summary>
        /// Maximum amount of time that a request should wait in the pending queue before starting a new instance to handle it.
        /// </summary>
        public readonly string MaxPendingLatency;
        /// <summary>
        /// Maximum number of instances that should be started to handle requests for this version.
        /// </summary>
        public readonly int MaxTotalInstances;
        /// <summary>
        /// Minimum number of idle instances that should be maintained for this version. Only applicable for the default version of a service.
        /// </summary>
        public readonly int MinIdleInstances;
        /// <summary>
        /// Minimum amount of time a request should wait in the pending queue before starting a new instance to handle it.
        /// </summary>
        public readonly string MinPendingLatency;
        /// <summary>
        /// Minimum number of running instances that should be maintained for this version.
        /// </summary>
        public readonly int MinTotalInstances;
        /// <summary>
        /// Target scaling by network usage.
        /// </summary>
        public readonly Outputs.NetworkUtilizationResponse NetworkUtilization;
        /// <summary>
        /// Target scaling by request utilization.
        /// </summary>
        public readonly Outputs.RequestUtilizationResponse RequestUtilization;
        /// <summary>
        /// Scheduler settings for standard environment.
        /// </summary>
        public readonly Outputs.StandardSchedulerSettingsResponse StandardSchedulerSettings;

        [OutputConstructor]
        private AutomaticScalingResponse(
            string coolDownPeriod,

            Outputs.CpuUtilizationResponse cpuUtilization,

            Outputs.DiskUtilizationResponse diskUtilization,

            int maxConcurrentRequests,

            int maxIdleInstances,

            string maxPendingLatency,

            int maxTotalInstances,

            int minIdleInstances,

            string minPendingLatency,

            int minTotalInstances,

            Outputs.NetworkUtilizationResponse networkUtilization,

            Outputs.RequestUtilizationResponse requestUtilization,

            Outputs.StandardSchedulerSettingsResponse standardSchedulerSettings)
        {
            CoolDownPeriod = coolDownPeriod;
            CpuUtilization = cpuUtilization;
            DiskUtilization = diskUtilization;
            MaxConcurrentRequests = maxConcurrentRequests;
            MaxIdleInstances = maxIdleInstances;
            MaxPendingLatency = maxPendingLatency;
            MaxTotalInstances = maxTotalInstances;
            MinIdleInstances = minIdleInstances;
            MinPendingLatency = minPendingLatency;
            MinTotalInstances = minTotalInstances;
            NetworkUtilization = networkUtilization;
            RequestUtilization = requestUtilization;
            StandardSchedulerSettings = standardSchedulerSettings;
        }
    }
}
