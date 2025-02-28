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
    /// By default, your agent responds to a matched intent with a static response. As an alternative, you can provide a more dynamic response by using fulfillment. When you enable fulfillment for an intent, Dialogflow responds to that intent by calling a service that you define. For example, if an end-user wants to schedule a haircut on Friday, your service can check your database and respond to the end-user with availability information for Friday. For more information, see the [fulfillment guide](https://cloud.google.com/dialogflow/docs/fulfillment-overview).
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudDialogflowV2FulfillmentResponse
    {
        /// <summary>
        /// Optional. The human-readable name of the fulfillment, unique within the agent. This field is not used for Fulfillment in an Environment.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// Optional. Whether fulfillment is enabled.
        /// </summary>
        public readonly bool Enabled;
        /// <summary>
        /// Optional. The field defines whether the fulfillment is enabled for certain features.
        /// </summary>
        public readonly ImmutableArray<Outputs.GoogleCloudDialogflowV2FulfillmentFeatureResponse> Features;
        /// <summary>
        /// Configuration for a generic web service.
        /// </summary>
        public readonly Outputs.GoogleCloudDialogflowV2FulfillmentGenericWebServiceResponse GenericWebService;
        /// <summary>
        /// The unique identifier of the fulfillment. Supported formats: - `projects//agent/fulfillment` - `projects//locations//agent/fulfillment` This field is not used for Fulfillment in an Environment.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private GoogleCloudDialogflowV2FulfillmentResponse(
            string displayName,

            bool enabled,

            ImmutableArray<Outputs.GoogleCloudDialogflowV2FulfillmentFeatureResponse> features,

            Outputs.GoogleCloudDialogflowV2FulfillmentGenericWebServiceResponse genericWebService,

            string name)
        {
            DisplayName = displayName;
            Enabled = enabled;
            Features = features;
            GenericWebService = genericWebService;
            Name = name;
        }
    }
}
