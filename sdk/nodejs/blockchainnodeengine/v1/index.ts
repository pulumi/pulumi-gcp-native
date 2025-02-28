// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

// Export members:
export { BlockchainNodeArgs } from "./blockchainNode";
export type BlockchainNode = import("./blockchainNode").BlockchainNode;
export const BlockchainNode: typeof import("./blockchainNode").BlockchainNode = null as any;
utilities.lazyLoad(exports, ["BlockchainNode"], () => require("./blockchainNode"));

export { GetBlockchainNodeArgs, GetBlockchainNodeResult, GetBlockchainNodeOutputArgs } from "./getBlockchainNode";
export const getBlockchainNode: typeof import("./getBlockchainNode").getBlockchainNode = null as any;
export const getBlockchainNodeOutput: typeof import("./getBlockchainNode").getBlockchainNodeOutput = null as any;
utilities.lazyLoad(exports, ["getBlockchainNode","getBlockchainNodeOutput"], () => require("./getBlockchainNode"));


// Export enums:
export * from "../../types/enums/blockchainnodeengine/v1";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "google-native:blockchainnodeengine/v1:BlockchainNode":
                return new BlockchainNode(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("google-native", "blockchainnodeengine/v1", _module)
