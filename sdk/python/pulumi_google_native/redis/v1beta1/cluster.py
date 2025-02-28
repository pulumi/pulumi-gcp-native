# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['ClusterArgs', 'Cluster']

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 psc_configs: pulumi.Input[Sequence[pulumi.Input['PscConfigArgs']]],
                 shard_count: pulumi.Input[int],
                 authorization_mode: Optional[pulumi.Input['ClusterAuthorizationMode']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 replica_count: Optional[pulumi.Input[int]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 transit_encryption_mode: Optional[pulumi.Input['ClusterTransitEncryptionMode']] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param pulumi.Input[str] cluster_id: Required. The logical name of the Redis cluster in the customer project with the following restrictions: * Must contain only lowercase letters, numbers, and hyphens. * Must start with a letter. * Must be between 1-63 characters. * Must end with a number or a letter. * Must be unique within the customer project / location
        :param pulumi.Input[Sequence[pulumi.Input['PscConfigArgs']]] psc_configs: Each PscConfig configures the consumer network where IPs will be designated to the cluster for client access through Private Service Connect Automation. Currently, only one PscConfig is supported.
        :param pulumi.Input[int] shard_count: Number of shards for the Redis cluster.
        :param pulumi.Input['ClusterAuthorizationMode'] authorization_mode: Optional. The authorization mode of the Redis cluster. If not provided, auth feature is disabled for the cluster.
        :param pulumi.Input[str] name: Unique name of the resource in this scope including project and location using the form: `projects/{project_id}/locations/{location_id}/clusters/{cluster_id}`
        :param pulumi.Input[int] replica_count: Optional. The number of replica nodes per shard.
        :param pulumi.Input[str] request_id: Idempotent request UUID.
        :param pulumi.Input['ClusterTransitEncryptionMode'] transit_encryption_mode: Optional. The in-transit encryption for the Redis cluster. If not provided, encryption is disabled for the cluster.
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "psc_configs", psc_configs)
        pulumi.set(__self__, "shard_count", shard_count)
        if authorization_mode is not None:
            pulumi.set(__self__, "authorization_mode", authorization_mode)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if replica_count is not None:
            pulumi.set(__self__, "replica_count", replica_count)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)
        if transit_encryption_mode is not None:
            pulumi.set(__self__, "transit_encryption_mode", transit_encryption_mode)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        Required. The logical name of the Redis cluster in the customer project with the following restrictions: * Must contain only lowercase letters, numbers, and hyphens. * Must start with a letter. * Must be between 1-63 characters. * Must end with a number or a letter. * Must be unique within the customer project / location
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="pscConfigs")
    def psc_configs(self) -> pulumi.Input[Sequence[pulumi.Input['PscConfigArgs']]]:
        """
        Each PscConfig configures the consumer network where IPs will be designated to the cluster for client access through Private Service Connect Automation. Currently, only one PscConfig is supported.
        """
        return pulumi.get(self, "psc_configs")

    @psc_configs.setter
    def psc_configs(self, value: pulumi.Input[Sequence[pulumi.Input['PscConfigArgs']]]):
        pulumi.set(self, "psc_configs", value)

    @property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> pulumi.Input[int]:
        """
        Number of shards for the Redis cluster.
        """
        return pulumi.get(self, "shard_count")

    @shard_count.setter
    def shard_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "shard_count", value)

    @property
    @pulumi.getter(name="authorizationMode")
    def authorization_mode(self) -> Optional[pulumi.Input['ClusterAuthorizationMode']]:
        """
        Optional. The authorization mode of the Redis cluster. If not provided, auth feature is disabled for the cluster.
        """
        return pulumi.get(self, "authorization_mode")

    @authorization_mode.setter
    def authorization_mode(self, value: Optional[pulumi.Input['ClusterAuthorizationMode']]):
        pulumi.set(self, "authorization_mode", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Unique name of the resource in this scope including project and location using the form: `projects/{project_id}/locations/{location_id}/clusters/{cluster_id}`
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[pulumi.Input[int]]:
        """
        Optional. The number of replica nodes per shard.
        """
        return pulumi.get(self, "replica_count")

    @replica_count.setter
    def replica_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "replica_count", value)

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> Optional[pulumi.Input[str]]:
        """
        Idempotent request UUID.
        """
        return pulumi.get(self, "request_id")

    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_id", value)

    @property
    @pulumi.getter(name="transitEncryptionMode")
    def transit_encryption_mode(self) -> Optional[pulumi.Input['ClusterTransitEncryptionMode']]:
        """
        Optional. The in-transit encryption for the Redis cluster. If not provided, encryption is disabled for the cluster.
        """
        return pulumi.get(self, "transit_encryption_mode")

    @transit_encryption_mode.setter
    def transit_encryption_mode(self, value: Optional[pulumi.Input['ClusterTransitEncryptionMode']]):
        pulumi.set(self, "transit_encryption_mode", value)


