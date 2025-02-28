// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Healthcare.V1Beta1.Inputs
{

    /// <summary>
    /// A 2D coordinate in an image. The origin is the top-left.
    /// </summary>
    public sealed class VertexArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// X coordinate.
        /// </summary>
        [Input("x")]
        public Input<double>? X { get; set; }

        /// <summary>
        /// Y coordinate.
        /// </summary>
        [Input("y")]
        public Input<double>? Y { get; set; }

        public VertexArgs()
        {
        }
        public static new VertexArgs Empty => new VertexArgs();
    }
}
