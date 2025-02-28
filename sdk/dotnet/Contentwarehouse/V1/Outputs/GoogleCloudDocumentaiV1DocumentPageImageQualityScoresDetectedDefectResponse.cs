// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Contentwarehouse.V1.Outputs
{

    /// <summary>
    /// Image Quality Defects
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectResponse
    {
        /// <summary>
        /// Confidence of detected defect. Range `[0, 1]` where `1` indicates strong confidence that the defect exists.
        /// </summary>
        public readonly double Confidence;
        /// <summary>
        /// Name of the defect type. Supported values are: - `quality/defect_blurry` - `quality/defect_noisy` - `quality/defect_dark` - `quality/defect_faint` - `quality/defect_text_too_small` - `quality/defect_document_cutoff` - `quality/defect_text_cutoff` - `quality/defect_glare`
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectResponse(
            double confidence,

            string type)
        {
            Confidence = confidence;
            Type = type;
        }
    }
}
