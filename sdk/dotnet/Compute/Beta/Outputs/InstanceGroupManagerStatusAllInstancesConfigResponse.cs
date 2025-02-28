// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Compute.Beta.Outputs
{

    [OutputType]
    public sealed class InstanceGroupManagerStatusAllInstancesConfigResponse
    {
        /// <summary>
        /// Current all-instances configuration revision. This value is in RFC3339 text format.
        /// </summary>
        public readonly string CurrentRevision;
        /// <summary>
        /// A bit indicating whether this configuration has been applied to all managed instances in the group.
        /// </summary>
        public readonly bool Effective;

        [OutputConstructor]
        private InstanceGroupManagerStatusAllInstancesConfigResponse(
            string currentRevision,

            bool effective)
        {
            CurrentRevision = currentRevision;
            Effective = effective;
        }
    }
}
