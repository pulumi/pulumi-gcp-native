// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Transcoder.V1.Outputs
{

    /// <summary>
    /// Segment settings for `ts`, `fmp4` and `vtt`.
    /// </summary>
    [OutputType]
    public sealed class SegmentSettingsResponse
    {
        /// <summary>
        /// Create an individual segment file. The default is `false`.
        /// </summary>
        public readonly bool IndividualSegments;
        /// <summary>
        /// Duration of the segments in seconds. The default is `6.0s`. Note that `segmentDuration` must be greater than or equal to [`gopDuration`](#videostream), and `segmentDuration` must be divisible by [`gopDuration`](#videostream).
        /// </summary>
        public readonly string SegmentDuration;

        [OutputConstructor]
        private SegmentSettingsResponse(
            bool individualSegments,

            string segmentDuration)
        {
            IndividualSegments = individualSegments;
            SegmentDuration = segmentDuration;
        }
    }
}
