# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetDataStoreResult',
    'AwaitableGetDataStoreResult',
    'get_data_store',
    'get_data_store_output',
]

@pulumi.output_type
class GetDataStoreResult:
    def __init__(__self__, content_config=None, create_time=None, default_schema_id=None, display_name=None, industry_vertical=None, name=None, solution_types=None):
        if content_config and not isinstance(content_config, str):
            raise TypeError("Expected argument 'content_config' to be a str")
        pulumi.set(__self__, "content_config", content_config)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if default_schema_id and not isinstance(default_schema_id, str):
            raise TypeError("Expected argument 'default_schema_id' to be a str")
        pulumi.set(__self__, "default_schema_id", default_schema_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if industry_vertical and not isinstance(industry_vertical, str):
            raise TypeError("Expected argument 'industry_vertical' to be a str")
        pulumi.set(__self__, "industry_vertical", industry_vertical)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if solution_types and not isinstance(solution_types, list):
            raise TypeError("Expected argument 'solution_types' to be a list")
        pulumi.set(__self__, "solution_types", solution_types)

    @property
    @pulumi.getter(name="contentConfig")
    def content_config(self) -> str:
        """
        Immutable. The content config of the data store. If this field is unset, the server behavior defaults to ContentConfig.NO_CONTENT.
        """
        return pulumi.get(self, "content_config")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Timestamp the DataStore was created at.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="defaultSchemaId")
    def default_schema_id(self) -> str:
        """
        The id of the default Schema asscociated to this data store.
        """
        return pulumi.get(self, "default_schema_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The data store display name. This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="industryVertical")
    def industry_vertical(self) -> str:
        """
        Immutable. The industry vertical that the data store registers.
        """
        return pulumi.get(self, "industry_vertical")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Immutable. The full resource name of the data store. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}`. This field must be a UTF-8 encoded string with a length limit of 1024 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="solutionTypes")
    def solution_types(self) -> Sequence[str]:
        """
        The solutions that the data store enrolls. Available solutions for each industry_vertical: * `MEDIA`: `SOLUTION_TYPE_RECOMMENDATION` and `SOLUTION_TYPE_SEARCH`. * `SITE_SEARCH`: `SOLUTION_TYPE_SEARCH` is automatically enrolled. Other solutions cannot be enrolled.
        """
        return pulumi.get(self, "solution_types")


class AwaitableGetDataStoreResult(GetDataStoreResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDataStoreResult(
            content_config=self.content_config,
            create_time=self.create_time,
            default_schema_id=self.default_schema_id,
            display_name=self.display_name,
            industry_vertical=self.industry_vertical,
            name=self.name,
            solution_types=self.solution_types)


def get_data_store(collection_id: Optional[str] = None,
                   data_store_id: Optional[str] = None,
                   location: Optional[str] = None,
                   project: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDataStoreResult:
    """
    Gets a DataStore.
    """
    __args__ = dict()
    __args__['collectionId'] = collection_id
    __args__['dataStoreId'] = data_store_id
    __args__['location'] = location
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:discoveryengine/v1alpha:getDataStore', __args__, opts=opts, typ=GetDataStoreResult).value

    return AwaitableGetDataStoreResult(
        content_config=pulumi.get(__ret__, 'content_config'),
        create_time=pulumi.get(__ret__, 'create_time'),
        default_schema_id=pulumi.get(__ret__, 'default_schema_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        industry_vertical=pulumi.get(__ret__, 'industry_vertical'),
        name=pulumi.get(__ret__, 'name'),
        solution_types=pulumi.get(__ret__, 'solution_types'))


@_utilities.lift_output_func(get_data_store)
def get_data_store_output(collection_id: Optional[pulumi.Input[str]] = None,
                          data_store_id: Optional[pulumi.Input[str]] = None,
                          location: Optional[pulumi.Input[str]] = None,
                          project: Optional[pulumi.Input[Optional[str]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDataStoreResult]:
    """
    Gets a DataStore.
    """
    ...
