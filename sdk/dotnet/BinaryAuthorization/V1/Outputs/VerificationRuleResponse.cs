// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.BinaryAuthorization.V1.Outputs
{

    /// <summary>
    /// Specifies verification rules for evaluating the SLSA attestations including: which builders to trust, where to fetch the SLSA attestations generated by those builders, and other builder-specific evaluation rules such as which source repositories are trusted. An image is considered verified by the rule if any of the fetched SLSA attestations is verified.
    /// </summary>
    [OutputType]
    public sealed class VerificationRuleResponse
    {
        /// <summary>
        /// Specifies where to fetch the provenances attestations generated by the builder (group).
        /// </summary>
        public readonly Outputs.AttestationSourceResponse AttestationSource;
        /// <summary>
        /// If true, require the image to be built from a top-level configuration. `trusted_source_repo_patterns` specifies the repositories containing this configuration.
        /// </summary>
        public readonly bool ConfigBasedBuildRequired;
        /// <summary>
        /// Each verification rule is used for evaluation against provenances generated by a specific builder (group). For some of the builders, such as the Google Cloud Build, users don't need to explicitly specify their roots of trust in the policy since the evaluation service can automatically fetch them based on the builder (group).
        /// </summary>
        public readonly string TrustedBuilder;
        /// <summary>
        /// List of trusted source code repository URL patterns. These patterns match the full repository URL without its scheme (e.g. `https://`). The patterns must not include schemes. For example, the pattern `source.cloud.google.com/my-project/my-repo-name` matches the following URLs: - `source.cloud.google.com/my-project/my-repo-name` - `git+ssh://source.cloud.google.com/my-project/my-repo-name` - `https://source.cloud.google.com/my-project/my-repo-name` A pattern matches a URL either exactly or with `*` wildcards. `*` can be used in only two ways: 1. trailing `*` after hosturi/ to match varying endings; 2. trailing `**` after hosturi/ to match `/` as well. `*` and `**` can only be used as wildcards and can only occur at the end of the pattern after a `/`. (So it's not possible to match a URL that contains literal `*`.) For example: - `github.com/my-project/my-repo` is valid to match a single repo - `github.com/my-project/*` will match all direct repos in `my-project` - `github.com/**` matches all repos in GitHub
        /// </summary>
        public readonly ImmutableArray<string> TrustedSourceRepoPatterns;

        [OutputConstructor]
        private VerificationRuleResponse(
            Outputs.AttestationSourceResponse attestationSource,

            bool configBasedBuildRequired,

            string trustedBuilder,

            ImmutableArray<string> trustedSourceRepoPatterns)
        {
            AttestationSource = attestationSource;
            ConfigBasedBuildRequired = configBasedBuildRequired;
            TrustedBuilder = trustedBuilder;
            TrustedSourceRepoPatterns = trustedSourceRepoPatterns;
        }
    }
}
