// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Run.V1.Outputs
{

    /// <summary>
    /// Information for connecting over HTTP(s).
    /// </summary>
    [OutputType]
    public sealed class AddressableResponse
    {
        public readonly string Url;

        [OutputConstructor]
        private AddressableResponse(string url)
        {
            Url = url;
        }
    }
}
