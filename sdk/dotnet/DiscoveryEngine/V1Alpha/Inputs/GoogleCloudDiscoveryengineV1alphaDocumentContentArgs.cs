// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.DiscoveryEngine.V1Alpha.Inputs
{

    /// <summary>
    /// Unstructured data linked to this document.
    /// </summary>
    public sealed class GoogleCloudDiscoveryengineV1alphaDocumentContentArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The MIME type of the content. Supported types: * `application/pdf` (PDF, only native PDFs are supported for now) * `text/html` (HTML) * `application/vnd.openxmlformats-officedocument.wordprocessingml.document` (DOCX) * `application/vnd.openxmlformats-officedocument.presentationml.presentation` (PPTX) * `text/plain` (TXT) See https://www.iana.org/assignments/media-types/media-types.xhtml.
        /// </summary>
        [Input("mimeType")]
        public Input<string>? MimeType { get; set; }

        /// <summary>
        /// The content represented as a stream of bytes. The maximum length is 1,000,000 bytes (1 MB / ~0.95 MiB). Note: As with all `bytes` fields, this field is represented as pure binary in Protocol Buffers and base64-encoded string in JSON. For example, `abc123!?$*&amp;()'-=@~` should be represented as `YWJjMTIzIT8kKiYoKSctPUB+` in JSON. See https://developers.google.com/protocol-buffers/docs/proto3#json.
        /// </summary>
        [Input("rawBytes")]
        public Input<string>? RawBytes { get; set; }

        /// <summary>
        /// The URI of the content. Only Cloud Storage URIs (e.g. `gs://bucket-name/path/to/file`) are supported. The maximum file size is 100 MB.
        /// </summary>
        [Input("uri")]
        public Input<string>? Uri { get; set; }

        public GoogleCloudDiscoveryengineV1alphaDocumentContentArgs()
        {
        }
        public static new GoogleCloudDiscoveryengineV1alphaDocumentContentArgs Empty => new GoogleCloudDiscoveryengineV1alphaDocumentContentArgs();
    }
}
