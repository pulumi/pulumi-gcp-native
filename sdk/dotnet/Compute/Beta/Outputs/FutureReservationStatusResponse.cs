// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Compute.Beta.Outputs
{

    /// <summary>
    /// [Output only] Represents status related to the future reservation.
    /// </summary>
    [OutputType]
    public sealed class FutureReservationStatusResponse
    {
        /// <summary>
        /// The current status of the requested amendment.
        /// </summary>
        public readonly string AmendmentStatus;
        /// <summary>
        /// Fully qualified urls of the automatically created reservations at start_time.
        /// </summary>
        public readonly ImmutableArray<string> AutoCreatedReservations;
        /// <summary>
        /// This count indicates the fulfilled capacity so far. This is set during "PROVISIONING" state. This count also includes capacity delivered as part of existing matching reservations.
        /// </summary>
        public readonly string FulfilledCount;
        /// <summary>
        /// This field represents the future reservation before an amendment was requested. If the amendment is declined, the Future Reservation will be reverted to the last known good state. The last known good state is not set when updating a future reservation whose Procurement Status is DRAFTING.
        /// </summary>
        public readonly Outputs.FutureReservationStatusLastKnownGoodStateResponse LastKnownGoodState;
        /// <summary>
        /// Time when Future Reservation would become LOCKED, after which no modifications to Future Reservation will be allowed. Applicable only after the Future Reservation is in the APPROVED state. The lock_time is an RFC3339 string. The procurement_status will transition to PROCURING state at this time.
        /// </summary>
        public readonly string LockTime;
        /// <summary>
        /// Current state of this Future Reservation
        /// </summary>
        public readonly string ProcurementStatus;
        public readonly Outputs.FutureReservationStatusSpecificSKUPropertiesResponse SpecificSkuProperties;

        [OutputConstructor]
        private FutureReservationStatusResponse(
            string amendmentStatus,

            ImmutableArray<string> autoCreatedReservations,

            string fulfilledCount,

            Outputs.FutureReservationStatusLastKnownGoodStateResponse lastKnownGoodState,

            string lockTime,

            string procurementStatus,

            Outputs.FutureReservationStatusSpecificSKUPropertiesResponse specificSkuProperties)
        {
            AmendmentStatus = amendmentStatus;
            AutoCreatedReservations = autoCreatedReservations;
            FulfilledCount = fulfilledCount;
            LastKnownGoodState = lastKnownGoodState;
            LockTime = lockTime;
            ProcurementStatus = procurementStatus;
            SpecificSkuProperties = specificSkuProperties;
        }
    }
}
