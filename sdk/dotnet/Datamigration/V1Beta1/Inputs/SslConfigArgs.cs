// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Datamigration.V1Beta1.Inputs
{

    /// <summary>
    /// SSL configuration information.
    /// </summary>
    public sealed class SslConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Input only. The x509 PEM-encoded certificate of the CA that signed the source database server's certificate. The replica will use this certificate to verify it's connecting to the right host.
        /// </summary>
        [Input("caCertificate", required: true)]
        public Input<string> CaCertificate { get; set; } = null!;

        /// <summary>
        /// Input only. The x509 PEM-encoded certificate that will be used by the replica to authenticate against the source database server.If this field is used then the 'client_key' field is mandatory.
        /// </summary>
        [Input("clientCertificate")]
        public Input<string>? ClientCertificate { get; set; }

        /// <summary>
        /// Input only. The unencrypted PKCS#1 or PKCS#8 PEM-encoded private key associated with the Client Certificate. If this field is used then the 'client_certificate' field is mandatory.
        /// </summary>
        [Input("clientKey")]
        public Input<string>? ClientKey { get; set; }

        public SslConfigArgs()
        {
        }
        public static new SslConfigArgs Empty => new SslConfigArgs();
    }
}
