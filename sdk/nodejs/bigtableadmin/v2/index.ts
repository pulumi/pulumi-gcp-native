// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

// Export members:
export { AppProfileArgs } from "./appProfile";
export type AppProfile = import("./appProfile").AppProfile;
export const AppProfile: typeof import("./appProfile").AppProfile = null as any;
utilities.lazyLoad(exports, ["AppProfile"], () => require("./appProfile"));

export { BackupArgs } from "./backup";
export type Backup = import("./backup").Backup;
export const Backup: typeof import("./backup").Backup = null as any;
utilities.lazyLoad(exports, ["Backup"], () => require("./backup"));

export { ClusterArgs } from "./cluster";
export type Cluster = import("./cluster").Cluster;
export const Cluster: typeof import("./cluster").Cluster = null as any;
utilities.lazyLoad(exports, ["Cluster"], () => require("./cluster"));

export { GetAppProfileArgs, GetAppProfileResult, GetAppProfileOutputArgs } from "./getAppProfile";
export const getAppProfile: typeof import("./getAppProfile").getAppProfile = null as any;
export const getAppProfileOutput: typeof import("./getAppProfile").getAppProfileOutput = null as any;
utilities.lazyLoad(exports, ["getAppProfile","getAppProfileOutput"], () => require("./getAppProfile"));

export { GetBackupArgs, GetBackupResult, GetBackupOutputArgs } from "./getBackup";
export const getBackup: typeof import("./getBackup").getBackup = null as any;
export const getBackupOutput: typeof import("./getBackup").getBackupOutput = null as any;
utilities.lazyLoad(exports, ["getBackup","getBackupOutput"], () => require("./getBackup"));

export { GetClusterArgs, GetClusterResult, GetClusterOutputArgs } from "./getCluster";
export const getCluster: typeof import("./getCluster").getCluster = null as any;
export const getClusterOutput: typeof import("./getCluster").getClusterOutput = null as any;
utilities.lazyLoad(exports, ["getCluster","getClusterOutput"], () => require("./getCluster"));

export { GetInstanceArgs, GetInstanceResult, GetInstanceOutputArgs } from "./getInstance";
export const getInstance: typeof import("./getInstance").getInstance = null as any;
export const getInstanceOutput: typeof import("./getInstance").getInstanceOutput = null as any;
utilities.lazyLoad(exports, ["getInstance","getInstanceOutput"], () => require("./getInstance"));

export { GetInstanceClusterBackupIamPolicyArgs, GetInstanceClusterBackupIamPolicyResult, GetInstanceClusterBackupIamPolicyOutputArgs } from "./getInstanceClusterBackupIamPolicy";
export const getInstanceClusterBackupIamPolicy: typeof import("./getInstanceClusterBackupIamPolicy").getInstanceClusterBackupIamPolicy = null as any;
export const getInstanceClusterBackupIamPolicyOutput: typeof import("./getInstanceClusterBackupIamPolicy").getInstanceClusterBackupIamPolicyOutput = null as any;
utilities.lazyLoad(exports, ["getInstanceClusterBackupIamPolicy","getInstanceClusterBackupIamPolicyOutput"], () => require("./getInstanceClusterBackupIamPolicy"));

export { GetInstanceIamPolicyArgs, GetInstanceIamPolicyResult, GetInstanceIamPolicyOutputArgs } from "./getInstanceIamPolicy";
export const getInstanceIamPolicy: typeof import("./getInstanceIamPolicy").getInstanceIamPolicy = null as any;
export const getInstanceIamPolicyOutput: typeof import("./getInstanceIamPolicy").getInstanceIamPolicyOutput = null as any;
utilities.lazyLoad(exports, ["getInstanceIamPolicy","getInstanceIamPolicyOutput"], () => require("./getInstanceIamPolicy"));

export { GetInstanceTableIamPolicyArgs, GetInstanceTableIamPolicyResult, GetInstanceTableIamPolicyOutputArgs } from "./getInstanceTableIamPolicy";
export const getInstanceTableIamPolicy: typeof import("./getInstanceTableIamPolicy").getInstanceTableIamPolicy = null as any;
export const getInstanceTableIamPolicyOutput: typeof import("./getInstanceTableIamPolicy").getInstanceTableIamPolicyOutput = null as any;
utilities.lazyLoad(exports, ["getInstanceTableIamPolicy","getInstanceTableIamPolicyOutput"], () => require("./getInstanceTableIamPolicy"));

export { GetTableArgs, GetTableResult, GetTableOutputArgs } from "./getTable";
export const getTable: typeof import("./getTable").getTable = null as any;
export const getTableOutput: typeof import("./getTable").getTableOutput = null as any;
utilities.lazyLoad(exports, ["getTable","getTableOutput"], () => require("./getTable"));

export { InstanceArgs } from "./instance";
export type Instance = import("./instance").Instance;
export const Instance: typeof import("./instance").Instance = null as any;
utilities.lazyLoad(exports, ["Instance"], () => require("./instance"));

export { InstanceClusterBackupIamBindingArgs } from "./instanceClusterBackupIamBinding";
export type InstanceClusterBackupIamBinding = import("./instanceClusterBackupIamBinding").InstanceClusterBackupIamBinding;
export const InstanceClusterBackupIamBinding: typeof import("./instanceClusterBackupIamBinding").InstanceClusterBackupIamBinding = null as any;
utilities.lazyLoad(exports, ["InstanceClusterBackupIamBinding"], () => require("./instanceClusterBackupIamBinding"));

