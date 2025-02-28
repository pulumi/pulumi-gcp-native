// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Compute.Alpha.Inputs
{

    public sealed class FileContentBufferArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The raw content in the secure keys file.
        /// </summary>
        [Input("content")]
        public Input<string>? Content { get; set; }

        /// <summary>
        /// The file type of source file.
        /// </summary>
        [Input("fileType")]
        public Input<Pulumi.GoogleNative.Compute.Alpha.FileContentBufferFileType>? FileType { get; set; }

        public FileContentBufferArgs()
        {
        }
        public static new FileContentBufferArgs Empty => new FileContentBufferArgs();
    }
}
