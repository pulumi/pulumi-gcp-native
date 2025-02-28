// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Connectors.V1.Inputs
{

    /// <summary>
    /// Endpoint message includes details of the Destination endpoint.
    /// </summary>
    public sealed class EndPointArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The URI of the Endpoint.
        /// </summary>
        [Input("endpointUri")]
        public Input<string>? EndpointUri { get; set; }

        [Input("headers")]
        private InputList<Inputs.HeaderArgs>? _headers;

        /// <summary>
        /// List of Header to be added to the Endpoint.
        /// </summary>
        public InputList<Inputs.HeaderArgs> Headers
        {
            get => _headers ?? (_headers = new InputList<Inputs.HeaderArgs>());
            set => _headers = value;
        }

        public EndPointArgs()
        {
        }
        public static new EndPointArgs Empty => new EndPointArgs();
    }
}
