// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dialogflow.V3.Inputs
{

    /// <summary>
    /// The inference result which includes an objective metric to optimize and the confidence interval.
    /// </summary>
    public sealed class GoogleCloudDialogflowCxV3ExperimentResultArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The last time the experiment's stats data was updated. Will have default value if stats have never been computed for this experiment.
        /// </summary>
        [Input("lastUpdateTime")]
        public Input<string>? LastUpdateTime { get; set; }

        [Input("versionMetrics")]
        private InputList<Inputs.GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsArgs>? _versionMetrics;

        /// <summary>
        /// Version variants and metrics.
        /// </summary>
        public InputList<Inputs.GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsArgs> VersionMetrics
        {
            get => _versionMetrics ?? (_versionMetrics = new InputList<Inputs.GoogleCloudDialogflowCxV3ExperimentResultVersionMetricsArgs>());
            set => _versionMetrics = value;
        }

        public GoogleCloudDialogflowCxV3ExperimentResultArgs()
        {
        }
        public static new GoogleCloudDialogflowCxV3ExperimentResultArgs Empty => new GoogleCloudDialogflowCxV3ExperimentResultArgs();
    }
}
