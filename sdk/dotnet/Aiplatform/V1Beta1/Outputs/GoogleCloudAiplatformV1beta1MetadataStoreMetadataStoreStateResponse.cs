// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1Beta1.Outputs
{

    /// <summary>
    /// Represents state information for a MetadataStore.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudAiplatformV1beta1MetadataStoreMetadataStoreStateResponse
    {
        /// <summary>
        /// The disk utilization of the MetadataStore in bytes.
        /// </summary>
        public readonly string DiskUtilizationBytes;

        [OutputConstructor]
        private GoogleCloudAiplatformV1beta1MetadataStoreMetadataStoreStateResponse(string diskUtilizationBytes)
        {
            DiskUtilizationBytes = diskUtilizationBytes;
        }
    }
}
