// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Creates a Group.
 * Auto-naming is currently not supported for this resource.
 */
export class Group extends pulumi.CustomResource {
    /**
     * Get an existing Group resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Group {
        return new Group(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:cloudidentity/v1:Group';

    /**
     * Returns true if the given object is an instance of Group.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Group {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Group.__pulumiType;
    }

    /**
     * Additional group keys associated with the Group.
     */
    public /*out*/ readonly additionalGroupKeys!: pulumi.Output<outputs.cloudidentity.v1.EntityKeyResponse[]>;
    /**
     * The time when the `Group` was created.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * An extended description to help users determine the purpose of a `Group`. Must not be longer than 4,096 characters.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * The display name of the `Group`.
     */
    public readonly displayName!: pulumi.Output<string>;
    /**
     * Optional. Dynamic group metadata like queries and status.
     */
    public readonly dynamicGroupMetadata!: pulumi.Output<outputs.cloudidentity.v1.DynamicGroupMetadataResponse>;
    /**
     * The `EntityKey` of the `Group`.
     */
    public readonly groupKey!: pulumi.Output<outputs.cloudidentity.v1.EntityKeyResponse>;
    /**
     * Optional. The initial configuration option for the `Group`.
     */
    public readonly initialGroupConfig!: pulumi.Output<string | undefined>;
    /**
     * One or more label entries that apply to the Group. Currently supported labels contain a key with an empty value. Google Groups are the default type of group and have a label with a key of `cloudidentity.googleapis.com/groups.discussion_forum` and an empty value. Existing Google Groups can have an additional label with a key of `cloudidentity.googleapis.com/groups.security` and an empty value added to them. **This is an immutable change and the security label cannot be removed once added.** Dynamic groups have a label with a key of `cloudidentity.googleapis.com/groups.dynamic`. Identity-mapped groups for Cloud Search have a label with a key of `system/groups/external` and an empty value.
     */
    public readonly labels!: pulumi.Output<{[key: string]: string}>;
    /**
     * The [resource name](https://cloud.google.com/apis/design/resource_names) of the `Group`. Shall be of the form `groups/{group}`.
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * Immutable. The resource name of the entity under which this `Group` resides in the Cloud Identity resource hierarchy. Must be of the form `identitysources/{identity_source}` for external [identity-mapped groups](https://support.google.com/a/answer/9039510) or `customers/{customer_id}` for Google Groups. The `customer_id` must begin with "C" (for example, 'C046psxkn'). [Find your customer ID.] (https://support.google.com/cloudidentity/answer/10070793)
     */
    public readonly parent!: pulumi.Output<string>;
    /**
     * The time when the `Group` was last updated.
     */
    public /*out*/ readonly updateTime!: pulumi.Output<string>;

    /**
     * Create a Group resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GroupArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.groupKey === undefined) && !opts.urn) {
                throw new Error("Missing required property 'groupKey'");
            }
            if ((!args || args.labels === undefined) && !opts.urn) {
                throw new Error("Missing required property 'labels'");
            }
            if ((!args || args.parent === undefined) && !opts.urn) {
                throw new Error("Missing required property 'parent'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["displayName"] = args ? args.displayName : undefined;
            resourceInputs["dynamicGroupMetadata"] = args ? args.dynamicGroupMetadata : undefined;
            resourceInputs["groupKey"] = args ? args.groupKey : undefined;
            resourceInputs["initialGroupConfig"] = args ? args.initialGroupConfig : undefined;
            resourceInputs["labels"] = args ? args.labels : undefined;
            resourceInputs["parent"] = args ? args.parent : undefined;
            resourceInputs["additionalGroupKeys"] = undefined /*out*/;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        } else {
            resourceInputs["additionalGroupKeys"] = undefined /*out*/;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["displayName"] = undefined /*out*/;
            resourceInputs["dynamicGroupMetadata"] = undefined /*out*/;
            resourceInputs["groupKey"] = undefined /*out*/;
            resourceInputs["initialGroupConfig"] = undefined /*out*/;
            resourceInputs["labels"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["parent"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Group.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Group resource.
 */
export interface GroupArgs {
    /**
     * An extended description to help users determine the purpose of a `Group`. Must not be longer than 4,096 characters.
     */
    description?: pulumi.Input<string>;
    /**
     * The display name of the `Group`.
     */
    displayName?: pulumi.Input<string>;
    /**
     * Optional. Dynamic group metadata like queries and status.
     */
    dynamicGroupMetadata?: pulumi.Input<inputs.cloudidentity.v1.DynamicGroupMetadataArgs>;
    /**
     * The `EntityKey` of the `Group`.
     */
    groupKey: pulumi.Input<inputs.cloudidentity.v1.EntityKeyArgs>;
    /**
     * Optional. The initial configuration option for the `Group`.
     */
    initialGroupConfig?: pulumi.Input<string>;
    /**
     * One or more label entries that apply to the Group. Currently supported labels contain a key with an empty value. Google Groups are the default type of group and have a label with a key of `cloudidentity.googleapis.com/groups.discussion_forum` and an empty value. Existing Google Groups can have an additional label with a key of `cloudidentity.googleapis.com/groups.security` and an empty value added to them. **This is an immutable change and the security label cannot be removed once added.** Dynamic groups have a label with a key of `cloudidentity.googleapis.com/groups.dynamic`. Identity-mapped groups for Cloud Search have a label with a key of `system/groups/external` and an empty value.
     */
    labels: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Immutable. The resource name of the entity under which this `Group` resides in the Cloud Identity resource hierarchy. Must be of the form `identitysources/{identity_source}` for external [identity-mapped groups](https://support.google.com/a/answer/9039510) or `customers/{customer_id}` for Google Groups. The `customer_id` must begin with "C" (for example, 'C046psxkn'). [Find your customer ID.] (https://support.google.com/cloudidentity/answer/10070793)
     */
    parent: pulumi.Input<string>;
}
