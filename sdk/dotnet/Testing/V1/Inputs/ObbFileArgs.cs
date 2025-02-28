// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Testing.V1.Inputs
{

    /// <summary>
    /// An opaque binary blob file to install on the device before the test starts.
    /// </summary>
    public sealed class ObbFileArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Opaque Binary Blob (OBB) file(s) to install on the device.
        /// </summary>
        [Input("obb", required: true)]
        public Input<Inputs.FileReferenceArgs> Obb { get; set; } = null!;

        /// <summary>
        /// OBB file name which must conform to the format as specified by Android e.g. [main|patch].0300110.com.example.android.obb which will be installed into \/Android/obb/\/ on the device.
        /// </summary>
        [Input("obbFileName", required: true)]
        public Input<string> ObbFileName { get; set; } = null!;

        public ObbFileArgs()
        {
        }
        public static new ObbFileArgs Empty => new ObbFileArgs();
    }
}
