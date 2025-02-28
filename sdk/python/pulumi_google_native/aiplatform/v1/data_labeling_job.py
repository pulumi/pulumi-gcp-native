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

__all__ = ['DataLabelingJobArgs', 'DataLabelingJob']

@pulumi.input_type
class DataLabelingJobArgs:
    def __init__(__self__, *,
                 datasets: pulumi.Input[Sequence[pulumi.Input[str]]],
                 display_name: pulumi.Input[str],
                 inputs: Any,
                 inputs_schema_uri: pulumi.Input[str],
                 instruction_uri: pulumi.Input[str],
                 labeler_count: pulumi.Input[int],
                 active_learning_config: Optional[pulumi.Input['GoogleCloudAiplatformV1ActiveLearningConfigArgs']] = None,
                 annotation_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 encryption_spec: Optional[pulumi.Input['GoogleCloudAiplatformV1EncryptionSpecArgs']] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 specialist_pools: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DataLabelingJob resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] datasets: Dataset resource names. Right now we only support labeling from a single Dataset. Format: `projects/{project}/locations/{location}/datasets/{dataset}`
        :param pulumi.Input[str] display_name: The user-defined name of the DataLabelingJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. Display name of a DataLabelingJob.
        :param Any inputs: Input config parameters for the DataLabelingJob.
        :param pulumi.Input[str] inputs_schema_uri: Points to a YAML file stored on Google Cloud Storage describing the config for a specific type of DataLabelingJob. The schema files that can be used here are found in the https://storage.googleapis.com/google-cloud-aiplatform bucket in the /schema/datalabelingjob/inputs/ folder.
        :param pulumi.Input[str] instruction_uri: The Google Cloud Storage location of the instruction pdf. This pdf is shared with labelers, and provides detailed description on how to label DataItems in Datasets.
        :param pulumi.Input[int] labeler_count: Number of labelers to work on each DataItem.
        :param pulumi.Input['GoogleCloudAiplatformV1ActiveLearningConfigArgs'] active_learning_config: Parameters that configure the active learning pipeline. Active learning will label the data incrementally via several iterations. For every iteration, it will select a batch of data based on the sampling strategy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotation_labels: Labels to assign to annotations generated by this DataLabelingJob. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.
        :param pulumi.Input['GoogleCloudAiplatformV1EncryptionSpecArgs'] encryption_spec: Customer-managed encryption key spec for a DataLabelingJob. If set, this DataLabelingJob will be secured by this key. Note: Annotations created in the DataLabelingJob are associated with the EncryptionSpec of the Dataset they are exported to.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels with user-defined metadata to organize your DataLabelingJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. Following system labels exist for each DataLabelingJob: * "aiplatform.googleapis.com/schema": output only, its value is the inputs_schema's title.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] specialist_pools: The SpecialistPools' resource names associated with this job.
        """
        pulumi.set(__self__, "datasets", datasets)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "inputs", inputs)
        pulumi.set(__self__, "inputs_schema_uri", inputs_schema_uri)
        pulumi.set(__self__, "instruction_uri", instruction_uri)
        pulumi.set(__self__, "labeler_count", labeler_count)
        if active_learning_config is not None:
            pulumi.set(__self__, "active_learning_config", active_learning_config)
        if annotation_labels is not None:
            pulumi.set(__self__, "annotation_labels", annotation_labels)
        if encryption_spec is not None:
            pulumi.set(__self__, "encryption_spec", encryption_spec)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if specialist_pools is not None:
            pulumi.set(__self__, "specialist_pools", specialist_pools)

    @property
    @pulumi.getter
    def datasets(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Dataset resource names. Right now we only support labeling from a single Dataset. Format: `projects/{project}/locations/{location}/datasets/{dataset}`
        """
        return pulumi.get(self, "datasets")

    @datasets.setter
    def datasets(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "datasets", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The user-defined name of the DataLabelingJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. Display name of a DataLabelingJob.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def inputs(self) -> Any:
        """
        Input config parameters for the DataLabelingJob.
        """
        return pulumi.get(self, "inputs")

    @inputs.setter
    def inputs(self, value: Any):
        pulumi.set(self, "inputs", value)

    @property
    @pulumi.getter(name="inputsSchemaUri")
    def inputs_schema_uri(self) -> pulumi.Input[str]:
        """
        Points to a YAML file stored on Google Cloud Storage describing the config for a specific type of DataLabelingJob. The schema files that can be used here are found in the https://storage.googleapis.com/google-cloud-aiplatform bucket in the /schema/datalabelingjob/inputs/ folder.
        """
        return pulumi.get(self, "inputs_schema_uri")

    @inputs_schema_uri.setter
    def inputs_schema_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "inputs_schema_uri", value)

    @property
    @pulumi.getter(name="instructionUri")
    def instruction_uri(self) -> pulumi.Input[str]:
        """
        The Google Cloud Storage location of the instruction pdf. This pdf is shared with labelers, and provides detailed description on how to label DataItems in Datasets.
        """
        return pulumi.get(self, "instruction_uri")

    @instruction_uri.setter
    def instruction_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "instruction_uri", value)

    @property
    @pulumi.getter(name="labelerCount")
    def labeler_count(self) -> pulumi.Input[int]:
        """
        Number of labelers to work on each DataItem.
        """
        return pulumi.get(self, "labeler_count")

    @labeler_count.setter
    def labeler_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "labeler_count", value)

    @property
    @pulumi.getter(name="activeLearningConfig")
    def active_learning_config(self) -> Optional[pulumi.Input['GoogleCloudAiplatformV1ActiveLearningConfigArgs']]:
        """
        Parameters that configure the active learning pipeline. Active learning will label the data incrementally via several iterations. For every iteration, it will select a batch of data based on the sampling strategy.
        """
        return pulumi.get(self, "active_learning_config")

    @active_learning_config.setter
    def active_learning_config(self, value: Optional[pulumi.Input['GoogleCloudAiplatformV1ActiveLearningConfigArgs']]):
        pulumi.set(self, "active_learning_config", value)

    @property
    @pulumi.getter(name="annotationLabels")
    def annotation_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Labels to assign to annotations generated by this DataLabelingJob. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.
        """
        return pulumi.get(self, "annotation_labels")

    @annotation_labels.setter
    def annotation_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "annotation_labels", value)

    @property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(self) -> Optional[pulumi.Input['GoogleCloudAiplatformV1EncryptionSpecArgs']]:
        """
        Customer-managed encryption key spec for a DataLabelingJob. If set, this DataLabelingJob will be secured by this key. Note: Annotations created in the DataLabelingJob are associated with the EncryptionSpec of the Dataset they are exported to.
        """
        return pulumi.get(self, "encryption_spec")

    @encryption_spec.setter
    def encryption_spec(self, value: Optional[pulumi.Input['GoogleCloudAiplatformV1EncryptionSpecArgs']]):
        pulumi.set(self, "encryption_spec", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The labels with user-defined metadata to organize your DataLabelingJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. Following system labels exist for each DataLabelingJob: * "aiplatform.googleapis.com/schema": output only, its value is the inputs_schema's title.
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
    @pulumi.getter(name="specialistPools")
    def specialist_pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The SpecialistPools' resource names associated with this job.
        """
        return pulumi.get(self, "specialist_pools")

    @specialist_pools.setter
    def specialist_pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "specialist_pools", value)


