// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1Beta1.Inputs
{

    /// <summary>
    /// Domain details of the input feature value. Provides numeric information about the feature, such as its range (min, max). If the feature has been pre-processed, for example with z-scoring, then it provides information about how to recover the original feature. For example, if the input feature is an image and it has been pre-processed to obtain 0-mean and stddev = 1 values, then original_mean, and original_stddev refer to the mean and stddev of the original feature (e.g. image tensor) from which input feature (with mean = 0 and stddev = 1) was obtained.
    /// </summary>
    public sealed class GoogleCloudAiplatformV1beta1ExplanationMetadataInputMetadataFeatureValueDomainArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The maximum permissible value for this feature.
        /// </summary>
        [Input("maxValue")]
        public Input<double>? MaxValue { get; set; }

        /// <summary>
        /// The minimum permissible value for this feature.
        /// </summary>
        [Input("minValue")]
        public Input<double>? MinValue { get; set; }

        /// <summary>
        /// If this input feature has been normalized to a mean value of 0, the original_mean specifies the mean value of the domain prior to normalization.
        /// </summary>
        [Input("originalMean")]
        public Input<double>? OriginalMean { get; set; }

        /// <summary>
        /// If this input feature has been normalized to a standard deviation of 1.0, the original_stddev specifies the standard deviation of the domain prior to normalization.
        /// </summary>
        [Input("originalStddev")]
        public Input<double>? OriginalStddev { get; set; }

        public GoogleCloudAiplatformV1beta1ExplanationMetadataInputMetadataFeatureValueDomainArgs()
        {
        }
        public static new GoogleCloudAiplatformV1beta1ExplanationMetadataInputMetadataFeatureValueDomainArgs Empty => new GoogleCloudAiplatformV1beta1ExplanationMetadataInputMetadataFeatureValueDomainArgs();
    }
}
