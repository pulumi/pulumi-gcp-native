// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Eventarc.V1
{
    /// <summary>
    /// Create a new trigger in a particular project and location.
    /// </summary>
    [GoogleNativeResourceType("google-native:eventarc/v1:Trigger")]
    public partial class Trigger : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Optional. The name of the channel associated with the trigger in `projects/{project}/locations/{location}/channels/{channel}` format. You must provide a channel to receive events from Eventarc SaaS partners.
        /// </summary>
        [Output("channel")]
        public Output<string> Channel { get; private set; } = null!;

        /// <summary>
        /// The reason(s) why a trigger is in FAILED state.
        /// </summary>
        [Output("conditions")]
        public Output<ImmutableDictionary<string, Outputs.StateConditionResponse>> Conditions { get; private set; } = null!;

        /// <summary>
        /// The creation time.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// Destination specifies where the events should be sent to.
        /// </summary>
        [Output("destination")]
        public Output<Outputs.DestinationResponse> Destination { get; private set; } = null!;

        /// <summary>
        /// This checksum is computed by the server based on the value of other fields, and might be sent only on create requests to ensure that the client has an up-to-date value before proceeding.
        /// </summary>
        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        /// <summary>
        /// Optional. EventDataContentType specifies the type of payload in MIME format that is expected from the CloudEvent data field. This is set to `application/json` if the value is not defined.
        /// </summary>
        [Output("eventDataContentType")]
        public Output<string> EventDataContentType { get; private set; } = null!;

        /// <summary>
        /// Unordered list. The list of filters that applies to event attributes. Only events that match all the provided filters are sent to the destination.
        /// </summary>
        [Output("eventFilters")]
        public Output<ImmutableArray<Outputs.EventFilterResponse>> EventFilters { get; private set; } = null!;

        /// <summary>
        /// Optional. User labels attached to the triggers that can be used to group resources.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>> Labels { get; private set; } = null!;

        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// The resource name of the trigger. Must be unique within the location of the project and must be in `projects/{project}/locations/{location}/triggers/{trigger}` format.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// Optional. The IAM service account email associated with the trigger. The service account represents the identity of the trigger. The `iam.serviceAccounts.actAs` permission must be granted on the service account to allow a principal to impersonate the service account. For more information, see the [Roles and permissions](/eventarc/docs/all-roles-permissions) page specific to the trigger destination.
        /// </summary>
        [Output("serviceAccount")]
        public Output<string> ServiceAccount { get; private set; } = null!;

        /// <summary>
        /// Optional. To deliver messages, Eventarc might use other Google Cloud products as a transport intermediary. This field contains a reference to that transport intermediary. This information can be used for debugging purposes.
        /// </summary>
        [Output("transport")]
        public Output<Outputs.TransportResponse> Transport { get; private set; } = null!;

        /// <summary>
        /// Required. The user-provided ID to be assigned to the trigger.
        /// </summary>
        [Output("triggerId")]
        public Output<string> TriggerId { get; private set; } = null!;

        /// <summary>
        /// Server-assigned unique identifier for the trigger. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted.
        /// </summary>
        [Output("uid")]
        public Output<string> Uid { get; private set; } = null!;

        /// <summary>
        /// The last-modified time.
        /// </summary>
        [Output("updateTime")]
        public Output<string> UpdateTime { get; private set; } = null!;


        /// <summary>
        /// Create a Trigger resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Trigger(string name, TriggerArgs args, CustomResourceOptions? options = null)
            : base("google-native:eventarc/v1:Trigger", name, args ?? new TriggerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Trigger(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-native:eventarc/v1:Trigger", name, null, MakeResourceOptions(options, id))
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
                    "triggerId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Trigger resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Trigger Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Trigger(name, id, options);
        }
    }

    public sealed class TriggerArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. The name of the channel associated with the trigger in `projects/{project}/locations/{location}/channels/{channel}` format. You must provide a channel to receive events from Eventarc SaaS partners.
        /// </summary>
        [Input("channel")]
        public Input<string>? Channel { get; set; }

        /// <summary>
        /// Destination specifies where the events should be sent to.
        /// </summary>
        [Input("destination", required: true)]
        public Input<Inputs.DestinationArgs> Destination { get; set; } = null!;

        /// <summary>
        /// Optional. EventDataContentType specifies the type of payload in MIME format that is expected from the CloudEvent data field. This is set to `application/json` if the value is not defined.
        /// </summary>
        [Input("eventDataContentType")]
        public Input<string>? EventDataContentType { get; set; }

        [Input("eventFilters", required: true)]
        private InputList<Inputs.EventFilterArgs>? _eventFilters;

        /// <summary>
        /// Unordered list. The list of filters that applies to event attributes. Only events that match all the provided filters are sent to the destination.
        /// </summary>
        public InputList<Inputs.EventFilterArgs> EventFilters
        {
            get => _eventFilters ?? (_eventFilters = new InputList<Inputs.EventFilterArgs>());
            set => _eventFilters = value;
        }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Optional. User labels attached to the triggers that can be used to group resources.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The resource name of the trigger. Must be unique within the location of the project and must be in `projects/{project}/locations/{location}/triggers/{trigger}` format.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// Optional. The IAM service account email associated with the trigger. The service account represents the identity of the trigger. The `iam.serviceAccounts.actAs` permission must be granted on the service account to allow a principal to impersonate the service account. For more information, see the [Roles and permissions](/eventarc/docs/all-roles-permissions) page specific to the trigger destination.
        /// </summary>
        [Input("serviceAccount")]
        public Input<string>? ServiceAccount { get; set; }

        /// <summary>
        /// Optional. To deliver messages, Eventarc might use other Google Cloud products as a transport intermediary. This field contains a reference to that transport intermediary. This information can be used for debugging purposes.
        /// </summary>
        [Input("transport")]
        public Input<Inputs.TransportArgs>? Transport { get; set; }

        /// <summary>
        /// Required. The user-provided ID to be assigned to the trigger.
        /// </summary>
        [Input("triggerId", required: true)]
        public Input<string> TriggerId { get; set; } = null!;

        public TriggerArgs()
        {
        }
        public static new TriggerArgs Empty => new TriggerArgs();
    }
}
