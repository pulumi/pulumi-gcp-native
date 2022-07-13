// Copyright 2016-2021, Pulumi Corporation.  All rights reserved.

import * as google from "@pulumi/google-native";

const computeNetwork = new google.compute.v1.Network("network", {
    autoCreateSubnetworks: true,
});

const computeFirewall = new google.compute.v1.Firewall("firewall", {
    network: computeNetwork.selfLink,
    allowed: [{
        ipProtocol: "tcp",
        ports: ["22", "80"],
    }],
});

// (optional) create a simple web server using the startup script for the instance
const startupScript = `#!/bin/bash
echo "Hello, World!" > index.html
nohup python -m SimpleHTTPServer 80 &`;

const computeInstance = new google.compute.v1.Instance("instance", {
    machineType: "f1-micro",
    metadata: {
        items: [{
            "key": "startup-script",
            "value": startupScript,
        }],
    },
    disks: [
        {
            boot: true,
            initializeParams: {
                sourceImage: "projects/debian-cloud/global/images/debian-9-stretch-v20181210",
            },
        },
    ],
    networkInterfaces: [{
        network: computeNetwork.id,
        accessConfigs: [{}], // must be empty to request an ephemeral IP
    }],
    serviceAccounts: [{
        scopes: ["https://www.googleapis.com/auth/cloud-platform"],
    }],
    tags: { items: ["test"] }, // <--- this is the change compared to step 1
}, { dependsOn: [computeFirewall] });

export const instanceLink = computeInstance.selfLink;
export const instanceIP = computeInstance.networkInterfaces[0].accessConfigs[0].natIP;
export const tag = computeInstance.tags.items[0];
