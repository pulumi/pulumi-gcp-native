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
    /// The configuration of post scan actions of DataProfileScan job.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudDataplexV1DataProfileSpecPostScanActionsResponse
    {
        /// <summary>
        /// Optional. If set, results will be exported to the provided BigQuery table.
        /// </summary>
        public readonly Outputs.GoogleCloudDataplexV1DataProfileSpecPostScanActionsBigQueryExportResponse BigqueryExport;

        [OutputConstructor]
        private GoogleCloudDataplexV1DataProfileSpecPostScanActionsResponse(Outputs.GoogleCloudDataplexV1DataProfileSpecPostScanActionsBigQueryExportResponse bigqueryExport)
        {
            BigqueryExport = bigqueryExport;
        }
    }
}
