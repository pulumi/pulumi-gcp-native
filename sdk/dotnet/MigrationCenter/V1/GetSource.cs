// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.MigrationCenter.V1
{
    public static class GetSource
    {
        /// <summary>
        /// Gets the details of a source.
        /// </summary>
        public static Task<GetSourceResult> InvokeAsync(GetSourceArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetSourceResult>("google-native:migrationcenter/v1:getSource", args ?? new GetSourceArgs(), options.WithDefaults());

        /// <summary>
        /// Gets the details of a source.
        /// </summary>
        public static Output<GetSourceResult> Invoke(GetSourceInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetSourceResult>("google-native:migrationcenter/v1:getSource", args ?? new GetSourceInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSourceArgs : global::Pulumi.InvokeArgs
    {
        [Input("location", required: true)]
        public string Location { get; set; } = null!;

        [Input("project")]
        public string? Project { get; set; }

        [Input("sourceId", required: true)]
        public string SourceId { get; set; } = null!;

        public GetSourceArgs()
        {
        }
        public static new GetSourceArgs Empty => new GetSourceArgs();
    }

    public sealed class GetSourceInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("sourceId", required: true)]
        public Input<string> SourceId { get; set; } = null!;

        public GetSourceInvokeArgs()
        {
        }
        public static new GetSourceInvokeArgs Empty => new GetSourceInvokeArgs();
    }


    [OutputType]
    public sealed class GetSourceResult
    {
        /// <summary>
        /// The timestamp when the source was created.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// Free-text description.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// User-friendly display name.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// The number of frames that were reported by the source and contained errors.
        /// </summary>
        public readonly int ErrorFrameCount;
        /// <summary>
        /// If `true`, the source is managed by other service(s).
        /// </summary>
        public readonly bool Managed;
        /// <summary>
        /// The full name of the source.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Number of frames that are still being processed.
        /// </summary>
        public readonly int PendingFrameCount;
        /// <summary>
        /// The information confidence of the source. The higher the value, the higher the confidence.
        /// </summary>
        public readonly int Priority;
        /// <summary>
        /// The state of the source.
        /// </summary>
        public readonly string State;
        /// <summary>
        /// Data source type.
        /// </summary>
        public readonly string Type;
        /// <summary>
        /// The timestamp when the source was last updated.
        /// </summary>
        public readonly string UpdateTime;

        [OutputConstructor]
        private GetSourceResult(
            string createTime,

            string description,

            string displayName,

            int errorFrameCount,

            bool managed,

            string name,

            int pendingFrameCount,

            int priority,

            string state,

            string type,

            string updateTime)
        {
            CreateTime = createTime;
            Description = description;
            DisplayName = displayName;
            ErrorFrameCount = errorFrameCount;
            Managed = managed;
            Name = name;
            PendingFrameCount = pendingFrameCount;
            Priority = priority;
            State = state;
            Type = type;
            UpdateTime = updateTime;
        }
    }
}
