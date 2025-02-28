// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.GoogleNative.NetworkServices.V1Beta1
{
    /// <summary>
    /// The log type that this config enables.
    /// </summary>
    [EnumType]
    public readonly struct AuditLogConfigLogType : IEquatable<AuditLogConfigLogType>
    {
        private readonly string _value;

        private AuditLogConfigLogType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// Default case. Should never be this.
        /// </summary>
        public static AuditLogConfigLogType LogTypeUnspecified { get; } = new AuditLogConfigLogType("LOG_TYPE_UNSPECIFIED");
        /// <summary>
        /// Admin reads. Example: CloudIAM getIamPolicy
        /// </summary>
        public static AuditLogConfigLogType AdminRead { get; } = new AuditLogConfigLogType("ADMIN_READ");
        /// <summary>
        /// Data writes. Example: CloudSQL Users create
        /// </summary>
        public static AuditLogConfigLogType DataWrite { get; } = new AuditLogConfigLogType("DATA_WRITE");
        /// <summary>
        /// Data reads. Example: CloudSQL Users list
        /// </summary>
        public static AuditLogConfigLogType DataRead { get; } = new AuditLogConfigLogType("DATA_READ");

        public static bool operator ==(AuditLogConfigLogType left, AuditLogConfigLogType right) => left.Equals(right);
        public static bool operator !=(AuditLogConfigLogType left, AuditLogConfigLogType right) => !left.Equals(right);

        public static explicit operator string(AuditLogConfigLogType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is AuditLogConfigLogType other && Equals(other);
        public bool Equals(AuditLogConfigLogType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Required. The type of endpoint policy. This is primarily used to validate the configuration.
    /// </summary>
    [EnumType]
    public readonly struct EndpointPolicyType : IEquatable<EndpointPolicyType>
    {
        private readonly string _value;

        private EndpointPolicyType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// Default value. Must not be used.
        /// </summary>
        public static EndpointPolicyType EndpointPolicyTypeUnspecified { get; } = new EndpointPolicyType("ENDPOINT_POLICY_TYPE_UNSPECIFIED");
        /// <summary>
        /// Represents a proxy deployed as a sidecar.
        /// </summary>
        public static EndpointPolicyType SidecarProxy { get; } = new EndpointPolicyType("SIDECAR_PROXY");
        /// <summary>
        /// Represents a proxyless gRPC backend.
        /// </summary>
        public static EndpointPolicyType GrpcServer { get; } = new EndpointPolicyType("GRPC_SERVER");

        public static bool operator ==(EndpointPolicyType left, EndpointPolicyType right) => left.Equals(right);
        public static bool operator !=(EndpointPolicyType left, EndpointPolicyType right) => !left.Equals(right);

        public static explicit operator string(EndpointPolicyType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is EndpointPolicyType other && Equals(other);
        public bool Equals(EndpointPolicyType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct ExtensionChainExtensionSupportedEventsItem : IEquatable<ExtensionChainExtensionSupportedEventsItem>
    {
        private readonly string _value;

        private ExtensionChainExtensionSupportedEventsItem(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// Unspecified value. Do not use.
        /// </summary>
        public static ExtensionChainExtensionSupportedEventsItem EventTypeUnspecified { get; } = new ExtensionChainExtensionSupportedEventsItem("EVENT_TYPE_UNSPECIFIED");
        /// <summary>
        /// If included in `supported_events`, the extension is called when the HTTP request headers arrive.
        /// </summary>
        public static ExtensionChainExtensionSupportedEventsItem RequestHeaders { get; } = new ExtensionChainExtensionSupportedEventsItem("REQUEST_HEADERS");
        /// <summary>
        /// If included in `supported_events`, the extension is called when the HTTP request body arrives.
        /// </summary>
        public static ExtensionChainExtensionSupportedEventsItem RequestBody { get; } = new ExtensionChainExtensionSupportedEventsItem("REQUEST_BODY");
        /// <summary>
        /// If included in `supported_events`, the extension is called when the HTTP response headers arrive.
        /// </summary>
        public static ExtensionChainExtensionSupportedEventsItem ResponseHeaders { get; } = new ExtensionChainExtensionSupportedEventsItem("RESPONSE_HEADERS");
        /// <summary>
        /// If included in `supported_events`, the extension is called when the HTTP response body arrives.
        /// </summary>
        public static ExtensionChainExtensionSupportedEventsItem ResponseBody { get; } = new ExtensionChainExtensionSupportedEventsItem("RESPONSE_BODY");

        public static bool operator ==(ExtensionChainExtensionSupportedEventsItem left, ExtensionChainExtensionSupportedEventsItem right) => left.Equals(right);
        public static bool operator !=(ExtensionChainExtensionSupportedEventsItem left, ExtensionChainExtensionSupportedEventsItem right) => !left.Equals(right);

        public static explicit operator string(ExtensionChainExtensionSupportedEventsItem value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ExtensionChainExtensionSupportedEventsItem other && Equals(other);
        public bool Equals(ExtensionChainExtensionSupportedEventsItem other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Immutable. The type of the customer managed gateway. This field is required. If unspecified, an error is returned.
    /// </summary>
    [EnumType]
    public readonly struct GatewayType : IEquatable<GatewayType>
    {
        private readonly string _value;

        private GatewayType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// The type of the customer managed gateway is unspecified.
        /// </summary>
        public static GatewayType TypeUnspecified { get; } = new GatewayType("TYPE_UNSPECIFIED");
        /// <summary>
        /// The type of the customer managed gateway is TrafficDirector Open Mesh.
        /// </summary>
        public static GatewayType OpenMesh { get; } = new GatewayType("OPEN_MESH");
        /// <summary>
        /// The type of the customer managed gateway is SecureWebGateway (SWG).
        /// </summary>
        public static GatewayType SecureWebGateway { get; } = new GatewayType("SECURE_WEB_GATEWAY");

        public static bool operator ==(GatewayType left, GatewayType right) => left.Equals(right);
        public static bool operator !=(GatewayType left, GatewayType right) => !left.Equals(right);

        public static explicit operator string(GatewayType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is GatewayType other && Equals(other);
        public bool Equals(GatewayType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Optional. Specifies how to match against the value of the header. If not specified, a default value of EXACT is used.
    /// </summary>
    [EnumType]
    public readonly struct GrpcRouteHeaderMatchType : IEquatable<GrpcRouteHeaderMatchType>
    {
        private readonly string _value;

        private GrpcRouteHeaderMatchType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// Unspecified.
        /// </summary>
        public static GrpcRouteHeaderMatchType TypeUnspecified { get; } = new GrpcRouteHeaderMatchType("TYPE_UNSPECIFIED");
        /// <summary>
        /// Will only match the exact value provided.
        /// </summary>
        public static GrpcRouteHeaderMatchType Exact { get; } = new GrpcRouteHeaderMatchType("EXACT");
        /// <summary>
        /// Will match paths conforming to the prefix specified by value. RE2 syntax is supported.
        /// </summary>
        public static GrpcRouteHeaderMatchType RegularExpression { get; } = new GrpcRouteHeaderMatchType("REGULAR_EXPRESSION");

        public static bool operator ==(GrpcRouteHeaderMatchType left, GrpcRouteHeaderMatchType right) => left.Equals(right);
        public static bool operator !=(GrpcRouteHeaderMatchType left, GrpcRouteHeaderMatchType right) => !left.Equals(right);

        public static explicit operator string(GrpcRouteHeaderMatchType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is GrpcRouteHeaderMatchType other && Equals(other);
        public bool Equals(GrpcRouteHeaderMatchType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Optional. Specifies how to match against the name. If not specified, a default value of "EXACT" is used.
    /// </summary>
    [EnumType]
    public readonly struct GrpcRouteMethodMatchType : IEquatable<GrpcRouteMethodMatchType>
    {
        private readonly string _value;

        private GrpcRouteMethodMatchType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// Unspecified.
        /// </summary>
        public static GrpcRouteMethodMatchType TypeUnspecified { get; } = new GrpcRouteMethodMatchType("TYPE_UNSPECIFIED");
        /// <summary>
        /// Will only match the exact name provided.
        /// </summary>
        public static GrpcRouteMethodMatchType Exact { get; } = new GrpcRouteMethodMatchType("EXACT");
        /// <summary>
        /// Will interpret grpc_method and grpc_service as regexes. RE2 syntax is supported.
        /// </summary>
        public static GrpcRouteMethodMatchType RegularExpression { get; } = new GrpcRouteMethodMatchType("REGULAR_EXPRESSION");

        public static bool operator ==(GrpcRouteMethodMatchType left, GrpcRouteMethodMatchType right) => left.Equals(right);
        public static bool operator !=(GrpcRouteMethodMatchType left, GrpcRouteMethodMatchType right) => !left.Equals(right);

        public static explicit operator string(GrpcRouteMethodMatchType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is GrpcRouteMethodMatchType other && Equals(other);
        public bool Equals(GrpcRouteMethodMatchType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The HTTP Status code to use for the redirect.
    /// </summary>
    [EnumType]
    public readonly struct HttpRouteRedirectResponseCode : IEquatable<HttpRouteRedirectResponseCode>
    {
        private readonly string _value;

        private HttpRouteRedirectResponseCode(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// Default value
        /// </summary>
        public static HttpRouteRedirectResponseCode ResponseCodeUnspecified { get; } = new HttpRouteRedirectResponseCode("RESPONSE_CODE_UNSPECIFIED");
        /// <summary>
        /// Corresponds to 301.
        /// </summary>
        public static HttpRouteRedirectResponseCode MovedPermanentlyDefault { get; } = new HttpRouteRedirectResponseCode("MOVED_PERMANENTLY_DEFAULT");
        /// <summary>
        /// Corresponds to 302.
        /// </summary>
        public static HttpRouteRedirectResponseCode Found { get; } = new HttpRouteRedirectResponseCode("FOUND");
        /// <summary>
        /// Corresponds to 303.
        /// </summary>
        public static HttpRouteRedirectResponseCode SeeOther { get; } = new HttpRouteRedirectResponseCode("SEE_OTHER");
        /// <summary>
        /// Corresponds to 307. In this case, the request method will be retained.
        /// </summary>
        public static HttpRouteRedirectResponseCode TemporaryRedirect { get; } = new HttpRouteRedirectResponseCode("TEMPORARY_REDIRECT");
        /// <summary>
        /// Corresponds to 308. In this case, the request method will be retained.
        /// </summary>
        public static HttpRouteRedirectResponseCode PermanentRedirect { get; } = new HttpRouteRedirectResponseCode("PERMANENT_REDIRECT");

        public static bool operator ==(HttpRouteRedirectResponseCode left, HttpRouteRedirectResponseCode right) => left.Equals(right);
        public static bool operator !=(HttpRouteRedirectResponseCode left, HttpRouteRedirectResponseCode right) => !left.Equals(right);

        public static explicit operator string(HttpRouteRedirectResponseCode value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is HttpRouteRedirectResponseCode other && Equals(other);
        public bool Equals(HttpRouteRedirectResponseCode other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Required. All backend services and forwarding rules referenced by this extension must share the same load balancing scheme. Supported values: `INTERNAL_MANAGED`, `EXTERNAL_MANAGED`. For more information, refer to [Choosing a load balancer](https://cloud.google.com/load-balancing/docs/backend-service).
    /// </summary>
    [EnumType]
    public readonly struct LbRouteExtensionLoadBalancingScheme : IEquatable<LbRouteExtensionLoadBalancingScheme>
    {
        private readonly string _value;

        private LbRouteExtensionLoadBalancingScheme(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// Default value. Do not use.
        /// </summary>
        public static LbRouteExtensionLoadBalancingScheme LoadBalancingSchemeUnspecified { get; } = new LbRouteExtensionLoadBalancingScheme("LOAD_BALANCING_SCHEME_UNSPECIFIED");
        /// <summary>
        /// Signifies that this is used for Internal HTTP(S) Load Balancing.
        /// </summary>
        public static LbRouteExtensionLoadBalancingScheme InternalManaged { get; } = new LbRouteExtensionLoadBalancingScheme("INTERNAL_MANAGED");
        /// <summary>
        /// Signifies that this is used for External Managed HTTP(S) Load Balancing.
        /// </summary>
        public static LbRouteExtensionLoadBalancingScheme ExternalManaged { get; } = new LbRouteExtensionLoadBalancingScheme("EXTERNAL_MANAGED");

        public static bool operator ==(LbRouteExtensionLoadBalancingScheme left, LbRouteExtensionLoadBalancingScheme right) => left.Equals(right);
        public static bool operator !=(LbRouteExtensionLoadBalancingScheme left, LbRouteExtensionLoadBalancingScheme right) => !left.Equals(right);

        public static explicit operator string(LbRouteExtensionLoadBalancingScheme value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is LbRouteExtensionLoadBalancingScheme other && Equals(other);
        public bool Equals(LbRouteExtensionLoadBalancingScheme other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Required. All backend services and forwarding rules referenced by this extension must share the same load balancing scheme. Supported values: `INTERNAL_MANAGED`, `EXTERNAL_MANAGED`. For more information, refer to [Choosing a load balancer](https://cloud.google.com/load-balancing/docs/backend-service).
    /// </summary>
    [EnumType]
    public readonly struct LbTrafficExtensionLoadBalancingScheme : IEquatable<LbTrafficExtensionLoadBalancingScheme>
    {
        private readonly string _value;

        private LbTrafficExtensionLoadBalancingScheme(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// Default value. Do not use.
        /// </summary>
        public static LbTrafficExtensionLoadBalancingScheme LoadBalancingSchemeUnspecified { get; } = new LbTrafficExtensionLoadBalancingScheme("LOAD_BALANCING_SCHEME_UNSPECIFIED");
        /// <summary>
        /// Signifies that this is used for Internal HTTP(S) Load Balancing.
        /// </summary>
        public static LbTrafficExtensionLoadBalancingScheme InternalManaged { get; } = new LbTrafficExtensionLoadBalancingScheme("INTERNAL_MANAGED");
        /// <summary>
        /// Signifies that this is used for External Managed HTTP(S) Load Balancing.
        /// </summary>
        public static LbTrafficExtensionLoadBalancingScheme ExternalManaged { get; } = new LbTrafficExtensionLoadBalancingScheme("EXTERNAL_MANAGED");

        public static bool operator ==(LbTrafficExtensionLoadBalancingScheme left, LbTrafficExtensionLoadBalancingScheme right) => left.Equals(right);
        public static bool operator !=(LbTrafficExtensionLoadBalancingScheme left, LbTrafficExtensionLoadBalancingScheme right) => !left.Equals(right);

        public static explicit operator string(LbTrafficExtensionLoadBalancingScheme value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is LbTrafficExtensionLoadBalancingScheme other && Equals(other);
        public bool Equals(LbTrafficExtensionLoadBalancingScheme other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Specifies how matching should be done. Supported values are: MATCH_ANY: At least one of the Labels specified in the matcher should match the metadata presented by xDS client. MATCH_ALL: The metadata presented by the xDS client should contain all of the labels specified here. The selection is determined based on the best match. For example, suppose there are three EndpointPolicy resources P1, P2 and P3 and if P1 has a the matcher as MATCH_ANY , P2 has MATCH_ALL , and P3 has MATCH_ALL . If a client with label connects, the config from P1 will be selected. If a client with label connects, the config from P2 will be selected. If a client with label connects, the config from P3 will be selected. If there is more than one best match, (for example, if a config P4 with selector exists and if a client with label connects), an error will be thrown.
    /// </summary>
    [EnumType]
    public readonly struct MetadataLabelMatcherMetadataLabelMatchCriteria : IEquatable<MetadataLabelMatcherMetadataLabelMatchCriteria>
    {
        private readonly string _value;

        private MetadataLabelMatcherMetadataLabelMatchCriteria(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// Default value. Should not be used.
        /// </summary>
        public static MetadataLabelMatcherMetadataLabelMatchCriteria MetadataLabelMatchCriteriaUnspecified { get; } = new MetadataLabelMatcherMetadataLabelMatchCriteria("METADATA_LABEL_MATCH_CRITERIA_UNSPECIFIED");
        /// <summary>
        /// At least one of the Labels specified in the matcher should match the metadata presented by xDS client.
        /// </summary>
        public static MetadataLabelMatcherMetadataLabelMatchCriteria MatchAny { get; } = new MetadataLabelMatcherMetadataLabelMatchCriteria("MATCH_ANY");
        /// <summary>
        /// The metadata presented by the xDS client should contain all of the labels specified here.
        /// </summary>
        public static MetadataLabelMatcherMetadataLabelMatchCriteria MatchAll { get; } = new MetadataLabelMatcherMetadataLabelMatchCriteria("MATCH_ALL");

        public static bool operator ==(MetadataLabelMatcherMetadataLabelMatchCriteria left, MetadataLabelMatcherMetadataLabelMatchCriteria right) => left.Equals(right);
        public static bool operator !=(MetadataLabelMatcherMetadataLabelMatchCriteria left, MetadataLabelMatcherMetadataLabelMatchCriteria right) => !left.Equals(right);

        public static explicit operator string(MetadataLabelMatcherMetadataLabelMatchCriteria value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is MetadataLabelMatcherMetadataLabelMatchCriteria other && Equals(other);
        public bool Equals(MetadataLabelMatcherMetadataLabelMatchCriteria other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Optional. The type of load balancing algorithm to be used. The default behavior is WATERFALL_BY_REGION.
    /// </summary>
    [EnumType]
    public readonly struct ServiceLbPolicyLoadBalancingAlgorithm : IEquatable<ServiceLbPolicyLoadBalancingAlgorithm>
    {
        private readonly string _value;

        private ServiceLbPolicyLoadBalancingAlgorithm(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// The type of the loadbalancing algorithm is unspecified.
        /// </summary>
        public static ServiceLbPolicyLoadBalancingAlgorithm LoadBalancingAlgorithmUnspecified { get; } = new ServiceLbPolicyLoadBalancingAlgorithm("LOAD_BALANCING_ALGORITHM_UNSPECIFIED");
        /// <summary>
        /// Balance traffic across all backends across the world proportionally based on capacity.
        /// </summary>
        public static ServiceLbPolicyLoadBalancingAlgorithm SprayToWorld { get; } = new ServiceLbPolicyLoadBalancingAlgorithm("SPRAY_TO_WORLD");
        /// <summary>
        /// Direct traffic to the nearest region with endpoints and capacity before spilling over to other regions and spread the traffic from each client to all the MIGs/NEGs in a region.
        /// </summary>
        public static ServiceLbPolicyLoadBalancingAlgorithm SprayToRegion { get; } = new ServiceLbPolicyLoadBalancingAlgorithm("SPRAY_TO_REGION");
        /// <summary>
        /// Direct traffic to the nearest region with endpoints and capacity before spilling over to other regions. All MIGs/NEGs within a region are evenly loaded but each client might not spread the traffic to all the MIGs/NEGs in the region.
        /// </summary>
        public static ServiceLbPolicyLoadBalancingAlgorithm WaterfallByRegion { get; } = new ServiceLbPolicyLoadBalancingAlgorithm("WATERFALL_BY_REGION");
        /// <summary>
        /// Attempt to keep traffic in a single zone closest to the client, before spilling over to other zones.
        /// </summary>
        public static ServiceLbPolicyLoadBalancingAlgorithm WaterfallByZone { get; } = new ServiceLbPolicyLoadBalancingAlgorithm("WATERFALL_BY_ZONE");

        public static bool operator ==(ServiceLbPolicyLoadBalancingAlgorithm left, ServiceLbPolicyLoadBalancingAlgorithm right) => left.Equals(right);
        public static bool operator !=(ServiceLbPolicyLoadBalancingAlgorithm left, ServiceLbPolicyLoadBalancingAlgorithm right) => !left.Equals(right);

        public static explicit operator string(ServiceLbPolicyLoadBalancingAlgorithm value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ServiceLbPolicyLoadBalancingAlgorithm other && Equals(other);
        public bool Equals(ServiceLbPolicyLoadBalancingAlgorithm other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
