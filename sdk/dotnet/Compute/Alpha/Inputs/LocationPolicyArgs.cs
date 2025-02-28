// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Compute.Alpha.Inputs
{

    /// <summary>
    /// Configuration for location policy among multiple possible locations (e.g. preferences for zone selection among zones in a single region).
    /// </summary>
    public sealed class LocationPolicyArgs : global::Pulumi.ResourceArgs
    {
        [Input("locations")]
        private InputMap<Inputs.LocationPolicyLocationArgs>? _locations;

        /// <summary>
        /// Location configurations mapped by location name. Currently only zone names are supported and must be represented as valid internal URLs, such as zones/us-central1-a.
        /// </summary>
        public InputMap<Inputs.LocationPolicyLocationArgs> Locations
        {
            get => _locations ?? (_locations = new InputMap<Inputs.LocationPolicyLocationArgs>());
            set => _locations = value;
        }

        /// <summary>
        /// Strategy for distributing VMs across zones in a region.
        /// </summary>
        [Input("targetShape")]
        public Input<Pulumi.GoogleNative.Compute.Alpha.LocationPolicyTargetShape>? TargetShape { get; set; }

        public LocationPolicyArgs()
        {
        }
        public static new LocationPolicyArgs Empty => new LocationPolicyArgs();
    }
}
