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

__all__ = ['DataAttributeBindingArgs', 'DataAttributeBinding']

@pulumi.input_type
class DataAttributeBindingArgs:
    def __init__(__self__, *,
                 data_attribute_binding_id: pulumi.Input[str],
                 attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 paths: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDataplexV1DataAttributeBindingPathArgs']]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 resource: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DataAttributeBinding resource.
        :param pulumi.Input[str] data_attribute_binding_id: Required. DataAttributeBinding identifier. * Must contain only lowercase letters, numbers and hyphens. * Must start with a letter. * Must be between 1-63 characters. * Must end with a number or a letter. * Must be unique within the Location.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] attributes: Optional. List of attributes to be associated with the resource, provided in the form: projects/{project}/locations/{location}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id}
        :param pulumi.Input[str] description: Optional. Description of the DataAttributeBinding.
        :param pulumi.Input[str] display_name: Optional. User friendly display name.
        :param pulumi.Input[str] etag: This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Etags must be used when calling the DeleteDataAttributeBinding and the UpdateDataAttributeBinding method.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. User-defined labels for the DataAttributeBinding.
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudDataplexV1DataAttributeBindingPathArgs']]] paths: Optional. The list of paths for items within the associated resource (eg. columns and partitions within a table) along with attribute bindings.
        :param pulumi.Input[str] resource: Optional. Immutable. The resource name of the resource that is associated to attributes. Presently, only entity resource is supported in the form: projects/{project}/locations/{location}/lakes/{lake}/zones/{zone}/entities/{entity_id} Must belong in the same project and region as the attribute binding, and there can only exist one active binding for a resource.
        """
        pulumi.set(__self__, "data_attribute_binding_id", data_attribute_binding_id)
        if attributes is not None:
            pulumi.set(__self__, "attributes", attributes)
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
        if paths is not None:
            pulumi.set(__self__, "paths", paths)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if resource is not None:
            pulumi.set(__self__, "resource", resource)

    @property
    @pulumi.getter(name="dataAttributeBindingId")
    def data_attribute_binding_id(self) -> pulumi.Input[str]:
        """
        Required. DataAttributeBinding identifier. * Must contain only lowercase letters, numbers and hyphens. * Must start with a letter. * Must be between 1-63 characters. * Must end with a number or a letter. * Must be unique within the Location.
        """
        return pulumi.get(self, "data_attribute_binding_id")

    @data_attribute_binding_id.setter
    def data_attribute_binding_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_attribute_binding_id", value)

    @property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Optional. List of attributes to be associated with the resource, provided in the form: projects/{project}/locations/{location}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id}
        """
        return pulumi.get(self, "attributes")

    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "attributes", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Description of the DataAttributeBinding.
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
        This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Etags must be used when calling the DeleteDataAttributeBinding and the UpdateDataAttributeBinding method.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional. User-defined labels for the DataAttributeBinding.
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
    def paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDataplexV1DataAttributeBindingPathArgs']]]]:
        """
        Optional. The list of paths for items within the associated resource (eg. columns and partitions within a table) along with attribute bindings.
        """
        return pulumi.get(self, "paths")

    @paths.setter
    def paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDataplexV1DataAttributeBindingPathArgs']]]]):
        pulumi.set(self, "paths", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Immutable. The resource name of the resource that is associated to attributes. Presently, only entity resource is supported in the form: projects/{project}/locations/{location}/lakes/{lake}/zones/{zone}/entities/{entity_id} Must belong in the same project and region as the attribute binding, and there can only exist one active binding for a resource.
        """
        return pulumi.get(self, "resource")

    @resource.setter
    def resource(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource", value)


class DataAttributeBinding(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 data_attribute_binding_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 paths: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDataplexV1DataAttributeBindingPathArgs']]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 resource: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a DataAttributeBinding resource.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] attributes: Optional. List of attributes to be associated with the resource, provided in the form: projects/{project}/locations/{location}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id}
        :param pulumi.Input[str] data_attribute_binding_id: Required. DataAttributeBinding identifier. * Must contain only lowercase letters, numbers and hyphens. * Must start with a letter. * Must be between 1-63 characters. * Must end with a number or a letter. * Must be unique within the Location.
        :param pulumi.Input[str] description: Optional. Description of the DataAttributeBinding.
        :param pulumi.Input[str] display_name: Optional. User friendly display name.
        :param pulumi.Input[str] etag: This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Etags must be used when calling the DeleteDataAttributeBinding and the UpdateDataAttributeBinding method.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. User-defined labels for the DataAttributeBinding.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDataplexV1DataAttributeBindingPathArgs']]]] paths: Optional. The list of paths for items within the associated resource (eg. columns and partitions within a table) along with attribute bindings.
        :param pulumi.Input[str] resource: Optional. Immutable. The resource name of the resource that is associated to attributes. Presently, only entity resource is supported in the form: projects/{project}/locations/{location}/lakes/{lake}/zones/{zone}/entities/{entity_id} Must belong in the same project and region as the attribute binding, and there can only exist one active binding for a resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataAttributeBindingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a DataAttributeBinding resource.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param DataAttributeBindingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataAttributeBindingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 data_attribute_binding_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 paths: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDataplexV1DataAttributeBindingPathArgs']]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 resource: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataAttributeBindingArgs.__new__(DataAttributeBindingArgs)

            __props__.__dict__["attributes"] = attributes
            if data_attribute_binding_id is None and not opts.urn:
                raise TypeError("Missing required property 'data_attribute_binding_id'")
            __props__.__dict__["data_attribute_binding_id"] = data_attribute_binding_id
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["etag"] = etag
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["paths"] = paths
            __props__.__dict__["project"] = project
            __props__.__dict__["resource"] = resource
            __props__.__dict__["create_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["uid"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["dataAttributeBindingId", "location", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DataAttributeBinding, __self__).__init__(
            'google-native:dataplex/v1:DataAttributeBinding',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DataAttributeBinding':
        """
        Get an existing DataAttributeBinding resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DataAttributeBindingArgs.__new__(DataAttributeBindingArgs)

        __props__.__dict__["attributes"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["data_attribute_binding_id"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["paths"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["resource"] = None
        __props__.__dict__["uid"] = None
        __props__.__dict__["update_time"] = None
        return DataAttributeBinding(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Sequence[str]]:
        """
        Optional. List of attributes to be associated with the resource, provided in the form: projects/{project}/locations/{location}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id}
        """
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time when the DataAttributeBinding was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dataAttributeBindingId")
    def data_attribute_binding_id(self) -> pulumi.Output[str]:
        """
        Required. DataAttributeBinding identifier. * Must contain only lowercase letters, numbers and hyphens. * Must start with a letter. * Must be between 1-63 characters. * Must end with a number or a letter. * Must be unique within the Location.
        """
        return pulumi.get(self, "data_attribute_binding_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Optional. Description of the DataAttributeBinding.
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
        This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Etags must be used when calling the DeleteDataAttributeBinding and the UpdateDataAttributeBinding method.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. User-defined labels for the DataAttributeBinding.
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
        The relative resource name of the Data Attribute Binding, of the form: projects/{project_number}/locations/{location}/dataAttributeBindings/{data_attribute_binding_id}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def paths(self) -> pulumi.Output[Sequence['outputs.GoogleCloudDataplexV1DataAttributeBindingPathResponse']]:
        """
        Optional. The list of paths for items within the associated resource (eg. columns and partitions within a table) along with attribute bindings.
        """
        return pulumi.get(self, "paths")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def resource(self) -> pulumi.Output[str]:
        """
        Optional. Immutable. The resource name of the resource that is associated to attributes. Presently, only entity resource is supported in the form: projects/{project}/locations/{location}/lakes/{lake}/zones/{zone}/entities/{entity_id} Must belong in the same project and region as the attribute binding, and there can only exist one active binding for a resource.
        """
        return pulumi.get(self, "resource")

    @property
    @pulumi.getter
    def uid(self) -> pulumi.Output[str]:
        """
        System generated globally unique ID for the DataAttributeBinding. This ID will be different if the DataAttributeBinding is deleted and re-created with the same name.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The time when the DataAttributeBinding was last updated.
        """
        return pulumi.get(self, "update_time")

