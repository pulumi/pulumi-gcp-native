# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['ManagedFolderArgs', 'ManagedFolder']

@pulumi.input_type
class ManagedFolderArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 create_time: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metageneration: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ManagedFolder resource.
        :param pulumi.Input[str] bucket: The name of the bucket containing this managed folder.
        :param pulumi.Input[str] create_time: The creation time of the managed folder in RFC 3339 format.
        :param pulumi.Input[str] id: The ID of the managed folder, including the bucket name and managed folder name.
        :param pulumi.Input[str] kind: The kind of item this is. For managed folders, this is always storage#managedFolder.
        :param pulumi.Input[str] metageneration: The version of the metadata for this managed folder. Used for preconditions and for detecting changes in metadata.
        :param pulumi.Input[str] name: The name of the managed folder. Required if not specified by URL parameter.
        :param pulumi.Input[str] self_link: The link to this managed folder.
        :param pulumi.Input[str] update_time: The last update time of the managed folder metadata in RFC 3339 format.
        """
        pulumi.set(__self__, "bucket", bucket)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if metageneration is not None:
            pulumi.set(__self__, "metageneration", metageneration)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if self_link is not None:
            pulumi.set(__self__, "self_link", self_link)
        if update_time is not None:
            pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        """
        The name of the bucket containing this managed folder.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        The creation time of the managed folder in RFC 3339 format.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the managed folder, including the bucket name and managed folder name.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        The kind of item this is. For managed folders, this is always storage#managedFolder.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def metageneration(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the metadata for this managed folder. Used for preconditions and for detecting changes in metadata.
        """
        return pulumi.get(self, "metageneration")

    @metageneration.setter
    def metageneration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metageneration", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the managed folder. Required if not specified by URL parameter.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[str]]:
        """
        The link to this managed folder.
        """
        return pulumi.get(self, "self_link")

    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "self_link", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        The last update time of the managed folder metadata in RFC 3339 format.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)


class ManagedFolder(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metageneration: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new managed folder.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the bucket containing this managed folder.
        :param pulumi.Input[str] create_time: The creation time of the managed folder in RFC 3339 format.
        :param pulumi.Input[str] id: The ID of the managed folder, including the bucket name and managed folder name.
        :param pulumi.Input[str] kind: The kind of item this is. For managed folders, this is always storage#managedFolder.
        :param pulumi.Input[str] metageneration: The version of the metadata for this managed folder. Used for preconditions and for detecting changes in metadata.
        :param pulumi.Input[str] name: The name of the managed folder. Required if not specified by URL parameter.
        :param pulumi.Input[str] self_link: The link to this managed folder.
        :param pulumi.Input[str] update_time: The last update time of the managed folder metadata in RFC 3339 format.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedFolderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new managed folder.

        :param str resource_name: The name of the resource.
        :param ManagedFolderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedFolderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metageneration: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagedFolderArgs.__new__(ManagedFolderArgs)

            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            __props__.__dict__["create_time"] = create_time
            __props__.__dict__["id"] = id
            __props__.__dict__["kind"] = kind
            __props__.__dict__["metageneration"] = metageneration
            __props__.__dict__["name"] = name
            __props__.__dict__["self_link"] = self_link
            __props__.__dict__["update_time"] = update_time
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["bucket"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ManagedFolder, __self__).__init__(
            'google-native:storage/v1:ManagedFolder',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagedFolder':
        """
        Get an existing ManagedFolder resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagedFolderArgs.__new__(ManagedFolderArgs)

        __props__.__dict__["bucket"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["metageneration"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["self_link"] = None
        __props__.__dict__["update_time"] = None
        return ManagedFolder(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The creation time of the managed folder in RFC 3339 format.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of item this is. For managed folders, this is always storage#managedFolder.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def metageneration(self) -> pulumi.Output[str]:
        """
        The version of the metadata for this managed folder. Used for preconditions and for detecting changes in metadata.
        """
        return pulumi.get(self, "metageneration")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the managed folder. Required if not specified by URL parameter.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The link to this managed folder.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The last update time of the managed folder metadata in RFC 3339 format.
        """
        return pulumi.get(self, "update_time")

