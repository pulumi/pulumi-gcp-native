// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.ContainerAnalysis.V1Alpha1.Inputs
{

    public sealed class BuildDefinitionArgs : global::Pulumi.ResourceArgs
    {
        [Input("buildType")]
        public Input<string>? BuildType { get; set; }

        [Input("externalParameters")]
        private InputMap<object>? _externalParameters;
        public InputMap<object> ExternalParameters
        {
            get => _externalParameters ?? (_externalParameters = new InputMap<object>());
            set => _externalParameters = value;
        }

        [Input("internalParameters")]
        private InputMap<object>? _internalParameters;
        public InputMap<object> InternalParameters
        {
            get => _internalParameters ?? (_internalParameters = new InputMap<object>());
            set => _internalParameters = value;
        }

        [Input("resolvedDependencies")]
        private InputList<Inputs.ResourceDescriptorArgs>? _resolvedDependencies;
        public InputList<Inputs.ResourceDescriptorArgs> ResolvedDependencies
        {
            get => _resolvedDependencies ?? (_resolvedDependencies = new InputList<Inputs.ResourceDescriptorArgs>());
            set => _resolvedDependencies = value;
        }

        public BuildDefinitionArgs()
        {
        }
        public static new BuildDefinitionArgs Empty => new BuildDefinitionArgs();
    }
}
