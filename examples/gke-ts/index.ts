// Copyright 2016-2021, Pulumi Corporation.

import * as pulumi from "@pulumi/pulumi";
import * as google from "@pulumi/google-native";

const config = new pulumi.Config();
const project = config.get("project") ?? "pulumi-ci-gcp-provider";

const region = "us-central1";

// TODO: Determine this dynamically once https://github.com/pulumi/pulumi-google-native/issues/166 is done.
const engineVersion = "1.19.9-gke.1900";

const nodeConfig: google.types.input.container.v1.NodeConfigArgs = {
    machineType: "n1-standard-2",
    oauthScopes: [
        "https://www.googleapis.com/auth/compute",
        "https://www.googleapis.com/auth/devstorage.read_only",
        "https://www.googleapis.com/auth/logging.write",
        "https://www.googleapis.com/auth/monitoring"
    ],
    preemptible: true,
};

const cluster = new google.container.v1.Cluster("cluster", {
    parent: `projects/${project}/locations/${region}`,
    initialClusterVersion: engineVersion,
    network: `projects/${project}/global/networks/default`,
    nodePools: [{
        config: nodeConfig,
        initialNodeCount: 1,
        management: {
            autoRepair: false,
        },
        name: "initial",
    }],
});
