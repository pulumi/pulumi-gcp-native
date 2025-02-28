// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dialogflow.V3.Inputs
{

    /// <summary>
    /// The output from the virtual agent.
    /// </summary>
    public sealed class GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Page on which the utterance was spoken. Only name and displayName will be set.
        /// </summary>
        [Input("currentPage")]
        public Input<Inputs.GoogleCloudDialogflowCxV3PageArgs>? CurrentPage { get; set; }

        [Input("diagnosticInfo", required: true)]
        private InputMap<object>? _diagnosticInfo;

        /// <summary>
        /// Input only. The diagnostic info output for the turn. Required to calculate the testing coverage.
        /// </summary>
        public InputMap<object> DiagnosticInfo
        {
            get => _diagnosticInfo ?? (_diagnosticInfo = new InputMap<object>());
            set => _diagnosticInfo = value;
        }

        [Input("sessionParameters")]
        private InputMap<object>? _sessionParameters;

        /// <summary>
        /// The session parameters available to the bot at this point.
        /// </summary>
        public InputMap<object> SessionParameters
        {
            get => _sessionParameters ?? (_sessionParameters = new InputMap<object>());
            set => _sessionParameters = value;
        }

        /// <summary>
        /// Response error from the agent in the test result. If set, other output is empty.
        /// </summary>
        [Input("status")]
        public Input<Inputs.GoogleRpcStatusArgs>? Status { get; set; }

        [Input("textResponses")]
        private InputList<Inputs.GoogleCloudDialogflowCxV3ResponseMessageTextArgs>? _textResponses;

        /// <summary>
        /// The text responses from the agent for the turn.
        /// </summary>
        public InputList<Inputs.GoogleCloudDialogflowCxV3ResponseMessageTextArgs> TextResponses
        {
            get => _textResponses ?? (_textResponses = new InputList<Inputs.GoogleCloudDialogflowCxV3ResponseMessageTextArgs>());
            set => _textResponses = value;
        }

        /// <summary>
        /// The Intent that triggered the response. Only name and displayName will be set.
        /// </summary>
        [Input("triggeredIntent")]
        public Input<Inputs.GoogleCloudDialogflowCxV3IntentArgs>? TriggeredIntent { get; set; }

        public GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputArgs()
        {
        }
        public static new GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputArgs Empty => new GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutputArgs();
    }
}
