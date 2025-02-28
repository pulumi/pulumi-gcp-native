// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Compute.V1.Outputs
{

    /// <summary>
    /// Upcoming Maintenance notification information.
    /// </summary>
    [OutputType]
    public sealed class UpcomingMaintenanceResponse
    {
        /// <summary>
        /// Indicates if the maintenance can be customer triggered.
        /// </summary>
        public readonly bool CanReschedule;
        /// <summary>
        /// The latest time for the planned maintenance window to start. This timestamp value is in RFC3339 text format.
        /// </summary>
        public readonly string LatestWindowStartTime;
        public readonly string MaintenanceStatus;
        /// <summary>
        /// Defines the type of maintenance.
        /// </summary>
        public readonly string Type;
        /// <summary>
        /// The time by which the maintenance disruption will be completed. This timestamp value is in RFC3339 text format.
        /// </summary>
        public readonly string WindowEndTime;
        /// <summary>
        /// The current start time of the maintenance window. This timestamp value is in RFC3339 text format.
        /// </summary>
        public readonly string WindowStartTime;

        [OutputConstructor]
        private UpcomingMaintenanceResponse(
            bool canReschedule,

            string latestWindowStartTime,

            string maintenanceStatus,

            string type,

            string windowEndTime,

            string windowStartTime)
        {
            CanReschedule = canReschedule;
            LatestWindowStartTime = latestWindowStartTime;
            MaintenanceStatus = maintenanceStatus;
            Type = type;
            WindowEndTime = windowEndTime;
            WindowStartTime = windowStartTime;
        }
    }
}
