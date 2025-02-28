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
    'GetNasJobResult',
    'AwaitableGetNasJobResult',
    'get_nas_job',
    'get_nas_job_output',
]

@pulumi.output_type
class GetNasJobResult:
    def __init__(__self__, create_time=None, display_name=None, enable_restricted_image_training=None, encryption_spec=None, end_time=None, error=None, labels=None, name=None, nas_job_output=None, nas_job_spec=None, start_time=None, state=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if enable_restricted_image_training and not isinstance(enable_restricted_image_training, bool):
            raise TypeError("Expected argument 'enable_restricted_image_training' to be a bool")
        pulumi.set(__self__, "enable_restricted_image_training", enable_restricted_image_training)
        if encryption_spec and not isinstance(encryption_spec, dict):
            raise TypeError("Expected argument 'encryption_spec' to be a dict")
        pulumi.set(__self__, "encryption_spec", encryption_spec)
        if end_time and not isinstance(end_time, str):
            raise TypeError("Expected argument 'end_time' to be a str")
        pulumi.set(__self__, "end_time", end_time)
        if error and not isinstance(error, dict):
            raise TypeError("Expected argument 'error' to be a dict")
        pulumi.set(__self__, "error", error)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if nas_job_output and not isinstance(nas_job_output, dict):
            raise TypeError("Expected argument 'nas_job_output' to be a dict")
        pulumi.set(__self__, "nas_job_output", nas_job_output)
        if nas_job_spec and not isinstance(nas_job_spec, dict):
            raise TypeError("Expected argument 'nas_job_spec' to be a dict")
        pulumi.set(__self__, "nas_job_spec", nas_job_spec)
        if start_time and not isinstance(start_time, str):
            raise TypeError("Expected argument 'start_time' to be a str")
        pulumi.set(__self__, "start_time", start_time)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Time when the NasJob was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the NasJob. The name can be up to 128 characters long and can consist of any UTF-8 characters.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="enableRestrictedImageTraining")
    def enable_restricted_image_training(self) -> bool:
        """
        Optional. Enable a separation of Custom model training and restricted image training for tenant project.
        """
        return pulumi.get(self, "enable_restricted_image_training")

    @property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(self) -> 'outputs.GoogleCloudAiplatformV1EncryptionSpecResponse':
        """
        Customer-managed encryption key options for a NasJob. If this is set, then all resources created by the NasJob will be encrypted with the provided encryption key.
        """
        return pulumi.get(self, "encryption_spec")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> str:
        """
        Time when the NasJob entered any of the following states: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter
    def error(self) -> 'outputs.GoogleRpcStatusResponse':
        """
        Only populated when job's state is JOB_STATE_FAILED or JOB_STATE_CANCELLED.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        The labels with user-defined metadata to organize NasJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name of the NasJob.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nasJobOutput")
    def nas_job_output(self) -> 'outputs.GoogleCloudAiplatformV1NasJobOutputResponse':
        """
        Output of the NasJob.
        """
        return pulumi.get(self, "nas_job_output")

    @property
    @pulumi.getter(name="nasJobSpec")
    def nas_job_spec(self) -> 'outputs.GoogleCloudAiplatformV1NasJobSpecResponse':
        """
        The specification of a NasJob.
        """
        return pulumi.get(self, "nas_job_spec")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> str:
        """
        Time when the NasJob for the first time entered the `JOB_STATE_RUNNING` state.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The detailed state of the job.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        Time when the NasJob was most recently updated.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetNasJobResult(GetNasJobResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNasJobResult(
            create_time=self.create_time,
            display_name=self.display_name,
            enable_restricted_image_training=self.enable_restricted_image_training,
            encryption_spec=self.encryption_spec,
            end_time=self.end_time,
            error=self.error,
            labels=self.labels,
            name=self.name,
            nas_job_output=self.nas_job_output,
            nas_job_spec=self.nas_job_spec,
            start_time=self.start_time,
            state=self.state,
            update_time=self.update_time)


def get_nas_job(location: Optional[str] = None,
                nas_job_id: Optional[str] = None,
                project: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNasJobResult:
    """
    Gets a NasJob
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['nasJobId'] = nas_job_id
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:aiplatform/v1:getNasJob', __args__, opts=opts, typ=GetNasJobResult).value

    return AwaitableGetNasJobResult(
        create_time=pulumi.get(__ret__, 'create_time'),
        display_name=pulumi.get(__ret__, 'display_name'),
        enable_restricted_image_training=pulumi.get(__ret__, 'enable_restricted_image_training'),
        encryption_spec=pulumi.get(__ret__, 'encryption_spec'),
        end_time=pulumi.get(__ret__, 'end_time'),
        error=pulumi.get(__ret__, 'error'),
        labels=pulumi.get(__ret__, 'labels'),
        name=pulumi.get(__ret__, 'name'),
        nas_job_output=pulumi.get(__ret__, 'nas_job_output'),
        nas_job_spec=pulumi.get(__ret__, 'nas_job_spec'),
        start_time=pulumi.get(__ret__, 'start_time'),
        state=pulumi.get(__ret__, 'state'),
        update_time=pulumi.get(__ret__, 'update_time'))


@_utilities.lift_output_func(get_nas_job)
def get_nas_job_output(location: Optional[pulumi.Input[str]] = None,
                       nas_job_id: Optional[pulumi.Input[str]] = None,
                       project: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNasJobResult]:
    """
    Gets a NasJob
    """
    ...