class DataLabelingJob(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active_learning_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudAiplatformV1ActiveLearningConfigArgs']]] = None,
                 annotation_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 datasets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 encryption_spec: Optional[pulumi.Input[pulumi.InputType['GoogleCloudAiplatformV1EncryptionSpecArgs']]] = None,
                 inputs: Optional[Any] = None,
                 inputs_schema_uri: Optional[pulumi.Input[str]] = None,
                 instruction_uri: Optional[pulumi.Input[str]] = None,
                 labeler_count: Optional[pulumi.Input[int]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 specialist_pools: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Creates a DataLabelingJob.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GoogleCloudAiplatformV1ActiveLearningConfigArgs']] active_learning_config: Parameters that configure the active learning pipeline. Active learning will label the data incrementally via several iterations. For every iteration, it will select a batch of data based on the sampling strategy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotation_labels: Labels to assign to annotations generated by this DataLabelingJob. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] datasets: Dataset resource names. Right now we only support labeling from a single Dataset. Format: `projects/{project}/locations/{location}/datasets/{dataset}`
        :param pulumi.Input[str] display_name: The user-defined name of the DataLabelingJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. Display name of a DataLabelingJob.
        :param pulumi.Input[pulumi.InputType['GoogleCloudAiplatformV1EncryptionSpecArgs']] encryption_spec: Customer-managed encryption key spec for a DataLabelingJob. If set, this DataLabelingJob will be secured by this key. Note: Annotations created in the DataLabelingJob are associated with the EncryptionSpec of the Dataset they are exported to.
        :param Any inputs: Input config parameters for the DataLabelingJob.
        :param pulumi.Input[str] inputs_schema_uri: Points to a YAML file stored on Google Cloud Storage describing the config for a specific type of DataLabelingJob. The schema files that can be used here are found in the https://storage.googleapis.com/google-cloud-aiplatform bucket in the /schema/datalabelingjob/inputs/ folder.
        :param pulumi.Input[str] instruction_uri: The Google Cloud Storage location of the instruction pdf. This pdf is shared with labelers, and provides detailed description on how to label DataItems in Datasets.
        :param pulumi.Input[int] labeler_count: Number of labelers to work on each DataItem.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels with user-defined metadata to organize your DataLabelingJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. Following system labels exist for each DataLabelingJob: * "aiplatform.googleapis.com/schema": output only, its value is the inputs_schema's title.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] specialist_pools: The SpecialistPools' resource names associated with this job.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataLabelingJobArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a DataLabelingJob.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param DataLabelingJobArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataLabelingJobArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active_learning_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudAiplatformV1ActiveLearningConfigArgs']]] = None,
                 annotation_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 datasets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 encryption_spec: Optional[pulumi.Input[pulumi.InputType['GoogleCloudAiplatformV1EncryptionSpecArgs']]] = None,
                 inputs: Optional[Any] = None,
                 inputs_schema_uri: Optional[pulumi.Input[str]] = None,
                 instruction_uri: Optional[pulumi.Input[str]] = None,
                 labeler_count: Optional[pulumi.Input[int]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 specialist_pools: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataLabelingJobArgs.__new__(DataLabelingJobArgs)

            __props__.__dict__["active_learning_config"] = active_learning_config
            __props__.__dict__["annotation_labels"] = annotation_labels
            if datasets is None and not opts.urn:
                raise TypeError("Missing required property 'datasets'")
            __props__.__dict__["datasets"] = datasets
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["encryption_spec"] = encryption_spec
            if inputs is None and not opts.urn:
                raise TypeError("Missing required property 'inputs'")
            __props__.__dict__["inputs"] = inputs
            if inputs_schema_uri is None and not opts.urn:
                raise TypeError("Missing required property 'inputs_schema_uri'")
            __props__.__dict__["inputs_schema_uri"] = inputs_schema_uri
            if instruction_uri is None and not opts.urn:
                raise TypeError("Missing required property 'instruction_uri'")
            __props__.__dict__["instruction_uri"] = instruction_uri
            if labeler_count is None and not opts.urn:
                raise TypeError("Missing required property 'labeler_count'")
            __props__.__dict__["labeler_count"] = labeler_count
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["project"] = project
            __props__.__dict__["specialist_pools"] = specialist_pools
            __props__.__dict__["create_time"] = None
            __props__.__dict__["current_spend"] = None
            __props__.__dict__["error"] = None
            __props__.__dict__["labeling_progress"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["location", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DataLabelingJob, __self__).__init__(
            'google-native:aiplatform/v1:DataLabelingJob',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DataLabelingJob':
        """
        Get an existing DataLabelingJob resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DataLabelingJobArgs.__new__(DataLabelingJobArgs)

        __props__.__dict__["active_learning_config"] = None
        __props__.__dict__["annotation_labels"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["current_spend"] = None
        __props__.__dict__["datasets"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["encryption_spec"] = None
        __props__.__dict__["error"] = None
        __props__.__dict__["inputs"] = None
        __props__.__dict__["inputs_schema_uri"] = None
        __props__.__dict__["instruction_uri"] = None
        __props__.__dict__["labeler_count"] = None
        __props__.__dict__["labeling_progress"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["specialist_pools"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["update_time"] = None
        return DataLabelingJob(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="activeLearningConfig")
    def active_learning_config(self) -> pulumi.Output['outputs.GoogleCloudAiplatformV1ActiveLearningConfigResponse']:
        """
        Parameters that configure the active learning pipeline. Active learning will label the data incrementally via several iterations. For every iteration, it will select a batch of data based on the sampling strategy.
        """
        return pulumi.get(self, "active_learning_config")

    @property
    @pulumi.getter(name="annotationLabels")
    def annotation_labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Labels to assign to annotations generated by this DataLabelingJob. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.
        """
        return pulumi.get(self, "annotation_labels")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Timestamp when this DataLabelingJob was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="currentSpend")
    def current_spend(self) -> pulumi.Output['outputs.GoogleTypeMoneyResponse']:
        """
        Estimated cost(in US dollars) that the DataLabelingJob has incurred to date.
        """
        return pulumi.get(self, "current_spend")

    @property
    @pulumi.getter
    def datasets(self) -> pulumi.Output[Sequence[str]]:
        """
        Dataset resource names. Right now we only support labeling from a single Dataset. Format: `projects/{project}/locations/{location}/datasets/{dataset}`
        """
        return pulumi.get(self, "datasets")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The user-defined name of the DataLabelingJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. Display name of a DataLabelingJob.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(self) -> pulumi.Output['outputs.GoogleCloudAiplatformV1EncryptionSpecResponse']:
        """
        Customer-managed encryption key spec for a DataLabelingJob. If set, this DataLabelingJob will be secured by this key. Note: Annotations created in the DataLabelingJob are associated with the EncryptionSpec of the Dataset they are exported to.
        """
        return pulumi.get(self, "encryption_spec")

    @property
    @pulumi.getter
    def error(self) -> pulumi.Output['outputs.GoogleRpcStatusResponse']:
        """
        DataLabelingJob errors. It is only populated when job's state is `JOB_STATE_FAILED` or `JOB_STATE_CANCELLED`.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter
    def inputs(self) -> pulumi.Output[Any]:
        """
        Input config parameters for the DataLabelingJob.
        """
        return pulumi.get(self, "inputs")

    @property
    @pulumi.getter(name="inputsSchemaUri")
    def inputs_schema_uri(self) -> pulumi.Output[str]:
        """
        Points to a YAML file stored on Google Cloud Storage describing the config for a specific type of DataLabelingJob. The schema files that can be used here are found in the https://storage.googleapis.com/google-cloud-aiplatform bucket in the /schema/datalabelingjob/inputs/ folder.
        """
        return pulumi.get(self, "inputs_schema_uri")

    @property
    @pulumi.getter(name="instructionUri")
    def instruction_uri(self) -> pulumi.Output[str]:
        """
        The Google Cloud Storage location of the instruction pdf. This pdf is shared with labelers, and provides detailed description on how to label DataItems in Datasets.
        """
        return pulumi.get(self, "instruction_uri")

    @property
    @pulumi.getter(name="labelerCount")
    def labeler_count(self) -> pulumi.Output[int]:
        """
        Number of labelers to work on each DataItem.
        """
        return pulumi.get(self, "labeler_count")

    @property
    @pulumi.getter(name="labelingProgress")
    def labeling_progress(self) -> pulumi.Output[int]:
        """
        Current labeling job progress percentage scaled in interval [0, 100], indicating the percentage of DataItems that has been finished.
        """
        return pulumi.get(self, "labeling_progress")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The labels with user-defined metadata to organize your DataLabelingJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. Following system labels exist for each DataLabelingJob: * "aiplatform.googleapis.com/schema": output only, its value is the inputs_schema's title.
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
        Resource name of the DataLabelingJob.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="specialistPools")
    def specialist_pools(self) -> pulumi.Output[Sequence[str]]:
        """
        The SpecialistPools' resource names associated with this job.
        """
        return pulumi.get(self, "specialist_pools")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The detailed state of the job.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Timestamp when this DataLabelingJob was updated most recently.
        """
        return pulumi.get(self, "update_time")

