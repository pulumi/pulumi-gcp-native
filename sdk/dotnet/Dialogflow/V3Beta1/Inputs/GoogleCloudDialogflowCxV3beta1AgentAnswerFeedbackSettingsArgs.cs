// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dialogflow.V3Beta1.Inputs
{

    /// <summary>
    /// Settings for answer feedback collection.
    /// </summary>
    public sealed class GoogleCloudDialogflowCxV3beta1AgentAnswerFeedbackSettingsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. If enabled, end users will be able to provide answer feedback to Dialogflow responses. Feature works only if interaction logging is enabled in the Dialogflow agent.
        /// </summary>
        [Input("enableAnswerFeedback")]
        public Input<bool>? EnableAnswerFeedback { get; set; }

        public GoogleCloudDialogflowCxV3beta1AgentAnswerFeedbackSettingsArgs()
        {
        }
        public static new GoogleCloudDialogflowCxV3beta1AgentAnswerFeedbackSettingsArgs Empty => new GoogleCloudDialogflowCxV3beta1AgentAnswerFeedbackSettingsArgs();
    }
}
