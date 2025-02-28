// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Healthcare.V1Beta1.Outputs
{

    /// <summary>
    /// Configures whether to enforce consent for the FHIR store and which consent enforcement version is being used.
    /// </summary>
    [OutputType]
    public sealed class ConsentConfigResponse
    {
        /// <summary>
        /// Optional. Specifies how the server logs the consent-aware requests. If not specified, the `AccessDeterminationLogConfig.LogLevel.MINIMUM` option is used.
        /// </summary>
        public readonly Outputs.AccessDeterminationLogConfigResponse AccessDeterminationLogConfig;
        /// <summary>
        /// Optional. If set to true, when accessing FHIR resources, the consent headers provided using [SMART-on-FHIR](https://cloud.google.com/healthcare/private/docs/how-tos/smart-on-fhir) will be verified against consents given by patients. See the ConsentEnforcementVersion for the supported consent headers.
        /// </summary>
        public readonly bool AccessEnforced;
        /// <summary>
        /// Optional. Different options to configure the behaviour of the server when handling the `X-Consent-Scope` header.
        /// </summary>
        public readonly Outputs.ConsentHeaderHandlingResponse ConsentHeaderHandling;
        /// <summary>
        /// The versioned names of the enforced admin Consent resource(s), in the format `projects/{project_id}/locations/{location}/datasets/{dataset_id}/fhirStores/{fhir_store_id}/fhir/Consent/{resource_id}/_history/{version_id}`. For FHIR stores with `disable_resource_versioning=true`, the format is `projects/{project_id}/locations/{location}/datasets/{dataset_id}/fhirStores/{fhir_store_id}/fhir/Consent/{resource_id}`. This field can only be updated using ApplyAdminConsents.
        /// </summary>
        public readonly ImmutableArray<string> EnforcedAdminConsents;
        /// <summary>
        /// Specifies which consent enforcement version is being used for this FHIR store. This field can only be set once by either CreateFhirStore or UpdateFhirStore. After that, you must call ApplyConsents to change the version.
        /// </summary>
        public readonly string Version;

        [OutputConstructor]
        private ConsentConfigResponse(
            Outputs.AccessDeterminationLogConfigResponse accessDeterminationLogConfig,

            bool accessEnforced,

            Outputs.ConsentHeaderHandlingResponse consentHeaderHandling,

            ImmutableArray<string> enforcedAdminConsents,

            string version)
        {
            AccessDeterminationLogConfig = accessDeterminationLogConfig;
            AccessEnforced = accessEnforced;
            ConsentHeaderHandling = consentHeaderHandling;
            EnforcedAdminConsents = enforcedAdminConsents;
            Version = version;
        }
    }
}
