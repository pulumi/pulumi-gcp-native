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
    /// Configuration for the runtime on a PersistentResource instance, including but not limited to: * Service accounts used to run the workloads. * Whether to make it a dedicated Ray Cluster.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudAiplatformV1beta1ResourceRuntimeSpecResponse
    {
        /// <summary>
        /// Optional. Ray cluster configuration. Required when creating a dedicated RayCluster on the PersistentResource.
        /// </summary>
        public readonly Outputs.GoogleCloudAiplatformV1beta1RaySpecResponse RaySpec;
        /// <summary>
        /// Optional. Configure the use of workload identity on the PersistentResource
        /// </summary>
        public readonly Outputs.GoogleCloudAiplatformV1beta1ServiceAccountSpecResponse ServiceAccountSpec;

        [OutputConstructor]
        private GoogleCloudAiplatformV1beta1ResourceRuntimeSpecResponse(
            Outputs.GoogleCloudAiplatformV1beta1RaySpecResponse raySpec,

            Outputs.GoogleCloudAiplatformV1beta1ServiceAccountSpecResponse serviceAccountSpec)
        {
            RaySpec = raySpec;
            ServiceAccountSpec = serviceAccountSpec;
        }
    }
}
