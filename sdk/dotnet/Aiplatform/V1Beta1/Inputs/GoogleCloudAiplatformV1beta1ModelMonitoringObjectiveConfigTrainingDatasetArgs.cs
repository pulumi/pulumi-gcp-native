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
    /// Training Dataset information.
    /// </summary>
    public sealed class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigTrainingDatasetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The BigQuery table of the unmanaged Dataset used to train this Model.
        /// </summary>
        [Input("bigquerySource")]
        public Input<Inputs.GoogleCloudAiplatformV1beta1BigQuerySourceArgs>? BigquerySource { get; set; }

        /// <summary>
        /// Data format of the dataset, only applicable if the input is from Google Cloud Storage. The possible formats are: "tf-record" The source file is a TFRecord file. "csv" The source file is a CSV file. "jsonl" The source file is a JSONL file.
        /// </summary>
        [Input("dataFormat")]
        public Input<string>? DataFormat { get; set; }

        /// <summary>
        /// The resource name of the Dataset used to train this Model.
        /// </summary>
        [Input("dataset")]
        public Input<string>? Dataset { get; set; }

        /// <summary>
        /// The Google Cloud Storage uri of the unmanaged Dataset used to train this Model.
        /// </summary>
        [Input("gcsSource")]
        public Input<Inputs.GoogleCloudAiplatformV1beta1GcsSourceArgs>? GcsSource { get; set; }

        /// <summary>
        /// Strategy to sample data from Training Dataset. If not set, we process the whole dataset.
        /// </summary>
        [Input("loggingSamplingStrategy")]
        public Input<Inputs.GoogleCloudAiplatformV1beta1SamplingStrategyArgs>? LoggingSamplingStrategy { get; set; }

        /// <summary>
        /// The target field name the model is to predict. This field will be excluded when doing Predict and (or) Explain for the training data.
        /// </summary>
        [Input("targetField")]
        public Input<string>? TargetField { get; set; }

        public GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigTrainingDatasetArgs()
        {
        }
        public static new GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigTrainingDatasetArgs Empty => new GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigTrainingDatasetArgs();
    }
}
