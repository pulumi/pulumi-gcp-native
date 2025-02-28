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

__all__ = [
    'GetHubResult',
    'AwaitableGetHubResult',
    'get_hub',
    'get_hub_output',
]

@pulumi.output_type
class GetHubResult:
    def __init__(__self__, create_time=None, description=None, labels=None, name=None, route_tables=None, routing_vpcs=None, spoke_summary=None, state=None, unique_id=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if route_tables and not isinstance(route_tables, list):
            raise TypeError("Expected argument 'route_tables' to be a list")
        pulumi.set(__self__, "route_tables", route_tables)
        if routing_vpcs and not isinstance(routing_vpcs, list):
            raise TypeError("Expected argument 'routing_vpcs' to be a list")
        pulumi.set(__self__, "routing_vpcs", routing_vpcs)
        if spoke_summary and not isinstance(spoke_summary, dict):
            raise TypeError("Expected argument 'spoke_summary' to be a dict")
        pulumi.set(__self__, "spoke_summary", spoke_summary)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if unique_id and not isinstance(unique_id, str):
            raise TypeError("Expected argument 'unique_id' to be a str")
        pulumi.set(__self__, "unique_id", unique_id)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time the hub was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        An optional description of the hub.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Optional labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements).
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Immutable. The name of the hub. Hub names must be unique. They use the following form: `projects/{project_number}/locations/global/hubs/{hub_id}`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="routeTables")
    def route_tables(self) -> Sequence[str]:
        """
        The route tables that belong to this hub. They use the following form: `projects/{project_number}/locations/global/hubs/{hub_id}/routeTables/{route_table_id}` This field is read-only. Network Connectivity Center automatically populates it based on the route tables nested under the hub.
        """
        return pulumi.get(self, "route_tables")

    @property
    @pulumi.getter(name="routingVpcs")
    def routing_vpcs(self) -> Sequence['outputs.RoutingVPCResponse']:
        """
        The VPC networks associated with this hub's spokes. This field is read-only. Network Connectivity Center automatically populates it based on the set of spokes attached to the hub.
        """
        return pulumi.get(self, "routing_vpcs")

    @property
    @pulumi.getter(name="spokeSummary")
    def spoke_summary(self) -> 'outputs.SpokeSummaryResponse':
        """
        A summary of the spokes associated with a hub. The summary includes a count of spokes according to type and according to state. If any spokes are inactive, the summary also lists the reasons they are inactive, including a count for each reason.
        """
        return pulumi.get(self, "spoke_summary")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current lifecycle state of this hub.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> str:
        """
        The Google-generated UUID for the hub. This value is unique across all hub resources. If a hub is deleted and another with the same name is created, the new hub is assigned a different unique_id.
        """
        return pulumi.get(self, "unique_id")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The time the hub was last updated.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetHubResult(GetHubResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHubResult(
            create_time=self.create_time,
            description=self.description,
            labels=self.labels,
            name=self.name,
            route_tables=self.route_tables,
            routing_vpcs=self.routing_vpcs,
            spoke_summary=self.spoke_summary,
            state=self.state,
            unique_id=self.unique_id,
            update_time=self.update_time)


def get_hub(hub_id: Optional[str] = None,
            project: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHubResult:
    """
    Gets details about a Network Connectivity Center hub.
    """
    __args__ = dict()
    __args__['hubId'] = hub_id
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:networkconnectivity/v1:getHub', __args__, opts=opts, typ=GetHubResult).value

    return AwaitableGetHubResult(
        create_time=pulumi.get(__ret__, 'create_time'),
        description=pulumi.get(__ret__, 'description'),
        labels=pulumi.get(__ret__, 'labels'),
        name=pulumi.get(__ret__, 'name'),
        route_tables=pulumi.get(__ret__, 'route_tables'),
        routing_vpcs=pulumi.get(__ret__, 'routing_vpcs'),
        spoke_summary=pulumi.get(__ret__, 'spoke_summary'),
        state=pulumi.get(__ret__, 'state'),
        unique_id=pulumi.get(__ret__, 'unique_id'),
        update_time=pulumi.get(__ret__, 'update_time'))


@_utilities.lift_output_func(get_hub)
def get_hub_output(hub_id: Optional[pulumi.Input[str]] = None,
                   project: Optional[pulumi.Input[Optional[str]]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetHubResult]:
    """
    Gets details about a Network Connectivity Center hub.
    """
    ...
