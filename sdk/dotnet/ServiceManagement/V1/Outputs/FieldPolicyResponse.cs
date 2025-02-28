// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.ServiceManagement.V1.Outputs
{

    /// <summary>
    /// Google API Policy Annotation This message defines a simple API policy annotation that can be used to annotate API request and response message fields with applicable policies. One field may have multiple applicable policies that must all be satisfied before a request can be processed. This policy annotation is used to generate the overall policy that will be used for automatic runtime policy enforcement and documentation generation.
    /// </summary>
    [OutputType]
    public sealed class FieldPolicyResponse
    {
        /// <summary>
        /// Specifies the required permission(s) for the resource referred to by the field. It requires the field contains a valid resource reference, and the request must pass the permission checks to proceed. For example, "resourcemanager.projects.get".
        /// </summary>
        public readonly string ResourcePermission;
        /// <summary>
        /// Specifies the resource type for the resource referred to by the field.
        /// </summary>
        public readonly string ResourceType;
        /// <summary>
        /// Selects one or more request or response message fields to apply this `FieldPolicy`. When a `FieldPolicy` is used in proto annotation, the selector must be left as empty. The service config generator will automatically fill the correct value. When a `FieldPolicy` is used in service config, the selector must be a comma-separated string with valid request or response field paths, such as "foo.bar" or "foo.bar,foo.baz".
        /// </summary>
        public readonly string Selector;

        [OutputConstructor]
        private FieldPolicyResponse(
            string resourcePermission,

            string resourceType,

            string selector)
        {
            ResourcePermission = resourcePermission;
            ResourceType = resourceType;
            Selector = selector;
        }
    }
}