class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_mode: Optional[pulumi.Input['ClusterAuthorizationMode']] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 psc_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PscConfigArgs']]]]] = None,
                 replica_count: Optional[pulumi.Input[int]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 shard_count: Optional[pulumi.Input[int]] = None,
                 transit_encryption_mode: Optional[pulumi.Input['ClusterTransitEncryptionMode']] = None,
                 __props__=None):
        """
        Creates a Redis cluster based on the specified properties. The creation is executed asynchronously and callers may check the returned operation to track its progress. Once the operation is completed the Redis cluster will be fully functional. The completed longrunning.Operation will contain the new cluster object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['ClusterAuthorizationMode'] authorization_mode: Optional. The authorization mode of the Redis cluster. If not provided, auth feature is disabled for the cluster.
        :param pulumi.Input[str] cluster_id: Required. The logical name of the Redis cluster in the customer project with the following restrictions: * Must contain only lowercase letters, numbers, and hyphens. * Must start with a letter. * Must be between 1-63 characters. * Must end with a number or a letter. * Must be unique within the customer project / location
        :param pulumi.Input[str] name: Unique name of the resource in this scope including project and location using the form: `projects/{project_id}/locations/{location_id}/clusters/{cluster_id}`
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PscConfigArgs']]]] psc_configs: Each PscConfig configures the consumer network where IPs will be designated to the cluster for client access through Private Service Connect Automation. Currently, only one PscConfig is supported.
        :param pulumi.Input[int] replica_count: Optional. The number of replica nodes per shard.
        :param pulumi.Input[str] request_id: Idempotent request UUID.
        :param pulumi.Input[int] shard_count: Number of shards for the Redis cluster.
        :param pulumi.Input['ClusterTransitEncryptionMode'] transit_encryption_mode: Optional. The in-transit encryption for the Redis cluster. If not provided, encryption is disabled for the cluster.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a Redis cluster based on the specified properties. The creation is executed asynchronously and callers may check the returned operation to track its progress. Once the operation is completed the Redis cluster will be fully functional. The completed longrunning.Operation will contain the new cluster object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

        :param str resource_name: The name of the resource.
        :param ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_mode: Optional[pulumi.Input['ClusterAuthorizationMode']] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 psc_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PscConfigArgs']]]]] = None,
                 replica_count: Optional[pulumi.Input[int]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 shard_count: Optional[pulumi.Input[int]] = None,
                 transit_encryption_mode: Optional[pulumi.Input['ClusterTransitEncryptionMode']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterArgs.__new__(ClusterArgs)

            __props__.__dict__["authorization_mode"] = authorization_mode
            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            if psc_configs is None and not opts.urn:
                raise TypeError("Missing required property 'psc_configs'")
            __props__.__dict__["psc_configs"] = psc_configs
            __props__.__dict__["replica_count"] = replica_count
            __props__.__dict__["request_id"] = request_id
            if shard_count is None and not opts.urn:
                raise TypeError("Missing required property 'shard_count'")
            __props__.__dict__["shard_count"] = shard_count
            __props__.__dict__["transit_encryption_mode"] = transit_encryption_mode
            __props__.__dict__["create_time"] = None
            __props__.__dict__["discovery_endpoints"] = None
            __props__.__dict__["psc_connections"] = None
            __props__.__dict__["size_gb"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["state_info"] = None
            __props__.__dict__["uid"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["clusterId", "location", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Cluster, __self__).__init__(
            'google-native:redis/v1beta1:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ClusterArgs.__new__(ClusterArgs)

        __props__.__dict__["authorization_mode"] = None
        __props__.__dict__["cluster_id"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["discovery_endpoints"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["psc_configs"] = None
        __props__.__dict__["psc_connections"] = None
        __props__.__dict__["replica_count"] = None
        __props__.__dict__["request_id"] = None
        __props__.__dict__["shard_count"] = None
        __props__.__dict__["size_gb"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["state_info"] = None
        __props__.__dict__["transit_encryption_mode"] = None
        __props__.__dict__["uid"] = None
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authorizationMode")
    def authorization_mode(self) -> pulumi.Output[str]:
        """
        Optional. The authorization mode of the Redis cluster. If not provided, auth feature is disabled for the cluster.
        """
        return pulumi.get(self, "authorization_mode")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        Required. The logical name of the Redis cluster in the customer project with the following restrictions: * Must contain only lowercase letters, numbers, and hyphens. * Must start with a letter. * Must be between 1-63 characters. * Must end with a number or a letter. * Must be unique within the customer project / location
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The timestamp associated with the cluster creation request.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="discoveryEndpoints")
    def discovery_endpoints(self) -> pulumi.Output[Sequence['outputs.DiscoveryEndpointResponse']]:
        """
        Endpoints created on each given network, for Redis clients to connect to the cluster. Currently only one discovery endpoint is supported.
        """
        return pulumi.get(self, "discovery_endpoints")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Unique name of the resource in this scope including project and location using the form: `projects/{project_id}/locations/{location_id}/clusters/{cluster_id}`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="pscConfigs")
    def psc_configs(self) -> pulumi.Output[Sequence['outputs.PscConfigResponse']]:
        """
        Each PscConfig configures the consumer network where IPs will be designated to the cluster for client access through Private Service Connect Automation. Currently, only one PscConfig is supported.
        """
        return pulumi.get(self, "psc_configs")

    @property
    @pulumi.getter(name="pscConnections")
    def psc_connections(self) -> pulumi.Output[Sequence['outputs.PscConnectionResponse']]:
        """
        PSC connections for discovery of the cluster topology and accessing the cluster.
        """
        return pulumi.get(self, "psc_connections")

    @property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> pulumi.Output[int]:
        """
        Optional. The number of replica nodes per shard.
        """
        return pulumi.get(self, "replica_count")

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> pulumi.Output[Optional[str]]:
        """
        Idempotent request UUID.
        """
        return pulumi.get(self, "request_id")

    @property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> pulumi.Output[int]:
        """
        Number of shards for the Redis cluster.
        """
        return pulumi.get(self, "shard_count")

    @property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> pulumi.Output[int]:
        """
        Redis memory size in GB for the entire cluster.
        """
        return pulumi.get(self, "size_gb")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of this cluster. Can be CREATING, READY, UPDATING, DELETING and SUSPENDED
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="stateInfo")
    def state_info(self) -> pulumi.Output['outputs.StateInfoResponse']:
        """
        Additional information about the current state of the cluster.
        """
        return pulumi.get(self, "state_info")

    @property
    @pulumi.getter(name="transitEncryptionMode")
    def transit_encryption_mode(self) -> pulumi.Output[str]:
        """
        Optional. The in-transit encryption for the Redis cluster. If not provided, encryption is disabled for the cluster.
        """
        return pulumi.get(self, "transit_encryption_mode")

    @property
    @pulumi.getter
    def uid(self) -> pulumi.Output[str]:
        """
        System assigned, unique identifier for the cluster.
        """
        return pulumi.get(self, "uid")

