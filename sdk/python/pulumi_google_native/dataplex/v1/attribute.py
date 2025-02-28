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

__all__ = ['AttributeArgs', 'Attribute']

@pulumi.input_type
class AttributeArgs:
    def __init__(__self__, *,
                 data_attribute_id: pulumi.Input[str],
                 data_taxonomy_id: pulumi.Input[str],
                 data_access_spec: Optional[pulumi.Input['GoogleCloudDataplexV1DataAccessSpecArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 resource_access_spec: Optional[pulumi.Input['GoogleCloudDataplexV1ResourceAccessSpecArgs']] = None):
        """
        The set of arguments for constructing a Attribute resource.
        :param pulumi.Input[str] data_attribute_id: Required. DataAttribute identifier. * Must contain only lowercase letters, numbers and hyphens. * Must start with a letter. * Must be between 1-63 characters. * Must end with a number or a letter. * Must be unique within the DataTaxonomy.
        :param pulumi.Input['GoogleCloudDataplexV1DataAccessSpecArgs'] data_access_spec: Optional. Specified when applied to data stored on the resource (eg: rows, columns in BigQuery Tables).
        :param pulumi.Input[str] description: Optional. Description of the DataAttribute.
        :param pulumi.Input[str] display_name: Optional. User friendly display name.
        :param pulumi.Input[str] etag: This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. User-defined labels for the DataAttribute.
        :param pulumi.Input[str] parent_id: Optional. The ID of the parent DataAttribute resource, should belong to the same data taxonomy. Circular dependency in parent chain is not valid. Maximum depth of the hierarchy allowed is 4. a -> b -> c -> d -> e, depth = 4
        :param pulumi.Input['GoogleCloudDataplexV1ResourceAccessSpecArgs'] resource_access_spec: Optional. Specified when applied to a resource (eg: Cloud Storage bucket, BigQuery dataset, BigQuery table).
        """
        pulumi.set(__self__, "data_attribute_id", data_attribute_id)
        pulumi.set(__self__, "data_taxonomy_id", data_taxonomy_id)
        if data_access_spec is not None:
            pulumi.set(__self__, "data_access_spec", data_access_spec)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if parent_id is not None:
            pulumi.set(__self__, "parent_id", parent_id)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if resource_access_spec is not None:
            pulumi.set(__self__, "resource_access_spec", resource_access_spec)

    @property
    @pulumi.getter(name="dataAttributeId")
    def data_attribute_id(self) -> pulumi.Input[str]:
        """
        Required. DataAttribute identifier. * Must contain only lowercase letters, numbers and hyphens. * Must start with a letter. * Must be between 1-63 characters. * Must end with a number or a letter. * Must be unique within the DataTaxonomy.
        """
        return pulumi.get(self, "data_attribute_id")

    @data_attribute_id.setter
    def data_attribute_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_attribute_id", value)

    @property
    @pulumi.getter(name="dataTaxonomyId")
    def data_taxonomy_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "data_taxonomy_id")

    @data_taxonomy_id.setter
    def data_taxonomy_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_taxonomy_id", value)

    @property
    @pulumi.getter(name="dataAccessSpec")
    def data_access_spec(self) -> Optional[pulumi.Input['GoogleCloudDataplexV1DataAccessSpecArgs']]:
        """
        Optional. Specified when applied to data stored on the resource (eg: rows, columns in BigQuery Tables).
        """
        return pulumi.get(self, "data_access_spec")

    @data_access_spec.setter
    def data_access_spec(self, value: Optional[pulumi.Input['GoogleCloudDataplexV1DataAccessSpecArgs']]):
        pulumi.set(self, "data_access_spec", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Description of the DataAttribute.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. User friendly display name.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional. User-defined labels for the DataAttribute.
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
    @pulumi.getter(name="parentId")
    def parent_id(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The ID of the parent DataAttribute resource, should belong to the same data taxonomy. Circular dependency in parent chain is not valid. Maximum depth of the hierarchy allowed is 4. a -> b -> c -> d -> e, depth = 4
        """
        return pulumi.get(self, "parent_id")

    @parent_id.setter
    def parent_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_id", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="resourceAccessSpec")
    def resource_access_spec(self) -> Optional[pulumi.Input['GoogleCloudDataplexV1ResourceAccessSpecArgs']]:
        """
        Optional. Specified when applied to a resource (eg: Cloud Storage bucket, BigQuery dataset, BigQuery table).
        """
        return pulumi.get(self, "resource_access_spec")

    @resource_access_spec.setter
    def resource_access_spec(self, value: Optional[pulumi.Input['GoogleCloudDataplexV1ResourceAccessSpecArgs']]):
        pulumi.set(self, "resource_access_spec", value)


class Attribute(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_access_spec: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDataplexV1DataAccessSpecArgs']]] = None,
                 data_attribute_id: Optional[pulumi.Input[str]] = None,
                 data_taxonomy_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 resource_access_spec: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDataplexV1ResourceAccessSpecArgs']]] = None,
                 __props__=None):
        """
        Create a DataAttribute resource.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDataplexV1DataAccessSpecArgs']] data_access_spec: Optional. Specified when applied to data stored on the resource (eg: rows, columns in BigQuery Tables).
        :param pulumi.Input[str] data_attribute_id: Required. DataAttribute identifier. * Must contain only lowercase letters, numbers and hyphens. * Must start with a letter. * Must be between 1-63 characters. * Must end with a number or a letter. * Must be unique within the DataTaxonomy.
        :param pulumi.Input[str] description: Optional. Description of the DataAttribute.
        :param pulumi.Input[str] display_name: Optional. User friendly display name.
        :param pulumi.Input[str] etag: This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. User-defined labels for the DataAttribute.
        :param pulumi.Input[str] parent_id: Optional. The ID of the parent DataAttribute resource, should belong to the same data taxonomy. Circular dependency in parent chain is not valid. Maximum depth of the hierarchy allowed is 4. a -> b -> c -> d -> e, depth = 4
        :param pulumi.Input[pulumi.InputType['GoogleCloudDataplexV1ResourceAccessSpecArgs']] resource_access_spec: Optional. Specified when applied to a resource (eg: Cloud Storage bucket, BigQuery dataset, BigQuery table).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AttributeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a DataAttribute resource.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param AttributeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AttributeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_access_spec: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDataplexV1DataAccessSpecArgs']]] = None,
                 data_attribute_id: Optional[pulumi.Input[str]] = None,
                 data_taxonomy_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 resource_access_spec: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDataplexV1ResourceAccessSpecArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AttributeArgs.__new__(AttributeArgs)

            __props__.__dict__["data_access_spec"] = data_access_spec
            if data_attribute_id is None and not opts.urn:
                raise TypeError("Missing required property 'data_attribute_id'")
            __props__.__dict__["data_attribute_id"] = data_attribute_id
            if data_taxonomy_id is None and not opts.urn:
                raise TypeError("Missing required property 'data_taxonomy_id'")
            __props__.__dict__["data_taxonomy_id"] = data_taxonomy_id
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["etag"] = etag
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["parent_id"] = parent_id
            __props__.__dict__["project"] = project
            __props__.__dict__["resource_access_spec"] = resource_access_spec
            __props__.__dict__["attribute_count"] = None
            __props__.__dict__["create_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["uid"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["dataAttributeId", "dataTaxonomyId", "location", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Attribute, __self__).__init__(
            'google-native:dataplex/v1:Attribute',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Attribute':
        """
        Get an existing Attribute resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AttributeArgs.__new__(AttributeArgs)

        __props__.__dict__["attribute_count"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["data_access_spec"] = None
        __props__.__dict__["data_attribute_id"] = None
        __props__.__dict__["data_taxonomy_id"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parent_id"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["resource_access_spec"] = None
        __props__.__dict__["uid"] = None
        __props__.__dict__["update_time"] = None
        return Attribute(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="attributeCount")
    def attribute_count(self) -> pulumi.Output[int]:
        """
        The number of child attributes present for this attribute.
        """
        return pulumi.get(self, "attribute_count")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time when the DataAttribute was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dataAccessSpec")
    def data_access_spec(self) -> pulumi.Output['outputs.GoogleCloudDataplexV1DataAccessSpecResponse']:
        """
        Optional. Specified when applied to data stored on the resource (eg: rows, columns in BigQuery Tables).
        """
        return pulumi.get(self, "data_access_spec")

    @property
    @pulumi.getter(name="dataAttributeId")
    def data_attribute_id(self) -> pulumi.Output[str]:
        """
        Required. DataAttribute identifier. * Must contain only lowercase letters, numbers and hyphens. * Must start with a letter. * Must be between 1-63 characters. * Must end with a number or a letter. * Must be unique within the DataTaxonomy.
        """
        return pulumi.get(self, "data_attribute_id")

    @property
    @pulumi.getter(name="dataTaxonomyId")
    def data_taxonomy_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "data_taxonomy_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Optional. Description of the DataAttribute.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Optional. User friendly display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. User-defined labels for the DataAttribute.
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
        The relative resource name of the dataAttribute, of the form: projects/{project_number}/locations/{location_id}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id}.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> pulumi.Output[str]:
        """
        Optional. The ID of the parent DataAttribute resource, should belong to the same data taxonomy. Circular dependency in parent chain is not valid. Maximum depth of the hierarchy allowed is 4. a -> b -> c -> d -> e, depth = 4
        """
        return pulumi.get(self, "parent_id")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="resourceAccessSpec")
    def resource_access_spec(self) -> pulumi.Output['outputs.GoogleCloudDataplexV1ResourceAccessSpecResponse']:
        """
        Optional. Specified when applied to a resource (eg: Cloud Storage bucket, BigQuery dataset, BigQuery table).
        """
        return pulumi.get(self, "resource_access_spec")

    @property
    @pulumi.getter
    def uid(self) -> pulumi.Output[str]:
        """
        System generated globally unique ID for the DataAttribute. This ID will be different if the DataAttribute is deleted and re-created with the same name.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The time when the DataAttribute was last updated.
        """
        return pulumi.get(self, "update_time")

