// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.ArtifactRegistry.V1.Outputs
{

    /// <summary>
    /// Username and password credentials.
    /// </summary>
    [OutputType]
    public sealed class UsernamePasswordCredentialsResponse
    {
        /// <summary>
        /// The Secret Manager key version that holds the password to access the remote repository. Must be in the format of `projects/{project}/secrets/{secret}/versions/{version}`.
        /// </summary>
        public readonly string PasswordSecretVersion;
        /// <summary>
        /// The username to access the remote repository.
        /// </summary>
        public readonly string Username;

        [OutputConstructor]
        private UsernamePasswordCredentialsResponse(
            string passwordSecretVersion,

            string username)
        {
            PasswordSecretVersion = passwordSecretVersion;
            Username = username;
        }
    }
}
