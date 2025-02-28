// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.BinaryAuthorization.V1.Inputs
{

    /// <summary>
    /// A public key in the PkixPublicKey [format](https://tools.ietf.org/html/rfc5280#section-4.1.2.7). Public keys of this type are typically textually encoded using the PEM format.
    /// </summary>
    public sealed class PkixPublicKeyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. The ID of this public key. Signatures verified by Binary Authorization must include the ID of the public key that can be used to verify them, and that ID must match the contents of this field exactly. This may be explicitly provided by the caller, but it MUST be a valid RFC3986 URI. If `key_id` is left blank and this `PkixPublicKey` is not used in the context of a wrapper (see next paragraph), a default key ID will be computed based on the digest of the DER encoding of the public key. If this `PkixPublicKey` is used in the context of a wrapper that has its own notion of key ID (e.g. `AttestorPublicKey`), then this field can either: * Match that value exactly. * Or be left blank, in which case it behaves exactly as though it is equal to that wrapper value.
        /// </summary>
        [Input("keyId")]
        public Input<string>? KeyId { get; set; }

        /// <summary>
        /// A PEM-encoded public key, as described in https://tools.ietf.org/html/rfc7468#section-13
        /// </summary>
        [Input("publicKeyPem")]
        public Input<string>? PublicKeyPem { get; set; }

        /// <summary>
        /// The signature algorithm used to verify a message against a signature using this key. These signature algorithm must match the structure and any object identifiers encoded in `public_key_pem` (i.e. this algorithm must match that of the public key).
        /// </summary>
        [Input("signatureAlgorithm")]
        public Input<Pulumi.GoogleNative.BinaryAuthorization.V1.PkixPublicKeySignatureAlgorithm>? SignatureAlgorithm { get; set; }

        public PkixPublicKeyArgs()
        {
        }
        public static new PkixPublicKeyArgs Empty => new PkixPublicKeyArgs();
    }
}
