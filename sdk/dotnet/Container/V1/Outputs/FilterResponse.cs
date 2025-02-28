// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Container.V1.Outputs
{

    /// <summary>
    /// Allows filtering to one or more specific event types. If event types are present, those and only those event types will be transmitted to the cluster. Other types will be skipped. If no filter is specified, or no event types are present, all event types will be sent
    /// </summary>
    [OutputType]
    public sealed class FilterResponse
    {
        /// <summary>
        /// Event types to allowlist.
        /// </summary>
        public readonly ImmutableArray<string> EventType;

        [OutputConstructor]
        private FilterResponse(ImmutableArray<string> eventType)
        {
            EventType = eventType;
        }
    }
}
