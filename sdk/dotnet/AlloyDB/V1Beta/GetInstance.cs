// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.AlloyDB.V1Beta
{
    public static class GetInstance
    {
        /// <summary>
        /// Gets details of a single Instance.
        /// </summary>
        public static Task<GetInstanceResult> InvokeAsync(GetInstanceArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetInstanceResult>("google-native:alloydb/v1beta:getInstance", args ?? new GetInstanceArgs(), options.WithDefaults());

        /// <summary>
        /// Gets details of a single Instance.
        /// </summary>
        public static Output<GetInstanceResult> Invoke(GetInstanceInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetInstanceResult>("google-native:alloydb/v1beta:getInstance", args ?? new GetInstanceInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetInstanceArgs : global::Pulumi.InvokeArgs
    {
        [Input("clusterId", required: true)]
        public string ClusterId { get; set; } = null!;

        [Input("instanceId", required: true)]
        public string InstanceId { get; set; } = null!;

        [Input("location", required: true)]
        public string Location { get; set; } = null!;

        [Input("project")]
        public string? Project { get; set; }

        [Input("view")]
        public string? View { get; set; }

        public GetInstanceArgs()
        {
        }
        public static new GetInstanceArgs Empty => new GetInstanceArgs();
    }

    public sealed class GetInstanceInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        [Input("instanceId", required: true)]
        public Input<string> InstanceId { get; set; } = null!;

        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("view")]
        public Input<string>? View { get; set; }

        public GetInstanceInvokeArgs()
        {
        }
        public static new GetInstanceInvokeArgs Empty => new GetInstanceInvokeArgs();
    }


    [OutputType]
    public sealed class GetInstanceResult
    {
        /// <summary>
        /// Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. https://google.aip.dev/128
        /// </summary>
        public readonly ImmutableDictionary<string, string> Annotations;
        /// <summary>
        /// Availability type of an Instance. If empty, defaults to REGIONAL for primary instances. For read pools, availability_type is always UNSPECIFIED. Instances in the read pools are evenly distributed across available zones within the region (i.e. read pools with more than one node will have a node in at least two zones).
        /// </summary>
        public readonly string AvailabilityType;
        /// <summary>
        /// Optional. Client connection specific configurations
        /// </summary>
        public readonly Outputs.ClientConnectionConfigResponse ClientConnectionConfig;
        /// <summary>
        /// Create time stamp
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// Database flags. Set at instance level. * They are copied from primary instance on read instance creation. * Read instances can set new or override existing flags that are relevant for reads, e.g. for enabling columnar cache on a read instance. Flags set on read instance may or may not be present on primary. This is a list of "key": "value" pairs. "key": The name of the flag. These flags are passed at instance setup time, so include both server options and system variables for Postgres. Flags are specified with underscores, not hyphens. "value": The value of the flag. Booleans are set to **on** for true and **off** for false. This field must be omitted if the flag doesn't take a value.
        /// </summary>
        public readonly ImmutableDictionary<string, string> DatabaseFlags;
        /// <summary>
        /// Delete time stamp
        /// </summary>
        public readonly string DeleteTime;
        /// <summary>
        /// User-settable and human-readable display name for the Instance.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// For Resource freshness validation (https://google.aip.dev/154)
        /// </summary>
        public readonly string Etag;
        /// <summary>
        /// The Compute Engine zone that the instance should serve from, per https://cloud.google.com/compute/docs/regions-zones This can ONLY be specified for ZONAL instances. If present for a REGIONAL instance, an error will be thrown. If this is absent for a ZONAL instance, instance is created in a random zone with available capacity.
        /// </summary>
        public readonly string GceZone;
        /// <summary>
        /// The type of the instance. Specified at creation time.
        /// </summary>
        public readonly string InstanceType;
        /// <summary>
        /// The IP address for the Instance. This is the connection endpoint for an end-user application.
        /// </summary>
        public readonly string IpAddress;
        /// <summary>
        /// Labels as key value pairs
        /// </summary>
        public readonly ImmutableDictionary<string, string> Labels;
        /// <summary>
        /// Configurations for the machines that host the underlying database engine.
        /// </summary>
        public readonly Outputs.MachineConfigResponse MachineConfig;
        /// <summary>
        /// The name of the instance resource with the format: * projects/{project}/locations/{region}/clusters/{cluster_id}/instances/{instance_id} where the cluster and instance ID segments should satisfy the regex expression `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`, e.g. 1-63 characters of lowercase letters, numbers, and dashes, starting with a letter, and ending with a letter or number. For more details see https://google.aip.dev/122. The prefix of the instance resource name is the name of the parent resource: * projects/{project}/locations/{region}/clusters/{cluster_id}
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// List of available read-only VMs in this instance, including the standby for a PRIMARY instance.
        /// </summary>
        public readonly ImmutableArray<Outputs.NodeResponse> Nodes;
        /// <summary>
        /// Configuration for query insights.
        /// </summary>
        public readonly Outputs.QueryInsightsInstanceConfigResponse QueryInsightsConfig;
        /// <summary>
        /// Read pool instance configuration. This is required if the value of instanceType is READ_POOL.
        /// </summary>
        public readonly Outputs.ReadPoolConfigResponse ReadPoolConfig;
        /// <summary>
        /// Reconciling (https://google.aip.dev/128#reconciliation). Set to true if the current state of Instance does not match the user's intended state, and the service is actively updating the resource to reconcile them. This can happen due to user-triggered updates or system actions like failover or maintenance.
        /// </summary>
        public readonly bool Reconciling;
        /// <summary>
        /// The current serving state of the instance.
        /// </summary>
        public readonly string State;
        /// <summary>
        /// The system-generated UID of the resource. The UID is assigned when the resource is created, and it is retained until it is deleted.
        /// </summary>
        public readonly string Uid;
        /// <summary>
        /// Update policy that will be applied during instance update. This field is not persisted when you update the instance. To use a non-default update policy, you must specify explicitly specify the value in each update request.
        /// </summary>
        public readonly Outputs.UpdatePolicyResponse UpdatePolicy;
        /// <summary>
        /// Update time stamp
        /// </summary>
        public readonly string UpdateTime;
        /// <summary>
        /// This is set for the read-write VM of the PRIMARY instance only.
        /// </summary>
        public readonly Outputs.NodeResponse WritableNode;

        [OutputConstructor]
        private GetInstanceResult(
            ImmutableDictionary<string, string> annotations,

            string availabilityType,

            Outputs.ClientConnectionConfigResponse clientConnectionConfig,

            string createTime,

            ImmutableDictionary<string, string> databaseFlags,

            string deleteTime,

            string displayName,

            string etag,

            string gceZone,

            string instanceType,

            string ipAddress,

            ImmutableDictionary<string, string> labels,

            Outputs.MachineConfigResponse machineConfig,

            string name,

            ImmutableArray<Outputs.NodeResponse> nodes,

            Outputs.QueryInsightsInstanceConfigResponse queryInsightsConfig,

            Outputs.ReadPoolConfigResponse readPoolConfig,

            bool reconciling,

            string state,

            string uid,

            Outputs.UpdatePolicyResponse updatePolicy,

            string updateTime,

            Outputs.NodeResponse writableNode)
        {
            Annotations = annotations;
            AvailabilityType = availabilityType;
            ClientConnectionConfig = clientConnectionConfig;
            CreateTime = createTime;
            DatabaseFlags = databaseFlags;
            DeleteTime = deleteTime;
            DisplayName = displayName;
            Etag = etag;
            GceZone = gceZone;
            InstanceType = instanceType;
            IpAddress = ipAddress;
            Labels = labels;
            MachineConfig = machineConfig;
            Name = name;
            Nodes = nodes;
            QueryInsightsConfig = queryInsightsConfig;
            ReadPoolConfig = readPoolConfig;
            Reconciling = reconciling;
            State = state;
            Uid = uid;
            UpdatePolicy = updatePolicy;
            UpdateTime = updateTime;
            WritableNode = writableNode;
        }
    }
}
