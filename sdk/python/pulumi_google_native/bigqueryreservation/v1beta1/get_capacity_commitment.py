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
    'GetCapacityCommitmentResult',
    'AwaitableGetCapacityCommitmentResult',
    'get_capacity_commitment',
    'get_capacity_commitment_output',
]

@pulumi.output_type
class GetCapacityCommitmentResult:
    def __init__(__self__, commitment_end_time=None, commitment_start_time=None, failure_status=None, multi_region_auxiliary=None, name=None, plan=None, renewal_plan=None, slot_count=None, state=None):
        if commitment_end_time and not isinstance(commitment_end_time, str):
            raise TypeError("Expected argument 'commitment_end_time' to be a str")
        pulumi.set(__self__, "commitment_end_time", commitment_end_time)
        if commitment_start_time and not isinstance(commitment_start_time, str):
            raise TypeError("Expected argument 'commitment_start_time' to be a str")
        pulumi.set(__self__, "commitment_start_time", commitment_start_time)
        if failure_status and not isinstance(failure_status, dict):
            raise TypeError("Expected argument 'failure_status' to be a dict")
        pulumi.set(__self__, "failure_status", failure_status)
        if multi_region_auxiliary and not isinstance(multi_region_auxiliary, bool):
            raise TypeError("Expected argument 'multi_region_auxiliary' to be a bool")
        pulumi.set(__self__, "multi_region_auxiliary", multi_region_auxiliary)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if plan and not isinstance(plan, str):
            raise TypeError("Expected argument 'plan' to be a str")
        pulumi.set(__self__, "plan", plan)
        if renewal_plan and not isinstance(renewal_plan, str):
            raise TypeError("Expected argument 'renewal_plan' to be a str")
        pulumi.set(__self__, "renewal_plan", renewal_plan)
        if slot_count and not isinstance(slot_count, str):
            raise TypeError("Expected argument 'slot_count' to be a str")
        pulumi.set(__self__, "slot_count", slot_count)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="commitmentEndTime")
    def commitment_end_time(self) -> str:
        """
        The end of the current commitment period. It is applicable only for ACTIVE capacity commitments.
        """
        return pulumi.get(self, "commitment_end_time")

    @property
    @pulumi.getter(name="commitmentStartTime")
    def commitment_start_time(self) -> str:
        """
        The start of the current commitment period. It is applicable only for ACTIVE capacity commitments.
        """
        return pulumi.get(self, "commitment_start_time")

    @property
    @pulumi.getter(name="failureStatus")
    def failure_status(self) -> 'outputs.StatusResponse':
        """
        For FAILED commitment plan, provides the reason of failure.
        """
        return pulumi.get(self, "failure_status")

    @property
    @pulumi.getter(name="multiRegionAuxiliary")
    def multi_region_auxiliary(self) -> bool:
        """
        Applicable only for commitments located within one of the BigQuery multi-regions (US or EU). If set to true, this commitment is placed in the organization's secondary region which is designated for disaster recovery purposes. If false, this commitment is placed in the organization's default region.
        """
        return pulumi.get(self, "multi_region_auxiliary")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the capacity commitment, e.g., `projects/myproject/locations/US/capacityCommitments/123` The commitment_id must only contain lower case alphanumeric characters or dashes. It must start with a letter and must not end with a dash. Its maximum length is 64 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def plan(self) -> str:
        """
        Capacity commitment commitment plan.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="renewalPlan")
    def renewal_plan(self) -> str:
        """
        The plan this capacity commitment is converted to after commitment_end_time passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable for ANNUAL commitments.
        """
        return pulumi.get(self, "renewal_plan")

    @property
    @pulumi.getter(name="slotCount")
    def slot_count(self) -> str:
        """
        Number of slots in this commitment.
        """
        return pulumi.get(self, "slot_count")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        State of the commitment.
        """
        return pulumi.get(self, "state")


class AwaitableGetCapacityCommitmentResult(GetCapacityCommitmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCapacityCommitmentResult(
            commitment_end_time=self.commitment_end_time,
            commitment_start_time=self.commitment_start_time,
            failure_status=self.failure_status,
            multi_region_auxiliary=self.multi_region_auxiliary,
            name=self.name,
            plan=self.plan,
            renewal_plan=self.renewal_plan,
            slot_count=self.slot_count,
            state=self.state)


def get_capacity_commitment(capacity_commitment_id: Optional[str] = None,
                            location: Optional[str] = None,
                            project: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCapacityCommitmentResult:
    """
    Returns information about the capacity commitment.
    """
    __args__ = dict()
    __args__['capacityCommitmentId'] = capacity_commitment_id
    __args__['location'] = location
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:bigqueryreservation/v1beta1:getCapacityCommitment', __args__, opts=opts, typ=GetCapacityCommitmentResult).value

    return AwaitableGetCapacityCommitmentResult(
        commitment_end_time=pulumi.get(__ret__, 'commitment_end_time'),
        commitment_start_time=pulumi.get(__ret__, 'commitment_start_time'),
        failure_status=pulumi.get(__ret__, 'failure_status'),
        multi_region_auxiliary=pulumi.get(__ret__, 'multi_region_auxiliary'),
        name=pulumi.get(__ret__, 'name'),
        plan=pulumi.get(__ret__, 'plan'),
        renewal_plan=pulumi.get(__ret__, 'renewal_plan'),
        slot_count=pulumi.get(__ret__, 'slot_count'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_capacity_commitment)
def get_capacity_commitment_output(capacity_commitment_id: Optional[pulumi.Input[str]] = None,
                                   location: Optional[pulumi.Input[str]] = None,
                                   project: Optional[pulumi.Input[Optional[str]]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCapacityCommitmentResult]:
    """
    Returns information about the capacity commitment.
    """
    ...
