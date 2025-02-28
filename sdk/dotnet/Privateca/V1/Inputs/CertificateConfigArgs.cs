// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Privateca.V1.Inputs
{

    /// <summary>
    /// A CertificateConfig describes an X.509 certificate or CSR that is to be created, as an alternative to using ASN.1.
    /// </summary>
    public sealed class CertificateConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. The public key that corresponds to this config. This is, for example, used when issuing Certificates, but not when creating a self-signed CertificateAuthority or CertificateAuthority CSR.
        /// </summary>
        [Input("publicKey")]
        public Input<Inputs.PublicKeyArgs>? PublicKey { get; set; }

        /// <summary>
        /// Specifies some of the values in a certificate that are related to the subject.
        /// </summary>
        [Input("subjectConfig", required: true)]
        public Input<Inputs.SubjectConfigArgs> SubjectConfig { get; set; } = null!;

        /// <summary>
        /// Describes how some of the technical X.509 fields in a certificate should be populated.
        /// </summary>
        [Input("x509Config", required: true)]
        public Input<Inputs.X509ParametersArgs> X509Config { get; set; } = null!;

        public CertificateConfigArgs()
        {
        }
        public static new CertificateConfigArgs Empty => new CertificateConfigArgs();
    }
}
