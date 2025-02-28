// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Datastream.V1
{
    /// <summary>
    /// Use this method to create a private connectivity configuration.
    /// Auto-naming is currently not supported for this resource.
    /// </summary>
    [GoogleNativeResourceType("google-native:datastream/v1:PrivateConnection")]
    public partial class PrivateConnection : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The create time of the resource.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// Display name.
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// In case of error, the details of the error in a user-friendly format.
        /// </summary>
        [Output("error")]
        public Output<Outputs.ErrorResponse> Error { get; private set; } = null!;

        /// <summary>
        /// Optional. If set to true, will skip validations.
        /// </summary>
        [Output("force")]
        public Output<bool?> Force { get; private set; } = null!;

        /// <summary>
        /// Labels.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>> Labels { get; private set; } = null!;

        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// The resource's name.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Required. The private connectivity identifier.
        /// </summary>
        [Output("privateConnectionId")]
        public Output<string> PrivateConnectionId { get; private set; } = null!;

        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        /// </summary>
        [Output("requestId")]
        public Output<string?> RequestId { get; private set; } = null!;

        /// <summary>
        /// The state of the Private Connection.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// The update time of the resource.
        /// </summary>
        [Output("updateTime")]
        public Output<string> UpdateTime { get; private set; } = null!;

        /// <summary>
        /// VPC Peering Config.
        /// </summary>
        [Output("vpcPeeringConfig")]
        public Output<Outputs.VpcPeeringConfigResponse> VpcPeeringConfig { get; private set; } = null!;


        /// <summary>
        /// Create a PrivateConnection resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public PrivateConnection(string name, PrivateConnectionArgs args, CustomResourceOptions? options = null)
            : base("google-native:datastream/v1:PrivateConnection", name, args ?? new PrivateConnectionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private PrivateConnection(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-native:datastream/v1:PrivateConnection", name, null, MakeResourceOptions(options, id))
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
                    "privateConnectionId",
                    "project",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing PrivateConnection resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static PrivateConnection Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new PrivateConnection(name, id, options);
        }
    }

    public sealed class PrivateConnectionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Display name.
        /// </summary>
        [Input("displayName", required: true)]
        public Input<string> DisplayName { get; set; } = null!;

        /// <summary>
        /// Optional. If set to true, will skip validations.
        /// </summary>
        [Input("force")]
        public Input<bool>? Force { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Labels.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Required. The private connectivity identifier.
        /// </summary>
        [Input("privateConnectionId", required: true)]
        public Input<string> PrivateConnectionId { get; set; } = null!;

        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        /// </summary>
        [Input("requestId")]
        public Input<string>? RequestId { get; set; }

        /// <summary>
        /// VPC Peering Config.
        /// </summary>
        [Input("vpcPeeringConfig")]
        public Input<Inputs.VpcPeeringConfigArgs>? VpcPeeringConfig { get; set; }

        public PrivateConnectionArgs()
        {
        }
        public static new PrivateConnectionArgs Empty => new PrivateConnectionArgs();
    }
}
