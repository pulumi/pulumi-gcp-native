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

__all__ = ['EngineArgs', 'Engine']

@pulumi.input_type
class EngineArgs:
    def __init__(__self__, *,
                 collection_id: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 engine_id: pulumi.Input[str],
                 solution_type: pulumi.Input['EngineSolutionType'],
                 chat_engine_config: Optional[pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfigArgs']] = None,
                 common_config: Optional[pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineCommonConfigArgs']] = None,
                 data_store_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 industry_vertical: Optional[pulumi.Input['EngineIndustryVertical']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 media_recommendation_engine_config: Optional[pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 search_engine_config: Optional[pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfigArgs']] = None,
                 similar_documents_config: Optional[pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineSimilarDocumentsEngineConfigArgs']] = None):
        """
        The set of arguments for constructing a Engine resource.
        :param pulumi.Input[str] display_name: The display name of the engine. Should be human readable. UTF-8 encoded string with limit of 1024 characters.
        :param pulumi.Input[str] engine_id: Required. The ID to use for the Engine, which will become the final component of the Engine's resource name. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. Otherwise, an INVALID_ARGUMENT error is returned.
        :param pulumi.Input['EngineSolutionType'] solution_type: The solutions of the engine.
        :param pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfigArgs'] chat_engine_config: Configurations for the Chat Engine. Only applicable if solution_type is SOLUTION_TYPE_CHAT.
        :param pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineCommonConfigArgs'] common_config: Common config spec that specifies the metadata of the engine.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] data_store_ids: The data stores associated with this engine. For SOLUTION_TYPE_SEARCH and SOLUTION_TYPE_RECOMMENDATION type of engines, they can only associate with at most one data store. If solution_type is SOLUTION_TYPE_CHAT, multiple DataStores in the same Collection can be associated here. Note that when used in CreateEngineRequest, one DataStore id must be provided as the system will use it for necessary intializations.
        :param pulumi.Input['EngineIndustryVertical'] industry_vertical: The industry vertical that the engine registers. The restriction of the Engine industry vertical is based on DataStore: If unspecified, default to `GENERIC`. Vertical on Engine has to match vertical of the DataStore liniked to the engine.
        :param pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigArgs'] media_recommendation_engine_config: Configurations for the Media Engine. Only applicable on the data stores with solution_type SOLUTION_TYPE_RECOMMENDATION and IndustryVertical.MEDIA vertical.
        :param pulumi.Input[str] name: Immutable. The fully qualified resource name of the engine. This field must be a UTF-8 encoded string with a length limit of 1024 characters. Format: `projects/{project_number}/locations/{location}/collections/{collection}/engines/{engine}` engine should be 1-63 characters, and valid characters are /a-z0-9*/. Otherwise, an INVALID_ARGUMENT error is returned.
        :param pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfigArgs'] search_engine_config: Configurations for the Search Engine. Only applicable if solution_type is SOLUTION_TYPE_SEARCH.
        :param pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineSimilarDocumentsEngineConfigArgs'] similar_documents_config: Additional config specs for a `similar-items` engine.
        """
        pulumi.set(__self__, "collection_id", collection_id)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "engine_id", engine_id)
        pulumi.set(__self__, "solution_type", solution_type)
        if chat_engine_config is not None:
            pulumi.set(__self__, "chat_engine_config", chat_engine_config)
        if common_config is not None:
            pulumi.set(__self__, "common_config", common_config)
        if data_store_ids is not None:
            pulumi.set(__self__, "data_store_ids", data_store_ids)
        if industry_vertical is not None:
            pulumi.set(__self__, "industry_vertical", industry_vertical)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if media_recommendation_engine_config is not None:
            pulumi.set(__self__, "media_recommendation_engine_config", media_recommendation_engine_config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if search_engine_config is not None:
            pulumi.set(__self__, "search_engine_config", search_engine_config)
        if similar_documents_config is not None:
            pulumi.set(__self__, "similar_documents_config", similar_documents_config)

    @property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "collection_id")

    @collection_id.setter
    def collection_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "collection_id", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The display name of the engine. Should be human readable. UTF-8 encoded string with limit of 1024 characters.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="engineId")
    def engine_id(self) -> pulumi.Input[str]:
        """
        Required. The ID to use for the Engine, which will become the final component of the Engine's resource name. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. Otherwise, an INVALID_ARGUMENT error is returned.
        """
        return pulumi.get(self, "engine_id")

    @engine_id.setter
    def engine_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "engine_id", value)

    @property
    @pulumi.getter(name="solutionType")
    def solution_type(self) -> pulumi.Input['EngineSolutionType']:
        """
        The solutions of the engine.
        """
        return pulumi.get(self, "solution_type")

    @solution_type.setter
    def solution_type(self, value: pulumi.Input['EngineSolutionType']):
        pulumi.set(self, "solution_type", value)

    @property
    @pulumi.getter(name="chatEngineConfig")
    def chat_engine_config(self) -> Optional[pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfigArgs']]:
        """
        Configurations for the Chat Engine. Only applicable if solution_type is SOLUTION_TYPE_CHAT.
        """
        return pulumi.get(self, "chat_engine_config")

    @chat_engine_config.setter
    def chat_engine_config(self, value: Optional[pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfigArgs']]):
        pulumi.set(self, "chat_engine_config", value)

    @property
    @pulumi.getter(name="commonConfig")
    def common_config(self) -> Optional[pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineCommonConfigArgs']]:
        """
        Common config spec that specifies the metadata of the engine.
        """
        return pulumi.get(self, "common_config")

    @common_config.setter
    def common_config(self, value: Optional[pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineCommonConfigArgs']]):
        pulumi.set(self, "common_config", value)

    @property
    @pulumi.getter(name="dataStoreIds")
    def data_store_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The data stores associated with this engine. For SOLUTION_TYPE_SEARCH and SOLUTION_TYPE_RECOMMENDATION type of engines, they can only associate with at most one data store. If solution_type is SOLUTION_TYPE_CHAT, multiple DataStores in the same Collection can be associated here. Note that when used in CreateEngineRequest, one DataStore id must be provided as the system will use it for necessary intializations.
        """
        return pulumi.get(self, "data_store_ids")

    @data_store_ids.setter
    def data_store_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "data_store_ids", value)

    @property
    @pulumi.getter(name="industryVertical")
    def industry_vertical(self) -> Optional[pulumi.Input['EngineIndustryVertical']]:
        """
        The industry vertical that the engine registers. The restriction of the Engine industry vertical is based on DataStore: If unspecified, default to `GENERIC`. Vertical on Engine has to match vertical of the DataStore liniked to the engine.
        """
        return pulumi.get(self, "industry_vertical")

    @industry_vertical.setter
    def industry_vertical(self, value: Optional[pulumi.Input['EngineIndustryVertical']]):
        pulumi.set(self, "industry_vertical", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="mediaRecommendationEngineConfig")
    def media_recommendation_engine_config(self) -> Optional[pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigArgs']]:
        """
        Configurations for the Media Engine. Only applicable on the data stores with solution_type SOLUTION_TYPE_RECOMMENDATION and IndustryVertical.MEDIA vertical.
        """
        return pulumi.get(self, "media_recommendation_engine_config")

    @media_recommendation_engine_config.setter
    def media_recommendation_engine_config(self, value: Optional[pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigArgs']]):
        pulumi.set(self, "media_recommendation_engine_config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. The fully qualified resource name of the engine. This field must be a UTF-8 encoded string with a length limit of 1024 characters. Format: `projects/{project_number}/locations/{location}/collections/{collection}/engines/{engine}` engine should be 1-63 characters, and valid characters are /a-z0-9*/. Otherwise, an INVALID_ARGUMENT error is returned.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="searchEngineConfig")
    def search_engine_config(self) -> Optional[pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfigArgs']]:
        """
        Configurations for the Search Engine. Only applicable if solution_type is SOLUTION_TYPE_SEARCH.
        """
        return pulumi.get(self, "search_engine_config")

    @search_engine_config.setter
    def search_engine_config(self, value: Optional[pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfigArgs']]):
        pulumi.set(self, "search_engine_config", value)

    @property
    @pulumi.getter(name="similarDocumentsConfig")
    def similar_documents_config(self) -> Optional[pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineSimilarDocumentsEngineConfigArgs']]:
        """
        Additional config specs for a `similar-items` engine.
        """
        return pulumi.get(self, "similar_documents_config")

    @similar_documents_config.setter
    def similar_documents_config(self, value: Optional[pulumi.Input['GoogleCloudDiscoveryengineV1alphaEngineSimilarDocumentsEngineConfigArgs']]):
        pulumi.set(self, "similar_documents_config", value)


class Engine(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 chat_engine_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfigArgs']]] = None,
                 collection_id: Optional[pulumi.Input[str]] = None,
                 common_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDiscoveryengineV1alphaEngineCommonConfigArgs']]] = None,
                 data_store_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 engine_id: Optional[pulumi.Input[str]] = None,
                 industry_vertical: Optional[pulumi.Input['EngineIndustryVertical']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 media_recommendation_engine_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 search_engine_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfigArgs']]] = None,
                 similar_documents_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDiscoveryengineV1alphaEngineSimilarDocumentsEngineConfigArgs']]] = None,
                 solution_type: Optional[pulumi.Input['EngineSolutionType']] = None,
                 __props__=None):
        """
        Creates a Engine.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfigArgs']] chat_engine_config: Configurations for the Chat Engine. Only applicable if solution_type is SOLUTION_TYPE_CHAT.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDiscoveryengineV1alphaEngineCommonConfigArgs']] common_config: Common config spec that specifies the metadata of the engine.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] data_store_ids: The data stores associated with this engine. For SOLUTION_TYPE_SEARCH and SOLUTION_TYPE_RECOMMENDATION type of engines, they can only associate with at most one data store. If solution_type is SOLUTION_TYPE_CHAT, multiple DataStores in the same Collection can be associated here. Note that when used in CreateEngineRequest, one DataStore id must be provided as the system will use it for necessary intializations.
        :param pulumi.Input[str] display_name: The display name of the engine. Should be human readable. UTF-8 encoded string with limit of 1024 characters.
        :param pulumi.Input[str] engine_id: Required. The ID to use for the Engine, which will become the final component of the Engine's resource name. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. Otherwise, an INVALID_ARGUMENT error is returned.
        :param pulumi.Input['EngineIndustryVertical'] industry_vertical: The industry vertical that the engine registers. The restriction of the Engine industry vertical is based on DataStore: If unspecified, default to `GENERIC`. Vertical on Engine has to match vertical of the DataStore liniked to the engine.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigArgs']] media_recommendation_engine_config: Configurations for the Media Engine. Only applicable on the data stores with solution_type SOLUTION_TYPE_RECOMMENDATION and IndustryVertical.MEDIA vertical.
        :param pulumi.Input[str] name: Immutable. The fully qualified resource name of the engine. This field must be a UTF-8 encoded string with a length limit of 1024 characters. Format: `projects/{project_number}/locations/{location}/collections/{collection}/engines/{engine}` engine should be 1-63 characters, and valid characters are /a-z0-9*/. Otherwise, an INVALID_ARGUMENT error is returned.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfigArgs']] search_engine_config: Configurations for the Search Engine. Only applicable if solution_type is SOLUTION_TYPE_SEARCH.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDiscoveryengineV1alphaEngineSimilarDocumentsEngineConfigArgs']] similar_documents_config: Additional config specs for a `similar-items` engine.
        :param pulumi.Input['EngineSolutionType'] solution_type: The solutions of the engine.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EngineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a Engine.

        :param str resource_name: The name of the resource.
        :param EngineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EngineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 chat_engine_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfigArgs']]] = None,
                 collection_id: Optional[pulumi.Input[str]] = None,
                 common_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDiscoveryengineV1alphaEngineCommonConfigArgs']]] = None,
                 data_store_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 engine_id: Optional[pulumi.Input[str]] = None,
                 industry_vertical: Optional[pulumi.Input['EngineIndustryVertical']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 media_recommendation_engine_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 search_engine_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfigArgs']]] = None,
                 similar_documents_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDiscoveryengineV1alphaEngineSimilarDocumentsEngineConfigArgs']]] = None,
                 solution_type: Optional[pulumi.Input['EngineSolutionType']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EngineArgs.__new__(EngineArgs)

            __props__.__dict__["chat_engine_config"] = chat_engine_config
            if collection_id is None and not opts.urn:
                raise TypeError("Missing required property 'collection_id'")
            __props__.__dict__["collection_id"] = collection_id
            __props__.__dict__["common_config"] = common_config
            __props__.__dict__["data_store_ids"] = data_store_ids
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            if engine_id is None and not opts.urn:
                raise TypeError("Missing required property 'engine_id'")
            __props__.__dict__["engine_id"] = engine_id
            __props__.__dict__["industry_vertical"] = industry_vertical
            __props__.__dict__["location"] = location
            __props__.__dict__["media_recommendation_engine_config"] = media_recommendation_engine_config
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["search_engine_config"] = search_engine_config
            __props__.__dict__["similar_documents_config"] = similar_documents_config
            if solution_type is None and not opts.urn:
                raise TypeError("Missing required property 'solution_type'")
            __props__.__dict__["solution_type"] = solution_type
            __props__.__dict__["chat_engine_metadata"] = None
            __props__.__dict__["create_time"] = None
            __props__.__dict__["recommendation_metadata"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["collectionId", "engineId", "location", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Engine, __self__).__init__(
            'google-native:discoveryengine/v1alpha:Engine',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Engine':
        """
        Get an existing Engine resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EngineArgs.__new__(EngineArgs)

        __props__.__dict__["chat_engine_config"] = None
        __props__.__dict__["chat_engine_metadata"] = None
        __props__.__dict__["collection_id"] = None
        __props__.__dict__["common_config"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["data_store_ids"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["engine_id"] = None
        __props__.__dict__["industry_vertical"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["media_recommendation_engine_config"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["recommendation_metadata"] = None
        __props__.__dict__["search_engine_config"] = None
        __props__.__dict__["similar_documents_config"] = None
        __props__.__dict__["solution_type"] = None
        __props__.__dict__["update_time"] = None
        return Engine(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="chatEngineConfig")
    def chat_engine_config(self) -> pulumi.Output['outputs.GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfigResponse']:
        """
        Configurations for the Chat Engine. Only applicable if solution_type is SOLUTION_TYPE_CHAT.
        """
        return pulumi.get(self, "chat_engine_config")

    @property
    @pulumi.getter(name="chatEngineMetadata")
    def chat_engine_metadata(self) -> pulumi.Output['outputs.GoogleCloudDiscoveryengineV1alphaEngineChatEngineMetadataResponse']:
        """
        Additional information of the Chat Engine. Only applicable if solution_type is SOLUTION_TYPE_CHAT.
        """
        return pulumi.get(self, "chat_engine_metadata")

    @property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "collection_id")

    @property
    @pulumi.getter(name="commonConfig")
    def common_config(self) -> pulumi.Output['outputs.GoogleCloudDiscoveryengineV1alphaEngineCommonConfigResponse']:
        """
        Common config spec that specifies the metadata of the engine.
        """
        return pulumi.get(self, "common_config")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Timestamp the Recommendation Engine was created at.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dataStoreIds")
    def data_store_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The data stores associated with this engine. For SOLUTION_TYPE_SEARCH and SOLUTION_TYPE_RECOMMENDATION type of engines, they can only associate with at most one data store. If solution_type is SOLUTION_TYPE_CHAT, multiple DataStores in the same Collection can be associated here. Note that when used in CreateEngineRequest, one DataStore id must be provided as the system will use it for necessary intializations.
        """
        return pulumi.get(self, "data_store_ids")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The display name of the engine. Should be human readable. UTF-8 encoded string with limit of 1024 characters.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="engineId")
    def engine_id(self) -> pulumi.Output[str]:
        """
        Required. The ID to use for the Engine, which will become the final component of the Engine's resource name. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. Otherwise, an INVALID_ARGUMENT error is returned.
        """
        return pulumi.get(self, "engine_id")

    @property
    @pulumi.getter(name="industryVertical")
    def industry_vertical(self) -> pulumi.Output[str]:
        """
        The industry vertical that the engine registers. The restriction of the Engine industry vertical is based on DataStore: If unspecified, default to `GENERIC`. Vertical on Engine has to match vertical of the DataStore liniked to the engine.
        """
        return pulumi.get(self, "industry_vertical")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mediaRecommendationEngineConfig")
    def media_recommendation_engine_config(self) -> pulumi.Output['outputs.GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigResponse']:
        """
        Configurations for the Media Engine. Only applicable on the data stores with solution_type SOLUTION_TYPE_RECOMMENDATION and IndustryVertical.MEDIA vertical.
        """
        return pulumi.get(self, "media_recommendation_engine_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Immutable. The fully qualified resource name of the engine. This field must be a UTF-8 encoded string with a length limit of 1024 characters. Format: `projects/{project_number}/locations/{location}/collections/{collection}/engines/{engine}` engine should be 1-63 characters, and valid characters are /a-z0-9*/. Otherwise, an INVALID_ARGUMENT error is returned.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="recommendationMetadata")
    def recommendation_metadata(self) -> pulumi.Output['outputs.GoogleCloudDiscoveryengineV1alphaEngineRecommendationMetadataResponse']:
        """
        Additional information of a recommendation engine. Only applicable if solution_type is SOLUTION_TYPE_RECOMMENDATION.
        """
        return pulumi.get(self, "recommendation_metadata")

    @property
    @pulumi.getter(name="searchEngineConfig")
    def search_engine_config(self) -> pulumi.Output['outputs.GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfigResponse']:
        """
        Configurations for the Search Engine. Only applicable if solution_type is SOLUTION_TYPE_SEARCH.
        """
        return pulumi.get(self, "search_engine_config")

    @property
    @pulumi.getter(name="similarDocumentsConfig")
    def similar_documents_config(self) -> pulumi.Output['outputs.GoogleCloudDiscoveryengineV1alphaEngineSimilarDocumentsEngineConfigResponse']:
        """
        Additional config specs for a `similar-items` engine.
        """
        return pulumi.get(self, "similar_documents_config")

    @property
    @pulumi.getter(name="solutionType")
    def solution_type(self) -> pulumi.Output[str]:
        """
        The solutions of the engine.
        """
        return pulumi.get(self, "solution_type")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Timestamp the Recommendation Engine was last updated.
        """
        return pulumi.get(self, "update_time")

