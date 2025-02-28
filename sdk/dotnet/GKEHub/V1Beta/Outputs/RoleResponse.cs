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
    /// Role is the type for Kubernetes roles
    /// </summary>
    [OutputType]
    public sealed class RoleResponse
    {
        /// <summary>
        /// predefined_role is the Kubernetes default role to use
        /// </summary>
        public readonly string PredefinedRole;

        [OutputConstructor]
        private RoleResponse(string predefinedRole)
        {
            PredefinedRole = predefinedRole;
        }
    }
}
