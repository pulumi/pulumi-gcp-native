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
    /// A description of resources that are dedicated to a DeployedModel, and that need a higher degree of manual configuration.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudAiplatformV1beta1DedicatedResourcesResponse
    {
        /// <summary>
        /// Immutable. The metric specifications that overrides a resource utilization metric (CPU utilization, accelerator's duty cycle, and so on) target value (default to 60 if not set). At most one entry is allowed per metric. If machine_spec.accelerator_count is above 0, the autoscaling will be based on both CPU utilization and accelerator's duty cycle metrics and scale up when either metrics exceeds its target value while scale down if both metrics are under their target value. The default target value is 60 for both metrics. If machine_spec.accelerator_count is 0, the autoscaling will be based on CPU utilization metric only with default target value 60 if not explicitly set. For example, in the case of Online Prediction, if you want to override target CPU utilization to 80, you should set autoscaling_metric_specs.metric_name to `aiplatform.googleapis.com/prediction/online/cpu/utilization` and autoscaling_metric_specs.target to `80`.
        /// </summary>
        public readonly ImmutableArray<Outputs.GoogleCloudAiplatformV1beta1AutoscalingMetricSpecResponse> AutoscalingMetricSpecs;
        /// <summary>
        /// Immutable. The specification of a single machine used by the prediction.
        /// </summary>
        public readonly Outputs.GoogleCloudAiplatformV1beta1MachineSpecResponse MachineSpec;
        /// <summary>
        /// Immutable. The maximum number of replicas this DeployedModel may be deployed on when the traffic against it increases. If the requested value is too large, the deployment will error, but if deployment succeeds then the ability to scale the model to that many replicas is guaranteed (barring service outages). If traffic against the DeployedModel increases beyond what its replicas at maximum may handle, a portion of the traffic will be dropped. If this value is not provided, will use min_replica_count as the default value. The value of this field impacts the charge against Vertex CPU and GPU quotas. Specifically, you will be charged for (max_replica_count * number of cores in the selected machine type) and (max_replica_count * number of GPUs per replica in the selected machine type).
        /// </summary>
        public readonly int MaxReplicaCount;
        /// <summary>
        /// Immutable. The minimum number of machine replicas this DeployedModel will be always deployed on. This value must be greater than or equal to 1. If traffic against the DeployedModel increases, it may dynamically be deployed onto more replicas, and as traffic decreases, some of these extra replicas may be freed.
        /// </summary>
        public readonly int MinReplicaCount;

        [OutputConstructor]
        private GoogleCloudAiplatformV1beta1DedicatedResourcesResponse(
            ImmutableArray<Outputs.GoogleCloudAiplatformV1beta1AutoscalingMetricSpecResponse> autoscalingMetricSpecs,

            Outputs.GoogleCloudAiplatformV1beta1MachineSpecResponse machineSpec,

            int maxReplicaCount,

            int minReplicaCount)
        {
            AutoscalingMetricSpecs = autoscalingMetricSpecs;
            MachineSpec = machineSpec;
            MaxReplicaCount = maxReplicaCount;
            MinReplicaCount = minReplicaCount;
        }
    }
}
