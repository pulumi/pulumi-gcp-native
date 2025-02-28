// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dialogflow.V2.Inputs
{

    /// <summary>
    /// Smart reply specific configuration for evaluation job.
    /// </summary>
    public sealed class GoogleCloudDialogflowV2EvaluationConfigSmartReplyConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The allowlist document resource name. Format: `projects//knowledgeBases//documents/`. Only used for smart reply model.
        /// </summary>
        [Input("allowlistDocument")]
        public Input<string>? AllowlistDocument { get; set; }

        /// <summary>
        /// The model to be evaluated can return multiple results with confidence score on each query. These results will be sorted by the descending order of the scores and we only keep the first max_result_count results as the final results to evaluate.
        /// </summary>
        [Input("maxResultCount", required: true)]
        public Input<int> MaxResultCount { get; set; } = null!;

        public GoogleCloudDialogflowV2EvaluationConfigSmartReplyConfigArgs()
        {
        }
        public static new GoogleCloudDialogflowV2EvaluationConfigSmartReplyConfigArgs Empty => new GoogleCloudDialogflowV2EvaluationConfigSmartReplyConfigArgs();
    }
}
