// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1.Outputs
{

    /// <summary>
    /// Assigns input data to training, validation, and test sets based on the value of a provided key. Supported only for tabular Datasets.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudAiplatformV1PredefinedSplitResponse
    {
        /// <summary>
        /// The key is a name of one of the Dataset's data columns. The value of the key (either the label's value or value in the column) must be one of {`training`, `validation`, `test`}, and it defines to which set the given piece of data is assigned. If for a piece of data the key is not present or has an invalid value, that piece is ignored by the pipeline.
        /// </summary>
        public readonly string Key;

        [OutputConstructor]
        private GoogleCloudAiplatformV1PredefinedSplitResponse(string key)
        {
            Key = key;
        }
    }
}
