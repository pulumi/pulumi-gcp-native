# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'InstancePolicyProvisioningModel',
    'LifecyclePolicyAction',
    'LogsPolicyDestination',
    'MessageNewJobState',
    'MessageNewTaskState',
    'MessageType',
    'TaskGroupSchedulingPolicy',
]


class InstancePolicyProvisioningModel(str, Enum):
    """
    The provisioning model.
    """
    PROVISIONING_MODEL_UNSPECIFIED = "PROVISIONING_MODEL_UNSPECIFIED"
    """
    Unspecified.
    """
    STANDARD = "STANDARD"
    """
    Standard VM.
    """
    SPOT = "SPOT"
    """
    SPOT VM.
    """
    PREEMPTIBLE = "PREEMPTIBLE"
    """
    Preemptible VM (PVM). Above SPOT VM is the preferable model for preemptible VM instances: the old preemptible VM model (indicated by this field) is the older model, and has been migrated to use the SPOT model as the underlying technology. This old model will still be supported.
    """


class LifecyclePolicyAction(str, Enum):
    """
    Action to execute when ActionCondition is true. When RETRY_TASK is specified, we will retry failed tasks if we notice any exit code match and fail tasks if no match is found. Likewise, when FAIL_TASK is specified, we will fail tasks if we notice any exit code match and retry tasks if no match is found.
    """
    ACTION_UNSPECIFIED = "ACTION_UNSPECIFIED"
    """
    Action unspecified.
    """
    RETRY_TASK = "RETRY_TASK"
    """
    Action that tasks in the group will be scheduled to re-execute.
    """
    FAIL_TASK = "FAIL_TASK"
    """
    Action that tasks in the group will be stopped immediately.
    """


class LogsPolicyDestination(str, Enum):
    """
    Where logs should be saved.
    """
    DESTINATION_UNSPECIFIED = "DESTINATION_UNSPECIFIED"
    """
    Logs are not preserved.
    """
    CLOUD_LOGGING = "CLOUD_LOGGING"
    """
    Logs are streamed to Cloud Logging.
    """
    PATH = "PATH"
    """
    Logs are saved to a file path.
    """


class MessageNewJobState(str, Enum):
    """
    The new job state.
    """
    STATE_UNSPECIFIED = "STATE_UNSPECIFIED"
    """
    Job state unspecified.
    """
    QUEUED = "QUEUED"
    """
    Job is admitted (validated and persisted) and waiting for resources.
    """
    SCHEDULED = "SCHEDULED"
    """
    Job is scheduled to run as soon as resource allocation is ready. The resource allocation may happen at a later time but with a high chance to succeed.
    """
    RUNNING = "RUNNING"
    """
    Resource allocation has been successful. At least one Task in the Job is RUNNING.
    """
    SUCCEEDED = "SUCCEEDED"
    """
    All Tasks in the Job have finished successfully.
    """
    FAILED = "FAILED"
    """
    At least one Task in the Job has failed.
    """
    DELETION_IN_PROGRESS = "DELETION_IN_PROGRESS"
    """
    The Job will be deleted, but has not been deleted yet. Typically this is because resources used by the Job are still being cleaned up.
    """


class MessageNewTaskState(str, Enum):
    """
    The new task state.
    """
    STATE_UNSPECIFIED = "STATE_UNSPECIFIED"
    """
    Unknown state.
    """
    PENDING = "PENDING"
    """
    The Task is created and waiting for resources.
    """
    ASSIGNED = "ASSIGNED"
    """
    The Task is assigned to at least one VM.
    """
    RUNNING = "RUNNING"
    """
    The Task is running.
    """
    FAILED = "FAILED"
    """
    The Task has failed.
    """
    SUCCEEDED = "SUCCEEDED"
    """
    The Task has succeeded.
    """
    UNEXECUTED = "UNEXECUTED"
    """
    The Task has not been executed when the Job finishes.
    """


class MessageType(str, Enum):
    """
    The message type.
    """
    TYPE_UNSPECIFIED = "TYPE_UNSPECIFIED"
    """
    Unspecified.
    """
    JOB_STATE_CHANGED = "JOB_STATE_CHANGED"
    """
    Notify users that the job state has changed.
    """
    TASK_STATE_CHANGED = "TASK_STATE_CHANGED"
    """
    Notify users that the task state has changed.
    """


class TaskGroupSchedulingPolicy(str, Enum):
    """
    Scheduling policy for Tasks in the TaskGroup. The default value is AS_SOON_AS_POSSIBLE.
    """
    SCHEDULING_POLICY_UNSPECIFIED = "SCHEDULING_POLICY_UNSPECIFIED"
    """
    Unspecified.
    """
    AS_SOON_AS_POSSIBLE = "AS_SOON_AS_POSSIBLE"
    """
    Run Tasks as soon as resources are available. Tasks might be executed in parallel depending on parallelism and task_count values.
    """
    IN_ORDER = "IN_ORDER"
    """
    Run Tasks sequentially with increased task index.
    """
