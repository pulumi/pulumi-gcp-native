// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.DNS.V1.Inputs
{

    public sealed class ManagedZonePrivateVisibilityConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("gkeClusters")]
        private InputList<Inputs.ManagedZonePrivateVisibilityConfigGKEClusterArgs>? _gkeClusters;

        /// <summary>
        /// The list of Google Kubernetes Engine clusters that can see this zone.
        /// </summary>
        public InputList<Inputs.ManagedZonePrivateVisibilityConfigGKEClusterArgs> GkeClusters
        {
            get => _gkeClusters ?? (_gkeClusters = new InputList<Inputs.ManagedZonePrivateVisibilityConfigGKEClusterArgs>());
            set => _gkeClusters = value;
        }

        [Input("kind")]
        public Input<string>? Kind { get; set; }

        [Input("networks")]
        private InputList<Inputs.ManagedZonePrivateVisibilityConfigNetworkArgs>? _networks;

        /// <summary>
        /// The list of VPC networks that can see this zone.
        /// </summary>
        public InputList<Inputs.ManagedZonePrivateVisibilityConfigNetworkArgs> Networks
        {
            get => _networks ?? (_networks = new InputList<Inputs.ManagedZonePrivateVisibilityConfigNetworkArgs>());
            set => _networks = value;
        }

        public ManagedZonePrivateVisibilityConfigArgs()
        {
        }
        public static new ManagedZonePrivateVisibilityConfigArgs Empty => new ManagedZonePrivateVisibilityConfigArgs();
    }
}
