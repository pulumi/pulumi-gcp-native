// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.APIGateway.V1Beta
{
    /// <summary>
    /// Creates a new Gateway in a given project and location.
    /// Auto-naming is currently not supported for this resource.
    /// </summary>
    [GoogleNativeResourceType("google-native:apigateway/v1beta:Gateway")]
    public partial class Gateway : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Resource name of the API Config for this Gateway. Format: projects/{project}/locations/global/apis/{api}/configs/{apiConfig}
        /// </summary>
        [Output("apiConfig")]
        public Output<string> ApiConfig { get; private set; } = null!;

        /// <summary>
        /// Created time.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// The default API Gateway host name of the form `{gateway_id}-{hash}.{region_code}.gateway.dev`.
        /// </summary>
        [Output("defaultHostname")]
        public Output<string> DefaultHostname { get; private set; } = null!;

        /// <summary>
        /// Optional. Display name.
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// Required. Identifier to assign to the Gateway. Must be unique within scope of the parent resource.
        /// </summary>
        [Output("gatewayId")]
        public Output<string> GatewayId { get; private set; } = null!;

        /// <summary>
        /// Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>> Labels { get; private set; } = null!;

        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// Resource name of the Gateway. Format: projects/{project}/locations/{location}/gateways/{gateway}
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// The current state of the Gateway.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// Updated time.
        /// </summary>
        [Output("updateTime")]
        public Output<string> UpdateTime { get; private set; } = null!;


        /// <summary>
        /// Create a Gateway resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Gateway(string name, GatewayArgs args, CustomResourceOptions? options = null)
            : base("google-native:apigateway/v1beta:Gateway", name, args ?? new GatewayArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Gateway(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-native:apigateway/v1beta:Gateway", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "gatewayId",
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
        /// Get an existing Gateway resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Gateway Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Gateway(name, id, options);
        }
    }

    public sealed class GatewayArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Resource name of the API Config for this Gateway. Format: projects/{project}/locations/global/apis/{api}/configs/{apiConfig}
        /// </summary>
        [Input("apiConfig", required: true)]
        public Input<string> ApiConfig { get; set; } = null!;

        /// <summary>
        /// Optional. Display name.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// Required. Identifier to assign to the Gateway. Must be unique within scope of the parent resource.
        /// </summary>
        [Input("gatewayId", required: true)]
        public Input<string> GatewayId { get; set; } = null!;

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources
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

        public GatewayArgs()
        {
        }
        public static new GatewayArgs Empty => new GatewayArgs();
    }
}
