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
from ._inputs import *

__all__ = ['RolloutArgs', 'Rollout']

@pulumi.input_type
class RolloutArgs:
    def __init__(__self__, *,
                 service_name: pulumi.Input[str],
                 create_time: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 delete_service_strategy: Optional[pulumi.Input['DeleteServiceStrategyArgs']] = None,
                 rollout_id: Optional[pulumi.Input[str]] = None,
                 traffic_percent_strategy: Optional[pulumi.Input['TrafficPercentStrategyArgs']] = None):
        """
        The set of arguments for constructing a Rollout resource.
        :param pulumi.Input[str] service_name: The name of the service associated with this Rollout.
        :param pulumi.Input[str] create_time: Creation time of the rollout. Readonly.
        :param pulumi.Input[str] created_by: The user who created the Rollout. Readonly.
        :param pulumi.Input['DeleteServiceStrategyArgs'] delete_service_strategy: The strategy associated with a rollout to delete a `ManagedService`. Readonly.
        :param pulumi.Input[str] rollout_id: Optional. Unique identifier of this Rollout. Must be no longer than 63 characters and only lower case letters, digits, '.', '_' and '-' are allowed. If not specified by client, the server will generate one. The generated id will have the form of , where "date" is the create date in ISO 8601 format. "revision number" is a monotonically increasing positive number that is reset every day for each service. An example of the generated rollout_id is '2016-02-16r1'
        :param pulumi.Input['TrafficPercentStrategyArgs'] traffic_percent_strategy: Google Service Control selects service configurations based on traffic percentage.
        """
        pulumi.set(__self__, "service_name", service_name)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if delete_service_strategy is not None:
            pulumi.set(__self__, "delete_service_strategy", delete_service_strategy)
        if rollout_id is not None:
            pulumi.set(__self__, "rollout_id", rollout_id)
        if traffic_percent_strategy is not None:
            pulumi.set(__self__, "traffic_percent_strategy", traffic_percent_strategy)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the service associated with this Rollout.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Creation time of the rollout. Readonly.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        """
        The user who created the Rollout. Readonly.
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter(name="deleteServiceStrategy")
    def delete_service_strategy(self) -> Optional[pulumi.Input['DeleteServiceStrategyArgs']]:
        """
        The strategy associated with a rollout to delete a `ManagedService`. Readonly.
        """
        return pulumi.get(self, "delete_service_strategy")

    @delete_service_strategy.setter
    def delete_service_strategy(self, value: Optional[pulumi.Input['DeleteServiceStrategyArgs']]):
        pulumi.set(self, "delete_service_strategy", value)

    @property
    @pulumi.getter(name="rolloutId")
    def rollout_id(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Unique identifier of this Rollout. Must be no longer than 63 characters and only lower case letters, digits, '.', '_' and '-' are allowed. If not specified by client, the server will generate one. The generated id will have the form of , where "date" is the create date in ISO 8601 format. "revision number" is a monotonically increasing positive number that is reset every day for each service. An example of the generated rollout_id is '2016-02-16r1'
        """
        return pulumi.get(self, "rollout_id")

    @rollout_id.setter
    def rollout_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rollout_id", value)

    @property
    @pulumi.getter(name="trafficPercentStrategy")
    def traffic_percent_strategy(self) -> Optional[pulumi.Input['TrafficPercentStrategyArgs']]:
        """
        Google Service Control selects service configurations based on traffic percentage.
        """
        return pulumi.get(self, "traffic_percent_strategy")

    @traffic_percent_strategy.setter
    def traffic_percent_strategy(self, value: Optional[pulumi.Input['TrafficPercentStrategyArgs']]):
        pulumi.set(self, "traffic_percent_strategy", value)


