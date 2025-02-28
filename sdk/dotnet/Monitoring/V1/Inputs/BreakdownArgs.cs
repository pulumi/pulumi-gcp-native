// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Monitoring.V1.Inputs
{

    /// <summary>
    /// Preview: A breakdown is an aggregation applied to the measures over a specified column. A breakdown can result in multiple series across a category for the provided measure. This is a preview feature and may be subject to change before final release.
    /// </summary>
    public sealed class BreakdownArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Aggregation function is applied across all data in each breakdown created.
        /// </summary>
        [Input("aggregationFunction", required: true)]
        public Input<Inputs.AggregationFunctionArgs> AggregationFunction { get; set; } = null!;

        /// <summary>
        /// The name of the column in the dataset containing the breakdown values.
        /// </summary>
        [Input("column", required: true)]
        public Input<string> Column { get; set; } = null!;

        /// <summary>
        /// A limit to the number of breakdowns. If set to zero then all possible breakdowns are applied. The list of breakdowns is dependent on the value of the sort_order field.
        /// </summary>
        [Input("limit", required: true)]
        public Input<int> Limit { get; set; } = null!;

        /// <summary>
        /// The sort order is applied to the values of the breakdown column.
        /// </summary>
        [Input("sortOrder", required: true)]
        public Input<Pulumi.GoogleNative.Monitoring.V1.BreakdownSortOrder> SortOrder { get; set; } = null!;

        public BreakdownArgs()
        {
        }
        public static new BreakdownArgs Empty => new BreakdownArgs();
    }
}
