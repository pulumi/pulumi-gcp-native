// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dialogflow.V2.Outputs
{

    /// <summary>
    /// Config for suggestion features.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionFeatureConfigResponse
    {
        /// <summary>
        /// Configs of custom conversation model.
        /// </summary>
        public readonly Outputs.GoogleCloudDialogflowV2HumanAgentAssistantConfigConversationModelConfigResponse ConversationModelConfig;
        /// <summary>
        /// Configs for processing conversation.
        /// </summary>
        public readonly Outputs.GoogleCloudDialogflowV2HumanAgentAssistantConfigConversationProcessConfigResponse ConversationProcessConfig;
        /// <summary>
        /// Optional. Disable the logging of search queries sent by human agents. It can prevent those queries from being stored at answer records. Supported features: KNOWLEDGE_SEARCH.
        /// </summary>
        public readonly bool DisableAgentQueryLogging;
        /// <summary>
        /// Automatically iterates all participants and tries to compile suggestions. Supported features: ARTICLE_SUGGESTION, FAQ, DIALOGFLOW_ASSIST, KNOWLEDGE_ASSIST.
        /// </summary>
        public readonly bool EnableEventBasedSuggestion;
        /// <summary>
        /// Configs of query.
        /// </summary>
        public readonly Outputs.GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigResponse QueryConfig;
        /// <summary>
        /// The suggestion feature.
        /// </summary>
        public readonly Outputs.GoogleCloudDialogflowV2SuggestionFeatureResponse SuggestionFeature;
        /// <summary>
        /// Settings of suggestion trigger. Currently, only ARTICLE_SUGGESTION and FAQ will use this field.
        /// </summary>
        public readonly Outputs.GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionTriggerSettingsResponse SuggestionTriggerSettings;

        [OutputConstructor]
        private GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionFeatureConfigResponse(
            Outputs.GoogleCloudDialogflowV2HumanAgentAssistantConfigConversationModelConfigResponse conversationModelConfig,

            Outputs.GoogleCloudDialogflowV2HumanAgentAssistantConfigConversationProcessConfigResponse conversationProcessConfig,

            bool disableAgentQueryLogging,

            bool enableEventBasedSuggestion,

            Outputs.GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigResponse queryConfig,

            Outputs.GoogleCloudDialogflowV2SuggestionFeatureResponse suggestionFeature,

            Outputs.GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionTriggerSettingsResponse suggestionTriggerSettings)
        {
            ConversationModelConfig = conversationModelConfig;
            ConversationProcessConfig = conversationProcessConfig;
            DisableAgentQueryLogging = disableAgentQueryLogging;
            EnableEventBasedSuggestion = enableEventBasedSuggestion;
            QueryConfig = queryConfig;
            SuggestionFeature = suggestionFeature;
            SuggestionTriggerSettings = suggestionTriggerSettings;
        }
    }
}
