// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1
{
    /// <summary>
    /// Creates a DataLabelingJob.
    /// Auto-naming is currently not supported for this resource.
    /// </summary>
    [GoogleNativeResourceType("google-native:aiplatform/v1:DataLabelingJob")]
    public partial class DataLabelingJob : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Parameters that configure the active learning pipeline. Active learning will label the data incrementally via several iterations. For every iteration, it will select a batch of data based on the sampling strategy.
        /// </summary>
        [Output("activeLearningConfig")]
        public Output<Outputs.GoogleCloudAiplatformV1ActiveLearningConfigResponse> ActiveLearningConfig { get; private set; } = null!;

        /// <summary>
        /// Labels to assign to annotations generated by this DataLabelingJob. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.
        /// </summary>
        [Output("annotationLabels")]
        public Output<ImmutableDictionary<string, string>> AnnotationLabels { get; private set; } = null!;

        /// <summary>
        /// Timestamp when this DataLabelingJob was created.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// Estimated cost(in US dollars) that the DataLabelingJob has incurred to date.
        /// </summary>
        [Output("currentSpend")]
        public Output<Outputs.GoogleTypeMoneyResponse> CurrentSpend { get; private set; } = null!;

        /// <summary>
        /// Dataset resource names. Right now we only support labeling from a single Dataset. Format: `projects/{project}/locations/{location}/datasets/{dataset}`
        /// </summary>
        [Output("datasets")]
        public Output<ImmutableArray<string>> Datasets { get; private set; } = null!;

        /// <summary>
        /// The user-defined name of the DataLabelingJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. Display name of a DataLabelingJob.
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// Customer-managed encryption key spec for a DataLabelingJob. If set, this DataLabelingJob will be secured by this key. Note: Annotations created in the DataLabelingJob are associated with the EncryptionSpec of the Dataset they are exported to.
        /// </summary>
        [Output("encryptionSpec")]
        public Output<Outputs.GoogleCloudAiplatformV1EncryptionSpecResponse> EncryptionSpec { get; private set; } = null!;

        /// <summary>
        /// DataLabelingJob errors. It is only populated when job's state is `JOB_STATE_FAILED` or `JOB_STATE_CANCELLED`.
        /// </summary>
        [Output("error")]
        public Output<Outputs.GoogleRpcStatusResponse> Error { get; private set; } = null!;

        /// <summary>
        /// Input config parameters for the DataLabelingJob.
        /// </summary>
        [Output("inputs")]
        public Output<object> Inputs { get; private set; } = null!;

        /// <summary>
        /// Points to a YAML file stored on Google Cloud Storage describing the config for a specific type of DataLabelingJob. The schema files that can be used here are found in the https://storage.googleapis.com/google-cloud-aiplatform bucket in the /schema/datalabelingjob/inputs/ folder.
        /// </summary>
        [Output("inputsSchemaUri")]
        public Output<string> InputsSchemaUri { get; private set; } = null!;

        /// <summary>
        /// The Google Cloud Storage location of the instruction pdf. This pdf is shared with labelers, and provides detailed description on how to label DataItems in Datasets.
        /// </summary>
        [Output("instructionUri")]
        public Output<string> InstructionUri { get; private set; } = null!;

        /// <summary>
        /// Number of labelers to work on each DataItem.
        /// </summary>
        [Output("labelerCount")]
        public Output<int> LabelerCount { get; private set; } = null!;

        /// <summary>
        /// Current labeling job progress percentage scaled in interval [0, 100], indicating the percentage of DataItems that has been finished.
        /// </summary>
        [Output("labelingProgress")]
        public Output<int> LabelingProgress { get; private set; } = null!;

        /// <summary>
        /// The labels with user-defined metadata to organize your DataLabelingJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. Following system labels exist for each DataLabelingJob: * "aiplatform.googleapis.com/schema": output only, its value is the inputs_schema's title.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>> Labels { get; private set; } = null!;

        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// Resource name of the DataLabelingJob.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// The SpecialistPools' resource names associated with this job.
        /// </summary>
        [Output("specialistPools")]
        public Output<ImmutableArray<string>> SpecialistPools { get; private set; } = null!;

        /// <summary>
        /// The detailed state of the job.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// Timestamp when this DataLabelingJob was updated most recently.
        /// </summary>
        [Output("updateTime")]
        public Output<string> UpdateTime { get; private set; } = null!;


        /// <summary>
        /// Create a DataLabelingJob resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DataLabelingJob(string name, DataLabelingJobArgs args, CustomResourceOptions? options = null)
            : base("google-native:aiplatform/v1:DataLabelingJob", name, args ?? new DataLabelingJobArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DataLabelingJob(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-native:aiplatform/v1:DataLabelingJob", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "location",
                    "project",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing DataLabelingJob resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DataLabelingJob Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new DataLabelingJob(name, id, options);
        }
    }

    public sealed class DataLabelingJobArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Parameters that configure the active learning pipeline. Active learning will label the data incrementally via several iterations. For every iteration, it will select a batch of data based on the sampling strategy.
        /// </summary>
        [Input("activeLearningConfig")]
        public Input<Inputs.GoogleCloudAiplatformV1ActiveLearningConfigArgs>? ActiveLearningConfig { get; set; }

        [Input("annotationLabels")]
        private InputMap<string>? _annotationLabels;

        /// <summary>
        /// Labels to assign to annotations generated by this DataLabelingJob. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.
        /// </summary>
        public InputMap<string> AnnotationLabels
        {
            get => _annotationLabels ?? (_annotationLabels = new InputMap<string>());
            set => _annotationLabels = value;
        }

        [Input("datasets", required: true)]
        private InputList<string>? _datasets;

        /// <summary>
        /// Dataset resource names. Right now we only support labeling from a single Dataset. Format: `projects/{project}/locations/{location}/datasets/{dataset}`
        /// </summary>
        public InputList<string> Datasets
        {
            get => _datasets ?? (_datasets = new InputList<string>());
            set => _datasets = value;
        }

        /// <summary>
        /// The user-defined name of the DataLabelingJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. Display name of a DataLabelingJob.
        /// </summary>
        [Input("displayName", required: true)]
        public Input<string> DisplayName { get; set; } = null!;

        /// <summary>
        /// Customer-managed encryption key spec for a DataLabelingJob. If set, this DataLabelingJob will be secured by this key. Note: Annotations created in the DataLabelingJob are associated with the EncryptionSpec of the Dataset they are exported to.
        /// </summary>
        [Input("encryptionSpec")]
        public Input<Inputs.GoogleCloudAiplatformV1EncryptionSpecArgs>? EncryptionSpec { get; set; }

        /// <summary>
        /// Input config parameters for the DataLabelingJob.
        /// </summary>
        [Input("inputs", required: true)]
        public Input<object> Inputs { get; set; } = null!;

        /// <summary>
        /// Points to a YAML file stored on Google Cloud Storage describing the config for a specific type of DataLabelingJob. The schema files that can be used here are found in the https://storage.googleapis.com/google-cloud-aiplatform bucket in the /schema/datalabelingjob/inputs/ folder.
        /// </summary>
        [Input("inputsSchemaUri", required: true)]
        public Input<string> InputsSchemaUri { get; set; } = null!;

        /// <summary>
        /// The Google Cloud Storage location of the instruction pdf. This pdf is shared with labelers, and provides detailed description on how to label DataItems in Datasets.
        /// </summary>
        [Input("instructionUri", required: true)]
        public Input<string> InstructionUri { get; set; } = null!;

        /// <summary>
        /// Number of labelers to work on each DataItem.
        /// </summary>
        [Input("labelerCount", required: true)]
        public Input<int> LabelerCount { get; set; } = null!;

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// The labels with user-defined metadata to organize your DataLabelingJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. Following system labels exist for each DataLabelingJob: * "aiplatform.googleapis.com/schema": output only, its value is the inputs_schema's title.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("location")]
        public Input<string>? Location { get; set; }

        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("specialistPools")]
        private InputList<string>? _specialistPools;

        /// <summary>
        /// The SpecialistPools' resource names associated with this job.
        /// </summary>
        public InputList<string> SpecialistPools
        {
            get => _specialistPools ?? (_specialistPools = new InputList<string>());
            set => _specialistPools = value;
        }

        public DataLabelingJobArgs()
        {
        }
        public static new DataLabelingJobArgs Empty => new DataLabelingJobArgs();
    }
}
