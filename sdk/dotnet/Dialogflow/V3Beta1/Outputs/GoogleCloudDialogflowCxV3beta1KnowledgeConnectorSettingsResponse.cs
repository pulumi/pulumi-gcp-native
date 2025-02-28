// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dialogflow.V3Beta1.Outputs
{

    /// <summary>
    /// The Knowledge Connector settings for this page or flow. This includes information such as the attached Knowledge Bases, and the way to execute fulfillment.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudDialogflowCxV3beta1KnowledgeConnectorSettingsResponse
    {
        /// <summary>
        /// Optional. List of related data store connections.
        /// </summary>
        public readonly ImmutableArray<Outputs.GoogleCloudDialogflowCxV3beta1DataStoreConnectionResponse> DataStoreConnections;
        /// <summary>
        /// Whether Knowledge Connector is enabled or not.
        /// </summary>
        public readonly bool Enabled;
        /// <summary>
        /// The target flow to transition to. Format: `projects//locations//agents//flows/`.
        /// </summary>
        public readonly string TargetFlow;
        /// <summary>
        /// The target page to transition to. Format: `projects//locations//agents//flows//pages/`.
        /// </summary>
        public readonly string TargetPage;
        /// <summary>
        /// The fulfillment to be triggered. When the answers from the Knowledge Connector are selected by Dialogflow, you can utitlize the request scoped parameter `$request.knowledge.answers` (contains up to the 5 highest confidence answers) and `$request.knowledge.questions` (contains the corresponding questions) to construct the fulfillment.
        /// </summary>
        public readonly Outputs.GoogleCloudDialogflowCxV3beta1FulfillmentResponse TriggerFulfillment;

        [OutputConstructor]
        private GoogleCloudDialogflowCxV3beta1KnowledgeConnectorSettingsResponse(
            ImmutableArray<Outputs.GoogleCloudDialogflowCxV3beta1DataStoreConnectionResponse> dataStoreConnections,

            bool enabled,

            string targetFlow,

            string targetPage,

            Outputs.GoogleCloudDialogflowCxV3beta1FulfillmentResponse triggerFulfillment)
        {
            DataStoreConnections = dataStoreConnections;
            Enabled = enabled;
            TargetFlow = targetFlow;
            TargetPage = targetPage;
            TriggerFulfillment = triggerFulfillment;
        }
    }
}
