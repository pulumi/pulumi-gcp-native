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

__all__ = ['SecurityActionArgs', 'SecurityAction']

@pulumi.input_type
class SecurityActionArgs:
    def __init__(__self__, *,
                 condition_config: pulumi.Input['GoogleCloudApigeeV1SecurityActionConditionConfigArgs'],
                 environment_id: pulumi.Input[str],
                 organization_id: pulumi.Input[str],
                 security_action_id: pulumi.Input[str],
                 state: pulumi.Input['SecurityActionState'],
                 allow: Optional[pulumi.Input['GoogleCloudApigeeV1SecurityActionAllowArgs']] = None,
                 deny: Optional[pulumi.Input['GoogleCloudApigeeV1SecurityActionDenyArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expire_time: Optional[pulumi.Input[str]] = None,
                 flag: Optional[pulumi.Input['GoogleCloudApigeeV1SecurityActionFlagArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SecurityAction resource.
        :param pulumi.Input['GoogleCloudApigeeV1SecurityActionConditionConfigArgs'] condition_config: A valid SecurityAction must contain at least one condition.
        :param pulumi.Input[str] security_action_id: Required. The ID to use for the SecurityAction, which will become the final component of the action's resource name. This value should be 0-61 characters, and valid format is (^[a-z]([a-z0-9-]{​0,61}[a-z0-9])?$).
        :param pulumi.Input['SecurityActionState'] state: Only an ENABLED SecurityAction is enforced. An ENABLED SecurityAction past its expiration time will not be enforced.
        :param pulumi.Input['GoogleCloudApigeeV1SecurityActionAllowArgs'] allow: Allow a request through if it matches this SecurityAction.
        :param pulumi.Input['GoogleCloudApigeeV1SecurityActionDenyArgs'] deny: Deny a request through if it matches this SecurityAction.
        :param pulumi.Input[str] description: Optional. An optional user provided description of the SecurityAction.
        :param pulumi.Input[str] expire_time: The expiration for this SecurityAction.
        :param pulumi.Input['GoogleCloudApigeeV1SecurityActionFlagArgs'] flag: Flag a request through if it matches this SecurityAction.
        :param pulumi.Input[str] name: Immutable. This field is ignored during creation as per AIP-133. Please set the `security_action_id` field in the CreateSecurityActionRequest when creating a new SecurityAction. Format: organizations/{org}/environments/{env}/securityActions/{security_action}
        :param pulumi.Input[str] ttl: Input only. The TTL for this SecurityAction.
        """
        pulumi.set(__self__, "condition_config", condition_config)
        pulumi.set(__self__, "environment_id", environment_id)
        pulumi.set(__self__, "organization_id", organization_id)
        pulumi.set(__self__, "security_action_id", security_action_id)
        pulumi.set(__self__, "state", state)
        if allow is not None:
            pulumi.set(__self__, "allow", allow)
        if deny is not None:
            pulumi.set(__self__, "deny", deny)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if expire_time is not None:
            pulumi.set(__self__, "expire_time", expire_time)
        if flag is not None:
            pulumi.set(__self__, "flag", flag)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)

    @property
    @pulumi.getter(name="conditionConfig")
    def condition_config(self) -> pulumi.Input['GoogleCloudApigeeV1SecurityActionConditionConfigArgs']:
        """
        A valid SecurityAction must contain at least one condition.
        """
        return pulumi.get(self, "condition_config")

    @condition_config.setter
    def condition_config(self, value: pulumi.Input['GoogleCloudApigeeV1SecurityActionConditionConfigArgs']):
        pulumi.set(self, "condition_config", value)

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "environment_id")

    @environment_id.setter
    def environment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment_id", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter(name="securityActionId")
    def security_action_id(self) -> pulumi.Input[str]:
        """
        Required. The ID to use for the SecurityAction, which will become the final component of the action's resource name. This value should be 0-61 characters, and valid format is (^[a-z]([a-z0-9-]{​0,61}[a-z0-9])?$).
        """
        return pulumi.get(self, "security_action_id")

    @security_action_id.setter
    def security_action_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "security_action_id", value)

    @property
    @pulumi.getter
    def state(self) -> pulumi.Input['SecurityActionState']:
        """
        Only an ENABLED SecurityAction is enforced. An ENABLED SecurityAction past its expiration time will not be enforced.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: pulumi.Input['SecurityActionState']):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def allow(self) -> Optional[pulumi.Input['GoogleCloudApigeeV1SecurityActionAllowArgs']]:
        """
        Allow a request through if it matches this SecurityAction.
        """
        return pulumi.get(self, "allow")

    @allow.setter
    def allow(self, value: Optional[pulumi.Input['GoogleCloudApigeeV1SecurityActionAllowArgs']]):
        pulumi.set(self, "allow", value)

    @property
    @pulumi.getter
    def deny(self) -> Optional[pulumi.Input['GoogleCloudApigeeV1SecurityActionDenyArgs']]:
        """
        Deny a request through if it matches this SecurityAction.
        """
        return pulumi.get(self, "deny")

    @deny.setter
    def deny(self, value: Optional[pulumi.Input['GoogleCloudApigeeV1SecurityActionDenyArgs']]):
        pulumi.set(self, "deny", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. An optional user provided description of the SecurityAction.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[str]]:
        """
        The expiration for this SecurityAction.
        """
        return pulumi.get(self, "expire_time")

    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expire_time", value)

    @property
    @pulumi.getter
    def flag(self) -> Optional[pulumi.Input['GoogleCloudApigeeV1SecurityActionFlagArgs']]:
        """
        Flag a request through if it matches this SecurityAction.
        """
        return pulumi.get(self, "flag")

    @flag.setter
    def flag(self, value: Optional[pulumi.Input['GoogleCloudApigeeV1SecurityActionFlagArgs']]):
        pulumi.set(self, "flag", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. This field is ignored during creation as per AIP-133. Please set the `security_action_id` field in the CreateSecurityActionRequest when creating a new SecurityAction. Format: organizations/{org}/environments/{env}/securityActions/{security_action}
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[str]]:
        """
        Input only. The TTL for this SecurityAction.
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ttl", value)


class SecurityAction(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow: Optional[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1SecurityActionAllowArgs']]] = None,
                 condition_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1SecurityActionConditionConfigArgs']]] = None,
                 deny: Optional[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1SecurityActionDenyArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment_id: Optional[pulumi.Input[str]] = None,
                 expire_time: Optional[pulumi.Input[str]] = None,
                 flag: Optional[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1SecurityActionFlagArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 security_action_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input['SecurityActionState']] = None,
                 ttl: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        CreateSecurityAction creates a SecurityAction.
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1SecurityActionAllowArgs']] allow: Allow a request through if it matches this SecurityAction.
        :param pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1SecurityActionConditionConfigArgs']] condition_config: A valid SecurityAction must contain at least one condition.
        :param pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1SecurityActionDenyArgs']] deny: Deny a request through if it matches this SecurityAction.
        :param pulumi.Input[str] description: Optional. An optional user provided description of the SecurityAction.
        :param pulumi.Input[str] expire_time: The expiration for this SecurityAction.
        :param pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1SecurityActionFlagArgs']] flag: Flag a request through if it matches this SecurityAction.
        :param pulumi.Input[str] name: Immutable. This field is ignored during creation as per AIP-133. Please set the `security_action_id` field in the CreateSecurityActionRequest when creating a new SecurityAction. Format: organizations/{org}/environments/{env}/securityActions/{security_action}
        :param pulumi.Input[str] security_action_id: Required. The ID to use for the SecurityAction, which will become the final component of the action's resource name. This value should be 0-61 characters, and valid format is (^[a-z]([a-z0-9-]{​0,61}[a-z0-9])?$).
        :param pulumi.Input['SecurityActionState'] state: Only an ENABLED SecurityAction is enforced. An ENABLED SecurityAction past its expiration time will not be enforced.
        :param pulumi.Input[str] ttl: Input only. The TTL for this SecurityAction.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecurityActionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        CreateSecurityAction creates a SecurityAction.
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param SecurityActionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecurityActionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow: Optional[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1SecurityActionAllowArgs']]] = None,
                 condition_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1SecurityActionConditionConfigArgs']]] = None,
                 deny: Optional[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1SecurityActionDenyArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment_id: Optional[pulumi.Input[str]] = None,
                 expire_time: Optional[pulumi.Input[str]] = None,
                 flag: Optional[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1SecurityActionFlagArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 security_action_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input['SecurityActionState']] = None,
                 ttl: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecurityActionArgs.__new__(SecurityActionArgs)

            __props__.__dict__["allow"] = allow
            if condition_config is None and not opts.urn:
                raise TypeError("Missing required property 'condition_config'")
            __props__.__dict__["condition_config"] = condition_config
            __props__.__dict__["deny"] = deny
            __props__.__dict__["description"] = description
            if environment_id is None and not opts.urn:
                raise TypeError("Missing required property 'environment_id'")
            __props__.__dict__["environment_id"] = environment_id
            __props__.__dict__["expire_time"] = expire_time
            __props__.__dict__["flag"] = flag
            __props__.__dict__["name"] = name
            if organization_id is None and not opts.urn:
                raise TypeError("Missing required property 'organization_id'")
            __props__.__dict__["organization_id"] = organization_id
            if security_action_id is None and not opts.urn:
                raise TypeError("Missing required property 'security_action_id'")
            __props__.__dict__["security_action_id"] = security_action_id
            if state is None and not opts.urn:
                raise TypeError("Missing required property 'state'")
            __props__.__dict__["state"] = state
            __props__.__dict__["ttl"] = ttl
            __props__.__dict__["create_time"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["environmentId", "organizationId", "securityActionId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(SecurityAction, __self__).__init__(
            'google-native:apigee/v1:SecurityAction',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SecurityAction':
        """
        Get an existing SecurityAction resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SecurityActionArgs.__new__(SecurityActionArgs)

        __props__.__dict__["allow"] = None
        __props__.__dict__["condition_config"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["deny"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["environment_id"] = None
        __props__.__dict__["expire_time"] = None
        __props__.__dict__["flag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["organization_id"] = None
        __props__.__dict__["security_action_id"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["ttl"] = None
        __props__.__dict__["update_time"] = None
        return SecurityAction(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def allow(self) -> pulumi.Output['outputs.GoogleCloudApigeeV1SecurityActionAllowResponse']:
        """
        Allow a request through if it matches this SecurityAction.
        """
        return pulumi.get(self, "allow")

    @property
    @pulumi.getter(name="conditionConfig")
    def condition_config(self) -> pulumi.Output['outputs.GoogleCloudApigeeV1SecurityActionConditionConfigResponse']:
        """
        A valid SecurityAction must contain at least one condition.
        """
        return pulumi.get(self, "condition_config")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The create time for this SecurityAction.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def deny(self) -> pulumi.Output['outputs.GoogleCloudApigeeV1SecurityActionDenyResponse']:
        """
        Deny a request through if it matches this SecurityAction.
        """
        return pulumi.get(self, "deny")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Optional. An optional user provided description of the SecurityAction.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "environment_id")

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[str]:
        """
        The expiration for this SecurityAction.
        """
        return pulumi.get(self, "expire_time")

    @property
    @pulumi.getter
    def flag(self) -> pulumi.Output['outputs.GoogleCloudApigeeV1SecurityActionFlagResponse']:
        """
        Flag a request through if it matches this SecurityAction.
        """
        return pulumi.get(self, "flag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Immutable. This field is ignored during creation as per AIP-133. Please set the `security_action_id` field in the CreateSecurityActionRequest when creating a new SecurityAction. Format: organizations/{org}/environments/{env}/securityActions/{security_action}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="securityActionId")
    def security_action_id(self) -> pulumi.Output[str]:
        """
        Required. The ID to use for the SecurityAction, which will become the final component of the action's resource name. This value should be 0-61 characters, and valid format is (^[a-z]([a-z0-9-]{​0,61}[a-z0-9])?$).
        """
        return pulumi.get(self, "security_action_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Only an ENABLED SecurityAction is enforced. An ENABLED SecurityAction past its expiration time will not be enforced.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[str]:
        """
        Input only. The TTL for this SecurityAction.
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The update time for this SecurityAction. This reflects when this SecurityAction changed states.
        """
        return pulumi.get(self, "update_time")

