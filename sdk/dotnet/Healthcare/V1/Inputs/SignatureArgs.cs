// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Healthcare.V1.Inputs
{

    /// <summary>
    /// User signature.
    /// </summary>
    public sealed class SignatureArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. An image of the user's signature.
        /// </summary>
        [Input("image")]
        public Input<Inputs.ImageArgs>? Image { get; set; }

        [Input("metadata")]
        private InputMap<string>? _metadata;

        /// <summary>
        /// Optional. Metadata associated with the user's signature. For example, the user's name or the user's title.
        /// </summary>
        public InputMap<string> Metadata
        {
            get => _metadata ?? (_metadata = new InputMap<string>());
            set => _metadata = value;
        }

        /// <summary>
        /// Optional. Timestamp of the signature.
        /// </summary>
        [Input("signatureTime")]
        public Input<string>? SignatureTime { get; set; }

        /// <summary>
        /// User's UUID provided by the client.
        /// </summary>
        [Input("userId", required: true)]
        public Input<string> UserId { get; set; } = null!;

        public SignatureArgs()
        {
        }
        public static new SignatureArgs Empty => new SignatureArgs();
    }
}
