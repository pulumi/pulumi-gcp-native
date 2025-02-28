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
    /// Indicates that the conversation succeeded, i.e., the bot handled the issue that the customer talked to it about. Dialogflow only uses this to determine which conversations should be counted as successful and doesn't process the metadata in this message in any way. Note that Dialogflow also considers conversations that get to the conversation end page as successful even if they don't return ConversationSuccess. You may set this, for example: * In the entry_fulfillment of a Page if entering the page indicates that the conversation succeeded. * In a webhook response when you determine that you handled the customer issue.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessResponse
    {
        /// <summary>
        /// Custom metadata. Dialogflow doesn't impose any structure on this.
        /// </summary>
        public readonly ImmutableDictionary<string, object> Metadata;

        [OutputConstructor]
        private GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccessResponse(ImmutableDictionary<string, object> metadata)
        {
            Metadata = metadata;
        }
    }
}
