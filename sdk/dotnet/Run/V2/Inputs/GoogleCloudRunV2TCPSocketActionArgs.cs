// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Run.V2.Inputs
{

    /// <summary>
    /// TCPSocketAction describes an action based on opening a socket
    /// </summary>
    public sealed class GoogleCloudRunV2TCPSocketActionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Port number to access on the container. Must be in the range 1 to 65535. If not specified, defaults to the exposed port of the container, which is the value of container.ports[0].containerPort.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        public GoogleCloudRunV2TCPSocketActionArgs()
        {
        }
        public static new GoogleCloudRunV2TCPSocketActionArgs Empty => new GoogleCloudRunV2TCPSocketActionArgs();
    }
}
