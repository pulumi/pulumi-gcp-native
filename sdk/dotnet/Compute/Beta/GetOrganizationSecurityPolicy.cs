// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Compute.Beta
{
    public static class GetOrganizationSecurityPolicy
    {
        /// <summary>
        /// List all of the ordered rules present in a single specified policy.
        /// </summary>
        public static Task<GetOrganizationSecurityPolicyResult> InvokeAsync(GetOrganizationSecurityPolicyArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetOrganizationSecurityPolicyResult>("google-native:compute/beta:getOrganizationSecurityPolicy", args ?? new GetOrganizationSecurityPolicyArgs(), options.WithDefaults());

        /// <summary>
        /// List all of the ordered rules present in a single specified policy.
        /// </summary>
        public static Output<GetOrganizationSecurityPolicyResult> Invoke(GetOrganizationSecurityPolicyInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetOrganizationSecurityPolicyResult>("google-native:compute/beta:getOrganizationSecurityPolicy", args ?? new GetOrganizationSecurityPolicyInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetOrganizationSecurityPolicyArgs : global::Pulumi.InvokeArgs
    {
        [Input("securityPolicy", required: true)]
        public string SecurityPolicy { get; set; } = null!;

        public GetOrganizationSecurityPolicyArgs()
        {
        }
        public static new GetOrganizationSecurityPolicyArgs Empty => new GetOrganizationSecurityPolicyArgs();
    }

    public sealed class GetOrganizationSecurityPolicyInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("securityPolicy", required: true)]
        public Input<string> SecurityPolicy { get; set; } = null!;

        public GetOrganizationSecurityPolicyInvokeArgs()
        {
        }
        public static new GetOrganizationSecurityPolicyInvokeArgs Empty => new GetOrganizationSecurityPolicyInvokeArgs();
    }


    [OutputType]
    public sealed class GetOrganizationSecurityPolicyResult
    {
        public readonly Outputs.SecurityPolicyAdaptiveProtectionConfigResponse AdaptiveProtectionConfig;
        public readonly Outputs.SecurityPolicyAdvancedOptionsConfigResponse AdvancedOptionsConfig;
        /// <summary>
        /// A list of associations that belong to this policy.
        /// </summary>
        public readonly ImmutableArray<Outputs.SecurityPolicyAssociationResponse> Associations;
        /// <summary>
        /// Creation timestamp in RFC3339 text format.
        /// </summary>
        public readonly string CreationTimestamp;
        public readonly Outputs.SecurityPolicyDdosProtectionConfigResponse DdosProtectionConfig;
        /// <summary>
        /// An optional description of this resource. Provide this property when you create the resource.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// User-provided name of the Organization security plicy. The name should be unique in the organization in which the security policy is created. This should only be used when SecurityPolicyType is FIREWALL. The name must be 1-63 characters long, and comply with https://www.ietf.org/rfc/rfc1035.txt. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// Specifies a fingerprint for this resource, which is essentially a hash of the metadata's contents and used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update metadata. You must always provide an up-to-date fingerprint hash in order to update or change metadata, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make get() request to the security policy.
        /// </summary>
        public readonly string Fingerprint;
        /// <summary>
        /// [Output only] Type of the resource. Always compute#securityPolicyfor security policies
        /// </summary>
        public readonly string Kind;
        /// <summary>
        /// A fingerprint for the labels being applied to this security policy, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels. To see the latest fingerprint, make get() request to the security policy.
        /// </summary>
        public readonly string LabelFingerprint;
        /// <summary>
        /// Labels for this resource. These can only be added or modified by the setLabels method. Each label key/value pair must comply with RFC1035. Label values may be empty.
        /// </summary>
        public readonly ImmutableDictionary<string, string> Labels;
        /// <summary>
        /// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The parent of the security policy.
        /// </summary>
        public readonly string Parent;
        public readonly Outputs.SecurityPolicyRecaptchaOptionsConfigResponse RecaptchaOptionsConfig;
        /// <summary>
        /// URL of the region where the regional security policy resides. This field is not applicable to global security policies.
        /// </summary>
        public readonly string Region;
        /// <summary>
        /// Total count of all security policy rule tuples. A security policy can not exceed a set number of tuples.
        /// </summary>
        public readonly int RuleTupleCount;
        /// <summary>
        /// A list of rules that belong to this policy. There must always be a default rule which is a rule with priority 2147483647 and match all condition (for the match condition this means match "*" for srcIpRanges and for the networkMatch condition every field must be either match "*" or not set). If no rules are provided when creating a security policy, a default rule with action "allow" will be added.
        /// </summary>
        public readonly ImmutableArray<Outputs.SecurityPolicyRuleResponse> Rules;
        /// <summary>
        /// Server-defined URL for the resource.
        /// </summary>
        public readonly string SelfLink;
        /// <summary>
        /// Server-defined URL for this resource with the resource id.
        /// </summary>
        public readonly string SelfLinkWithId;
        /// <summary>
        /// The type indicates the intended use of the security policy. - CLOUD_ARMOR: Cloud Armor backend security policies can be configured to filter incoming HTTP requests targeting backend services. They filter requests before they hit the origin servers. - CLOUD_ARMOR_EDGE: Cloud Armor edge security policies can be configured to filter incoming HTTP requests targeting backend services (including Cloud CDN-enabled) as well as backend buckets (Cloud Storage). They filter requests before the request is served from Google's cache. - CLOUD_ARMOR_INTERNAL_SERVICE: Cloud Armor internal service policies can be configured to filter HTTP requests targeting services managed by Traffic Director in a service mesh. They filter requests before the request is served from the application. - CLOUD_ARMOR_NETWORK: Cloud Armor network policies can be configured to filter packets targeting network load balancing resources such as backend services, target pools, target instances, and instances with external IPs. They filter requests before the request is served from the application. This field can be set only at resource creation time.
        /// </summary>
        public readonly string Type;
        /// <summary>
        /// Definitions of user-defined fields for CLOUD_ARMOR_NETWORK policies. A user-defined field consists of up to 4 bytes extracted from a fixed offset in the packet, relative to the IPv4, IPv6, TCP, or UDP header, with an optional mask to select certain bits. Rules may then specify matching values for these fields. Example: userDefinedFields: - name: "ipv4_fragment_offset" base: IPV4 offset: 6 size: 2 mask: "0x1fff"
        /// </summary>
        public readonly ImmutableArray<Outputs.SecurityPolicyUserDefinedFieldResponse> UserDefinedFields;

        [OutputConstructor]
        private GetOrganizationSecurityPolicyResult(
            Outputs.SecurityPolicyAdaptiveProtectionConfigResponse adaptiveProtectionConfig,

            Outputs.SecurityPolicyAdvancedOptionsConfigResponse advancedOptionsConfig,

            ImmutableArray<Outputs.SecurityPolicyAssociationResponse> associations,

            string creationTimestamp,

            Outputs.SecurityPolicyDdosProtectionConfigResponse ddosProtectionConfig,

            string description,

            string displayName,

            string fingerprint,

            string kind,

            string labelFingerprint,

            ImmutableDictionary<string, string> labels,

            string name,

            string parent,

            Outputs.SecurityPolicyRecaptchaOptionsConfigResponse recaptchaOptionsConfig,

            string region,

            int ruleTupleCount,

            ImmutableArray<Outputs.SecurityPolicyRuleResponse> rules,

            string selfLink,

            string selfLinkWithId,

            string type,

            ImmutableArray<Outputs.SecurityPolicyUserDefinedFieldResponse> userDefinedFields)
        {
            AdaptiveProtectionConfig = adaptiveProtectionConfig;
            AdvancedOptionsConfig = advancedOptionsConfig;
            Associations = associations;
            CreationTimestamp = creationTimestamp;
            DdosProtectionConfig = ddosProtectionConfig;
            Description = description;
            DisplayName = displayName;
            Fingerprint = fingerprint;
            Kind = kind;
            LabelFingerprint = labelFingerprint;
            Labels = labels;
            Name = name;
            Parent = parent;
            RecaptchaOptionsConfig = recaptchaOptionsConfig;
            Region = region;
            RuleTupleCount = ruleTupleCount;
            Rules = rules;
            SelfLink = selfLink;
            SelfLinkWithId = selfLinkWithId;
            Type = type;
            UserDefinedFields = userDefinedFields;
        }
    }
}
