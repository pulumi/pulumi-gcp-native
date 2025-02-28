// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Securitycenter.V1.Inputs
{

    /// <summary>
    /// A set of optional name-value pairs that define custom source properties to return with each finding that is generated by the custom module. The custom source properties that are defined here are included in the finding JSON under `sourceProperties`.
    /// </summary>
    public sealed class GoogleCloudSecuritycenterV1CustomOutputSpecArgs : global::Pulumi.ResourceArgs
    {
        [Input("properties")]
        private InputList<Inputs.GoogleCloudSecuritycenterV1PropertyArgs>? _properties;

        /// <summary>
        /// A list of custom output properties to add to the finding.
        /// </summary>
        public InputList<Inputs.GoogleCloudSecuritycenterV1PropertyArgs> Properties
        {
            get => _properties ?? (_properties = new InputList<Inputs.GoogleCloudSecuritycenterV1PropertyArgs>());
            set => _properties = value;
        }

        public GoogleCloudSecuritycenterV1CustomOutputSpecArgs()
        {
        }
        public static new GoogleCloudSecuritycenterV1CustomOutputSpecArgs Empty => new GoogleCloudSecuritycenterV1CustomOutputSpecArgs();
    }
}
