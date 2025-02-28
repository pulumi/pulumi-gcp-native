// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Creates a new TagKey. If another request with the same parameters is sent while the original request is in process, the second request will receive an error. A maximum of 1000 TagKeys can exist under a parent at any given time.
 */
export class TagKey extends pulumi.CustomResource {
    /**
     * Get an existing TagKey resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): TagKey {
        return new TagKey(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:cloudresourcemanager/v3:TagKey';

    /**
     * Returns true if the given object is an instance of TagKey.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TagKey {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TagKey.__pulumiType;
    }

    /**
     * Creation time.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * Optional. User-assigned description of the TagKey. Must not exceed 256 characters. Read-write.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * Optional. Entity tag which users can pass to prevent race conditions. This field is always set in server responses. See UpdateTagKeyRequest for details.
     */
    public readonly etag!: pulumi.Output<string>;
    /**
     * Immutable. The resource name for a TagKey. Must be in the format `tagKeys/{tag_key_id}`, where `tag_key_id` is the generated numeric id for the TagKey.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Immutable. Namespaced name of the TagKey.
     */
    public /*out*/ readonly namespacedName!: pulumi.Output<string>;
    /**
     * Immutable. The resource name of the TagKey's parent. A TagKey can be parented by an Organization or a Project. For a TagKey parented by an Organization, its parent must be in the form `organizations/{org_id}`. For a TagKey parented by a Project, its parent can be in the form `projects/{project_id}` or `projects/{project_number}`.
     */
    public readonly parent!: pulumi.Output<string>;
    /**
     * Optional. A purpose denotes that this Tag is intended for use in policies of a specific policy engine, and will involve that policy engine in management operations involving this Tag. A purpose does not grant a policy engine exclusive rights to the Tag, and it may be referenced by other policy engines. A purpose cannot be changed once set.
     */
    public readonly purpose!: pulumi.Output<string>;
    /**
     * Optional. Purpose data corresponds to the policy system that the tag is intended for. See documentation for `Purpose` for formatting of this field. Purpose data cannot be changed once set.
     */
    public readonly purposeData!: pulumi.Output<{[key: string]: string}>;
    /**
     * Immutable. The user friendly name for a TagKey. The short name should be unique for TagKeys within the same tag namespace. The short name must be 1-63 characters, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.
     */
    public readonly shortName!: pulumi.Output<string>;
    /**
     * Update time.
     */
    public /*out*/ readonly updateTime!: pulumi.Output<string>;

    /**
     * Create a TagKey resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TagKeyArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.shortName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'shortName'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["etag"] = args ? args.etag : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["parent"] = args ? args.parent : undefined;
            resourceInputs["purpose"] = args ? args.purpose : undefined;
            resourceInputs["purposeData"] = args ? args.purposeData : undefined;
            resourceInputs["shortName"] = args ? args.shortName : undefined;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["namespacedName"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        } else {
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["etag"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["namespacedName"] = undefined /*out*/;
            resourceInputs["parent"] = undefined /*out*/;
            resourceInputs["purpose"] = undefined /*out*/;
            resourceInputs["purposeData"] = undefined /*out*/;
            resourceInputs["shortName"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(TagKey.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a TagKey resource.
 */
export interface TagKeyArgs {
    /**
     * Optional. User-assigned description of the TagKey. Must not exceed 256 characters. Read-write.
     */
    description?: pulumi.Input<string>;
    /**
     * Optional. Entity tag which users can pass to prevent race conditions. This field is always set in server responses. See UpdateTagKeyRequest for details.
     */
    etag?: pulumi.Input<string>;
    /**
     * Immutable. The resource name for a TagKey. Must be in the format `tagKeys/{tag_key_id}`, where `tag_key_id` is the generated numeric id for the TagKey.
     */
    name?: pulumi.Input<string>;
    /**
     * Immutable. The resource name of the TagKey's parent. A TagKey can be parented by an Organization or a Project. For a TagKey parented by an Organization, its parent must be in the form `organizations/{org_id}`. For a TagKey parented by a Project, its parent can be in the form `projects/{project_id}` or `projects/{project_number}`.
     */
    parent?: pulumi.Input<string>;
    /**
     * Optional. A purpose denotes that this Tag is intended for use in policies of a specific policy engine, and will involve that policy engine in management operations involving this Tag. A purpose does not grant a policy engine exclusive rights to the Tag, and it may be referenced by other policy engines. A purpose cannot be changed once set.
     */
    purpose?: pulumi.Input<enums.cloudresourcemanager.v3.TagKeyPurpose>;
    /**
     * Optional. Purpose data corresponds to the policy system that the tag is intended for. See documentation for `Purpose` for formatting of this field. Purpose data cannot be changed once set.
     */
    purposeData?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Immutable. The user friendly name for a TagKey. The short name should be unique for TagKeys within the same tag namespace. The short name must be 1-63 characters, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.
     */
    shortName: pulumi.Input<string>;
}
