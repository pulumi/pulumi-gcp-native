// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Contentwarehouse.V1.Outputs
{

    /// <summary>
    /// Timestamp values.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudContentwarehouseV1TimestampArrayResponse
    {
        /// <summary>
        /// List of timestamp values.
        /// </summary>
        public readonly ImmutableArray<Outputs.GoogleCloudContentwarehouseV1TimestampValueResponse> Values;

        [OutputConstructor]
        private GoogleCloudContentwarehouseV1TimestampArrayResponse(ImmutableArray<Outputs.GoogleCloudContentwarehouseV1TimestampValueResponse> values)
        {
            Values = values;
        }
    }
}
