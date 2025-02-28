// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.DataCatalog.V1.Inputs
{

    /// <summary>
    /// Schema in protocol buffer format.
    /// </summary>
    public sealed class GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Protocol buffer source of the schema.
        /// </summary>
        [Input("text")]
        public Input<string>? Text { get; set; }

        public GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaArgs()
        {
        }
        public static new GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaArgs Empty => new GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaArgs();
    }
}
