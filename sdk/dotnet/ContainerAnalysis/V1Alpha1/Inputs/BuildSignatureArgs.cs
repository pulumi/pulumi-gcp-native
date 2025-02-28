// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.ContainerAnalysis.V1Alpha1.Inputs
{

    /// <summary>
    /// Message encapsulating the signature of the verified build.
    /// </summary>
    public sealed class BuildSignatureArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// An Id for the key used to sign. This could be either an Id for the key stored in `public_key` (such as the Id or fingerprint for a PGP key, or the CN for a cert), or a reference to an external key (such as a reference to a key in Cloud Key Management Service).
        /// </summary>
        [Input("keyId")]
        public Input<string>? KeyId { get; set; }

        /// <summary>
        /// The type of the key, either stored in `public_key` or referenced in `key_id`
        /// </summary>
        [Input("keyType")]
        public Input<Pulumi.GoogleNative.ContainerAnalysis.V1Alpha1.BuildSignatureKeyType>? KeyType { get; set; }

        /// <summary>
        /// Public key of the builder which can be used to verify that the related findings are valid and unchanged. If `key_type` is empty, this defaults to PEM encoded public keys. This field may be empty if `key_id` references an external key. For Cloud Build based signatures, this is a PEM encoded public key. To verify the Cloud Build signature, place the contents of this field into a file (public.pem). The signature field is base64-decoded into its binary representation in signature.bin, and the provenance bytes from `BuildDetails` are base64-decoded into a binary representation in signed.bin. OpenSSL can then verify the signature: `openssl sha256 -verify public.pem -signature signature.bin signed.bin`
        /// </summary>
        [Input("publicKey")]
        public Input<string>? PublicKey { get; set; }

        /// <summary>
        /// Signature of the related `BuildProvenance`, encoded in a base64 string.
        /// </summary>
        [Input("signature")]
        public Input<string>? Signature { get; set; }

        public BuildSignatureArgs()
        {
        }
        public static new BuildSignatureArgs Empty => new BuildSignatureArgs();
    }
}
