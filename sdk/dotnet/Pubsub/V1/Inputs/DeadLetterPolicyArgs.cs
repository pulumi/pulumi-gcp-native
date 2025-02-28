// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Pubsub.V1.Inputs
{

    /// <summary>
    /// Dead lettering is done on a best effort basis. The same message might be dead lettered multiple times. If validation on any of the fields fails at subscription creation/updation, the create/update subscription request will fail.
    /// </summary>
    public sealed class DeadLetterPolicyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. The name of the topic to which dead letter messages should be published. Format is `projects/{project}/topics/{topic}`.The Pub/Sub service account associated with the enclosing subscription's parent project (i.e., service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com) must have permission to Publish() to this topic. The operation will fail if the topic does not exist. Users should ensure that there is a subscription attached to this topic since messages published to a topic with no subscriptions are lost.
        /// </summary>
        [Input("deadLetterTopic")]
        public Input<string>? DeadLetterTopic { get; set; }

        /// <summary>
        /// Optional. The maximum number of delivery attempts for any message. The value must be between 5 and 100. The number of delivery attempts is defined as 1 + (the sum of number of NACKs and number of times the acknowledgement deadline has been exceeded for the message). A NACK is any call to ModifyAckDeadline with a 0 deadline. Note that client libraries may automatically extend ack_deadlines. This field will be honored on a best effort basis. If this parameter is 0, a default value of 5 is used.
        /// </summary>
        [Input("maxDeliveryAttempts")]
        public Input<int>? MaxDeliveryAttempts { get; set; }

        public DeadLetterPolicyArgs()
        {
        }
        public static new DeadLetterPolicyArgs Empty => new DeadLetterPolicyArgs();
    }
}
