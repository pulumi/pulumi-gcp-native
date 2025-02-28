// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dialogflow.V2Beta1.Outputs
{

    /// <summary>
    /// Opens the given URI.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionResponse
    {
        /// <summary>
        /// The HTTP or HTTPS scheme URI.
        /// </summary>
        public readonly string Uri;

        [OutputConstructor]
        private GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriActionResponse(string uri)
        {
            Uri = uri;
        }
    }
}
