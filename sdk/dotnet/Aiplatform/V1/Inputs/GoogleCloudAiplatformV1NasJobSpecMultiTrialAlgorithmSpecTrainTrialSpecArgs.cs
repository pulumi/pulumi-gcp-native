// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1.Inputs
{

    /// <summary>
    /// Represent spec for train trials.
    /// </summary>
    public sealed class GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpecTrainTrialSpecArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Frequency of search trials to start train stage. Top N [TrainTrialSpec.max_parallel_trial_count] search trials will be trained for every M [TrainTrialSpec.frequency] trials searched.
        /// </summary>
        [Input("frequency", required: true)]
        public Input<int> Frequency { get; set; } = null!;

        /// <summary>
        /// The maximum number of trials to run in parallel.
        /// </summary>
        [Input("maxParallelTrialCount", required: true)]
        public Input<int> MaxParallelTrialCount { get; set; } = null!;

        /// <summary>
        /// The spec of a train trial job. The same spec applies to all train trials.
        /// </summary>
        [Input("trainTrialJobSpec", required: true)]
        public Input<Inputs.GoogleCloudAiplatformV1CustomJobSpecArgs> TrainTrialJobSpec { get; set; } = null!;

        public GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpecTrainTrialSpecArgs()
        {
        }
        public static new GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpecTrainTrialSpecArgs Empty => new GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpecTrainTrialSpecArgs();
    }
}
