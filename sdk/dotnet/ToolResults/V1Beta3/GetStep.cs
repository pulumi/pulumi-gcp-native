// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.ToolResults.V1Beta3
{
    public static class GetStep
    {
        /// <summary>
        /// Gets a Step. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to read project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the Step does not exist
        /// </summary>
        public static Task<GetStepResult> InvokeAsync(GetStepArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetStepResult>("google-native:toolresults/v1beta3:getStep", args ?? new GetStepArgs(), options.WithDefaults());

        /// <summary>
        /// Gets a Step. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to read project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the Step does not exist
        /// </summary>
        public static Output<GetStepResult> Invoke(GetStepInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetStepResult>("google-native:toolresults/v1beta3:getStep", args ?? new GetStepInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetStepArgs : global::Pulumi.InvokeArgs
    {
        [Input("executionId", required: true)]
        public string ExecutionId { get; set; } = null!;

        [Input("historyId", required: true)]
        public string HistoryId { get; set; } = null!;

        [Input("project")]
        public string? Project { get; set; }

        [Input("stepId", required: true)]
        public string StepId { get; set; } = null!;

        public GetStepArgs()
        {
        }
        public static new GetStepArgs Empty => new GetStepArgs();
    }

    public sealed class GetStepInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("executionId", required: true)]
        public Input<string> ExecutionId { get; set; } = null!;

        [Input("historyId", required: true)]
        public Input<string> HistoryId { get; set; } = null!;

        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("stepId", required: true)]
        public Input<string> StepId { get; set; } = null!;

        public GetStepInvokeArgs()
        {
        }
        public static new GetStepInvokeArgs Empty => new GetStepInvokeArgs();
    }


    [OutputType]
    public sealed class GetStepResult
    {
        /// <summary>
        /// The time when the step status was set to complete. This value will be set automatically when state transitions to COMPLETE. - In response: set if the execution state is COMPLETE. - In create/update request: never set
        /// </summary>
        public readonly Outputs.TimestampResponse CompletionTime;
        /// <summary>
        /// The time when the step was created. - In response: always set - In create/update request: never set
        /// </summary>
        public readonly Outputs.TimestampResponse CreationTime;
        /// <summary>
        /// A description of this tool For example: mvn clean package -D skipTests=true - In response: present if set by create/update request - In create/update request: optional
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// How much the device resource is used to perform the test. This is the device usage used for billing purpose, which is different from the run_duration, for example, infrastructure failure won't be charged for device usage. PRECONDITION_FAILED will be returned if one attempts to set a device_usage on a step which already has this field set. - In response: present if previously set. - In create request: optional - In update request: optional
        /// </summary>
        public readonly Outputs.DurationResponse DeviceUsageDuration;
        /// <summary>
        /// If the execution containing this step has any dimension_definition set, then this field allows the child to specify the values of the dimensions. The keys must exactly match the dimension_definition of the execution. For example, if the execution has `dimension_definition = ['attempt', 'device']` then a step must define values for those dimensions, eg. `dimension_value = ['attempt': '1', 'device': 'Nexus 6']` If a step does not participate in one dimension of the matrix, the value for that dimension should be empty string. For example, if one of the tests is executed by a runner which does not support retries, the step could have `dimension_value = ['attempt': '', 'device': 'Nexus 6']` If the step does not participate in any dimensions of the matrix, it may leave dimension_value unset. A PRECONDITION_FAILED will be returned if any of the keys do not exist in the dimension_definition of the execution. A PRECONDITION_FAILED will be returned if another step in this execution already has the same name and dimension_value, but differs on other data fields, for example, step field is different. A PRECONDITION_FAILED will be returned if dimension_value is set, and there is a dimension_definition in the execution which is not specified as one of the keys. - In response: present if set by create - In create request: optional - In update request: never set
        /// </summary>
        public readonly ImmutableArray<Outputs.StepDimensionValueEntryResponse> DimensionValue;
        /// <summary>
        /// Whether any of the outputs of this step are images whose thumbnails can be fetched with ListThumbnails. - In response: always set - In create/update request: never set
        /// </summary>
        public readonly bool HasImages;
        /// <summary>
        /// Arbitrary user-supplied key/value pairs that are associated with the step. Users are responsible for managing the key namespace such that keys don't accidentally collide. An INVALID_ARGUMENT will be returned if the number of labels exceeds 100 or if the length of any of the keys or values exceeds 100 characters. - In response: always set - In create request: optional - In update request: optional; any new key/value pair will be added to the map, and any new value for an existing key will update that key's value
        /// </summary>
        public readonly ImmutableArray<Outputs.StepLabelsEntryResponse> Labels;
        /// <summary>
        /// Details when multiple steps are run with the same configuration as a group. These details can be used identify which group this step is part of. It also identifies the groups 'primary step' which indexes all the group members. - In response: present if previously set. - In create request: optional, set iff this step was performed more than once. - In update request: optional
        /// </summary>
        public readonly Outputs.MultiStepResponse MultiStep;
        /// <summary>
        /// A short human-readable name to display in the UI. Maximum of 100 characters. For example: Clean build A PRECONDITION_FAILED will be returned upon creating a new step if it shares its name and dimension_value with an existing step. If two steps represent a similar action, but have different dimension values, they should share the same name. For instance, if the same set of tests is run on two different platforms, the two steps should have the same name. - In response: always set - In create request: always set - In update request: never set
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Classification of the result, for example into SUCCESS or FAILURE - In response: present if set by create/update request - In create/update request: optional
        /// </summary>
        public readonly Outputs.OutcomeResponse Outcome;
        /// <summary>
        /// How long it took for this step to run. If unset, this is set to the difference between creation_time and completion_time when the step is set to the COMPLETE state. In some cases, it is appropriate to set this value separately: For instance, if a step is created, but the operation it represents is queued for a few minutes before it executes, it would be appropriate not to include the time spent queued in its run_duration. PRECONDITION_FAILED will be returned if one attempts to set a run_duration on a step which already has this field set. - In response: present if previously set; always present on COMPLETE step - In create request: optional - In update request: optional
        /// </summary>
        public readonly Outputs.DurationResponse RunDuration;
        /// <summary>
        /// The initial state is IN_PROGRESS. The only legal state transitions are * IN_PROGRESS -&gt; COMPLETE A PRECONDITION_FAILED will be returned if an invalid transition is requested. It is valid to create Step with a state set to COMPLETE. The state can only be set to COMPLETE once. A PRECONDITION_FAILED will be returned if the state is set to COMPLETE multiple times. - In response: always set - In create/update request: optional
        /// </summary>
        public readonly string State;
        /// <summary>
        /// A unique identifier within a Execution for this Step. Returns INVALID_ARGUMENT if this field is set or overwritten by the caller. - In response: always set - In create/update request: never set
        /// </summary>
        public readonly string StepId;
        /// <summary>
        /// An execution of a test runner.
        /// </summary>
        public readonly Outputs.TestExecutionStepResponse TestExecutionStep;
        /// <summary>
        /// An execution of a tool (used for steps we don't explicitly support).
        /// </summary>
        public readonly Outputs.ToolExecutionStepResponse ToolExecutionStep;

        [OutputConstructor]
        private GetStepResult(
            Outputs.TimestampResponse completionTime,

            Outputs.TimestampResponse creationTime,

            string description,

            Outputs.DurationResponse deviceUsageDuration,

            ImmutableArray<Outputs.StepDimensionValueEntryResponse> dimensionValue,

            bool hasImages,

            ImmutableArray<Outputs.StepLabelsEntryResponse> labels,

            Outputs.MultiStepResponse multiStep,

            string name,

            Outputs.OutcomeResponse outcome,

            Outputs.DurationResponse runDuration,

            string state,

            string stepId,

            Outputs.TestExecutionStepResponse testExecutionStep,

            Outputs.ToolExecutionStepResponse toolExecutionStep)
        {
            CompletionTime = completionTime;
            CreationTime = creationTime;
            Description = description;
            DeviceUsageDuration = deviceUsageDuration;
            DimensionValue = dimensionValue;
            HasImages = hasImages;
            Labels = labels;
            MultiStep = multiStep;
            Name = name;
            Outcome = outcome;
            RunDuration = runDuration;
            State = state;
            StepId = stepId;
            TestExecutionStep = testExecutionStep;
            ToolExecutionStep = toolExecutionStep;
        }
    }
}
