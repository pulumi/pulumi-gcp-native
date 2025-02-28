// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1Beta1
{
    public static class GetSchedule
    {
        /// <summary>
        /// Gets a Schedule.
        /// </summary>
        public static Task<GetScheduleResult> InvokeAsync(GetScheduleArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetScheduleResult>("google-native:aiplatform/v1beta1:getSchedule", args ?? new GetScheduleArgs(), options.WithDefaults());

        /// <summary>
        /// Gets a Schedule.
        /// </summary>
        public static Output<GetScheduleResult> Invoke(GetScheduleInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetScheduleResult>("google-native:aiplatform/v1beta1:getSchedule", args ?? new GetScheduleInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetScheduleArgs : global::Pulumi.InvokeArgs
    {
        [Input("location", required: true)]
        public string Location { get; set; } = null!;

        [Input("project")]
        public string? Project { get; set; }

        [Input("scheduleId", required: true)]
        public string ScheduleId { get; set; } = null!;

        public GetScheduleArgs()
        {
        }
        public static new GetScheduleArgs Empty => new GetScheduleArgs();
    }

    public sealed class GetScheduleInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("scheduleId", required: true)]
        public Input<string> ScheduleId { get; set; } = null!;

        public GetScheduleInvokeArgs()
        {
        }
        public static new GetScheduleInvokeArgs Empty => new GetScheduleInvokeArgs();
    }


    [OutputType]
    public sealed class GetScheduleResult
    {
        /// <summary>
        /// Optional. Whether new scheduled runs can be queued when max_concurrent_runs limit is reached. If set to true, new runs will be queued instead of skipped. Default to false.
        /// </summary>
        public readonly bool AllowQueueing;
        /// <summary>
        /// Whether to backfill missed runs when the schedule is resumed from PAUSED state. If set to true, all missed runs will be scheduled. New runs will be scheduled after the backfill is complete. Default to false.
        /// </summary>
        public readonly bool CatchUp;
        /// <summary>
        /// Request for PipelineService.CreatePipelineJob. CreatePipelineJobRequest.parent field is required (format: projects/{project}/locations/{location}).
        /// </summary>
        public readonly Outputs.GoogleCloudAiplatformV1beta1CreatePipelineJobRequestResponse CreatePipelineJobRequest;
        /// <summary>
        /// Timestamp when this Schedule was created.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// Cron schedule (https://en.wikipedia.org/wiki/Cron) to launch scheduled runs. To explicitly set a timezone to the cron tab, apply a prefix in the cron tab: "CRON_TZ=${IANA_TIME_ZONE}" or "TZ=${IANA_TIME_ZONE}". The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, "CRON_TZ=America/New_York 1 * * * *", or "TZ=America/New_York 1 * * * *".
        /// </summary>
        public readonly string Cron;
        /// <summary>
        /// User provided name of the Schedule. The name can be up to 128 characters long and can consist of any UTF-8 characters.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// Optional. Timestamp after which no new runs can be scheduled. If specified, The schedule will be completed when either end_time is reached or when scheduled_run_count &gt;= max_run_count. If not specified, new runs will keep getting scheduled until this Schedule is paused or deleted. Already scheduled runs will be allowed to complete. Unset if not specified.
        /// </summary>
        public readonly string EndTime;
        /// <summary>
        /// Timestamp when this Schedule was last paused. Unset if never paused.
        /// </summary>
        public readonly string LastPauseTime;
        /// <summary>
        /// Timestamp when this Schedule was last resumed. Unset if never resumed from pause.
        /// </summary>
        public readonly string LastResumeTime;
        /// <summary>
        /// Response of the last scheduled run. This is the response for starting the scheduled requests and not the execution of the operations/jobs created by the requests (if applicable). Unset if no run has been scheduled yet.
        /// </summary>
        public readonly Outputs.GoogleCloudAiplatformV1beta1ScheduleRunResponseResponse LastScheduledRunResponse;
        /// <summary>
        /// Maximum number of runs that can be started concurrently for this Schedule. This is the limit for starting the scheduled requests and not the execution of the operations/jobs created by the requests (if applicable).
        /// </summary>
        public readonly string MaxConcurrentRunCount;
        /// <summary>
        /// Optional. Maximum run count of the schedule. If specified, The schedule will be completed when either started_run_count &gt;= max_run_count or when end_time is reached. If not specified, new runs will keep getting scheduled until this Schedule is paused or deleted. Already scheduled runs will be allowed to complete. Unset if not specified.
        /// </summary>
        public readonly string MaxRunCount;
        /// <summary>
        /// Immutable. The resource name of the Schedule.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Timestamp when this Schedule should schedule the next run. Having a next_run_time in the past means the runs are being started behind schedule.
        /// </summary>
        public readonly string NextRunTime;
        /// <summary>
        /// Optional. Timestamp after which the first run can be scheduled. Default to Schedule create time if not specified.
        /// </summary>
        public readonly string StartTime;
        /// <summary>
        /// The number of runs started by this schedule.
        /// </summary>
        public readonly string StartedRunCount;
        /// <summary>
        /// The state of this Schedule.
        /// </summary>
        public readonly string State;
        /// <summary>
        /// Timestamp when this Schedule was updated.
        /// </summary>
        public readonly string UpdateTime;

        [OutputConstructor]
        private GetScheduleResult(
            bool allowQueueing,

            bool catchUp,

            Outputs.GoogleCloudAiplatformV1beta1CreatePipelineJobRequestResponse createPipelineJobRequest,

            string createTime,

            string cron,

            string displayName,

            string endTime,

            string lastPauseTime,

            string lastResumeTime,

            Outputs.GoogleCloudAiplatformV1beta1ScheduleRunResponseResponse lastScheduledRunResponse,

            string maxConcurrentRunCount,

            string maxRunCount,

            string name,

            string nextRunTime,

            string startTime,

            string startedRunCount,

            string state,

            string updateTime)
        {
            AllowQueueing = allowQueueing;
            CatchUp = catchUp;
            CreatePipelineJobRequest = createPipelineJobRequest;
            CreateTime = createTime;
            Cron = cron;
            DisplayName = displayName;
            EndTime = endTime;
            LastPauseTime = lastPauseTime;
            LastResumeTime = lastResumeTime;
            LastScheduledRunResponse = lastScheduledRunResponse;
            MaxConcurrentRunCount = maxConcurrentRunCount;
            MaxRunCount = maxRunCount;
            Name = name;
            NextRunTime = nextRunTime;
            StartTime = startTime;
            StartedRunCount = startedRunCount;
            State = state;
            UpdateTime = updateTime;
        }
    }
}
