// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.PolicySimulator.V1
{
    /// <summary>
    /// Creates and starts a Replay using the given ReplayConfig.
    /// Auto-naming is currently not supported for this resource.
    /// Note - this resource's API doesn't support deletion. When deleted, the resource will persist
    /// on Google Cloud even though it will be deleted from Pulumi state.
    /// </summary>
    [GoogleNativeResourceType("google-native:policysimulator/v1:FolderReplay")]
    public partial class FolderReplay : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The configuration used for the `Replay`.
        /// </summary>
        [Output("config")]
        public Output<Outputs.GoogleCloudPolicysimulatorV1ReplayConfigResponse> Config { get; private set; } = null!;

        [Output("folderId")]
        public Output<string> FolderId { get; private set; } = null!;

        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// The resource name of the `Replay`, which has the following format: `{projects|folders|organizations}/{resource-id}/locations/global/replays/{replay-id}`, where `{resource-id}` is the ID of the project, folder, or organization that owns the Replay. Example: `projects/my-example-project/locations/global/replays/506a5f7f-38ce-4d7d-8e03-479ce1833c36`
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Summary statistics about the replayed log entries.
        /// </summary>
        [Output("resultsSummary")]
        public Output<Outputs.GoogleCloudPolicysimulatorV1ReplayResultsSummaryResponse> ResultsSummary { get; private set; } = null!;

        /// <summary>
        /// The current state of the `Replay`.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;


        /// <summary>
        /// Create a FolderReplay resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FolderReplay(string name, FolderReplayArgs args, CustomResourceOptions? options = null)
            : base("google-native:policysimulator/v1:FolderReplay", name, args ?? new FolderReplayArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FolderReplay(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-native:policysimulator/v1:FolderReplay", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "folderId",
                    "location",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing FolderReplay resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FolderReplay Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new FolderReplay(name, id, options);
        }
    }

    public sealed class FolderReplayArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The configuration used for the `Replay`.
        /// </summary>
        [Input("config", required: true)]
        public Input<Inputs.GoogleCloudPolicysimulatorV1ReplayConfigArgs> Config { get; set; } = null!;

        [Input("folderId", required: true)]
        public Input<string> FolderId { get; set; } = null!;

        [Input("location")]
        public Input<string>? Location { get; set; }

        public FolderReplayArgs()
        {
        }
        public static new FolderReplayArgs Empty => new FolderReplayArgs();
    }
}