export { InstanceClusterBackupIamMemberArgs } from "./instanceClusterBackupIamMember";
export type InstanceClusterBackupIamMember = import("./instanceClusterBackupIamMember").InstanceClusterBackupIamMember;
export const InstanceClusterBackupIamMember: typeof import("./instanceClusterBackupIamMember").InstanceClusterBackupIamMember = null as any;
utilities.lazyLoad(exports, ["InstanceClusterBackupIamMember"], () => require("./instanceClusterBackupIamMember"));

export { InstanceClusterBackupIamPolicyArgs } from "./instanceClusterBackupIamPolicy";
export type InstanceClusterBackupIamPolicy = import("./instanceClusterBackupIamPolicy").InstanceClusterBackupIamPolicy;
export const InstanceClusterBackupIamPolicy: typeof import("./instanceClusterBackupIamPolicy").InstanceClusterBackupIamPolicy = null as any;
utilities.lazyLoad(exports, ["InstanceClusterBackupIamPolicy"], () => require("./instanceClusterBackupIamPolicy"));

export { InstanceIamBindingArgs } from "./instanceIamBinding";
export type InstanceIamBinding = import("./instanceIamBinding").InstanceIamBinding;
export const InstanceIamBinding: typeof import("./instanceIamBinding").InstanceIamBinding = null as any;
utilities.lazyLoad(exports, ["InstanceIamBinding"], () => require("./instanceIamBinding"));

export { InstanceIamMemberArgs } from "./instanceIamMember";
export type InstanceIamMember = import("./instanceIamMember").InstanceIamMember;
export const InstanceIamMember: typeof import("./instanceIamMember").InstanceIamMember = null as any;
utilities.lazyLoad(exports, ["InstanceIamMember"], () => require("./instanceIamMember"));

export { InstanceIamPolicyArgs } from "./instanceIamPolicy";
export type InstanceIamPolicy = import("./instanceIamPolicy").InstanceIamPolicy;
export const InstanceIamPolicy: typeof import("./instanceIamPolicy").InstanceIamPolicy = null as any;
utilities.lazyLoad(exports, ["InstanceIamPolicy"], () => require("./instanceIamPolicy"));

export { InstanceTableIamBindingArgs } from "./instanceTableIamBinding";
export type InstanceTableIamBinding = import("./instanceTableIamBinding").InstanceTableIamBinding;
export const InstanceTableIamBinding: typeof import("./instanceTableIamBinding").InstanceTableIamBinding = null as any;
utilities.lazyLoad(exports, ["InstanceTableIamBinding"], () => require("./instanceTableIamBinding"));

export { InstanceTableIamMemberArgs } from "./instanceTableIamMember";
export type InstanceTableIamMember = import("./instanceTableIamMember").InstanceTableIamMember;
export const InstanceTableIamMember: typeof import("./instanceTableIamMember").InstanceTableIamMember = null as any;
utilities.lazyLoad(exports, ["InstanceTableIamMember"], () => require("./instanceTableIamMember"));

export { InstanceTableIamPolicyArgs } from "./instanceTableIamPolicy";
export type InstanceTableIamPolicy = import("./instanceTableIamPolicy").InstanceTableIamPolicy;
export const InstanceTableIamPolicy: typeof import("./instanceTableIamPolicy").InstanceTableIamPolicy = null as any;
utilities.lazyLoad(exports, ["InstanceTableIamPolicy"], () => require("./instanceTableIamPolicy"));

export { TableArgs } from "./table";
export type Table = import("./table").Table;
export const Table: typeof import("./table").Table = null as any;
utilities.lazyLoad(exports, ["Table"], () => require("./table"));


// Export enums:
export * from "../../types/enums/bigtableadmin/v2";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "google-native:bigtableadmin/v2:AppProfile":
                return new AppProfile(name, <any>undefined, { urn })
            case "google-native:bigtableadmin/v2:Backup":
                return new Backup(name, <any>undefined, { urn })
            case "google-native:bigtableadmin/v2:Cluster":
                return new Cluster(name, <any>undefined, { urn })
            case "google-native:bigtableadmin/v2:Instance":
                return new Instance(name, <any>undefined, { urn })
            case "google-native:bigtableadmin/v2:InstanceClusterBackupIamBinding":
                return new InstanceClusterBackupIamBinding(name, <any>undefined, { urn })
            case "google-native:bigtableadmin/v2:InstanceClusterBackupIamMember":
                return new InstanceClusterBackupIamMember(name, <any>undefined, { urn })
            case "google-native:bigtableadmin/v2:InstanceClusterBackupIamPolicy":
                return new InstanceClusterBackupIamPolicy(name, <any>undefined, { urn })
            case "google-native:bigtableadmin/v2:InstanceIamBinding":
                return new InstanceIamBinding(name, <any>undefined, { urn })
            case "google-native:bigtableadmin/v2:InstanceIamMember":
                return new InstanceIamMember(name, <any>undefined, { urn })
            case "google-native:bigtableadmin/v2:InstanceIamPolicy":
                return new InstanceIamPolicy(name, <any>undefined, { urn })
            case "google-native:bigtableadmin/v2:InstanceTableIamBinding":
                return new InstanceTableIamBinding(name, <any>undefined, { urn })
            case "google-native:bigtableadmin/v2:InstanceTableIamMember":
                return new InstanceTableIamMember(name, <any>undefined, { urn })
            case "google-native:bigtableadmin/v2:InstanceTableIamPolicy":
                return new InstanceTableIamPolicy(name, <any>undefined, { urn })
            case "google-native:bigtableadmin/v2:Table":
                return new Table(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("google-native", "bigtableadmin/v2", _module)
