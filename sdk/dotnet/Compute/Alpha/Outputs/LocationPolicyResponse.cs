// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Compute.Alpha.Outputs
{

    /// <summary>
    /// Configuration for location policy among multiple possible locations (e.g. preferences for zone selection among zones in a single region).
    /// </summary>
    [OutputType]
    public sealed class LocationPolicyResponse
    {
        /// <summary>
        /// Location configurations mapped by location name. Currently only zone names are supported and must be represented as valid internal URLs, such as zones/us-central1-a.
        /// </summary>
        public readonly ImmutableDictionary<string, Outputs.LocationPolicyLocationResponse> Locations;
        /// <summary>
        /// Strategy for distributing VMs across zones in a region.
        /// </summary>
        public readonly string TargetShape;

        [OutputConstructor]
        private LocationPolicyResponse(
            ImmutableDictionary<string, Outputs.LocationPolicyLocationResponse> locations,

            string targetShape)
        {
            Locations = locations;
            TargetShape = targetShape;
        }
    }
}
