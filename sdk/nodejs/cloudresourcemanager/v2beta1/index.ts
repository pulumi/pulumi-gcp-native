// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

// Export members:
export { FolderArgs } from "./folder";
export type Folder = import("./folder").Folder;
export const Folder: typeof import("./folder").Folder = null as any;
utilities.lazyLoad(exports, ["Folder"], () => require("./folder"));

export { FolderIamBindingArgs } from "./folderIamBinding";
export type FolderIamBinding = import("./folderIamBinding").FolderIamBinding;
export const FolderIamBinding: typeof import("./folderIamBinding").FolderIamBinding = null as any;
utilities.lazyLoad(exports, ["FolderIamBinding"], () => require("./folderIamBinding"));

export { FolderIamMemberArgs } from "./folderIamMember";
export type FolderIamMember = import("./folderIamMember").FolderIamMember;
export const FolderIamMember: typeof import("./folderIamMember").FolderIamMember = null as any;
utilities.lazyLoad(exports, ["FolderIamMember"], () => require("./folderIamMember"));

export { FolderIamPolicyArgs } from "./folderIamPolicy";
export type FolderIamPolicy = import("./folderIamPolicy").FolderIamPolicy;
export const FolderIamPolicy: typeof import("./folderIamPolicy").FolderIamPolicy = null as any;
utilities.lazyLoad(exports, ["FolderIamPolicy"], () => require("./folderIamPolicy"));

export { GetFolderArgs, GetFolderResult, GetFolderOutputArgs } from "./getFolder";
export const getFolder: typeof import("./getFolder").getFolder = null as any;
export const getFolderOutput: typeof import("./getFolder").getFolderOutput = null as any;
utilities.lazyLoad(exports, ["getFolder","getFolderOutput"], () => require("./getFolder"));

export { GetFolderIamPolicyArgs, GetFolderIamPolicyResult, GetFolderIamPolicyOutputArgs } from "./getFolderIamPolicy";
export const getFolderIamPolicy: typeof import("./getFolderIamPolicy").getFolderIamPolicy = null as any;
export const getFolderIamPolicyOutput: typeof import("./getFolderIamPolicy").getFolderIamPolicyOutput = null as any;
utilities.lazyLoad(exports, ["getFolderIamPolicy","getFolderIamPolicyOutput"], () => require("./getFolderIamPolicy"));


// Export enums:
export * from "../../types/enums/cloudresourcemanager/v2beta1";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "google-native:cloudresourcemanager/v2beta1:Folder":
                return new Folder(name, <any>undefined, { urn })
            case "google-native:cloudresourcemanager/v2beta1:FolderIamBinding":
                return new FolderIamBinding(name, <any>undefined, { urn })
            case "google-native:cloudresourcemanager/v2beta1:FolderIamMember":
                return new FolderIamMember(name, <any>undefined, { urn })
            case "google-native:cloudresourcemanager/v2beta1:FolderIamPolicy":
                return new FolderIamPolicy(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("google-native", "cloudresourcemanager/v2beta1", _module)
