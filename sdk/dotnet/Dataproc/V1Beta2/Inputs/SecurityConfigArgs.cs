// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dataproc.V1Beta2.Inputs
{

    /// <summary>
    /// Security related configuration, including encryption, Kerberos, etc.
    /// </summary>
    public sealed class SecurityConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. Kerberos related configuration.
        /// </summary>
        [Input("kerberosConfig")]
        public Input<Inputs.KerberosConfigArgs>? KerberosConfig { get; set; }

        public SecurityConfigArgs()
        {
        }
        public static new SecurityConfigArgs Empty => new SecurityConfigArgs();
    }
}
