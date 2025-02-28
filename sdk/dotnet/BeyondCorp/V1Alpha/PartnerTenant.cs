// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.BeyondCorp.V1Alpha
{
    /// <summary>
    /// Creates a new BeyondCorp Enterprise partnerTenant in a given organization and can only be called by onboarded BeyondCorp Enterprise partner.
    /// Auto-naming is currently not supported for this resource.
    /// </summary>
    [GoogleNativeResourceType("google-native:beyondcorp/v1alpha:PartnerTenant")]
    public partial class PartnerTenant : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Timestamp when the resource was created.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// Optional. An arbitrary caller-provided name for the PartnerTenant. Cannot exceed 64 characters.
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// Optional. Group information for the users enabled to use the partnerTenant. If the group information is not provided then the partnerTenant will be enabled for all users.
        /// </summary>
        [Output("group")]
        public Output<Outputs.GoogleCloudBeyondcorpPartnerservicesV1alphaGroupResponse> Group { get; private set; } = null!;

        /// <summary>
        /// Unique resource name of the PartnerTenant. The name is ignored when creating PartnerTenant.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("organizationId")]
        public Output<string> OrganizationId { get; private set; } = null!;

        /// <summary>
        /// Optional. Metadata provided by the Partner associated with PartnerTenant.
        /// </summary>
        [Output("partnerMetadata")]
        public Output<Outputs.GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerMetadataResponse> PartnerMetadata { get; private set; } = null!;

        /// <summary>
        /// Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        /// </summary>
        [Output("requestId")]
        public Output<string?> RequestId { get; private set; } = null!;

        /// <summary>
        /// Timestamp when the resource was last modified.
        /// </summary>
        [Output("updateTime")]
        public Output<string> UpdateTime { get; private set; } = null!;


        /// <summary>
        /// Create a PartnerTenant resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public PartnerTenant(string name, PartnerTenantArgs args, CustomResourceOptions? options = null)
            : base("google-native:beyondcorp/v1alpha:PartnerTenant", name, args ?? new PartnerTenantArgs(), MakeResourceOptions(options, ""))
        {
        }

        private PartnerTenant(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-native:beyondcorp/v1alpha:PartnerTenant", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "organizationId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing PartnerTenant resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static PartnerTenant Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new PartnerTenant(name, id, options);
        }
    }

    public sealed class PartnerTenantArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. An arbitrary caller-provided name for the PartnerTenant. Cannot exceed 64 characters.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// Optional. Group information for the users enabled to use the partnerTenant. If the group information is not provided then the partnerTenant will be enabled for all users.
        /// </summary>
        [Input("group")]
        public Input<Inputs.GoogleCloudBeyondcorpPartnerservicesV1alphaGroupArgs>? Group { get; set; }

        [Input("organizationId", required: true)]
        public Input<string> OrganizationId { get; set; } = null!;

        /// <summary>
        /// Optional. Metadata provided by the Partner associated with PartnerTenant.
        /// </summary>
        [Input("partnerMetadata")]
        public Input<Inputs.GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerMetadataArgs>? PartnerMetadata { get; set; }

        /// <summary>
        /// Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        /// </summary>
        [Input("requestId")]
        public Input<string>? RequestId { get; set; }

        public PartnerTenantArgs()
        {
        }
        public static new PartnerTenantArgs Empty => new PartnerTenantArgs();
    }
}
