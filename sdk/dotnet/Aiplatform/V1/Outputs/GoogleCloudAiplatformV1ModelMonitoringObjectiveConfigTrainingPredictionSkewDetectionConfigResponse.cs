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
    /// The config for Training &amp; Prediction data skew detection. It specifies the training dataset sources and the skew detection parameters.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigTrainingPredictionSkewDetectionConfigResponse
    {
        /// <summary>
        /// Key is the feature name and value is the threshold. The threshold here is against attribution score distance between the training and prediction feature.
        /// </summary>
        public readonly ImmutableDictionary<string, Outputs.GoogleCloudAiplatformV1ThresholdConfigResponse> AttributionScoreSkewThresholds;
        /// <summary>
        /// Skew anomaly detection threshold used by all features. When the per-feature thresholds are not set, this field can be used to specify a threshold for all features.
        /// </summary>
        public readonly Outputs.GoogleCloudAiplatformV1ThresholdConfigResponse DefaultSkewThreshold;
        /// <summary>
        /// Key is the feature name and value is the threshold. If a feature needs to be monitored for skew, a value threshold must be configured for that feature. The threshold here is against feature distribution distance between the training and prediction feature.
        /// </summary>
        public readonly ImmutableDictionary<string, Outputs.GoogleCloudAiplatformV1ThresholdConfigResponse> SkewThresholds;

        [OutputConstructor]
        private GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigTrainingPredictionSkewDetectionConfigResponse(
            ImmutableDictionary<string, Outputs.GoogleCloudAiplatformV1ThresholdConfigResponse> attributionScoreSkewThresholds,

            Outputs.GoogleCloudAiplatformV1ThresholdConfigResponse defaultSkewThreshold,

            ImmutableDictionary<string, Outputs.GoogleCloudAiplatformV1ThresholdConfigResponse> skewThresholds)
        {
            AttributionScoreSkewThresholds = attributionScoreSkewThresholds;
            DefaultSkewThreshold = defaultSkewThreshold;
            SkewThresholds = skewThresholds;
        }
    }
}
