// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Gkeonprem.V1.Inputs
{

    /// <summary>
    /// Represents an arg name-&gt;value pair. Only a subset of customized flags are supported. For the exact format, refer to the [API server documentation](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/).
    /// </summary>
    public sealed class BareMetalApiServerArgumentArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The argument name as it appears on the API Server command line, make sure to remove the leading dashes.
        /// </summary>
        [Input("argument", required: true)]
        public Input<string> Argument { get; set; } = null!;

        /// <summary>
        /// The value of the arg as it will be passed to the API Server command line.
        /// </summary>
        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public BareMetalApiServerArgumentArgs()
        {
        }
        public static new BareMetalApiServerArgumentArgs Empty => new BareMetalApiServerArgumentArgs();
    }
}
