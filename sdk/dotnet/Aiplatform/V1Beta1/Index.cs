// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1Beta1
{
    /// <summary>
    /// Creates an Index.
    /// Auto-naming is currently not supported for this resource.
    /// </summary>
    [GoogleNativeResourceType("google-native:aiplatform/v1beta1:Index")]
    public partial class Index : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Timestamp when this Index was created.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// The pointers to DeployedIndexes created from this Index. An Index can be only deleted if all its DeployedIndexes had been undeployed first.
        /// </summary>
        [Output("deployedIndexes")]
        public Output<ImmutableArray<Outputs.GoogleCloudAiplatformV1beta1DeployedIndexRefResponse>> DeployedIndexes { get; private set; } = null!;

        /// <summary>
        /// The description of the Index.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// The display name of the Index. The name can be up to 128 characters long and can consist of any UTF-8 characters.
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// Immutable. Customer-managed encryption key spec for an Index. If set, this Index and all sub-resources of this Index will be secured by this key.
        /// </summary>
        [Output("encryptionSpec")]
        public Output<Outputs.GoogleCloudAiplatformV1beta1EncryptionSpecResponse> EncryptionSpec { get; private set; } = null!;

        /// <summary>
        /// Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
        /// </summary>
        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        /// <summary>
        /// Stats of the index resource.
        /// </summary>
        [Output("indexStats")]
        public Output<Outputs.GoogleCloudAiplatformV1beta1IndexStatsResponse> IndexStats { get; private set; } = null!;

        /// <summary>
        /// Immutable. The update method to use with this Index. If not set, BATCH_UPDATE will be used by default.
        /// </summary>
        [Output("indexUpdateMethod")]
        public Output<string> IndexUpdateMethod { get; private set; } = null!;

        /// <summary>
        /// The labels with user-defined metadata to organize your Indexes. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>> Labels { get; private set; } = null!;

        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// An additional information about the Index; the schema of the metadata can be found in metadata_schema.
        /// </summary>
        [Output("metadata")]
        public Output<object> Metadata { get; private set; } = null!;

        /// <summary>
        /// Immutable. Points to a YAML file stored on Google Cloud Storage describing additional information about the Index, that is specific to it. Unset if the Index does not have any additional information. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access.
        /// </summary>
        [Output("metadataSchemaUri")]
        public Output<string> MetadataSchemaUri { get; private set; } = null!;

        /// <summary>
        /// The resource name of the Index.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// Timestamp when this Index was most recently updated. This also includes any update to the contents of the Index. Note that Operations working on this Index may have their Operations.metadata.generic_metadata.update_time a little after the value of this timestamp, yet that does not mean their results are not already reflected in the Index. Result of any successfully completed Operation on the Index is reflected in it.
        /// </summary>
        [Output("updateTime")]
        public Output<string> UpdateTime { get; private set; } = null!;


        /// <summary>
        /// Create a Index resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Index(string name, IndexArgs args, CustomResourceOptions? options = null)
            : base("google-native:aiplatform/v1beta1:Index", name, args ?? new IndexArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Index(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-native:aiplatform/v1beta1:Index", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Index resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Index Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Index(name, id, options);
        }
    }

    public sealed class IndexArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the Index.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The display name of the Index. The name can be up to 128 characters long and can consist of any UTF-8 characters.
        /// </summary>
        [Input("displayName", required: true)]
        public Input<string> DisplayName { get; set; } = null!;

        /// <summary>
        /// Immutable. Customer-managed encryption key spec for an Index. If set, this Index and all sub-resources of this Index will be secured by this key.
        /// </summary>
        [Input("encryptionSpec")]
        public Input<Inputs.GoogleCloudAiplatformV1beta1EncryptionSpecArgs>? EncryptionSpec { get; set; }

        /// <summary>
        /// Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.
        /// </summary>
        [Input("etag")]
        public Input<string>? Etag { get; set; }

        /// <summary>
        /// Immutable. The update method to use with this Index. If not set, BATCH_UPDATE will be used by default.
        /// </summary>
        [Input("indexUpdateMethod")]
        public Input<Pulumi.GoogleNative.Aiplatform.V1Beta1.IndexIndexUpdateMethod>? IndexUpdateMethod { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// The labels with user-defined metadata to organize your Indexes. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// An additional information about the Index; the schema of the metadata can be found in metadata_schema.
        /// </summary>
        [Input("metadata")]
        public Input<object>? Metadata { get; set; }

        /// <summary>
        /// Immutable. Points to a YAML file stored on Google Cloud Storage describing additional information about the Index, that is specific to it. Unset if the Index does not have any additional information. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access.
        /// </summary>
        [Input("metadataSchemaUri")]
        public Input<string>? MetadataSchemaUri { get; set; }

        [Input("project")]
        public Input<string>? Project { get; set; }

        public IndexArgs()
        {
        }
        public static new IndexArgs Empty => new IndexArgs();
    }
}
