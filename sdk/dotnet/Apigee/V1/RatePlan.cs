// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Apigee.V1
{
    /// <summary>
    /// Create a rate plan that is associated with an API product in an organization. Using rate plans, API product owners can monetize their API products by configuring one or more of the following: - Billing frequency - Initial setup fees for using an API product - Payment funding model (postpaid only) - Fixed recurring or consumption-based charges for using an API product - Revenue sharing with developer partners An API product can have multiple rate plans associated with it but *only one* rate plan can be active at any point of time. **Note: From the developer's perspective, they purchase API products not rate plans.
    /// Auto-naming is currently not supported for this resource.
    /// </summary>
    [GoogleNativeResourceType("google-native:apigee/v1:RatePlan")]
    public partial class RatePlan : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Name of the API product that the rate plan is associated with.
        /// </summary>
        [Output("apiproduct")]
        public Output<string> Apiproduct { get; private set; } = null!;

        [Output("apiproductId")]
        public Output<string> ApiproductId { get; private set; } = null!;

        /// <summary>
        /// Frequency at which the customer will be billed.
        /// </summary>
        [Output("billingPeriod")]
        public Output<string> BillingPeriod { get; private set; } = null!;

        /// <summary>
        /// API call volume ranges and the fees charged when the total number of API calls is within a given range. The method used to calculate the final fee depends on the selected pricing model. For example, if the pricing model is `STAIRSTEP` and the ranges are defined as follows: ``` { "start": 1, "end": 100, "fee": 75 }, { "start": 101, "end": 200, "fee": 100 }, } ``` Then the following fees would be charged based on the total number of API calls (assuming the currency selected is `USD`): * 1 call costs $75 * 50 calls cost $75 * 150 calls cost $100 The number of API calls cannot exceed 200.
        /// </summary>
        [Output("consumptionPricingRates")]
        public Output<ImmutableArray<Outputs.GoogleCloudApigeeV1RateRangeResponse>> ConsumptionPricingRates { get; private set; } = null!;

        /// <summary>
        /// Pricing model used for consumption-based charges.
        /// </summary>
        [Output("consumptionPricingType")]
        public Output<string> ConsumptionPricingType { get; private set; } = null!;

        /// <summary>
        /// Time that the rate plan was created in milliseconds since epoch.
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// Currency to be used for billing. Consists of a three-letter code as defined by the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) standard.
        /// </summary>
        [Output("currencyCode")]
        public Output<string> CurrencyCode { get; private set; } = null!;

        /// <summary>
        /// Description of the rate plan.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// Display name of the rate plan.
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// Time when the rate plan will expire in milliseconds since epoch. Set to 0 or `null` to indicate that the rate plan should never expire.
        /// </summary>
        [Output("endTime")]
        public Output<string> EndTime { get; private set; } = null!;

        /// <summary>
        /// Frequency at which the fixed fee is charged.
        /// </summary>
        [Output("fixedFeeFrequency")]
        public Output<int> FixedFeeFrequency { get; private set; } = null!;

        /// <summary>
        /// Fixed amount that is charged at a defined interval and billed in advance of use of the API product. The fee will be prorated for the first billing period.
        /// </summary>
        [Output("fixedRecurringFee")]
        public Output<Outputs.GoogleTypeMoneyResponse> FixedRecurringFee { get; private set; } = null!;

        /// <summary>
        /// Time the rate plan was last modified in milliseconds since epoch.
        /// </summary>
        [Output("lastModifiedAt")]
        public Output<string> LastModifiedAt { get; private set; } = null!;

        /// <summary>
        /// Name of the rate plan.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("organizationId")]
        public Output<string> OrganizationId { get; private set; } = null!;

        /// <summary>
        /// DEPRECATED: This field is no longer supported and will eventually be removed when Apigee Hybrid 1.5/1.6 is no longer supported. Instead, use the `billingType` field inside `DeveloperMonetizationConfig` resource. Flag that specifies the billing account type, prepaid or postpaid.
        /// </summary>
        [Output("paymentFundingModel")]
        public Output<string> PaymentFundingModel { get; private set; } = null!;

        /// <summary>
        /// Details of the revenue sharing model.
        /// </summary>
        [Output("revenueShareRates")]
        public Output<ImmutableArray<Outputs.GoogleCloudApigeeV1RevenueShareRangeResponse>> RevenueShareRates { get; private set; } = null!;

        /// <summary>
        /// Method used to calculate the revenue that is shared with developers.
        /// </summary>
        [Output("revenueShareType")]
        public Output<string> RevenueShareType { get; private set; } = null!;

        /// <summary>
        /// Initial, one-time fee paid when purchasing the API product.
        /// </summary>
        [Output("setupFee")]
        public Output<Outputs.GoogleTypeMoneyResponse> SetupFee { get; private set; } = null!;

        /// <summary>
        /// Time when the rate plan becomes active in milliseconds since epoch.
        /// </summary>
        [Output("startTime")]
        public Output<string> StartTime { get; private set; } = null!;

        /// <summary>
        /// Current state of the rate plan (draft or published).
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;


        /// <summary>
        /// Create a RatePlan resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RatePlan(string name, RatePlanArgs args, CustomResourceOptions? options = null)
            : base("google-native:apigee/v1:RatePlan", name, args ?? new RatePlanArgs(), MakeResourceOptions(options, ""))
        {
        }

        private RatePlan(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-native:apigee/v1:RatePlan", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "apiproductId",
                    "organizationId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing RatePlan resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RatePlan Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new RatePlan(name, id, options);
        }
    }

    public sealed class RatePlanArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the API product that the rate plan is associated with.
        /// </summary>
        [Input("apiproduct")]
        public Input<string>? Apiproduct { get; set; }

        [Input("apiproductId", required: true)]
        public Input<string> ApiproductId { get; set; } = null!;

        /// <summary>
        /// Frequency at which the customer will be billed.
        /// </summary>
        [Input("billingPeriod")]
        public Input<Pulumi.GoogleNative.Apigee.V1.RatePlanBillingPeriod>? BillingPeriod { get; set; }

        [Input("consumptionPricingRates")]
        private InputList<Inputs.GoogleCloudApigeeV1RateRangeArgs>? _consumptionPricingRates;

        /// <summary>
        /// API call volume ranges and the fees charged when the total number of API calls is within a given range. The method used to calculate the final fee depends on the selected pricing model. For example, if the pricing model is `STAIRSTEP` and the ranges are defined as follows: ``` { "start": 1, "end": 100, "fee": 75 }, { "start": 101, "end": 200, "fee": 100 }, } ``` Then the following fees would be charged based on the total number of API calls (assuming the currency selected is `USD`): * 1 call costs $75 * 50 calls cost $75 * 150 calls cost $100 The number of API calls cannot exceed 200.
        /// </summary>
        public InputList<Inputs.GoogleCloudApigeeV1RateRangeArgs> ConsumptionPricingRates
        {
            get => _consumptionPricingRates ?? (_consumptionPricingRates = new InputList<Inputs.GoogleCloudApigeeV1RateRangeArgs>());
            set => _consumptionPricingRates = value;
        }

        /// <summary>
        /// Pricing model used for consumption-based charges.
        /// </summary>
        [Input("consumptionPricingType")]
        public Input<Pulumi.GoogleNative.Apigee.V1.RatePlanConsumptionPricingType>? ConsumptionPricingType { get; set; }

        /// <summary>
        /// Currency to be used for billing. Consists of a three-letter code as defined by the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) standard.
        /// </summary>
        [Input("currencyCode")]
        public Input<string>? CurrencyCode { get; set; }

        /// <summary>
        /// Description of the rate plan.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Display name of the rate plan.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// Time when the rate plan will expire in milliseconds since epoch. Set to 0 or `null` to indicate that the rate plan should never expire.
        /// </summary>
        [Input("endTime")]
        public Input<string>? EndTime { get; set; }

        /// <summary>
        /// Frequency at which the fixed fee is charged.
        /// </summary>
        [Input("fixedFeeFrequency")]
        public Input<int>? FixedFeeFrequency { get; set; }

        /// <summary>
        /// Fixed amount that is charged at a defined interval and billed in advance of use of the API product. The fee will be prorated for the first billing period.
        /// </summary>
        [Input("fixedRecurringFee")]
        public Input<Inputs.GoogleTypeMoneyArgs>? FixedRecurringFee { get; set; }

        [Input("organizationId", required: true)]
        public Input<string> OrganizationId { get; set; } = null!;

        /// <summary>
        /// DEPRECATED: This field is no longer supported and will eventually be removed when Apigee Hybrid 1.5/1.6 is no longer supported. Instead, use the `billingType` field inside `DeveloperMonetizationConfig` resource. Flag that specifies the billing account type, prepaid or postpaid.
        /// </summary>
        [Input("paymentFundingModel")]
        public Input<Pulumi.GoogleNative.Apigee.V1.RatePlanPaymentFundingModel>? PaymentFundingModel { get; set; }

        [Input("revenueShareRates")]
        private InputList<Inputs.GoogleCloudApigeeV1RevenueShareRangeArgs>? _revenueShareRates;

        /// <summary>
        /// Details of the revenue sharing model.
        /// </summary>
        public InputList<Inputs.GoogleCloudApigeeV1RevenueShareRangeArgs> RevenueShareRates
        {
            get => _revenueShareRates ?? (_revenueShareRates = new InputList<Inputs.GoogleCloudApigeeV1RevenueShareRangeArgs>());
            set => _revenueShareRates = value;
        }

        /// <summary>
        /// Method used to calculate the revenue that is shared with developers.
        /// </summary>
        [Input("revenueShareType")]
        public Input<Pulumi.GoogleNative.Apigee.V1.RatePlanRevenueShareType>? RevenueShareType { get; set; }

        /// <summary>
        /// Initial, one-time fee paid when purchasing the API product.
        /// </summary>
        [Input("setupFee")]
        public Input<Inputs.GoogleTypeMoneyArgs>? SetupFee { get; set; }

        /// <summary>
        /// Time when the rate plan becomes active in milliseconds since epoch.
        /// </summary>
        [Input("startTime")]
        public Input<string>? StartTime { get; set; }

        /// <summary>
        /// Current state of the rate plan (draft or published).
        /// </summary>
        [Input("state")]
        public Input<Pulumi.GoogleNative.Apigee.V1.RatePlanState>? State { get; set; }

        public RatePlanArgs()
        {
        }
        public static new RatePlanArgs Empty => new RatePlanArgs();
    }
}
