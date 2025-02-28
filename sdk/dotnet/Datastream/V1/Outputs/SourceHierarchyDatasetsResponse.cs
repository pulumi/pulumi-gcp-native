// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Datastream.V1.Outputs
{

    /// <summary>
    /// Destination datasets are created so that hierarchy of the destination data objects matches the source hierarchy.
    /// </summary>
    [OutputType]
    public sealed class SourceHierarchyDatasetsResponse
    {
        /// <summary>
        /// The dataset template to use for dynamic dataset creation.
        /// </summary>
        public readonly Outputs.DatasetTemplateResponse DatasetTemplate;

        [OutputConstructor]
        private SourceHierarchyDatasetsResponse(Outputs.DatasetTemplateResponse datasetTemplate)
        {
            DatasetTemplate = datasetTemplate;
        }
    }
}
