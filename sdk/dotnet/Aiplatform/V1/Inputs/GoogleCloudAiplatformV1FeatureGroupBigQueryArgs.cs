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
    /// Input source type for BigQuery Tables and Views.
    /// </summary>
    public sealed class GoogleCloudAiplatformV1FeatureGroupBigQueryArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Immutable. The BigQuery source URI that points to either a BigQuery Table or View.
        /// </summary>
        [Input("bigQuerySource", required: true)]
        public Input<Inputs.GoogleCloudAiplatformV1BigQuerySourceArgs> BigQuerySource { get; set; } = null!;

        [Input("entityIdColumns")]
        private InputList<string>? _entityIdColumns;

        /// <summary>
        /// Optional. Columns to construct entity_id / row keys. Currently only supports 1 entity_id_column. If not provided defaults to `entity_id`.
        /// </summary>
        public InputList<string> EntityIdColumns
        {
            get => _entityIdColumns ?? (_entityIdColumns = new InputList<string>());
            set => _entityIdColumns = value;
        }

        public GoogleCloudAiplatformV1FeatureGroupBigQueryArgs()
        {
        }
        public static new GoogleCloudAiplatformV1FeatureGroupBigQueryArgs Empty => new GoogleCloudAiplatformV1FeatureGroupBigQueryArgs();
    }
}
