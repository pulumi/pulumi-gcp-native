// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Contentwarehouse.V1.Inputs
{

    /// <summary>
    /// Encodes the detailed information of a barcode.
    /// </summary>
    public sealed class GoogleCloudDocumentaiV1BarcodeArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Format of a barcode. The supported formats are: - `CODE_128`: Code 128 type. - `CODE_39`: Code 39 type. - `CODE_93`: Code 93 type. - `CODABAR`: Codabar type. - `DATA_MATRIX`: 2D Data Matrix type. - `ITF`: ITF type. - `EAN_13`: EAN-13 type. - `EAN_8`: EAN-8 type. - `QR_CODE`: 2D QR code type. - `UPC_A`: UPC-A type. - `UPC_E`: UPC-E type. - `PDF417`: PDF417 type. - `AZTEC`: 2D Aztec code type. - `DATABAR`: GS1 DataBar code type.
        /// </summary>
        [Input("format")]
        public Input<string>? Format { get; set; }

        /// <summary>
        /// Raw value encoded in the barcode. For example: `'MEBKM:TITLE:Google;URL:https://www.google.com;;'`.
        /// </summary>
        [Input("rawValue")]
        public Input<string>? RawValue { get; set; }

        /// <summary>
        /// Value format describes the format of the value that a barcode encodes. The supported formats are: - `CONTACT_INFO`: Contact information. - `EMAIL`: Email address. - `ISBN`: ISBN identifier. - `PHONE`: Phone number. - `PRODUCT`: Product. - `SMS`: SMS message. - `TEXT`: Text string. - `URL`: URL address. - `WIFI`: Wifi information. - `GEO`: Geo-localization. - `CALENDAR_EVENT`: Calendar event. - `DRIVER_LICENSE`: Driver's license.
        /// </summary>
        [Input("valueFormat")]
        public Input<string>? ValueFormat { get; set; }

        public GoogleCloudDocumentaiV1BarcodeArgs()
        {
        }
        public static new GoogleCloudDocumentaiV1BarcodeArgs Empty => new GoogleCloudDocumentaiV1BarcodeArgs();
    }
}
