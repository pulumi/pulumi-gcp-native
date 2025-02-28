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

__all__ = ['BackupArgs', 'Backup']

@pulumi.input_type
class BackupArgs:
    def __init__(__self__, *,
                 backup_id: pulumi.Input[str],
                 cluster_name: pulumi.Input[str],
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 encryption_config: Optional[pulumi.Input['EncryptionConfigArgs']] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['BackupType']] = None):
        """
        The set of arguments for constructing a Backup resource.
        :param pulumi.Input[str] backup_id: Required. ID of the requesting object.
        :param pulumi.Input[str] cluster_name: The full resource name of the backup source cluster (e.g., projects/{project}/locations/{region}/clusters/{cluster_id}).
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. https://google.aip.dev/128
        :param pulumi.Input[str] description: User-provided description of the backup.
        :param pulumi.Input[str] display_name: User-settable and human-readable display name for the Backup.
        :param pulumi.Input['EncryptionConfigArgs'] encryption_config: Optional. The encryption config can be specified to encrypt the backup with a customer-managed encryption key (CMEK). When this field is not specified, the backup will then use default encryption scheme to protect the user data.
        :param pulumi.Input[str] etag: For Resource freshness validation (https://google.aip.dev/154)
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels as key value pairs
        :param pulumi.Input[str] request_id: Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        :param pulumi.Input['BackupType'] type: The backup type, which suggests the trigger for the backup.
        """
        pulumi.set(__self__, "backup_id", backup_id)
        pulumi.set(__self__, "cluster_name", cluster_name)
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if encryption_config is not None:
            pulumi.set(__self__, "encryption_config", encryption_config)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> pulumi.Input[str]:
        """
        Required. ID of the requesting object.
        """
        return pulumi.get(self, "backup_id")

    @backup_id.setter
    def backup_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "backup_id", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        The full resource name of the backup source cluster (e.g., projects/{project}/locations/{region}/clusters/{cluster_id}).
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. https://google.aip.dev/128
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        User-provided description of the backup.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        User-settable and human-readable display name for the Backup.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional[pulumi.Input['EncryptionConfigArgs']]:
        """
        Optional. The encryption config can be specified to encrypt the backup with a customer-managed encryption key (CMEK). When this field is not specified, the backup will then use default encryption scheme to protect the user data.
        """
        return pulumi.get(self, "encryption_config")

    @encryption_config.setter
    def encryption_config(self, value: Optional[pulumi.Input['EncryptionConfigArgs']]):
        pulumi.set(self, "encryption_config", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        For Resource freshness validation (https://google.aip.dev/154)
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Labels as key value pairs
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
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['BackupType']]:
        """
        The backup type, which suggests the trigger for the backup.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['BackupType']]):
        pulumi.set(self, "type", value)


class Backup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 backup_id: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 encryption_config: Optional[pulumi.Input[pulumi.InputType['EncryptionConfigArgs']]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['BackupType']] = None,
                 __props__=None):
        """
        Creates a new Backup in a given project and location.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. https://google.aip.dev/128
        :param pulumi.Input[str] backup_id: Required. ID of the requesting object.
        :param pulumi.Input[str] cluster_name: The full resource name of the backup source cluster (e.g., projects/{project}/locations/{region}/clusters/{cluster_id}).
        :param pulumi.Input[str] description: User-provided description of the backup.
        :param pulumi.Input[str] display_name: User-settable and human-readable display name for the Backup.
        :param pulumi.Input[pulumi.InputType['EncryptionConfigArgs']] encryption_config: Optional. The encryption config can be specified to encrypt the backup with a customer-managed encryption key (CMEK). When this field is not specified, the backup will then use default encryption scheme to protect the user data.
        :param pulumi.Input[str] etag: For Resource freshness validation (https://google.aip.dev/154)
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels as key value pairs
        :param pulumi.Input[str] request_id: Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
        :param pulumi.Input['BackupType'] type: The backup type, which suggests the trigger for the backup.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BackupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new Backup in a given project and location.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param BackupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BackupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 backup_id: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 encryption_config: Optional[pulumi.Input[pulumi.InputType['EncryptionConfigArgs']]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['BackupType']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BackupArgs.__new__(BackupArgs)

            __props__.__dict__["annotations"] = annotations
            if backup_id is None and not opts.urn:
                raise TypeError("Missing required property 'backup_id'")
            __props__.__dict__["backup_id"] = backup_id
            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["encryption_config"] = encryption_config
            __props__.__dict__["etag"] = etag
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["project"] = project
            __props__.__dict__["request_id"] = request_id
            __props__.__dict__["type"] = type
            __props__.__dict__["cluster_uid"] = None
            __props__.__dict__["create_time"] = None
            __props__.__dict__["database_version"] = None
            __props__.__dict__["delete_time"] = None
            __props__.__dict__["encryption_info"] = None
            __props__.__dict__["expiry_quantity"] = None
            __props__.__dict__["expiry_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["reconciling"] = None
            __props__.__dict__["size_bytes"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["uid"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["backupId", "location", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Backup, __self__).__init__(
            'google-native:alloydb/v1beta:Backup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Backup':
        """
        Get an existing Backup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BackupArgs.__new__(BackupArgs)

        __props__.__dict__["annotations"] = None
        __props__.__dict__["backup_id"] = None
        __props__.__dict__["cluster_name"] = None
        __props__.__dict__["cluster_uid"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["database_version"] = None
        __props__.__dict__["delete_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["encryption_config"] = None
        __props__.__dict__["encryption_info"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["expiry_quantity"] = None
        __props__.__dict__["expiry_time"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["reconciling"] = None
        __props__.__dict__["request_id"] = None
        __props__.__dict__["size_bytes"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["uid"] = None
        __props__.__dict__["update_time"] = None
        return Backup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. https://google.aip.dev/128
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> pulumi.Output[str]:
        """
        Required. ID of the requesting object.
        """
        return pulumi.get(self, "backup_id")

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[str]:
        """
        The full resource name of the backup source cluster (e.g., projects/{project}/locations/{region}/clusters/{cluster_id}).
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="clusterUid")
    def cluster_uid(self) -> pulumi.Output[str]:
        """
        The system-generated UID of the cluster which was used to create this resource.
        """
        return pulumi.get(self, "cluster_uid")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Create time stamp
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="databaseVersion")
    def database_version(self) -> pulumi.Output[str]:
        """
        The database engine major version of the cluster this backup was created from. Any restored cluster created from this backup will have the same database version.
        """
        return pulumi.get(self, "database_version")

    @property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[str]:
        """
        Delete time stamp
        """
        return pulumi.get(self, "delete_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        User-provided description of the backup.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        User-settable and human-readable display name for the Backup.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> pulumi.Output['outputs.EncryptionConfigResponse']:
        """
        Optional. The encryption config can be specified to encrypt the backup with a customer-managed encryption key (CMEK). When this field is not specified, the backup will then use default encryption scheme to protect the user data.
        """
        return pulumi.get(self, "encryption_config")

    @property
    @pulumi.getter(name="encryptionInfo")
    def encryption_info(self) -> pulumi.Output['outputs.EncryptionInfoResponse']:
        """
        The encryption information for the backup.
        """
        return pulumi.get(self, "encryption_info")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        For Resource freshness validation (https://google.aip.dev/154)
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="expiryQuantity")
    def expiry_quantity(self) -> pulumi.Output['outputs.QuantityBasedExpiryResponse']:
        """
        The QuantityBasedExpiry of the backup, specified by the backup's retention policy. Once the expiry quantity is over retention, the backup is eligible to be garbage collected.
        """
        return pulumi.get(self, "expiry_quantity")

    @property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> pulumi.Output[str]:
        """
        The time at which after the backup is eligible to be garbage collected. It is the duration specified by the backup's retention policy, added to the backup's create_time.
        """
        return pulumi.get(self, "expiry_time")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Labels as key value pairs
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
        The name of the backup resource with the format: * projects/{project}/locations/{region}/backups/{backup_id} where the cluster and backup ID segments should satisfy the regex expression `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`, e.g. 1-63 characters of lowercase letters, numbers, and dashes, starting with a letter, and ending with a letter or number. For more details see https://google.aip.dev/122. The prefix of the backup resource name is the name of the parent resource: * projects/{project}/locations/{region}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[bool]:
        """
        Reconciling (https://google.aip.dev/128#reconciliation), if true, indicates that the service is actively updating the resource. This can happen due to user-triggered updates or system actions like failover or maintenance.
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
    @pulumi.getter(name="sizeBytes")
    def size_bytes(self) -> pulumi.Output[str]:
        """
        The size of the backup in bytes.
        """
        return pulumi.get(self, "size_bytes")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the backup.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The backup type, which suggests the trigger for the backup.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uid(self) -> pulumi.Output[str]:
        """
        The system-generated UID of the resource. The UID is assigned when the resource is created, and it is retained until it is deleted.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Update time stamp
        """
        return pulumi.get(self, "update_time")

