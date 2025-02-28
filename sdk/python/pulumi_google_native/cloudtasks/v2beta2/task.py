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

__all__ = ['TaskArgs', 'Task']

@pulumi.input_type
class TaskArgs:
    def __init__(__self__, *,
                 queue_id: pulumi.Input[str],
                 app_engine_http_request: Optional[pulumi.Input['AppEngineHttpRequestArgs']] = None,
                 http_request: Optional[pulumi.Input['HttpRequestArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 pull_message: Optional[pulumi.Input['PullMessageArgs']] = None,
                 response_view: Optional[pulumi.Input['TaskResponseView']] = None,
                 schedule_time: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Task resource.
        :param pulumi.Input['AppEngineHttpRequestArgs'] app_engine_http_request: App Engine HTTP request that is sent to the task's target. Can be set only if app_engine_http_target is set on the queue. An App Engine task is a task that has AppEngineHttpRequest set.
        :param pulumi.Input['HttpRequestArgs'] http_request: HTTP request that is sent to the task's target. An HTTP task is a task that has HttpRequest set.
        :param pulumi.Input[str] name: Optionally caller-specified in CreateTask. The task name. The task name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID` * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) * `LOCATION_ID` is the canonical ID for the task's location. The list of available locations can be obtained by calling ListLocations. For more information, see https://cloud.google.com/about/locations/. * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters. * `TASK_ID` can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), or underscores (_). The maximum length is 500 characters.
        :param pulumi.Input['PullMessageArgs'] pull_message: LeaseTasks to process the task. Can be set only if pull_target is set on the queue. A pull task is a task that has PullMessage set.
        :param pulumi.Input['TaskResponseView'] response_view: The response_view specifies which subset of the Task will be returned. By default response_view is BASIC; not all information is retrieved by default because some data, such as payloads, might be desirable to return only when needed because of its large size or because of the sensitivity of data that it contains. Authorization for FULL requires `cloudtasks.tasks.fullView` [Google IAM](https://cloud.google.com/iam/) permission on the Task resource.
        :param pulumi.Input[str] schedule_time: The time when the task is scheduled to be attempted. For App Engine queues, this is when the task will be attempted or retried. For pull queues, this is the time when the task is available to be leased; if a task is currently leased, this is the time when the current lease expires, that is, the time that the task was leased plus the lease_duration. `schedule_time` will be truncated to the nearest microsecond.
        """
        pulumi.set(__self__, "queue_id", queue_id)
        if app_engine_http_request is not None:
            pulumi.set(__self__, "app_engine_http_request", app_engine_http_request)
        if http_request is not None:
            pulumi.set(__self__, "http_request", http_request)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if pull_message is not None:
            pulumi.set(__self__, "pull_message", pull_message)
        if response_view is not None:
            pulumi.set(__self__, "response_view", response_view)
        if schedule_time is not None:
            pulumi.set(__self__, "schedule_time", schedule_time)

    @property
    @pulumi.getter(name="queueId")
    def queue_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "queue_id")

    @queue_id.setter
    def queue_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "queue_id", value)

    @property
    @pulumi.getter(name="appEngineHttpRequest")
    def app_engine_http_request(self) -> Optional[pulumi.Input['AppEngineHttpRequestArgs']]:
        """
        App Engine HTTP request that is sent to the task's target. Can be set only if app_engine_http_target is set on the queue. An App Engine task is a task that has AppEngineHttpRequest set.
        """
        return pulumi.get(self, "app_engine_http_request")

    @app_engine_http_request.setter
    def app_engine_http_request(self, value: Optional[pulumi.Input['AppEngineHttpRequestArgs']]):
        pulumi.set(self, "app_engine_http_request", value)

    @property
    @pulumi.getter(name="httpRequest")
    def http_request(self) -> Optional[pulumi.Input['HttpRequestArgs']]:
        """
        HTTP request that is sent to the task's target. An HTTP task is a task that has HttpRequest set.
        """
        return pulumi.get(self, "http_request")

    @http_request.setter
    def http_request(self, value: Optional[pulumi.Input['HttpRequestArgs']]):
        pulumi.set(self, "http_request", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Optionally caller-specified in CreateTask. The task name. The task name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID` * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) * `LOCATION_ID` is the canonical ID for the task's location. The list of available locations can be obtained by calling ListLocations. For more information, see https://cloud.google.com/about/locations/. * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters. * `TASK_ID` can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), or underscores (_). The maximum length is 500 characters.
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
    @pulumi.getter(name="pullMessage")
    def pull_message(self) -> Optional[pulumi.Input['PullMessageArgs']]:
        """
        LeaseTasks to process the task. Can be set only if pull_target is set on the queue. A pull task is a task that has PullMessage set.
        """
        return pulumi.get(self, "pull_message")

    @pull_message.setter
    def pull_message(self, value: Optional[pulumi.Input['PullMessageArgs']]):
        pulumi.set(self, "pull_message", value)

    @property
    @pulumi.getter(name="responseView")
    def response_view(self) -> Optional[pulumi.Input['TaskResponseView']]:
        """
        The response_view specifies which subset of the Task will be returned. By default response_view is BASIC; not all information is retrieved by default because some data, such as payloads, might be desirable to return only when needed because of its large size or because of the sensitivity of data that it contains. Authorization for FULL requires `cloudtasks.tasks.fullView` [Google IAM](https://cloud.google.com/iam/) permission on the Task resource.
        """
        return pulumi.get(self, "response_view")

    @response_view.setter
    def response_view(self, value: Optional[pulumi.Input['TaskResponseView']]):
        pulumi.set(self, "response_view", value)

    @property
    @pulumi.getter(name="scheduleTime")
    def schedule_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time when the task is scheduled to be attempted. For App Engine queues, this is when the task will be attempted or retried. For pull queues, this is the time when the task is available to be leased; if a task is currently leased, this is the time when the current lease expires, that is, the time that the task was leased plus the lease_duration. `schedule_time` will be truncated to the nearest microsecond.
        """
        return pulumi.get(self, "schedule_time")

    @schedule_time.setter
    def schedule_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schedule_time", value)


class Task(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_engine_http_request: Optional[pulumi.Input[pulumi.InputType['AppEngineHttpRequestArgs']]] = None,
                 http_request: Optional[pulumi.Input[pulumi.InputType['HttpRequestArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 pull_message: Optional[pulumi.Input[pulumi.InputType['PullMessageArgs']]] = None,
                 queue_id: Optional[pulumi.Input[str]] = None,
                 response_view: Optional[pulumi.Input['TaskResponseView']] = None,
                 schedule_time: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a task and adds it to a queue. Tasks cannot be updated after creation; there is no UpdateTask command. * For App Engine queues, the maximum task size is 100KB. * For pull queues, the maximum task size is 1MB.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AppEngineHttpRequestArgs']] app_engine_http_request: App Engine HTTP request that is sent to the task's target. Can be set only if app_engine_http_target is set on the queue. An App Engine task is a task that has AppEngineHttpRequest set.
        :param pulumi.Input[pulumi.InputType['HttpRequestArgs']] http_request: HTTP request that is sent to the task's target. An HTTP task is a task that has HttpRequest set.
        :param pulumi.Input[str] name: Optionally caller-specified in CreateTask. The task name. The task name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID` * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) * `LOCATION_ID` is the canonical ID for the task's location. The list of available locations can be obtained by calling ListLocations. For more information, see https://cloud.google.com/about/locations/. * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters. * `TASK_ID` can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), or underscores (_). The maximum length is 500 characters.
        :param pulumi.Input[pulumi.InputType['PullMessageArgs']] pull_message: LeaseTasks to process the task. Can be set only if pull_target is set on the queue. A pull task is a task that has PullMessage set.
        :param pulumi.Input['TaskResponseView'] response_view: The response_view specifies which subset of the Task will be returned. By default response_view is BASIC; not all information is retrieved by default because some data, such as payloads, might be desirable to return only when needed because of its large size or because of the sensitivity of data that it contains. Authorization for FULL requires `cloudtasks.tasks.fullView` [Google IAM](https://cloud.google.com/iam/) permission on the Task resource.
        :param pulumi.Input[str] schedule_time: The time when the task is scheduled to be attempted. For App Engine queues, this is when the task will be attempted or retried. For pull queues, this is the time when the task is available to be leased; if a task is currently leased, this is the time when the current lease expires, that is, the time that the task was leased plus the lease_duration. `schedule_time` will be truncated to the nearest microsecond.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TaskArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a task and adds it to a queue. Tasks cannot be updated after creation; there is no UpdateTask command. * For App Engine queues, the maximum task size is 100KB. * For pull queues, the maximum task size is 1MB.

        :param str resource_name: The name of the resource.
        :param TaskArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TaskArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_engine_http_request: Optional[pulumi.Input[pulumi.InputType['AppEngineHttpRequestArgs']]] = None,
                 http_request: Optional[pulumi.Input[pulumi.InputType['HttpRequestArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 pull_message: Optional[pulumi.Input[pulumi.InputType['PullMessageArgs']]] = None,
                 queue_id: Optional[pulumi.Input[str]] = None,
                 response_view: Optional[pulumi.Input['TaskResponseView']] = None,
                 schedule_time: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TaskArgs.__new__(TaskArgs)

            __props__.__dict__["app_engine_http_request"] = app_engine_http_request
            __props__.__dict__["http_request"] = http_request
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["pull_message"] = pull_message
            if queue_id is None and not opts.urn:
                raise TypeError("Missing required property 'queue_id'")
            __props__.__dict__["queue_id"] = queue_id
            __props__.__dict__["response_view"] = response_view
            __props__.__dict__["schedule_time"] = schedule_time
            __props__.__dict__["create_time"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["view"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["location", "project", "queueId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Task, __self__).__init__(
            'google-native:cloudtasks/v2beta2:Task',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Task':
        """
        Get an existing Task resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TaskArgs.__new__(TaskArgs)

        __props__.__dict__["app_engine_http_request"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["http_request"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["pull_message"] = None
        __props__.__dict__["queue_id"] = None
        __props__.__dict__["schedule_time"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["view"] = None
        return Task(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appEngineHttpRequest")
    def app_engine_http_request(self) -> pulumi.Output['outputs.AppEngineHttpRequestResponse']:
        """
        App Engine HTTP request that is sent to the task's target. Can be set only if app_engine_http_target is set on the queue. An App Engine task is a task that has AppEngineHttpRequest set.
        """
        return pulumi.get(self, "app_engine_http_request")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time that the task was created. `create_time` will be truncated to the nearest second.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="httpRequest")
    def http_request(self) -> pulumi.Output['outputs.HttpRequestResponse']:
        """
        HTTP request that is sent to the task's target. An HTTP task is a task that has HttpRequest set.
        """
        return pulumi.get(self, "http_request")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Optionally caller-specified in CreateTask. The task name. The task name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID` * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) * `LOCATION_ID` is the canonical ID for the task's location. The list of available locations can be obtained by calling ListLocations. For more information, see https://cloud.google.com/about/locations/. * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters. * `TASK_ID` can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), or underscores (_). The maximum length is 500 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="pullMessage")
    def pull_message(self) -> pulumi.Output['outputs.PullMessageResponse']:
        """
        LeaseTasks to process the task. Can be set only if pull_target is set on the queue. A pull task is a task that has PullMessage set.
        """
        return pulumi.get(self, "pull_message")

    @property
    @pulumi.getter(name="queueId")
    def queue_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "queue_id")

    @property
    @pulumi.getter(name="scheduleTime")
    def schedule_time(self) -> pulumi.Output[str]:
        """
        The time when the task is scheduled to be attempted. For App Engine queues, this is when the task will be attempted or retried. For pull queues, this is the time when the task is available to be leased; if a task is currently leased, this is the time when the current lease expires, that is, the time that the task was leased plus the lease_duration. `schedule_time` will be truncated to the nearest microsecond.
        """
        return pulumi.get(self, "schedule_time")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.TaskStatusResponse']:
        """
        The task status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def view(self) -> pulumi.Output[str]:
        """
        The view specifies which subset of the Task has been returned.
        """
        return pulumi.get(self, "view")

