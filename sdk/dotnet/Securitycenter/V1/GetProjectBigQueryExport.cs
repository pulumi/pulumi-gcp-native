// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Securitycenter.V1
{
    public static class GetProjectBigQueryExport
    {
        /// <summary>
        /// Gets a BigQuery export.
        /// </summary>
        public static Task<GetProjectBigQueryExportResult> InvokeAsync(GetProjectBigQueryExportArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetProjectBigQueryExportResult>("google-native:securitycenter/v1:getProjectBigQueryExport", args ?? new GetProjectBigQueryExportArgs(), options.WithDefaults());

        /// <summary>
        /// Gets a BigQuery export.
        /// </summary>
        public static Output<GetProjectBigQueryExportResult> Invoke(GetProjectBigQueryExportInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetProjectBigQueryExportResult>("google-native:securitycenter/v1:getProjectBigQueryExport", args ?? new GetProjectBigQueryExportInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetProjectBigQueryExportArgs : global::Pulumi.InvokeArgs
    {
        [Input("bigQueryExportId", required: true)]
        public string BigQueryExportId { get; set; } = null!;

        [Input("project")]
        public string? Project { get; set; }

        public GetProjectBigQueryExportArgs()
        {
        }
        public static new GetProjectBigQueryExportArgs Empty => new GetProjectBigQueryExportArgs();
    }

    public sealed class GetProjectBigQueryExportInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("bigQueryExportId", required: true)]
        public Input<string> BigQueryExportId { get; set; } = null!;

        [Input("project")]
        public Input<string>? Project { get; set; }

        public GetProjectBigQueryExportInvokeArgs()
        {
        }
        public static new GetProjectBigQueryExportInvokeArgs Empty => new GetProjectBigQueryExportInvokeArgs();
    }


    [OutputType]
    public sealed class GetProjectBigQueryExportResult
    {
        /// <summary>
        /// The time at which the BigQuery export was created. This field is set by the server and will be ignored if provided on export on creation.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// The dataset to write findings' updates to. Its format is "projects/[project_id]/datasets/[bigquery_dataset_id]". BigQuery Dataset unique ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_).
        /// </summary>
        public readonly string Dataset;
        /// <summary>
        /// The description of the export (max of 1024 characters).
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// Expression that defines the filter to apply across create/update events of findings. The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. Parentheses are supported, and `OR` has higher precedence than `AND`. Restrictions have the form ` ` and may have a `-` character in front of them to indicate negation. The fields map to those defined in the corresponding resource. The supported operators are: * `=` for all value types. * `&gt;`, `&lt;`, `&gt;=`, `&lt;=` for integer values. * `:`, meaning substring matching, for strings. The supported value types are: * string literals in quotes. * integer literals without quotes. * boolean literals `true` and `false` without quotes.
        /// </summary>
        public readonly string Filter;
        /// <summary>
        /// Email address of the user who last edited the BigQuery export. This field is set by the server and will be ignored if provided on export creation or update.
        /// </summary>
        public readonly string MostRecentEditor;
        /// <summary>
        /// The relative resource name of this export. See: https://cloud.google.com/apis/design/resource_names#relative_resource_name. Example format: "organizations/{organization_id}/bigQueryExports/{export_id}" Example format: "folders/{folder_id}/bigQueryExports/{export_id}" Example format: "projects/{project_id}/bigQueryExports/{export_id}" This field is provided in responses, and is ignored when provided in create requests.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The service account that needs permission to create table and upload data to the BigQuery dataset.
        /// </summary>
        public readonly string Principal;
        /// <summary>
        /// The most recent time at which the BigQuery export was updated. This field is set by the server and will be ignored if provided on export creation or update.
        /// </summary>
        public readonly string UpdateTime;

        [OutputConstructor]
        private GetProjectBigQueryExportResult(
            string createTime,

            string dataset,

            string description,

            string filter,

            string mostRecentEditor,

            string name,

            string principal,

            string updateTime)
        {
            CreateTime = createTime;
            Dataset = dataset;
            Description = description;
            Filter = filter;
            MostRecentEditor = mostRecentEditor;
            Name = name;
            Principal = principal;
            UpdateTime = updateTime;
        }
    }
}
