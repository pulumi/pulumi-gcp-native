// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dataplex.V1.Outputs
{

    /// <summary>
    /// Settings to manage the metadata discovery and publishing for an asset.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudDataplexV1AssetDiscoverySpecResponse
    {
        /// <summary>
        /// Optional. Configuration for CSV data.
        /// </summary>
        public readonly Outputs.GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsResponse CsvOptions;
        /// <summary>
        /// Optional. Whether discovery is enabled.
        /// </summary>
        public readonly bool Enabled;
        /// <summary>
        /// Optional. The list of patterns to apply for selecting data to exclude during discovery. For Cloud Storage bucket assets, these are interpreted as glob patterns used to match object names. For BigQuery dataset assets, these are interpreted as patterns to match table names.
        /// </summary>
        public readonly ImmutableArray<string> ExcludePatterns;
        /// <summary>
        /// Optional. The list of patterns to apply for selecting data to include during discovery if only a subset of the data should considered. For Cloud Storage bucket assets, these are interpreted as glob patterns used to match object names. For BigQuery dataset assets, these are interpreted as patterns to match table names.
        /// </summary>
        public readonly ImmutableArray<string> IncludePatterns;
        /// <summary>
        /// Optional. Configuration for Json data.
        /// </summary>
        public readonly Outputs.GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsResponse JsonOptions;
        /// <summary>
        /// Optional. Cron schedule (https://en.wikipedia.org/wiki/Cron) for running discovery periodically. Successive discovery runs must be scheduled at least 60 minutes apart. The default value is to run discovery every 60 minutes. To explicitly set a timezone to the cron tab, apply a prefix in the cron tab: "CRON_TZ=${IANA_TIME_ZONE}" or TZ=${IANA_TIME_ZONE}". The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, CRON_TZ=America/New_York 1 * * * *, or TZ=America/New_York 1 * * * *.
        /// </summary>
        public readonly string Schedule;

        [OutputConstructor]
        private GoogleCloudDataplexV1AssetDiscoverySpecResponse(
            Outputs.GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsResponse csvOptions,

            bool enabled,

            ImmutableArray<string> excludePatterns,

            ImmutableArray<string> includePatterns,

            Outputs.GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsResponse jsonOptions,

            string schedule)
        {
            CsvOptions = csvOptions;
            Enabled = enabled;
            ExcludePatterns = excludePatterns;
            IncludePatterns = includePatterns;
            JsonOptions = jsonOptions;
            Schedule = schedule;
        }
    }
}
