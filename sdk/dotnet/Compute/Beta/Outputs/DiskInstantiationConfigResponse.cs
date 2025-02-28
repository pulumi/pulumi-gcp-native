// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Compute.Beta.Outputs
{

    /// <summary>
    /// A specification of the desired way to instantiate a disk in the instance template when its created from a source instance.
    /// </summary>
    [OutputType]
    public sealed class DiskInstantiationConfigResponse
    {
        /// <summary>
        /// Specifies whether the disk will be auto-deleted when the instance is deleted (but not when the disk is detached from the instance).
        /// </summary>
        public readonly bool AutoDelete;
        /// <summary>
        /// The custom source image to be used to restore this disk when instantiating this instance template.
        /// </summary>
        public readonly string CustomImage;
        /// <summary>
        /// Specifies the device name of the disk to which the configurations apply to.
        /// </summary>
        public readonly string DeviceName;
        /// <summary>
        /// Specifies whether to include the disk and what image to use. Possible values are: - source-image: to use the same image that was used to create the source instance's corresponding disk. Applicable to the boot disk and additional read-write disks. - source-image-family: to use the same image family that was used to create the source instance's corresponding disk. Applicable to the boot disk and additional read-write disks. - custom-image: to use a user-provided image url for disk creation. Applicable to the boot disk and additional read-write disks. - attach-read-only: to attach a read-only disk. Applicable to read-only disks. - do-not-include: to exclude a disk from the template. Applicable to additional read-write disks, local SSDs, and read-only disks. 
        /// </summary>
        public readonly string InstantiateFrom;

        [OutputConstructor]
        private DiskInstantiationConfigResponse(
            bool autoDelete,

            string customImage,

            string deviceName,

            string instantiateFrom)
        {
            AutoDelete = autoDelete;
            CustomImage = customImage;
            DeviceName = deviceName;
            InstantiateFrom = instantiateFrom;
        }
    }
}
