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

__all__ = ['ExternalAccessRuleArgs', 'ExternalAccessRule']

@pulumi.input_type
class ExternalAccessRuleArgs:
    def __init__(__self__, *,
                 external_access_rule_id: pulumi.Input[str],
                 network_policy_id: pulumi.Input[str],
                 action: Optional[pulumi.Input['ExternalAccessRuleAction']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input['IpRangeArgs']]]] = None,
                 destination_ports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ip_protocol: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 source_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input['IpRangeArgs']]]] = None,
                 source_ports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ExternalAccessRule resource.
        :param pulumi.Input[str] external_access_rule_id: Required. The user-provided identifier of the `ExternalAccessRule` to be created. This identifier must be unique among `ExternalAccessRule` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: * Only contains 1-63 alphanumeric characters and hyphens * Begins with an alphabetical character * Ends with a non-hyphen character * Not formatted as a UUID * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)
        :param pulumi.Input['ExternalAccessRuleAction'] action: The action that the external access rule performs.
        :param pulumi.Input[str] description: User-provided description for this external access rule.
        :param pulumi.Input[Sequence[pulumi.Input['IpRangeArgs']]] destination_ip_ranges: If destination ranges are specified, the external access rule applies only to the traffic that has a destination IP address in these ranges. The specified IP addresses must have reserved external IP addresses in the scope of the parent network policy. To match all external IP addresses in the scope of the parent network policy, specify `0.0.0.0/0`. To match a specific external IP address, specify it using the `IpRange.external_address` property.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] destination_ports: A list of destination ports to which the external access rule applies. This field is only applicable for the UDP or TCP protocol. Each entry must be either an integer or a range. For example: `["22"]`, `["80","443"]`, or `["12345-12349"]`. To match all destination ports, specify `["0-65535"]`.
        :param pulumi.Input[str] ip_protocol: The IP protocol to which the external access rule applies. This value can be one of the following three protocol strings (not case-sensitive): `tcp`, `udp`, or `icmp`.
        :param pulumi.Input[int] priority: External access rule priority, which determines the external access rule to use when multiple rules apply. If multiple rules have the same priority, their ordering is non-deterministic. If specific ordering is required, assign unique priorities to enforce such ordering. The external access rule priority is an integer from 100 to 4096, both inclusive. Lower integers indicate higher precedence. For example, a rule with priority `100` has higher precedence than a rule with priority `101`.
        :param pulumi.Input[str] request_id: A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        :param pulumi.Input[Sequence[pulumi.Input['IpRangeArgs']]] source_ip_ranges: If source ranges are specified, the external access rule applies only to traffic that has a source IP address in these ranges. These ranges can either be expressed in the CIDR format or as an IP address. As only inbound rules are supported, `ExternalAddress` resources cannot be the source IP addresses of an external access rule. To match all source addresses, specify `0.0.0.0/0`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] source_ports: A list of source ports to which the external access rule applies. This field is only applicable for the UDP or TCP protocol. Each entry must be either an integer or a range. For example: `["22"]`, `["80","443"]`, or `["12345-12349"]`. To match all source ports, specify `["0-65535"]`.
        """
        pulumi.set(__self__, "external_access_rule_id", external_access_rule_id)
        pulumi.set(__self__, "network_policy_id", network_policy_id)
        if action is not None:
            pulumi.set(__self__, "action", action)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if destination_ip_ranges is not None:
            pulumi.set(__self__, "destination_ip_ranges", destination_ip_ranges)
        if destination_ports is not None:
            pulumi.set(__self__, "destination_ports", destination_ports)
        if ip_protocol is not None:
            pulumi.set(__self__, "ip_protocol", ip_protocol)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)
        if source_ip_ranges is not None:
            pulumi.set(__self__, "source_ip_ranges", source_ip_ranges)
        if source_ports is not None:
            pulumi.set(__self__, "source_ports", source_ports)

    @property
    @pulumi.getter(name="externalAccessRuleId")
    def external_access_rule_id(self) -> pulumi.Input[str]:
        """
        Required. The user-provided identifier of the `ExternalAccessRule` to be created. This identifier must be unique among `ExternalAccessRule` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: * Only contains 1-63 alphanumeric characters and hyphens * Begins with an alphabetical character * Ends with a non-hyphen character * Not formatted as a UUID * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)
        """
        return pulumi.get(self, "external_access_rule_id")

    @external_access_rule_id.setter
    def external_access_rule_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "external_access_rule_id", value)

    @property
    @pulumi.getter(name="networkPolicyId")
    def network_policy_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "network_policy_id")

    @network_policy_id.setter
    def network_policy_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_policy_id", value)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input['ExternalAccessRuleAction']]:
        """
        The action that the external access rule performs.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input['ExternalAccessRuleAction']]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        User-provided description for this external access rule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="destinationIpRanges")
    def destination_ip_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IpRangeArgs']]]]:
        """
        If destination ranges are specified, the external access rule applies only to the traffic that has a destination IP address in these ranges. The specified IP addresses must have reserved external IP addresses in the scope of the parent network policy. To match all external IP addresses in the scope of the parent network policy, specify `0.0.0.0/0`. To match a specific external IP address, specify it using the `IpRange.external_address` property.
        """
        return pulumi.get(self, "destination_ip_ranges")

    @destination_ip_ranges.setter
    def destination_ip_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IpRangeArgs']]]]):
        pulumi.set(self, "destination_ip_ranges", value)

    @property
    @pulumi.getter(name="destinationPorts")
    def destination_ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of destination ports to which the external access rule applies. This field is only applicable for the UDP or TCP protocol. Each entry must be either an integer or a range. For example: `["22"]`, `["80","443"]`, or `["12345-12349"]`. To match all destination ports, specify `["0-65535"]`.
        """
        return pulumi.get(self, "destination_ports")

    @destination_ports.setter
    def destination_ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "destination_ports", value)

    @property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The IP protocol to which the external access rule applies. This value can be one of the following three protocol strings (not case-sensitive): `tcp`, `udp`, or `icmp`.
        """
        return pulumi.get(self, "ip_protocol")

    @ip_protocol.setter
    def ip_protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_protocol", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        External access rule priority, which determines the external access rule to use when multiple rules apply. If multiple rules have the same priority, their ordering is non-deterministic. If specific ordering is required, assign unique priorities to enforce such ordering. The external access rule priority is an integer from 100 to 4096, both inclusive. Lower integers indicate higher precedence. For example, a rule with priority `100` has higher precedence than a rule with priority `101`.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> Optional[pulumi.Input[str]]:
        """
        A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        """
        return pulumi.get(self, "request_id")

    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_id", value)

    @property
    @pulumi.getter(name="sourceIpRanges")
    def source_ip_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IpRangeArgs']]]]:
        """
        If source ranges are specified, the external access rule applies only to traffic that has a source IP address in these ranges. These ranges can either be expressed in the CIDR format or as an IP address. As only inbound rules are supported, `ExternalAddress` resources cannot be the source IP addresses of an external access rule. To match all source addresses, specify `0.0.0.0/0`.
        """
        return pulumi.get(self, "source_ip_ranges")

    @source_ip_ranges.setter
    def source_ip_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IpRangeArgs']]]]):
        pulumi.set(self, "source_ip_ranges", value)

    @property
    @pulumi.getter(name="sourcePorts")
    def source_ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of source ports to which the external access rule applies. This field is only applicable for the UDP or TCP protocol. Each entry must be either an integer or a range. For example: `["22"]`, `["80","443"]`, or `["12345-12349"]`. To match all source ports, specify `["0-65535"]`.
        """
        return pulumi.get(self, "source_ports")

    @source_ports.setter
    def source_ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "source_ports", value)


class ExternalAccessRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input['ExternalAccessRuleAction']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpRangeArgs']]]]] = None,
                 destination_ports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 external_access_rule_id: Optional[pulumi.Input[str]] = None,
                 ip_protocol: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_policy_id: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 source_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpRangeArgs']]]]] = None,
                 source_ports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Creates a new external access rule in a given network policy.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['ExternalAccessRuleAction'] action: The action that the external access rule performs.
        :param pulumi.Input[str] description: User-provided description for this external access rule.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpRangeArgs']]]] destination_ip_ranges: If destination ranges are specified, the external access rule applies only to the traffic that has a destination IP address in these ranges. The specified IP addresses must have reserved external IP addresses in the scope of the parent network policy. To match all external IP addresses in the scope of the parent network policy, specify `0.0.0.0/0`. To match a specific external IP address, specify it using the `IpRange.external_address` property.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] destination_ports: A list of destination ports to which the external access rule applies. This field is only applicable for the UDP or TCP protocol. Each entry must be either an integer or a range. For example: `["22"]`, `["80","443"]`, or `["12345-12349"]`. To match all destination ports, specify `["0-65535"]`.
        :param pulumi.Input[str] external_access_rule_id: Required. The user-provided identifier of the `ExternalAccessRule` to be created. This identifier must be unique among `ExternalAccessRule` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: * Only contains 1-63 alphanumeric characters and hyphens * Begins with an alphabetical character * Ends with a non-hyphen character * Not formatted as a UUID * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)
        :param pulumi.Input[str] ip_protocol: The IP protocol to which the external access rule applies. This value can be one of the following three protocol strings (not case-sensitive): `tcp`, `udp`, or `icmp`.
        :param pulumi.Input[int] priority: External access rule priority, which determines the external access rule to use when multiple rules apply. If multiple rules have the same priority, their ordering is non-deterministic. If specific ordering is required, assign unique priorities to enforce such ordering. The external access rule priority is an integer from 100 to 4096, both inclusive. Lower integers indicate higher precedence. For example, a rule with priority `100` has higher precedence than a rule with priority `101`.
        :param pulumi.Input[str] request_id: A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpRangeArgs']]]] source_ip_ranges: If source ranges are specified, the external access rule applies only to traffic that has a source IP address in these ranges. These ranges can either be expressed in the CIDR format or as an IP address. As only inbound rules are supported, `ExternalAddress` resources cannot be the source IP addresses of an external access rule. To match all source addresses, specify `0.0.0.0/0`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] source_ports: A list of source ports to which the external access rule applies. This field is only applicable for the UDP or TCP protocol. Each entry must be either an integer or a range. For example: `["22"]`, `["80","443"]`, or `["12345-12349"]`. To match all source ports, specify `["0-65535"]`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExternalAccessRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new external access rule in a given network policy.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param ExternalAccessRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExternalAccessRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input['ExternalAccessRuleAction']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpRangeArgs']]]]] = None,
                 destination_ports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 external_access_rule_id: Optional[pulumi.Input[str]] = None,
                 ip_protocol: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_policy_id: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 source_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpRangeArgs']]]]] = None,
                 source_ports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExternalAccessRuleArgs.__new__(ExternalAccessRuleArgs)

            __props__.__dict__["action"] = action
            __props__.__dict__["description"] = description
            __props__.__dict__["destination_ip_ranges"] = destination_ip_ranges
            __props__.__dict__["destination_ports"] = destination_ports
            if external_access_rule_id is None and not opts.urn:
                raise TypeError("Missing required property 'external_access_rule_id'")
            __props__.__dict__["external_access_rule_id"] = external_access_rule_id
            __props__.__dict__["ip_protocol"] = ip_protocol
            __props__.__dict__["location"] = location
            if network_policy_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_policy_id'")
            __props__.__dict__["network_policy_id"] = network_policy_id
            __props__.__dict__["priority"] = priority
            __props__.__dict__["project"] = project
            __props__.__dict__["request_id"] = request_id
            __props__.__dict__["source_ip_ranges"] = source_ip_ranges
            __props__.__dict__["source_ports"] = source_ports
            __props__.__dict__["create_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["uid"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["externalAccessRuleId", "location", "networkPolicyId", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ExternalAccessRule, __self__).__init__(
            'google-native:vmwareengine/v1:ExternalAccessRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ExternalAccessRule':
        """
        Get an existing ExternalAccessRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ExternalAccessRuleArgs.__new__(ExternalAccessRuleArgs)

        __props__.__dict__["action"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["destination_ip_ranges"] = None
        __props__.__dict__["destination_ports"] = None
        __props__.__dict__["external_access_rule_id"] = None
        __props__.__dict__["ip_protocol"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_policy_id"] = None
        __props__.__dict__["priority"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["request_id"] = None
        __props__.__dict__["source_ip_ranges"] = None
        __props__.__dict__["source_ports"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["uid"] = None
        __props__.__dict__["update_time"] = None
        return ExternalAccessRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output[str]:
        """
        The action that the external access rule performs.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Creation time of this resource.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        User-provided description for this external access rule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destinationIpRanges")
    def destination_ip_ranges(self) -> pulumi.Output[Sequence['outputs.IpRangeResponse']]:
        """
        If destination ranges are specified, the external access rule applies only to the traffic that has a destination IP address in these ranges. The specified IP addresses must have reserved external IP addresses in the scope of the parent network policy. To match all external IP addresses in the scope of the parent network policy, specify `0.0.0.0/0`. To match a specific external IP address, specify it using the `IpRange.external_address` property.
        """
        return pulumi.get(self, "destination_ip_ranges")

    @property
    @pulumi.getter(name="destinationPorts")
    def destination_ports(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of destination ports to which the external access rule applies. This field is only applicable for the UDP or TCP protocol. Each entry must be either an integer or a range. For example: `["22"]`, `["80","443"]`, or `["12345-12349"]`. To match all destination ports, specify `["0-65535"]`.
        """
        return pulumi.get(self, "destination_ports")

    @property
    @pulumi.getter(name="externalAccessRuleId")
    def external_access_rule_id(self) -> pulumi.Output[str]:
        """
        Required. The user-provided identifier of the `ExternalAccessRule` to be created. This identifier must be unique among `ExternalAccessRule` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: * Only contains 1-63 alphanumeric characters and hyphens * Begins with an alphabetical character * Ends with a non-hyphen character * Not formatted as a UUID * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)
        """
        return pulumi.get(self, "external_access_rule_id")

    @property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> pulumi.Output[str]:
        """
        The IP protocol to which the external access rule applies. This value can be one of the following three protocol strings (not case-sensitive): `tcp`, `udp`, or `icmp`.
        """
        return pulumi.get(self, "ip_protocol")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of this external access rule. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1/networkPolicies/my-policy/externalAccessRules/my-rule`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkPolicyId")
    def network_policy_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "network_policy_id")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        External access rule priority, which determines the external access rule to use when multiple rules apply. If multiple rules have the same priority, their ordering is non-deterministic. If specific ordering is required, assign unique priorities to enforce such ordering. The external access rule priority is an integer from 100 to 4096, both inclusive. Lower integers indicate higher precedence. For example, a rule with priority `100` has higher precedence than a rule with priority `101`.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> pulumi.Output[Optional[str]]:
        """
        A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        """
        return pulumi.get(self, "request_id")

    @property
    @pulumi.getter(name="sourceIpRanges")
    def source_ip_ranges(self) -> pulumi.Output[Sequence['outputs.IpRangeResponse']]:
        """
        If source ranges are specified, the external access rule applies only to traffic that has a source IP address in these ranges. These ranges can either be expressed in the CIDR format or as an IP address. As only inbound rules are supported, `ExternalAddress` resources cannot be the source IP addresses of an external access rule. To match all source addresses, specify `0.0.0.0/0`.
        """
        return pulumi.get(self, "source_ip_ranges")

    @property
    @pulumi.getter(name="sourcePorts")
    def source_ports(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of source ports to which the external access rule applies. This field is only applicable for the UDP or TCP protocol. Each entry must be either an integer or a range. For example: `["22"]`, `["80","443"]`, or `["12345-12349"]`. To match all source ports, specify `["0-65535"]`.
        """
        return pulumi.get(self, "source_ports")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def uid(self) -> pulumi.Output[str]:
        """
        System-generated unique identifier for the resource.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Last update time of this resource.
        """
        return pulumi.get(self, "update_time")

