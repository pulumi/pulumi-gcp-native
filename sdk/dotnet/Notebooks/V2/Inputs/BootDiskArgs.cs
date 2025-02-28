// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Notebooks.V2.Inputs
{

    /// <summary>
    /// The definition of a boot disk.
    /// </summary>
    public sealed class BootDiskArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. Input only. Disk encryption method used on the boot and data disks, defaults to GMEK.
        /// </summary>
        [Input("diskEncryption")]
        public Input<Pulumi.GoogleNative.Notebooks.V2.BootDiskDiskEncryption>? DiskEncryption { get; set; }

        /// <summary>
        /// Optional. The size of the boot disk in GB attached to this instance, up to a maximum of 64000 GB (64 TB). If not specified, this defaults to the recommended value of 150GB.
        /// </summary>
        [Input("diskSizeGb")]
        public Input<string>? DiskSizeGb { get; set; }

        /// <summary>
        /// Optional. Indicates the type of the disk.
        /// </summary>
        [Input("diskType")]
        public Input<Pulumi.GoogleNative.Notebooks.V2.BootDiskDiskType>? DiskType { get; set; }

        /// <summary>
        /// Optional. Input only. The KMS key used to encrypt the disks, only applicable if disk_encryption is CMEK. Format: `projects/{project_id}/locations/{location}/keyRings/{key_ring_id}/cryptoKeys/{key_id}` Learn more about using your own encryption keys.
        /// </summary>
        [Input("kmsKey")]
        public Input<string>? KmsKey { get; set; }

        public BootDiskArgs()
        {
        }
        public static new BootDiskArgs Empty => new BootDiskArgs();
    }
}
