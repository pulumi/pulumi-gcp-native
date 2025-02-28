// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Compute.Alpha.Inputs
{

    public sealed class InstanceGroupManagerInstanceFlexibilityPolicyArgs : global::Pulumi.ResourceArgs
    {
        [Input("instanceSelectionLists")]
        private InputMap<Inputs.InstanceGroupManagerInstanceFlexibilityPolicyInstanceSelectionArgs>? _instanceSelectionLists;

        /// <summary>
        /// Named instance selections configuring properties that the group will use when creating new VMs.
        /// </summary>
        public InputMap<Inputs.InstanceGroupManagerInstanceFlexibilityPolicyInstanceSelectionArgs> InstanceSelectionLists
        {
            get => _instanceSelectionLists ?? (_instanceSelectionLists = new InputMap<Inputs.InstanceGroupManagerInstanceFlexibilityPolicyInstanceSelectionArgs>());
            set => _instanceSelectionLists = value;
        }

        [Input("instanceSelections")]
        private InputMap<Inputs.InstanceGroupManagerInstanceFlexibilityPolicyInstanceSelectionArgs>? _instanceSelections;

        /// <summary>
        /// Named instance selections configuring properties that the group will use when creating new VMs.
        /// </summary>
        public InputMap<Inputs.InstanceGroupManagerInstanceFlexibilityPolicyInstanceSelectionArgs> InstanceSelections
        {
            get => _instanceSelections ?? (_instanceSelections = new InputMap<Inputs.InstanceGroupManagerInstanceFlexibilityPolicyInstanceSelectionArgs>());
            set => _instanceSelections = value;
        }

        public InstanceGroupManagerInstanceFlexibilityPolicyArgs()
        {
        }
        public static new InstanceGroupManagerInstanceFlexibilityPolicyArgs Empty => new InstanceGroupManagerInstanceFlexibilityPolicyArgs();
    }
}
