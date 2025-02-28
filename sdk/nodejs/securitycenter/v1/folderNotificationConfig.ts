// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Creates a notification config.
 * Auto-naming is currently not supported for this resource.
 */
export class FolderNotificationConfig extends pulumi.CustomResource {
    /**
     * Get an existing FolderNotificationConfig resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): FolderNotificationConfig {
        return new FolderNotificationConfig(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:securitycenter/v1:FolderNotificationConfig';

    /**
     * Returns true if the given object is an instance of FolderNotificationConfig.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is FolderNotificationConfig {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === FolderNotificationConfig.__pulumiType;
    }

    /**
     * Required. Unique identifier provided by the client within the parent scope. It must be between 1 and 128 characters and contain alphanumeric characters, underscores, or hyphens only.
     */
    public readonly configId!: pulumi.Output<string>;
    /**
     * The description of the notification config (max of 1024 characters).
     */
    public readonly description!: pulumi.Output<string>;
    public readonly folderId!: pulumi.Output<string>;
    /**
     * The relative resource name of this notification config. See: https://cloud.google.com/apis/design/resource_names#relative_resource_name Example: "organizations/{organization_id}/notificationConfigs/notify_public_bucket", "folders/{folder_id}/notificationConfigs/notify_public_bucket", or "projects/{project_id}/notificationConfigs/notify_public_bucket".
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The Pub/Sub topic to send notifications to. Its format is "projects/[project_id]/topics/[topic]".
     */
    public readonly pubsubTopic!: pulumi.Output<string>;
    /**
     * The service account that needs "pubsub.topics.publish" permission to publish to the Pub/Sub topic.
     */
    public /*out*/ readonly serviceAccount!: pulumi.Output<string>;
    /**
     * The config for triggering streaming-based notifications.
     */
    public readonly streamingConfig!: pulumi.Output<outputs.securitycenter.v1.StreamingConfigResponse>;

    /**
     * Create a FolderNotificationConfig resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FolderNotificationConfigArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.configId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'configId'");
            }
            if ((!args || args.folderId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'folderId'");
            }
            resourceInputs["configId"] = args ? args.configId : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["folderId"] = args ? args.folderId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["pubsubTopic"] = args ? args.pubsubTopic : undefined;
            resourceInputs["streamingConfig"] = args ? args.streamingConfig : undefined;
            resourceInputs["serviceAccount"] = undefined /*out*/;
        } else {
            resourceInputs["configId"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["folderId"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["pubsubTopic"] = undefined /*out*/;
            resourceInputs["serviceAccount"] = undefined /*out*/;
            resourceInputs["streamingConfig"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["configId", "folderId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(FolderNotificationConfig.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a FolderNotificationConfig resource.
 */
export interface FolderNotificationConfigArgs {
    /**
     * Required. Unique identifier provided by the client within the parent scope. It must be between 1 and 128 characters and contain alphanumeric characters, underscores, or hyphens only.
     */
    configId: pulumi.Input<string>;
    /**
     * The description of the notification config (max of 1024 characters).
     */
    description?: pulumi.Input<string>;
    folderId: pulumi.Input<string>;
    /**
     * The relative resource name of this notification config. See: https://cloud.google.com/apis/design/resource_names#relative_resource_name Example: "organizations/{organization_id}/notificationConfigs/notify_public_bucket", "folders/{folder_id}/notificationConfigs/notify_public_bucket", or "projects/{project_id}/notificationConfigs/notify_public_bucket".
     */
    name?: pulumi.Input<string>;
    /**
     * The Pub/Sub topic to send notifications to. Its format is "projects/[project_id]/topics/[topic]".
     */
    pubsubTopic?: pulumi.Input<string>;
    /**
     * The config for triggering streaming-based notifications.
     */
    streamingConfig?: pulumi.Input<inputs.securitycenter.v1.StreamingConfigArgs>;
}
