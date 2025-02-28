// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.AnalyticsHub.V1.Outputs
{

    /// <summary>
    /// Sharing environment is a behavior model for sharing data within a data exchange. This option is configurable for a data exchange.
    /// </summary>
    [OutputType]
    public sealed class SharingEnvironmentConfigResponse
    {
        /// <summary>
        /// Data Clean Room (DCR), used for privacy-safe and secured data sharing.
        /// </summary>
        public readonly Outputs.DcrExchangeConfigResponse DcrExchangeConfig;
        /// <summary>
        /// Default Analytics Hub data exchange, used for secured data sharing.
        /// </summary>
        public readonly Outputs.DefaultExchangeConfigResponse DefaultExchangeConfig;

        [OutputConstructor]
        private SharingEnvironmentConfigResponse(
            Outputs.DcrExchangeConfigResponse dcrExchangeConfig,

            Outputs.DefaultExchangeConfigResponse defaultExchangeConfig)
        {
            DcrExchangeConfig = dcrExchangeConfig;
            DefaultExchangeConfig = defaultExchangeConfig;
        }
    }
}
