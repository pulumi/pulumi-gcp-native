// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.GKEHub.V1.Inputs
{

    /// <summary>
    /// The config specifying which default library templates to install.
    /// </summary>
    public sealed class PolicyControllerTemplateLibraryConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Configures the manner in which the template library is installed on the cluster.
        /// </summary>
        [Input("installation")]
        public Input<Pulumi.GoogleNative.GKEHub.V1.PolicyControllerTemplateLibraryConfigInstallation>? Installation { get; set; }

        public PolicyControllerTemplateLibraryConfigArgs()
        {
        }
        public static new PolicyControllerTemplateLibraryConfigArgs Empty => new PolicyControllerTemplateLibraryConfigArgs();
    }
}
