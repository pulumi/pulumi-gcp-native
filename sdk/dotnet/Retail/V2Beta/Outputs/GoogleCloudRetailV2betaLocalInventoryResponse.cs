// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Retail.V2Beta.Outputs
{

    /// <summary>
    /// The inventory information at a place (e.g. a store) identified by a place ID.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudRetailV2betaLocalInventoryResponse
    {
        /// <summary>
        /// Additional local inventory attributes, for example, store name, promotion tags, etc. This field needs to pass all below criteria, otherwise an INVALID_ARGUMENT error is returned: * At most 30 attributes are allowed. * The key must be a UTF-8 encoded string with a length limit of 32 characters. * The key must match the pattern: `a-zA-Z0-9*`. For example, key0LikeThis or KEY_1_LIKE_THIS. * The attribute values must be of the same type (text or number). * Only 1 value is allowed for each attribute. * For text values, the length limit is 256 UTF-8 characters. * The attribute does not support search. The `searchable` field should be unset or set to false. * The max summed total bytes of custom attribute keys and values per product is 5MiB.
        /// </summary>
        public readonly ImmutableDictionary<string, Outputs.GoogleCloudRetailV2betaCustomAttributeResponse> Attributes;
        /// <summary>
        /// Input only. Supported fulfillment types. Valid fulfillment type values include commonly used types (such as pickup in store and same day delivery), and custom types. Customers have to map custom types to their display names before rendering UI. Supported values: * "pickup-in-store" * "ship-to-store" * "same-day-delivery" * "next-day-delivery" * "custom-type-1" * "custom-type-2" * "custom-type-3" * "custom-type-4" * "custom-type-5" If this field is set to an invalid value other than these, an INVALID_ARGUMENT error is returned. All the elements must be distinct. Otherwise, an INVALID_ARGUMENT error is returned.
        /// </summary>
        public readonly ImmutableArray<string> FulfillmentTypes;
        /// <summary>
        /// The place ID for the current set of inventory information.
        /// </summary>
        public readonly string PlaceId;
        /// <summary>
        /// Product price and cost information. Google Merchant Center property [price](https://support.google.com/merchants/answer/6324371).
        /// </summary>
        public readonly Outputs.GoogleCloudRetailV2betaPriceInfoResponse PriceInfo;

        [OutputConstructor]
        private GoogleCloudRetailV2betaLocalInventoryResponse(
            ImmutableDictionary<string, Outputs.GoogleCloudRetailV2betaCustomAttributeResponse> attributes,

            ImmutableArray<string> fulfillmentTypes,

            string placeId,

            Outputs.GoogleCloudRetailV2betaPriceInfoResponse priceInfo)
        {
            Attributes = attributes;
            FulfillmentTypes = fulfillmentTypes;
            PlaceId = placeId;
            PriceInfo = priceInfo;
        }
    }
}
