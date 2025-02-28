// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dialogflow.V3.Outputs
{

    /// <summary>
    /// The input from the human user.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudDialogflowCxV3ConversationTurnUserInputResponse
    {
        /// <summary>
        /// Whether sentiment analysis is enabled.
        /// </summary>
        public readonly bool EnableSentimentAnalysis;
        /// <summary>
        /// Parameters that need to be injected into the conversation during intent detection.
        /// </summary>
        public readonly ImmutableDictionary<string, object> InjectedParameters;
        /// <summary>
        /// Supports text input, event input, dtmf input in the test case.
        /// </summary>
        public readonly Outputs.GoogleCloudDialogflowCxV3QueryInputResponse Input;
        /// <summary>
        /// If webhooks should be allowed to trigger in response to the user utterance. Often if parameters are injected, webhooks should not be enabled.
        /// </summary>
        public readonly bool IsWebhookEnabled;

        [OutputConstructor]
        private GoogleCloudDialogflowCxV3ConversationTurnUserInputResponse(
            bool enableSentimentAnalysis,

            ImmutableDictionary<string, object> injectedParameters,

            Outputs.GoogleCloudDialogflowCxV3QueryInputResponse input,

            bool isWebhookEnabled)
        {
            EnableSentimentAnalysis = enableSentimentAnalysis;
            InjectedParameters = injectedParameters;
            Input = input;
            IsWebhookEnabled = isWebhookEnabled;
        }
    }
}
