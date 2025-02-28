// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1Beta1.Outputs
{

    /// <summary>
    /// Value specification for a parameter in `INTEGER` type.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudAiplatformV1beta1StudySpecParameterSpecIntegerValueSpecResponse
    {
        /// <summary>
        /// A default value for an `INTEGER` parameter that is assumed to be a relatively good starting point. Unset value signals that there is no offered starting point. Currently only supported by the Vertex AI Vizier service. Not supported by HyperparameterTuningJob or TrainingPipeline.
        /// </summary>
        public readonly string DefaultValue;
        /// <summary>
        /// Inclusive maximum value of the parameter.
        /// </summary>
        public readonly string MaxValue;
        /// <summary>
        /// Inclusive minimum value of the parameter.
        /// </summary>
        public readonly string MinValue;

        [OutputConstructor]
        private GoogleCloudAiplatformV1beta1StudySpecParameterSpecIntegerValueSpecResponse(
            string defaultValue,

            string maxValue,

            string minValue)
        {
            DefaultValue = defaultValue;
            MaxValue = maxValue;
            MinValue = minValue;
        }
    }
}
