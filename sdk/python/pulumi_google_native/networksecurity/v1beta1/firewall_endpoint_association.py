# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['FirewallEndpointAssociationArgs', 'FirewallEndpointAssociation']

@pulumi.input_type
class FirewallEndpointAssociationArgs:
    def __init__(__self__, *,
                 firewall_endpoint: pulumi.Input[str],
                 network: pulumi.Input[str],
                 firewall_endpoint_association_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 tls_inspection_policy: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FirewallEndpointAssociation resource.
        :param pulumi.Input[str] firewall_endpoint: The URL of the FirewallEndpoint that is being associated.
        :param pulumi.Input[str] network: The URL of the network that is being associated.
        :param pulumi.Input[str] firewall_endpoint_association_id: Optional. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_association_id from the method_signature of Create RPC.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. Labels as key value pairs
        :param pulumi.Input[str] request_id: Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        :param pulumi.Input[str] tls_inspection_policy: Optional. The URL of the TlsInspectionPolicy that is being associated.
        """
        pulumi.set(__self__, "firewall_endpoint", firewall_endpoint)
        pulumi.set(__self__, "network", network)
        if firewall_endpoint_association_id is not None:
            pulumi.set(__self__, "firewall_endpoint_association_id", firewall_endpoint_association_id)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)
        if tls_inspection_policy is not None:
            pulumi.set(__self__, "tls_inspection_policy", tls_inspection_policy)

    @property
    @pulumi.getter(name="firewallEndpoint")
    def firewall_endpoint(self) -> pulumi.Input[str]:
        """
        The URL of the FirewallEndpoint that is being associated.
        """
        return pulumi.get(self, "firewall_endpoint")

    @firewall_endpoint.setter
    def firewall_endpoint(self, value: pulumi.Input[str]):
        pulumi.set(self, "firewall_endpoint", value)

    @property
    @pulumi.getter
    def network(self) -> pulumi.Input[str]:
        """
        The URL of the network that is being associated.
        """
        return pulumi.get(self, "network")

    @network.setter
    def network(self, value: pulumi.Input[str]):
        pulumi.set(self, "network", value)

    @property
    @pulumi.getter(name="firewallEndpointAssociationId")
    def firewall_endpoint_association_id(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_association_id from the method_signature of Create RPC.
        """
        return pulumi.get(self, "firewall_endpoint_association_id")

    @firewall_endpoint_association_id.setter
    def firewall_endpoint_association_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "firewall_endpoint_association_id", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional. Labels as key value pairs
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
        Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        """
        return pulumi.get(self, "request_id")

    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_id", value)

    @property
    @pulumi.getter(name="tlsInspectionPolicy")
    def tls_inspection_policy(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The URL of the TlsInspectionPolicy that is being associated.
        """
        return pulumi.get(self, "tls_inspection_policy")

    @tls_inspection_policy.setter
    def tls_inspection_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tls_inspection_policy", value)


class FirewallEndpointAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 firewall_endpoint: Optional[pulumi.Input[str]] = None,
                 firewall_endpoint_association_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 tls_inspection_policy: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new FirewallEndpointAssociation in a given project and location.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] firewall_endpoint: The URL of the FirewallEndpoint that is being associated.
        :param pulumi.Input[str] firewall_endpoint_association_id: Optional. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_association_id from the method_signature of Create RPC.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. Labels as key value pairs
        :param pulumi.Input[str] network: The URL of the network that is being associated.
        :param pulumi.Input[str] request_id: Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        :param pulumi.Input[str] tls_inspection_policy: Optional. The URL of the TlsInspectionPolicy that is being associated.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FirewallEndpointAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new FirewallEndpointAssociation in a given project and location.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param FirewallEndpointAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirewallEndpointAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 firewall_endpoint: Optional[pulumi.Input[str]] = None,
                 firewall_endpoint_association_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 tls_inspection_policy: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FirewallEndpointAssociationArgs.__new__(FirewallEndpointAssociationArgs)

            if firewall_endpoint is None and not opts.urn:
                raise TypeError("Missing required property 'firewall_endpoint'")
            __props__.__dict__["firewall_endpoint"] = firewall_endpoint
            __props__.__dict__["firewall_endpoint_association_id"] = firewall_endpoint_association_id
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            if network is None and not opts.urn:
                raise TypeError("Missing required property 'network'")
            __props__.__dict__["network"] = network
            __props__.__dict__["project"] = project
            __props__.__dict__["request_id"] = request_id
            __props__.__dict__["tls_inspection_policy"] = tls_inspection_policy
            __props__.__dict__["create_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["reconciling"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["location", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(FirewallEndpointAssociation, __self__).__init__(
            'google-native:networksecurity/v1beta1:FirewallEndpointAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FirewallEndpointAssociation':
        """
        Get an existing FirewallEndpointAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FirewallEndpointAssociationArgs.__new__(FirewallEndpointAssociationArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["firewall_endpoint"] = None
        __props__.__dict__["firewall_endpoint_association_id"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["reconciling"] = None
        __props__.__dict__["request_id"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["tls_inspection_policy"] = None
        __props__.__dict__["update_time"] = None
        return FirewallEndpointAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Create time stamp
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="firewallEndpoint")
    def firewall_endpoint(self) -> pulumi.Output[str]:
        """
        The URL of the FirewallEndpoint that is being associated.
        """
        return pulumi.get(self, "firewall_endpoint")

    @property
    @pulumi.getter(name="firewallEndpointAssociationId")
    def firewall_endpoint_association_id(self) -> pulumi.Output[Optional[str]]:
        """
        Optional. Id of the requesting object. If auto-generating Id server-side, remove this field and firewall_endpoint_association_id from the method_signature of Create RPC.
        """
        return pulumi.get(self, "firewall_endpoint_association_id")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. Labels as key value pairs
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
        name of resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output[str]:
        """
        The URL of the network that is being associated.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[bool]:
        """
        Whether reconciling is in progress, recommended per https://google.aip.dev/128.
        """
        return pulumi.get(self, "reconciling")

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> pulumi.Output[Optional[str]]:
        """
        Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        """
        return pulumi.get(self, "request_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Current state of the association.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="tlsInspectionPolicy")
    def tls_inspection_policy(self) -> pulumi.Output[str]:
        """
        Optional. The URL of the TlsInspectionPolicy that is being associated.
        """
        return pulumi.get(self, "tls_inspection_policy")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Update time stamp
        """
        return pulumi.get(self, "update_time")

