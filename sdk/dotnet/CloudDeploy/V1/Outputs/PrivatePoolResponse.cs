// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.CloudDeploy.V1.Outputs
{

    /// <summary>
    /// Execution using a private Cloud Build pool.
    /// </summary>
    [OutputType]
    public sealed class PrivatePoolResponse
    {
        /// <summary>
        /// Optional. Cloud Storage location where execution outputs should be stored. This can either be a bucket ("gs://my-bucket") or a path within a bucket ("gs://my-bucket/my-dir"). If unspecified, a default bucket located in the same region will be used.
        /// </summary>
        public readonly string ArtifactStorage;
        /// <summary>
        /// Optional. Google service account to use for execution. If unspecified, the project execution service account (-compute@developer.gserviceaccount.com) will be used.
        /// </summary>
        public readonly string ServiceAccount;
        /// <summary>
        /// Resource name of the Cloud Build worker pool to use. The format is `projects/{project}/locations/{location}/workerPools/{pool}`.
        /// </summary>
        public readonly string WorkerPool;

        [OutputConstructor]
        private PrivatePoolResponse(
            string artifactStorage,

            string serviceAccount,

            string workerPool)
        {
            ArtifactStorage = artifactStorage;
            ServiceAccount = serviceAccount;
            WorkerPool = workerPool;
        }
    }
}
