// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1.Outputs
{

    /// <summary>
    /// Configures the output of BatchPredictionJob. See Model.supported_output_storage_formats for supported output formats, and how predictions are expressed via any of them.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudAiplatformV1BatchPredictionJobOutputConfigResponse
    {
        /// <summary>
        /// The BigQuery project or dataset location where the output is to be written to. If project is provided, a new dataset is created with name `prediction__` where is made BigQuery-dataset-name compatible (for example, most special characters become underscores), and timestamp is in YYYY_MM_DDThh_mm_ss_sssZ "based on ISO-8601" format. In the dataset two tables will be created, `predictions`, and `errors`. If the Model has both instance and prediction schemata defined then the tables have columns as follows: The `predictions` table contains instances for which the prediction succeeded, it has columns as per a concatenation of the Model's instance and prediction schemata. The `errors` table contains rows for which the prediction has failed, it has instance columns, as per the instance schema, followed by a single "errors" column, which as values has google.rpc.Status represented as a STRUCT, and containing only `code` and `message`.
        /// </summary>
        public readonly Outputs.GoogleCloudAiplatformV1BigQueryDestinationResponse BigqueryDestination;
        /// <summary>
        /// The Cloud Storage location of the directory where the output is to be written to. In the given directory a new directory is created. Its name is `prediction--`, where timestamp is in YYYY-MM-DDThh:mm:ss.sssZ ISO-8601 format. Inside of it files `predictions_0001.`, `predictions_0002.`, ..., `predictions_N.` are created where `` depends on chosen predictions_format, and N may equal 0001 and depends on the total number of successfully predicted instances. If the Model has both instance and prediction schemata defined then each such file contains predictions as per the predictions_format. If prediction for any instance failed (partially or completely), then an additional `errors_0001.`, `errors_0002.`,..., `errors_N.` files are created (N depends on total number of failed predictions). These files contain the failed instances, as per their schema, followed by an additional `error` field which as value has google.rpc.Status containing only `code` and `message` fields.
        /// </summary>
        public readonly Outputs.GoogleCloudAiplatformV1GcsDestinationResponse GcsDestination;
        /// <summary>
        /// The format in which Vertex AI gives the predictions, must be one of the Model's supported_output_storage_formats.
        /// </summary>
        public readonly string PredictionsFormat;

        [OutputConstructor]
        private GoogleCloudAiplatformV1BatchPredictionJobOutputConfigResponse(
            Outputs.GoogleCloudAiplatformV1BigQueryDestinationResponse bigqueryDestination,

            Outputs.GoogleCloudAiplatformV1GcsDestinationResponse gcsDestination,

            string predictionsFormat)
        {
            BigqueryDestination = bigqueryDestination;
            GcsDestination = gcsDestination;
            PredictionsFormat = predictionsFormat;
        }
    }
}
