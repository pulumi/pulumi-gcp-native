// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dialogflow.V3.Inputs
{

    /// <summary>
    /// Each case has a Boolean condition. When it is evaluated to be True, the corresponding messages will be selected and evaluated recursively.
    /// </summary>
    public sealed class GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseArgs : global::Pulumi.ResourceArgs
    {
        [Input("caseContent")]
        private InputList<Inputs.GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentArgs>? _caseContent;

        /// <summary>
        /// A list of case content.
        /// </summary>
        public InputList<Inputs.GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentArgs> CaseContent
        {
            get => _caseContent ?? (_caseContent = new InputList<Inputs.GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContentArgs>());
            set => _caseContent = value;
        }

        /// <summary>
        /// The condition to activate and select this case. Empty means the condition is always true. The condition is evaluated against form parameters or session parameters. See the [conditions reference](https://cloud.google.com/dialogflow/cx/docs/reference/condition).
        /// </summary>
        [Input("condition")]
        public Input<string>? Condition { get; set; }

        public GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseArgs()
        {
        }
        public static new GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseArgs Empty => new GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseArgs();
    }
}
