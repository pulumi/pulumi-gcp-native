// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.SQLAdmin.V1Beta4.Outputs
{

    /// <summary>
    /// Represents a Sql Server user on the Cloud SQL instance.
    /// </summary>
    [OutputType]
    public sealed class SqlServerUserDetailsResponse
    {
        /// <summary>
        /// If the user has been disabled
        /// </summary>
        public readonly bool Disabled;
        /// <summary>
        /// The server roles for this user
        /// </summary>
        public readonly ImmutableArray<string> ServerRoles;

        [OutputConstructor]
        private SqlServerUserDetailsResponse(
            bool disabled,

            ImmutableArray<string> serverRoles)
        {
            Disabled = disabled;
            ServerRoles = serverRoles;
        }
    }
}
