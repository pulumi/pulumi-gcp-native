// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const ChannelPartnerLinkLinkState = {
    /**
     * Not used.
     */
    ChannelPartnerLinkStateUnspecified: "CHANNEL_PARTNER_LINK_STATE_UNSPECIFIED",
    /**
     * An invitation has been sent to the reseller to create a channel partner link.
     */
    Invited: "INVITED",
    /**
     * Status when the reseller is active.
     */
    Active: "ACTIVE",
    /**
     * Status when the reseller has been revoked by the distributor.
     */
    Revoked: "REVOKED",
    /**
     * Status when the reseller is suspended by Google or distributor.
     */
    Suspended: "SUSPENDED",
} as const;

/**
 * Required. State of the channel partner link.
 */
export type ChannelPartnerLinkLinkState = (typeof ChannelPartnerLinkLinkState)[keyof typeof ChannelPartnerLinkLinkState];

export const GoogleCloudChannelV1ConditionalOverrideRebillingBasis = {
    /**
     * Not used.
     */
    RebillingBasisUnspecified: "REBILLING_BASIS_UNSPECIFIED",
    /**
     * Use the list cost, also known as the MSRP.
     */
    CostAtList: "COST_AT_LIST",
    /**
     * Pass through all discounts except the Reseller Program Discount. If this is the default cost base and no adjustments are specified, the output cost will be exactly what the customer would see if they viewed the bill in the Google Cloud Console.
     */
    DirectCustomerCost: "DIRECT_CUSTOMER_COST",
} as const;

/**
 * Required. The RebillingBasis to use for the applied override. Shows the relative cost based on your repricing costs.
 */
export type GoogleCloudChannelV1ConditionalOverrideRebillingBasis = (typeof GoogleCloudChannelV1ConditionalOverrideRebillingBasis)[keyof typeof GoogleCloudChannelV1ConditionalOverrideRebillingBasis];

export const GoogleCloudChannelV1PeriodPeriodType = {
    /**
     * Not used.
     */
    PeriodTypeUnspecified: "PERIOD_TYPE_UNSPECIFIED",
    /**
     * Day.
     */
    Day: "DAY",
    /**
     * Month.
     */
    Month: "MONTH",
    /**
     * Year.
     */
    Year: "YEAR",
} as const;

/**
 * Period Type.
 */
export type GoogleCloudChannelV1PeriodPeriodType = (typeof GoogleCloudChannelV1PeriodPeriodType)[keyof typeof GoogleCloudChannelV1PeriodPeriodType];

export const GoogleCloudChannelV1RenewalSettingsPaymentPlan = {
    /**
     * Not used.
     */
    PaymentPlanUnspecified: "PAYMENT_PLAN_UNSPECIFIED",
    /**
     * Commitment.
     */
    Commitment: "COMMITMENT",
    /**
     * No commitment.
     */
    Flexible: "FLEXIBLE",
    /**
     * Free.
     */
    Free: "FREE",
    /**
     * Trial.
     */
    Trial: "TRIAL",
    /**
     * Price and ordering not available through API.
     */
    Offline: "OFFLINE",
} as const;

/**
 * Describes how a reseller will be billed.
 */
export type GoogleCloudChannelV1RenewalSettingsPaymentPlan = (typeof GoogleCloudChannelV1RenewalSettingsPaymentPlan)[keyof typeof GoogleCloudChannelV1RenewalSettingsPaymentPlan];

export const GoogleCloudChannelV1RepricingConfigRebillingBasis = {
    /**
     * Not used.
     */
    RebillingBasisUnspecified: "REBILLING_BASIS_UNSPECIFIED",
    /**
     * Use the list cost, also known as the MSRP.
     */
    CostAtList: "COST_AT_LIST",
    /**
     * Pass through all discounts except the Reseller Program Discount. If this is the default cost base and no adjustments are specified, the output cost will be exactly what the customer would see if they viewed the bill in the Google Cloud Console.
     */
    DirectCustomerCost: "DIRECT_CUSTOMER_COST",
} as const;

/**
 * Required. The RebillingBasis to use for this bill. Specifies the relative cost based on repricing costs you will apply.
 */
export type GoogleCloudChannelV1RepricingConfigRebillingBasis = (typeof GoogleCloudChannelV1RepricingConfigRebillingBasis)[keyof typeof GoogleCloudChannelV1RepricingConfigRebillingBasis];
