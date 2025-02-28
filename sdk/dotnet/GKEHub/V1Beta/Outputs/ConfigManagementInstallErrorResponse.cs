// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.GKEHub.V1Beta.Outputs
{

    /// <summary>
    /// Errors pertaining to the installation of ACM
    /// </summary>
    [OutputType]
    public sealed class ConfigManagementInstallErrorResponse
    {
        /// <summary>
        /// A string representing the user facing error message
        /// </summary>
        public readonly string ErrorMessage;

        [OutputConstructor]
        private ConfigManagementInstallErrorResponse(string errorMessage)
        {
            ErrorMessage = errorMessage;
        }
    }
}
