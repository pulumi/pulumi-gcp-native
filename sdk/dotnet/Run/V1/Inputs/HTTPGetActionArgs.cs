// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Run.V1.Inputs
{

    /// <summary>
    /// HTTPGetAction describes an action based on HTTP Get requests.
    /// </summary>
    public sealed class HTTPGetActionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Not supported by Cloud Run.
        /// </summary>
        [Input("host")]
        public Input<string>? Host { get; set; }

        [Input("httpHeaders")]
        private InputList<Inputs.HTTPHeaderArgs>? _httpHeaders;

        /// <summary>
        /// Custom headers to set in the request. HTTP allows repeated headers.
        /// </summary>
        public InputList<Inputs.HTTPHeaderArgs> HttpHeaders
        {
            get => _httpHeaders ?? (_httpHeaders = new InputList<Inputs.HTTPHeaderArgs>());
            set => _httpHeaders = value;
        }

        /// <summary>
        /// Path to access on the HTTP server.
        /// </summary>
        [Input("path")]
        public Input<string>? Path { get; set; }

        /// <summary>
        /// Port number to access on the container. Number must be in the range 1 to 65535.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// Not supported by Cloud Run.
        /// </summary>
        [Input("scheme")]
        public Input<string>? Scheme { get; set; }

        public HTTPGetActionArgs()
        {
        }
        public static new HTTPGetActionArgs Empty => new HTTPGetActionArgs();
    }
}
