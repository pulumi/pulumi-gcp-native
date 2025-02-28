// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Healthcare.V1.Outputs
{

    /// <summary>
    /// Configuration for FHIR BigQuery time-partitioned tables.
    /// </summary>
    [OutputType]
    public sealed class TimePartitioningResponse
    {
        /// <summary>
        /// Number of milliseconds for which to keep the storage for a partition.
        /// </summary>
        public readonly string ExpirationMs;
        /// <summary>
        /// Type of partitioning.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private TimePartitioningResponse(
            string expirationMs,

            string type)
        {
            ExpirationMs = expirationMs;
            Type = type;
        }
    }
}
