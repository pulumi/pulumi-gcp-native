// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Apigee.V1.Inputs
{

    /// <summary>
    /// Message for compatibility with legacy Edge specification for Java Properties object in JSON.
    /// </summary>
    public sealed class GoogleCloudApigeeV1PropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("property")]
        private InputList<Inputs.GoogleCloudApigeeV1PropertyArgs>? _property;

        /// <summary>
        /// List of all properties in the object
        /// </summary>
        public InputList<Inputs.GoogleCloudApigeeV1PropertyArgs> Property
        {
            get => _property ?? (_property = new InputList<Inputs.GoogleCloudApigeeV1PropertyArgs>());
            set => _property = value;
        }

        public GoogleCloudApigeeV1PropertiesArgs()
        {
        }
        public static new GoogleCloudApigeeV1PropertiesArgs Empty => new GoogleCloudApigeeV1PropertiesArgs();
    }
}
