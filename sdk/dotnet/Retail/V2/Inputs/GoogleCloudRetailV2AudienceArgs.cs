// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Retail.V2.Inputs
{

    /// <summary>
    /// An intended audience of the Product for whom it's sold.
    /// </summary>
    public sealed class GoogleCloudRetailV2AudienceArgs : global::Pulumi.ResourceArgs
    {
        [Input("ageGroups")]
        private InputList<string>? _ageGroups;

        /// <summary>
        /// The age groups of the audience. Strongly encouraged to use the standard values: "newborn" (up to 3 months old), "infant" (3–12 months old), "toddler" (1–5 years old), "kids" (5–13 years old), "adult" (typically teens or older). At most 5 values are allowed. Each value must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned. Google Merchant Center property [age_group](https://support.google.com/merchants/answer/6324463). Schema.org property [Product.audience.suggestedMinAge](https://schema.org/suggestedMinAge) and [Product.audience.suggestedMaxAge](https://schema.org/suggestedMaxAge).
        /// </summary>
        public InputList<string> AgeGroups
        {
            get => _ageGroups ?? (_ageGroups = new InputList<string>());
            set => _ageGroups = value;
        }

        [Input("genders")]
        private InputList<string>? _genders;

        /// <summary>
        /// The genders of the audience. Strongly encouraged to use the standard values: "male", "female", "unisex". At most 5 values are allowed. Each value must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned. Google Merchant Center property [gender](https://support.google.com/merchants/answer/6324479). Schema.org property [Product.audience.suggestedGender](https://schema.org/suggestedGender).
        /// </summary>
        public InputList<string> Genders
        {
            get => _genders ?? (_genders = new InputList<string>());
            set => _genders = value;
        }

        public GoogleCloudRetailV2AudienceArgs()
        {
        }
        public static new GoogleCloudRetailV2AudienceArgs Empty => new GoogleCloudRetailV2AudienceArgs();
    }
}
