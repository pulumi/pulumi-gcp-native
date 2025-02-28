// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1.Outputs
{

    /// <summary>
    /// The config for Featurestore Monitoring threshold.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudAiplatformV1FeaturestoreMonitoringConfigThresholdConfigResponse
    {
        /// <summary>
        /// Specify a threshold value that can trigger the alert. 1. For categorical feature, the distribution distance is calculated by L-inifinity norm. 2. For numerical feature, the distribution distance is calculated by Jensen–Shannon divergence. Each feature must have a non-zero threshold if they need to be monitored. Otherwise no alert will be triggered for that feature.
        /// </summary>
        public readonly double Value;

        [OutputConstructor]
        private GoogleCloudAiplatformV1FeaturestoreMonitoringConfigThresholdConfigResponse(double value)
        {
            Value = value;
        }
    }
}