class Rollout(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 delete_service_strategy: Optional[pulumi.Input[pulumi.InputType['DeleteServiceStrategyArgs']]] = None,
                 rollout_id: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 traffic_percent_strategy: Optional[pulumi.Input[pulumi.InputType['TrafficPercentStrategyArgs']]] = None,
                 __props__=None):
        """
        Creates a new service configuration rollout. Based on rollout, the Google Service Management will roll out the service configurations to different backend services. For example, the logging configuration will be pushed to Google Cloud Logging. Please note that any previous pending and running Rollouts and associated Operations will be automatically cancelled so that the latest Rollout will not be blocked by previous Rollouts. Only the 100 most recent (in any state) and the last 10 successful (if not already part of the set of 100 most recent) rollouts are kept for each service. The rest will be deleted eventually. Operation
        Auto-naming is currently not supported for this resource.
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: Creation time of the rollout. Readonly.
        :param pulumi.Input[str] created_by: The user who created the Rollout. Readonly.
        :param pulumi.Input[pulumi.InputType['DeleteServiceStrategyArgs']] delete_service_strategy: The strategy associated with a rollout to delete a `ManagedService`. Readonly.
        :param pulumi.Input[str] rollout_id: Optional. Unique identifier of this Rollout. Must be no longer than 63 characters and only lower case letters, digits, '.', '_' and '-' are allowed. If not specified by client, the server will generate one. The generated id will have the form of , where "date" is the create date in ISO 8601 format. "revision number" is a monotonically increasing positive number that is reset every day for each service. An example of the generated rollout_id is '2016-02-16r1'
        :param pulumi.Input[str] service_name: The name of the service associated with this Rollout.
        :param pulumi.Input[pulumi.InputType['TrafficPercentStrategyArgs']] traffic_percent_strategy: Google Service Control selects service configurations based on traffic percentage.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RolloutArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new service configuration rollout. Based on rollout, the Google Service Management will roll out the service configurations to different backend services. For example, the logging configuration will be pushed to Google Cloud Logging. Please note that any previous pending and running Rollouts and associated Operations will be automatically cancelled so that the latest Rollout will not be blocked by previous Rollouts. Only the 100 most recent (in any state) and the last 10 successful (if not already part of the set of 100 most recent) rollouts are kept for each service. The rest will be deleted eventually. Operation
        Auto-naming is currently not supported for this resource.
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param RolloutArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RolloutArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 delete_service_strategy: Optional[pulumi.Input[pulumi.InputType['DeleteServiceStrategyArgs']]] = None,
                 rollout_id: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 traffic_percent_strategy: Optional[pulumi.Input[pulumi.InputType['TrafficPercentStrategyArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RolloutArgs.__new__(RolloutArgs)

            __props__.__dict__["create_time"] = create_time
            __props__.__dict__["created_by"] = created_by
            __props__.__dict__["delete_service_strategy"] = delete_service_strategy
            __props__.__dict__["rollout_id"] = rollout_id
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["traffic_percent_strategy"] = traffic_percent_strategy
            __props__.__dict__["status"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["serviceName"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Rollout, __self__).__init__(
            'google-native:servicemanagement/v1:Rollout',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Rollout':
        """
        Get an existing Rollout resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RolloutArgs.__new__(RolloutArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["created_by"] = None
        __props__.__dict__["delete_service_strategy"] = None
        __props__.__dict__["rollout_id"] = None
        __props__.__dict__["service_name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["traffic_percent_strategy"] = None
        return Rollout(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Creation time of the rollout. Readonly.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[str]:
        """
        The user who created the Rollout. Readonly.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="deleteServiceStrategy")
    def delete_service_strategy(self) -> pulumi.Output['outputs.DeleteServiceStrategyResponse']:
        """
        The strategy associated with a rollout to delete a `ManagedService`. Readonly.
        """
        return pulumi.get(self, "delete_service_strategy")

    @property
    @pulumi.getter(name="rolloutId")
    def rollout_id(self) -> pulumi.Output[str]:
        """
        Optional. Unique identifier of this Rollout. Must be no longer than 63 characters and only lower case letters, digits, '.', '_' and '-' are allowed. If not specified by client, the server will generate one. The generated id will have the form of , where "date" is the create date in ISO 8601 format. "revision number" is a monotonically increasing positive number that is reset every day for each service. An example of the generated rollout_id is '2016-02-16r1'
        """
        return pulumi.get(self, "rollout_id")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of this rollout. Readonly. In case of a failed rollout, the system will automatically rollback to the current Rollout version. Readonly.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="trafficPercentStrategy")
    def traffic_percent_strategy(self) -> pulumi.Output['outputs.TrafficPercentStrategyResponse']:
        """
        Google Service Control selects service configurations based on traffic percentage.
        """
        return pulumi.get(self, "traffic_percent_strategy")

