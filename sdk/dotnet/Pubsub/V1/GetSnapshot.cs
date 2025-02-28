// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Pubsub.V1
{
    public static class GetSnapshot
    {
        /// <summary>
        /// Gets the configuration details of a snapshot. Snapshots are used in [Seek](https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot.
        /// </summary>
        public static Task<GetSnapshotResult> InvokeAsync(GetSnapshotArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetSnapshotResult>("google-native:pubsub/v1:getSnapshot", args ?? new GetSnapshotArgs(), options.WithDefaults());

        /// <summary>
        /// Gets the configuration details of a snapshot. Snapshots are used in [Seek](https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot.
        /// </summary>
        public static Output<GetSnapshotResult> Invoke(GetSnapshotInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetSnapshotResult>("google-native:pubsub/v1:getSnapshot", args ?? new GetSnapshotInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSnapshotArgs : global::Pulumi.InvokeArgs
    {
        [Input("project")]
        public string? Project { get; set; }

        [Input("snapshotId", required: true)]
        public string SnapshotId { get; set; } = null!;

        public GetSnapshotArgs()
        {
        }
        public static new GetSnapshotArgs Empty => new GetSnapshotArgs();
    }

    public sealed class GetSnapshotInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("snapshotId", required: true)]
        public Input<string> SnapshotId { get; set; } = null!;

        public GetSnapshotInvokeArgs()
        {
        }
        public static new GetSnapshotInvokeArgs Empty => new GetSnapshotInvokeArgs();
    }


    [OutputType]
    public sealed class GetSnapshotResult
    {
        /// <summary>
        /// Optional. The snapshot is guaranteed to exist up until this time. A newly-created snapshot expires no later than 7 days from the time of its creation. Its exact lifetime is determined at creation by the existing backlog in the source subscription. Specifically, the lifetime of the snapshot is `7 days - (age of oldest unacked message in the subscription)`. For example, consider a subscription whose oldest unacked message is 3 days old. If a snapshot is created from this subscription, the snapshot -- which will always capture this 3-day-old backlog as long as the snapshot exists -- will expire in 4 days. The service will refuse to create a snapshot that would expire in less than 1 hour after creation.
        /// </summary>
        public readonly string ExpireTime;
        /// <summary>
        /// Optional. See [Creating and managing labels] (https://cloud.google.com/pubsub/docs/labels).
        /// </summary>
        public readonly ImmutableDictionary<string, string> Labels;
        /// <summary>
        /// Optional. The name of the snapshot.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Optional. The name of the topic from which this snapshot is retaining messages.
        /// </summary>
        public readonly string Topic;

        [OutputConstructor]
        private GetSnapshotResult(
            string expireTime,

            ImmutableDictionary<string, string> labels,

            string name,

            string topic)
        {
            ExpireTime = expireTime;
            Labels = labels;
            Name = name;
            Topic = topic;
        }
    }
}
