// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Ml.V1
{
    /// <summary>
    /// Creates a training or a batch prediction job.
    /// Auto-naming is currently not supported for this resource.
    /// Note - this resource's API doesn't support deletion. When deleted, the resource will persist
    /// on Google Cloud even though it will be deleted from Pulumi state.
    /// </summary>
    [GoogleNativeResourceType("google-native:ml/v1:Job")]
    public partial class Job : global::Pulumi.CustomResource
    {
        /// <summary>
        /// When the job was created.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// When the job processing was completed.
        /// </summary>
        [Output("endTime")]
        public Output<string> EndTime { get; private set; } = null!;

        /// <summary>
        /// The details of a failure or a cancellation.
        /// </summary>
        [Output("errorMessage")]
        public Output<string> ErrorMessage { get; private set; } = null!;

        /// <summary>
        /// `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a job from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform job updates in order to avoid race conditions: An `etag` is returned in the response to `GetJob`, and systems are expected to put that etag in the request to `UpdateJob` to ensure that their change will be applied to the same version of the job.
        /// </summary>
        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        /// <summary>
        /// The user-specified id of the job.
        /// </summary>
        [Output("jobId")]
        public Output<string> JobId { get; private set; } = null!;

        /// <summary>
        /// It's only effect when the job is in QUEUED state. If it's positive, it indicates the job's position in the job scheduler. It's 0 when the job is already scheduled.
        /// </summary>
        [Output("jobPosition")]
        public Output<string> JobPosition { get; private set; } = null!;

        /// <summary>
        /// Optional. One or more labels that you can add, to organize your jobs. Each label is a key-value pair, where both the key and the value are arbitrary strings that you supply. For more information, see the documentation on using labels.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>> Labels { get; private set; } = null!;

        /// <summary>
        /// Input parameters to create a prediction job.
        /// </summary>
        [Output("predictionInput")]
        public Output<Outputs.GoogleCloudMlV1__PredictionInputResponse> PredictionInput { get; private set; } = null!;

        /// <summary>
        /// The current prediction job result.
        /// </summary>
        [Output("predictionOutput")]
        public Output<Outputs.GoogleCloudMlV1__PredictionOutputResponse> PredictionOutput { get; private set; } = null!;

        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// When the job processing was started.
        /// </summary>
        [Output("startTime")]
        public Output<string> StartTime { get; private set; } = null!;

        /// <summary>
        /// The detailed state of a job.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// Input parameters to create a training job.
        /// </summary>
        [Output("trainingInput")]
        public Output<Outputs.GoogleCloudMlV1__TrainingInputResponse> TrainingInput { get; private set; } = null!;

        /// <summary>
        /// The current training job result.
        /// </summary>
        [Output("trainingOutput")]
        public Output<Outputs.GoogleCloudMlV1__TrainingOutputResponse> TrainingOutput { get; private set; } = null!;


        /// <summary>
        /// Create a Job resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Job(string name, JobArgs args, CustomResourceOptions? options = null)
            : base("google-native:ml/v1:Job", name, args ?? new JobArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Job(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-native:ml/v1:Job", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "project",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Job resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Job Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Job(name, id, options);
        }
    }

    public sealed class JobArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a job from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform job updates in order to avoid race conditions: An `etag` is returned in the response to `GetJob`, and systems are expected to put that etag in the request to `UpdateJob` to ensure that their change will be applied to the same version of the job.
        /// </summary>
        [Input("etag")]
        public Input<string>? Etag { get; set; }

        /// <summary>
        /// The user-specified id of the job.
        /// </summary>
        [Input("jobId", required: true)]
        public Input<string> JobId { get; set; } = null!;

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Optional. One or more labels that you can add, to organize your jobs. Each label is a key-value pair, where both the key and the value are arbitrary strings that you supply. For more information, see the documentation on using labels.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// Input parameters to create a prediction job.
        /// </summary>
        [Input("predictionInput")]
        public Input<Inputs.GoogleCloudMlV1__PredictionInputArgs>? PredictionInput { get; set; }

        /// <summary>
        /// The current prediction job result.
        /// </summary>
        [Input("predictionOutput")]
        public Input<Inputs.GoogleCloudMlV1__PredictionOutputArgs>? PredictionOutput { get; set; }

        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// Input parameters to create a training job.
        /// </summary>
        [Input("trainingInput")]
        public Input<Inputs.GoogleCloudMlV1__TrainingInputArgs>? TrainingInput { get; set; }

        /// <summary>
        /// The current training job result.
        /// </summary>
        [Input("trainingOutput")]
        public Input<Inputs.GoogleCloudMlV1__TrainingOutputArgs>? TrainingOutput { get; set; }

        public JobArgs()
        {
        }
        public static new JobArgs Empty => new JobArgs();
    }
}
