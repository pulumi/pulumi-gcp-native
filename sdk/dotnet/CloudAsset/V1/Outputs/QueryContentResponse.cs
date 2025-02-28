// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.CloudAsset.V1.Outputs
{

    /// <summary>
    /// The query content.
    /// </summary>
    [OutputType]
    public sealed class QueryContentResponse
    {
        /// <summary>
        /// An IAM Policy Analysis query, which could be used in the AssetService.AnalyzeIamPolicy RPC or the AssetService.AnalyzeIamPolicyLongrunning RPC.
        /// </summary>
        public readonly Outputs.IamPolicyAnalysisQueryResponse IamPolicyAnalysisQuery;

        [OutputConstructor]
        private QueryContentResponse(Outputs.IamPolicyAnalysisQueryResponse iamPolicyAnalysisQuery)
        {
            IamPolicyAnalysisQuery = iamPolicyAnalysisQuery;
        }
    }
}
