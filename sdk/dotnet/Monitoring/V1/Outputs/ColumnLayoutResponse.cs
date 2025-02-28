// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Monitoring.V1.Outputs
{

    /// <summary>
    /// A simplified layout that divides the available space into vertical columns and arranges a set of widgets vertically in each column.
    /// </summary>
    [OutputType]
    public sealed class ColumnLayoutResponse
    {
        /// <summary>
        /// The columns of content to display.
        /// </summary>
        public readonly ImmutableArray<Outputs.ColumnResponse> Columns;

        [OutputConstructor]
        private ColumnLayoutResponse(ImmutableArray<Outputs.ColumnResponse> columns)
        {
            Columns = columns;
        }
    }
}
