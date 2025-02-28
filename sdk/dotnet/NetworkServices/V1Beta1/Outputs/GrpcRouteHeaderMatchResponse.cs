// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.NetworkServices.V1Beta1.Outputs
{

    /// <summary>
    /// A match against a collection of headers.
    /// </summary>
    [OutputType]
    public sealed class GrpcRouteHeaderMatchResponse
    {
        /// <summary>
        /// The key of the header.
        /// </summary>
        public readonly string Key;
        /// <summary>
        /// Optional. Specifies how to match against the value of the header. If not specified, a default value of EXACT is used.
        /// </summary>
        public readonly string Type;
        /// <summary>
        /// The value of the header.
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private GrpcRouteHeaderMatchResponse(
            string key,

            string type,

            string value)
        {
            Key = key;
            Type = type;
            Value = value;
        }
    }
}
