// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.CloudSearch.V1
{
    /// <summary>
    /// Creates a datasource. **Note:** This API requires an admin account to execute.
    /// </summary>
    [GoogleNativeResourceType("google-native:cloudsearch/v1:DataSource")]
    public partial class DataSource : global::Pulumi.CustomResource
    {
        /// <summary>
        /// If true, sets the datasource to read-only mode. In read-only mode, the Indexing API rejects any requests to index or delete items in this source. Enabling read-only mode does not stop the processing of previously accepted data.
        /// </summary>
        [Output("disableModifications")]
        public Output<bool> DisableModifications { get; private set; } = null!;

        /// <summary>
        /// Disable serving any search or assist results.
        /// </summary>
        [Output("disableServing")]
        public Output<bool> DisableServing { get; private set; } = null!;

        /// <summary>
        /// Display name of the datasource The maximum length is 300 characters.
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// List of service accounts that have indexing access.
        /// </summary>
        [Output("indexingServiceAccounts")]
        public Output<ImmutableArray<string>> IndexingServiceAccounts { get; private set; } = null!;

        /// <summary>
        /// This field restricts visibility to items at the datasource level. Items within the datasource are restricted to the union of users and groups included in this field. Note that, this does not ensure access to a specific item, as users need to have ACL permissions on the contained items. This ensures a high level access on the entire datasource, and that the individual items are not shared outside this visibility.
        /// </summary>
        [Output("itemsVisibility")]
        public Output<ImmutableArray<Outputs.GSuitePrincipalResponse>> ItemsVisibility { get; private set; } = null!;

        /// <summary>
        /// The name of the datasource resource. Format: datasources/{source_id}. The name is ignored when creating a datasource.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// IDs of the Long Running Operations (LROs) currently running for this schema.
        /// </summary>
        [Output("operationIds")]
        public Output<ImmutableArray<string>> OperationIds { get; private set; } = null!;

        /// <summary>
        /// Can a user request to get thumbnail URI for Items indexed in this data source.
        /// </summary>
        [Output("returnThumbnailUrls")]
        public Output<bool> ReturnThumbnailUrls { get; private set; } = null!;

        /// <summary>
        /// A short name or alias for the source. This value will be used to match the 'source' operator. For example, if the short name is *&lt;value&gt;* then queries like *source:&lt;value&gt;* will only return results for this source. The value must be unique across all datasources. The value must only contain alphanumeric characters (a-zA-Z0-9). The value cannot start with 'google' and cannot be one of the following: mail, gmail, docs, drive, groups, sites, calendar, hangouts, gplus, keep, people, teams. Its maximum length is 32 characters.
        /// </summary>
        [Output("shortName")]
        public Output<string> ShortName { get; private set; } = null!;


        /// <summary>
        /// Create a DataSource resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DataSource(string name, DataSourceArgs args, CustomResourceOptions? options = null)
            : base("google-native:cloudsearch/v1:DataSource", name, args ?? new DataSourceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DataSource(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-native:cloudsearch/v1:DataSource", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing DataSource resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DataSource Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new DataSource(name, id, options);
        }
    }

    public sealed class DataSourceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// If true, sets the datasource to read-only mode. In read-only mode, the Indexing API rejects any requests to index or delete items in this source. Enabling read-only mode does not stop the processing of previously accepted data.
        /// </summary>
        [Input("disableModifications")]
        public Input<bool>? DisableModifications { get; set; }

        /// <summary>
        /// Disable serving any search or assist results.
        /// </summary>
        [Input("disableServing")]
        public Input<bool>? DisableServing { get; set; }

        /// <summary>
        /// Display name of the datasource The maximum length is 300 characters.
        /// </summary>
        [Input("displayName", required: true)]
        public Input<string> DisplayName { get; set; } = null!;

        [Input("indexingServiceAccounts")]
        private InputList<string>? _indexingServiceAccounts;

        /// <summary>
        /// List of service accounts that have indexing access.
        /// </summary>
        public InputList<string> IndexingServiceAccounts
        {
            get => _indexingServiceAccounts ?? (_indexingServiceAccounts = new InputList<string>());
            set => _indexingServiceAccounts = value;
        }

        [Input("itemsVisibility")]
        private InputList<Inputs.GSuitePrincipalArgs>? _itemsVisibility;

        /// <summary>
        /// This field restricts visibility to items at the datasource level. Items within the datasource are restricted to the union of users and groups included in this field. Note that, this does not ensure access to a specific item, as users need to have ACL permissions on the contained items. This ensures a high level access on the entire datasource, and that the individual items are not shared outside this visibility.
        /// </summary>
        public InputList<Inputs.GSuitePrincipalArgs> ItemsVisibility
        {
            get => _itemsVisibility ?? (_itemsVisibility = new InputList<Inputs.GSuitePrincipalArgs>());
            set => _itemsVisibility = value;
        }

        /// <summary>
        /// The name of the datasource resource. Format: datasources/{source_id}. The name is ignored when creating a datasource.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("operationIds")]
        private InputList<string>? _operationIds;

        /// <summary>
        /// IDs of the Long Running Operations (LROs) currently running for this schema.
        /// </summary>
        public InputList<string> OperationIds
        {
            get => _operationIds ?? (_operationIds = new InputList<string>());
            set => _operationIds = value;
        }

        /// <summary>
        /// Can a user request to get thumbnail URI for Items indexed in this data source.
        /// </summary>
        [Input("returnThumbnailUrls")]
        public Input<bool>? ReturnThumbnailUrls { get; set; }

        /// <summary>
        /// A short name or alias for the source. This value will be used to match the 'source' operator. For example, if the short name is *&lt;value&gt;* then queries like *source:&lt;value&gt;* will only return results for this source. The value must be unique across all datasources. The value must only contain alphanumeric characters (a-zA-Z0-9). The value cannot start with 'google' and cannot be one of the following: mail, gmail, docs, drive, groups, sites, calendar, hangouts, gplus, keep, people, teams. Its maximum length is 32 characters.
        /// </summary>
        [Input("shortName")]
        public Input<string>? ShortName { get; set; }

        public DataSourceArgs()
        {
        }
        public static new DataSourceArgs Empty => new DataSourceArgs();
    }
}
