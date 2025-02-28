// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Compute.Alpha.Outputs
{

    /// <summary>
    /// Errors encountered during the queueing or provisioning phases of the ResizeRequest.
    /// </summary>
    [OutputType]
    public sealed class InstanceGroupManagerResizeRequestStatusErrorResponse
    {
        /// <summary>
        /// The array of errors encountered while processing this operation.
        /// </summary>
        public readonly ImmutableArray<Outputs.InstanceGroupManagerResizeRequestStatusErrorErrorsItemResponse> Errors;

        [OutputConstructor]
        private InstanceGroupManagerResizeRequestStatusErrorResponse(ImmutableArray<Outputs.InstanceGroupManagerResizeRequestStatusErrorErrorsItemResponse> errors)
        {
            Errors = errors;
        }
    }
}
