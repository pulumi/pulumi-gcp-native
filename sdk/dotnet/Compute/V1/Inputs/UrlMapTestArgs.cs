// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Compute.V1.Inputs
{

    /// <summary>
    /// Message for the expected URL mappings.
    /// </summary>
    public sealed class UrlMapTestArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Description of this test case.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The expected output URL evaluated by the load balancer containing the scheme, host, path and query parameters. For rules that forward requests to backends, the test passes only when expectedOutputUrl matches the request forwarded by the load balancer to backends. For rules with urlRewrite, the test verifies that the forwarded request matches hostRewrite and pathPrefixRewrite in the urlRewrite action. When service is specified, expectedOutputUrl`s scheme is ignored. For rules with urlRedirect, the test passes only if expectedOutputUrl matches the URL in the load balancer's redirect response. If urlRedirect specifies https_redirect, the test passes only if the scheme in expectedOutputUrl is also set to HTTPS. If urlRedirect specifies strip_query, the test passes only if expectedOutputUrl does not contain any query parameters. expectedOutputUrl is optional when service is specified.
        /// </summary>
        [Input("expectedOutputUrl")]
        public Input<string>? ExpectedOutputUrl { get; set; }

        /// <summary>
        /// For rules with urlRedirect, the test passes only if expectedRedirectResponseCode matches the HTTP status code in load balancer's redirect response. expectedRedirectResponseCode cannot be set when service is set.
        /// </summary>
        [Input("expectedRedirectResponseCode")]
        public Input<int>? ExpectedRedirectResponseCode { get; set; }

        [Input("headers")]
        private InputList<Inputs.UrlMapTestHeaderArgs>? _headers;

        /// <summary>
        /// HTTP headers for this request. If headers contains a host header, then host must also match the header value.
        /// </summary>
        public InputList<Inputs.UrlMapTestHeaderArgs> Headers
        {
            get => _headers ?? (_headers = new InputList<Inputs.UrlMapTestHeaderArgs>());
            set => _headers = value;
        }

        /// <summary>
        /// Host portion of the URL. If headers contains a host header, then host must also match the header value.
        /// </summary>
        [Input("host")]
        public Input<string>? Host { get; set; }

        /// <summary>
        /// Path portion of the URL.
        /// </summary>
        [Input("path")]
        public Input<string>? Path { get; set; }

        /// <summary>
        /// Expected BackendService or BackendBucket resource the given URL should be mapped to. The service field cannot be set if expectedRedirectResponseCode is set.
        /// </summary>
        [Input("service")]
        public Input<string>? Service { get; set; }

        public UrlMapTestArgs()
        {
        }
        public static new UrlMapTestArgs Empty => new UrlMapTestArgs();
    }
}
