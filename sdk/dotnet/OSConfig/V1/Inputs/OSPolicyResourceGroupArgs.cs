// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.OSConfig.V1.Inputs
{

    /// <summary>
    /// Resource groups provide a mechanism to group OS policy resources. Resource groups enable OS policy authors to create a single OS policy to be applied to VMs running different operating Systems. When the OS policy is applied to a target VM, the appropriate resource group within the OS policy is selected based on the `OSFilter` specified within the resource group.
    /// </summary>
    public sealed class OSPolicyResourceGroupArgs : global::Pulumi.ResourceArgs
    {
        [Input("inventoryFilters")]
        private InputList<Inputs.OSPolicyInventoryFilterArgs>? _inventoryFilters;

        /// <summary>
        /// List of inventory filters for the resource group. The resources in this resource group are applied to the target VM if it satisfies at least one of the following inventory filters. For example, to apply this resource group to VMs running either `RHEL` or `CentOS` operating systems, specify 2 items for the list with following values: inventory_filters[0].os_short_name='rhel' and inventory_filters[1].os_short_name='centos' If the list is empty, this resource group will be applied to the target VM unconditionally.
        /// </summary>
        public InputList<Inputs.OSPolicyInventoryFilterArgs> InventoryFilters
        {
            get => _inventoryFilters ?? (_inventoryFilters = new InputList<Inputs.OSPolicyInventoryFilterArgs>());
            set => _inventoryFilters = value;
        }

        [Input("resources", required: true)]
        private InputList<Inputs.OSPolicyResourceArgs>? _resources;

        /// <summary>
        /// List of resources configured for this resource group. The resources are executed in the exact order specified here.
        /// </summary>
        public InputList<Inputs.OSPolicyResourceArgs> Resources
        {
            get => _resources ?? (_resources = new InputList<Inputs.OSPolicyResourceArgs>());
            set => _resources = value;
        }

        public OSPolicyResourceGroupArgs()
        {
        }
        public static new OSPolicyResourceGroupArgs Empty => new OSPolicyResourceGroupArgs();
    }
}
