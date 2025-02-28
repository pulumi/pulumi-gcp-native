// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.AppEngine.V1.Inputs
{

    /// <summary>
    /// Google Cloud Endpoints (https://cloud.google.com/endpoints) configuration. The Endpoints API Service provides tooling for serving Open API and gRPC endpoints via an NGINX proxy. Only valid for App Engine Flexible environment deployments.The fields here refer to the name and configuration ID of a "service" resource in the Service Management API (https://cloud.google.com/service-management/overview).
    /// </summary>
    public sealed class EndpointsApiServiceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Endpoints service configuration ID as specified by the Service Management API. For example "2016-09-19r1".By default, the rollout strategy for Endpoints is RolloutStrategy.FIXED. This means that Endpoints starts up with a particular configuration ID. When a new configuration is rolled out, Endpoints must be given the new configuration ID. The config_id field is used to give the configuration ID and is required in this case.Endpoints also has a rollout strategy called RolloutStrategy.MANAGED. When using this, Endpoints fetches the latest configuration and does not need the configuration ID. In this case, config_id must be omitted.
        /// </summary>
        [Input("configId")]
        public Input<string>? ConfigId { get; set; }

        /// <summary>
        /// Enable or disable trace sampling. By default, this is set to false for enabled.
        /// </summary>
        [Input("disableTraceSampling")]
        public Input<bool>? DisableTraceSampling { get; set; }

        /// <summary>
        /// Endpoints service name which is the name of the "service" resource in the Service Management API. For example "myapi.endpoints.myproject.cloud.goog"
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Endpoints rollout strategy. If FIXED, config_id must be specified. If MANAGED, config_id must be omitted.
        /// </summary>
        [Input("rolloutStrategy")]
        public Input<Pulumi.GoogleNative.AppEngine.V1.EndpointsApiServiceRolloutStrategy>? RolloutStrategy { get; set; }

        public EndpointsApiServiceArgs()
        {
        }
        public static new EndpointsApiServiceArgs Empty => new EndpointsApiServiceArgs();
    }
}
