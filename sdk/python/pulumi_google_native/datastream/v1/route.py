# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['RouteArgs', 'Route']

@pulumi.input_type
class RouteArgs:
    def __init__(__self__, *,
                 destination_address: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 private_connection_id: pulumi.Input[str],
                 route_id: pulumi.Input[str],
                 destination_port: Optional[pulumi.Input[int]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Route resource.
        :param pulumi.Input[str] destination_address: Destination address for connection
        :param pulumi.Input[str] display_name: Display name.
        :param pulumi.Input[str] route_id: Required. The Route identifier.
        :param pulumi.Input[int] destination_port: Destination port for connection
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels.
        :param pulumi.Input[str] request_id: Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        """
        pulumi.set(__self__, "destination_address", destination_address)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "private_connection_id", private_connection_id)
        pulumi.set(__self__, "route_id", route_id)
        if destination_port is not None:
            pulumi.set(__self__, "destination_port", destination_port)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)

    @property
    @pulumi.getter(name="destinationAddress")
    def destination_address(self) -> pulumi.Input[str]:
        """
        Destination address for connection
        """
        return pulumi.get(self, "destination_address")

    @destination_address.setter
    def destination_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "destination_address", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        Display name.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="privateConnectionId")
    def private_connection_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "private_connection_id")

    @private_connection_id.setter
    def private_connection_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_connection_id", value)

    @property
    @pulumi.getter(name="routeId")
    def route_id(self) -> pulumi.Input[str]:
        """
        Required. The Route identifier.
        """
        return pulumi.get(self, "route_id")

    @route_id.setter
    def route_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "route_id", value)

    @property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> Optional[pulumi.Input[int]]:
        """
        Destination port for connection
        """
        return pulumi.get(self, "destination_port")

    @destination_port.setter
    def destination_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "destination_port", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Labels.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

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
        Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        """
        return pulumi.get(self, "request_id")

    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_id", value)


class Route(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination_address: Optional[pulumi.Input[str]] = None,
                 destination_port: Optional[pulumi.Input[int]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 private_connection_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 route_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Use this method to create a route for a private connectivity configuration in a project and location.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] destination_address: Destination address for connection
        :param pulumi.Input[int] destination_port: Destination port for connection
        :param pulumi.Input[str] display_name: Display name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels.
        :param pulumi.Input[str] request_id: Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        :param pulumi.Input[str] route_id: Required. The Route identifier.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RouteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Use this method to create a route for a private connectivity configuration in a project and location.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param RouteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RouteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination_address: Optional[pulumi.Input[str]] = None,
                 destination_port: Optional[pulumi.Input[int]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 private_connection_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 route_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RouteArgs.__new__(RouteArgs)

            if destination_address is None and not opts.urn:
                raise TypeError("Missing required property 'destination_address'")
            __props__.__dict__["destination_address"] = destination_address
            __props__.__dict__["destination_port"] = destination_port
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            if private_connection_id is None and not opts.urn:
                raise TypeError("Missing required property 'private_connection_id'")
            __props__.__dict__["private_connection_id"] = private_connection_id
            __props__.__dict__["project"] = project
            __props__.__dict__["request_id"] = request_id
            if route_id is None and not opts.urn:
                raise TypeError("Missing required property 'route_id'")
            __props__.__dict__["route_id"] = route_id
            __props__.__dict__["create_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["location", "privateConnectionId", "project", "routeId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Route, __self__).__init__(
            'google-native:datastream/v1:Route',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Route':
        """
        Get an existing Route resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RouteArgs.__new__(RouteArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["destination_address"] = None
        __props__.__dict__["destination_port"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_connection_id"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["request_id"] = None
        __props__.__dict__["route_id"] = None
        __props__.__dict__["update_time"] = None
        return Route(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The create time of the resource.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="destinationAddress")
    def destination_address(self) -> pulumi.Output[str]:
        """
        Destination address for connection
        """
        return pulumi.get(self, "destination_address")

    @property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> pulumi.Output[int]:
        """
        Destination port for connection
        """
        return pulumi.get(self, "destination_port")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Labels.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource's name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateConnectionId")
    def private_connection_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "private_connection_id")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> pulumi.Output[Optional[str]]:
        """
        Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        """
        return pulumi.get(self, "request_id")

    @property
    @pulumi.getter(name="routeId")
    def route_id(self) -> pulumi.Output[str]:
        """
        Required. The Route identifier.
        """
        return pulumi.get(self, "route_id")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The update time of the resource.
        """
        return pulumi.get(self, "update_time")

