# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'AcceleratorConfigArgs',
    'AttachedDiskArgs',
    'NetworkConfigArgs',
    'SchedulingConfigArgs',
    'ServiceAccountArgs',
    'ShieldedInstanceConfigArgs',
]

@pulumi.input_type
class AcceleratorConfigArgs:
    def __init__(__self__, *,
                 topology: pulumi.Input[str],
                 type: pulumi.Input['AcceleratorConfigType']):
        """
        A TPU accelerator configuration.
        :param pulumi.Input[str] topology: Topology of TPU in chips.
        :param pulumi.Input['AcceleratorConfigType'] type: Type of TPU.
        """
        pulumi.set(__self__, "topology", topology)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def topology(self) -> pulumi.Input[str]:
        """
        Topology of TPU in chips.
        """
        return pulumi.get(self, "topology")

    @topology.setter
    def topology(self, value: pulumi.Input[str]):
        pulumi.set(self, "topology", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['AcceleratorConfigType']:
        """
        Type of TPU.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['AcceleratorConfigType']):
        pulumi.set(self, "type", value)


@pulumi.input_type
class AttachedDiskArgs:
    def __init__(__self__, *,
                 mode: Optional[pulumi.Input['AttachedDiskMode']] = None,
                 source_disk: Optional[pulumi.Input[str]] = None):
        """
        A node-attached disk resource. Next ID: 8;
        :param pulumi.Input['AttachedDiskMode'] mode: The mode in which to attach this disk. If not specified, the default is READ_WRITE mode. Only applicable to data_disks.
        :param pulumi.Input[str] source_disk: Specifies the full path to an existing disk. For example: "projects/my-project/zones/us-central1-c/disks/my-disk".
        """
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if source_disk is not None:
            pulumi.set(__self__, "source_disk", source_disk)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input['AttachedDiskMode']]:
        """
        The mode in which to attach this disk. If not specified, the default is READ_WRITE mode. Only applicable to data_disks.
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input['AttachedDiskMode']]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the full path to an existing disk. For example: "projects/my-project/zones/us-central1-c/disks/my-disk".
        """
        return pulumi.get(self, "source_disk")

    @source_disk.setter
    def source_disk(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_disk", value)


@pulumi.input_type
class NetworkConfigArgs:
    def __init__(__self__, *,
                 can_ip_forward: Optional[pulumi.Input[bool]] = None,
                 enable_external_ips: Optional[pulumi.Input[bool]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 subnetwork: Optional[pulumi.Input[str]] = None):
        """
        Network related configurations.
        :param pulumi.Input[bool] can_ip_forward: Allows the TPU node to send and receive packets with non-matching destination or source IPs. This is required if you plan to use the TPU workers to forward routes.
        :param pulumi.Input[bool] enable_external_ips: Indicates that external IP addresses would be associated with the TPU workers. If set to false, the specified subnetwork or network should have Private Google Access enabled.
        :param pulumi.Input[str] network: The name of the network for the TPU node. It must be a preexisting Google Compute Engine network. If none is provided, "default" will be used.
        :param pulumi.Input[str] subnetwork: The name of the subnetwork for the TPU node. It must be a preexisting Google Compute Engine subnetwork. If none is provided, "default" will be used.
        """
        if can_ip_forward is not None:
            pulumi.set(__self__, "can_ip_forward", can_ip_forward)
        if enable_external_ips is not None:
            pulumi.set(__self__, "enable_external_ips", enable_external_ips)
        if network is not None:
            pulumi.set(__self__, "network", network)
        if subnetwork is not None:
            pulumi.set(__self__, "subnetwork", subnetwork)

    @property
    @pulumi.getter(name="canIpForward")
    def can_ip_forward(self) -> Optional[pulumi.Input[bool]]:
        """
        Allows the TPU node to send and receive packets with non-matching destination or source IPs. This is required if you plan to use the TPU workers to forward routes.
        """
        return pulumi.get(self, "can_ip_forward")

    @can_ip_forward.setter
    def can_ip_forward(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "can_ip_forward", value)

    @property
    @pulumi.getter(name="enableExternalIps")
    def enable_external_ips(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates that external IP addresses would be associated with the TPU workers. If set to false, the specified subnetwork or network should have Private Google Access enabled.
        """
        return pulumi.get(self, "enable_external_ips")

    @enable_external_ips.setter
    def enable_external_ips(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_external_ips", value)

    @property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the network for the TPU node. It must be a preexisting Google Compute Engine network. If none is provided, "default" will be used.
        """
        return pulumi.get(self, "network")

    @network.setter
    def network(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network", value)

    @property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the subnetwork for the TPU node. It must be a preexisting Google Compute Engine subnetwork. If none is provided, "default" will be used.
        """
        return pulumi.get(self, "subnetwork")

    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnetwork", value)


@pulumi.input_type
class SchedulingConfigArgs:
    def __init__(__self__, *,
                 preemptible: Optional[pulumi.Input[bool]] = None,
                 reserved: Optional[pulumi.Input[bool]] = None):
        """
        Sets the scheduling options for this node.
        :param pulumi.Input[bool] preemptible: Defines whether the node is preemptible.
        :param pulumi.Input[bool] reserved: Whether the node is created under a reservation.
        """
        if preemptible is not None:
            pulumi.set(__self__, "preemptible", preemptible)
        if reserved is not None:
            pulumi.set(__self__, "reserved", reserved)

    @property
    @pulumi.getter
    def preemptible(self) -> Optional[pulumi.Input[bool]]:
        """
        Defines whether the node is preemptible.
        """
        return pulumi.get(self, "preemptible")

    @preemptible.setter
    def preemptible(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "preemptible", value)

    @property
    @pulumi.getter
    def reserved(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the node is created under a reservation.
        """
        return pulumi.get(self, "reserved")

    @reserved.setter
    def reserved(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "reserved", value)


@pulumi.input_type
class ServiceAccountArgs:
    def __init__(__self__, *,
                 email: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        A service account.
        :param pulumi.Input[str] email: Email address of the service account. If empty, default Compute service account will be used.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scope: The list of scopes to be made available for this service account. If empty, access to all Cloud APIs will be allowed.
        """
        if email is not None:
            pulumi.set(__self__, "email", email)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        Email address of the service account. If empty, default Compute service account will be used.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of scopes to be made available for this service account. If empty, access to all Cloud APIs will be allowed.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "scope", value)


@pulumi.input_type
class ShieldedInstanceConfigArgs:
    def __init__(__self__, *,
                 enable_secure_boot: Optional[pulumi.Input[bool]] = None):
        """
        A set of Shielded Instance options.
        :param pulumi.Input[bool] enable_secure_boot: Defines whether the instance has Secure Boot enabled.
        """
        if enable_secure_boot is not None:
            pulumi.set(__self__, "enable_secure_boot", enable_secure_boot)

    @property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[pulumi.Input[bool]]:
        """
        Defines whether the instance has Secure Boot enabled.
        """
        return pulumi.get(self, "enable_secure_boot")

    @enable_secure_boot.setter
    def enable_secure_boot(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_secure_boot", value)


