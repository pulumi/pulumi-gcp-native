// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.FirebaseRules.V1.Outputs
{

    /// <summary>
    /// `File` containing source content.
    /// </summary>
    [OutputType]
    public sealed class FileResponse
    {
        /// <summary>
        /// Textual Content.
        /// </summary>
        public readonly string Content;
        /// <summary>
        /// Fingerprint (e.g. github sha) associated with the `File`.
        /// </summary>
        public readonly string Fingerprint;
        /// <summary>
        /// File name.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private FileResponse(
            string content,

            string fingerprint,

            string name)
        {
            Content = content;
            Fingerprint = fingerprint;
            Name = name;
        }
    }
}
