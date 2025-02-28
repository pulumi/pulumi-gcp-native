// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Integrations.V1Alpha.Outputs
{

    /// <summary>
    /// The task configuration details. This is not the implementation of Task. There might be multiple TaskConfigs for the same Task.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudIntegrationsV1alphaTaskConfigResponse
    {
        /// <summary>
        /// Optional. User-provided description intended to give additional business context about the task.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// Optional. User-provided label that is attached to this TaskConfig in the UI.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// Optional. Optional Error catcher id of the error catch flow which will be executed when execution error happens in the task
        /// </summary>
        public readonly string ErrorCatcherId;
        /// <summary>
        /// Optional. External task type of the task
        /// </summary>
        public readonly string ExternalTaskType;
        /// <summary>
        /// Optional. Determines the number of times the task will be retried on failure and with what retry strategy. This is applicable for asynchronous calls to Eventbus alone (Post To Queue, Schedule etc.).
        /// </summary>
        public readonly Outputs.GoogleCloudIntegrationsV1alphaFailurePolicyResponse FailurePolicy;
        /// <summary>
        /// Optional. If set, overrides the option configured in the Task implementation class.
        /// </summary>
        public readonly string JsonValidationOption;
        /// <summary>
        /// Optional. The set of tasks that are next in line to be executed as per the execution graph defined for the parent event, specified by `event_config_id`. Each of these next tasks are executed only if the condition associated with them evaluates to true.
        /// </summary>
        public readonly ImmutableArray<Outputs.GoogleCloudIntegrationsV1alphaNextTaskResponse> NextTasks;
        /// <summary>
        /// Optional. The policy dictating the execution of the next set of tasks for the current task.
        /// </summary>
        public readonly string NextTasksExecutionPolicy;
        /// <summary>
        /// Optional. The customized parameters the user can pass to this task.
        /// </summary>
        public readonly ImmutableDictionary<string, Outputs.GoogleCloudIntegrationsV1alphaEventParameterResponse> Parameters;
        /// <summary>
        /// Optional. Informs the front-end application where to draw this error catcher config on the UI.
        /// </summary>
        public readonly Outputs.GoogleCloudIntegrationsV1alphaCoordinateResponse Position;
        /// <summary>
        /// Optional. Determines what action to take upon successful task completion.
        /// </summary>
        public readonly Outputs.GoogleCloudIntegrationsV1alphaSuccessPolicyResponse SuccessPolicy;
        /// <summary>
        /// Optional. Determines the number of times the task will be retried on failure and with what retry strategy. This is applicable for synchronous calls to Eventbus alone (Post).
        /// </summary>
        public readonly Outputs.GoogleCloudIntegrationsV1alphaFailurePolicyResponse SynchronousCallFailurePolicy;
        /// <summary>
        /// Optional. The name for the task.
        /// </summary>
        public readonly string Task;
        /// <summary>
        /// Optional. The policy dictating the execution strategy of this task.
        /// </summary>
        public readonly string TaskExecutionStrategy;
        /// <summary>
        /// The identifier of this task within its parent event config, specified by the client. This should be unique among all the tasks belong to the same event config. We use this field as the identifier to find next tasks (via field `next_tasks.task_id`).
        /// </summary>
        public readonly string TaskId;
        /// <summary>
        /// Optional. Used to define task-template name if task is of type task-template
        /// </summary>
        public readonly string TaskTemplate;

        [OutputConstructor]
        private GoogleCloudIntegrationsV1alphaTaskConfigResponse(
            string description,

            string displayName,

            string errorCatcherId,

            string externalTaskType,

            Outputs.GoogleCloudIntegrationsV1alphaFailurePolicyResponse failurePolicy,

            string jsonValidationOption,

            ImmutableArray<Outputs.GoogleCloudIntegrationsV1alphaNextTaskResponse> nextTasks,

            string nextTasksExecutionPolicy,

            ImmutableDictionary<string, Outputs.GoogleCloudIntegrationsV1alphaEventParameterResponse> parameters,

            Outputs.GoogleCloudIntegrationsV1alphaCoordinateResponse position,

            Outputs.GoogleCloudIntegrationsV1alphaSuccessPolicyResponse successPolicy,

            Outputs.GoogleCloudIntegrationsV1alphaFailurePolicyResponse synchronousCallFailurePolicy,

            string task,

            string taskExecutionStrategy,

            string taskId,

            string taskTemplate)
        {
            Description = description;
            DisplayName = displayName;
            ErrorCatcherId = errorCatcherId;
            ExternalTaskType = externalTaskType;
            FailurePolicy = failurePolicy;
            JsonValidationOption = jsonValidationOption;
            NextTasks = nextTasks;
            NextTasksExecutionPolicy = nextTasksExecutionPolicy;
            Parameters = parameters;
            Position = position;
            SuccessPolicy = successPolicy;
            SynchronousCallFailurePolicy = synchronousCallFailurePolicy;
            Task = task;
            TaskExecutionStrategy = taskExecutionStrategy;
            TaskId = taskId;
            TaskTemplate = taskTemplate;
        }
    }
}
