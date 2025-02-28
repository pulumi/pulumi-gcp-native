// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.BigQuery.V2.Outputs
{

    [OutputType]
    public sealed class ViewDefinitionResponse
    {
        /// <summary>
        /// [Required] A query that BigQuery executes when the view is referenced.
        /// </summary>
        public readonly string Query;
        /// <summary>
        /// True if the column names are explicitly specified. For example by using the 'CREATE VIEW v(c1, c2) AS ...' syntax. Can only be set using BigQuery's standard SQL: https://cloud.google.com/bigquery/sql-reference/
        /// </summary>
        public readonly bool UseExplicitColumnNames;
        /// <summary>
        /// Specifies whether to use BigQuery's legacy SQL for this view. The default value is true. If set to false, the view will use BigQuery's standard SQL: https://cloud.google.com/bigquery/sql-reference/ Queries and views that reference this view must use the same flag value.
        /// </summary>
        public readonly bool UseLegacySql;
        /// <summary>
        /// Describes user-defined function resources used in the query.
        /// </summary>
        public readonly ImmutableArray<Outputs.UserDefinedFunctionResourceResponse> UserDefinedFunctionResources;

        [OutputConstructor]
        private ViewDefinitionResponse(
            string query,

            bool useExplicitColumnNames,

            bool useLegacySql,

            ImmutableArray<Outputs.UserDefinedFunctionResourceResponse> userDefinedFunctionResources)
        {
            Query = query;
            UseExplicitColumnNames = useExplicitColumnNames;
            UseLegacySql = useLegacySql;
            UserDefinedFunctionResources = userDefinedFunctionResources;
        }
    }
}
