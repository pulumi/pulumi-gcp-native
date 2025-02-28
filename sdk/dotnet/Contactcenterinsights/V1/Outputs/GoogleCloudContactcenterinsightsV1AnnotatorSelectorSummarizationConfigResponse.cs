// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Contactcenterinsights.V1.Outputs
{

    /// <summary>
    /// Configuration for summarization.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudContactcenterinsightsV1AnnotatorSelectorSummarizationConfigResponse
    {
        /// <summary>
        /// Resource name of the Dialogflow conversation profile. Format: projects/{project}/locations/{location}/conversationProfiles/{conversation_profile}
        /// </summary>
        public readonly string ConversationProfile;
        /// <summary>
        /// Default summarization model to be used.
        /// </summary>
        public readonly string SummarizationModel;

        [OutputConstructor]
        private GoogleCloudContactcenterinsightsV1AnnotatorSelectorSummarizationConfigResponse(
            string conversationProfile,

            string summarizationModel)
        {
            ConversationProfile = conversationProfile;
            SummarizationModel = summarizationModel;
        }
    }
}
