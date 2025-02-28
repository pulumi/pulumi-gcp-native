// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1.Outputs
{

    /// <summary>
    /// Represents the spec of persistent disk options.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudAiplatformV1PersistentDiskSpecResponse
    {
        /// <summary>
        /// Size in GB of the disk (default is 100GB).
        /// </summary>
        public readonly string DiskSizeGb;
        /// <summary>
        /// Type of the disk (default is "pd-standard"). Valid values: "pd-ssd" (Persistent Disk Solid State Drive) "pd-standard" (Persistent Disk Hard Disk Drive) "pd-balanced" (Balanced Persistent Disk) "pd-extreme" (Extreme Persistent Disk)
        /// </summary>
        public readonly string DiskType;

        [OutputConstructor]
        private GoogleCloudAiplatformV1PersistentDiskSpecResponse(
            string diskSizeGb,

            string diskType)
        {
            DiskSizeGb = diskSizeGb;
            DiskType = diskType;
        }
    }
}
