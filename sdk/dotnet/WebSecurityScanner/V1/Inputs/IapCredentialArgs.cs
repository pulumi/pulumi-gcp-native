// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.WebSecurityScanner.V1.Inputs
{

    /// <summary>
    /// Describes authentication configuration for Identity-Aware-Proxy (IAP).
    /// </summary>
    public sealed class IapCredentialArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Authentication configuration when Web-Security-Scanner service account is added in Identity-Aware-Proxy (IAP) access policies.
        /// </summary>
        [Input("iapTestServiceAccountInfo")]
        public Input<Inputs.IapTestServiceAccountInfoArgs>? IapTestServiceAccountInfo { get; set; }

        public IapCredentialArgs()
        {
        }
        public static new IapCredentialArgs Empty => new IapCredentialArgs();
    }
}
