// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dataproc.V1Beta2.Outputs
{

    /// <summary>
    /// A YARN application created by a job. Application information is a subset of org.apache.hadoop.yarn.proto.YarnProtos.ApplicationReportProto.Beta Feature: This report is available for testing purposes only. It may be changed before final release.
    /// </summary>
    [OutputType]
    public sealed class YarnApplicationResponse
    {
        /// <summary>
        /// The application name.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The numerical progress of the application, from 1 to 100.
        /// </summary>
        public readonly double Progress;
        /// <summary>
        /// The application state.
        /// </summary>
        public readonly string State;
        /// <summary>
        /// The HTTP URL of the ApplicationMaster, HistoryServer, or TimelineServer that provides application-specific information. The URL uses the internal hostname, and requires a proxy server for resolution and, possibly, access.
        /// </summary>
        public readonly string TrackingUrl;

        [OutputConstructor]
        private YarnApplicationResponse(
            string name,

            double progress,

            string state,

            string trackingUrl)
        {
            Name = name;
            Progress = progress;
            State = state;
            TrackingUrl = trackingUrl;
        }
    }
}
