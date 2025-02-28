// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Creates a namespace, and returns the new namespace.
 */
export class Namespace extends pulumi.CustomResource {
    /**
     * Get an existing Namespace resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Namespace {
        return new Namespace(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:servicedirectory/v1beta1:Namespace';

    /**
     * Returns true if the given object is an instance of Namespace.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Namespace {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Namespace.__pulumiType;
    }

    /**
     * The timestamp when the namespace was created.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * Optional. Resource labels associated with this namespace. No more than 64 user labels can be associated with a given resource. Label keys and values can be no longer than 63 characters.
     */
    public readonly labels!: pulumi.Output<{[key: string]: string}>;
    public readonly location!: pulumi.Output<string>;
    /**
     * Immutable. The resource name for the namespace in the format `projects/*&#47;locations/*&#47;namespaces/*`.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Required. The Resource ID must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
     */
    public readonly namespaceId!: pulumi.Output<string>;
    public readonly project!: pulumi.Output<string>;
    /**
     * A globally unique identifier (in UUID4 format) for this namespace.
     */
    public /*out*/ readonly uid!: pulumi.Output<string>;
    /**
     * The timestamp when the namespace was last updated.
     */
    public /*out*/ readonly updateTime!: pulumi.Output<string>;

    /**
     * Create a Namespace resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NamespaceArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.namespaceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'namespaceId'");
            }
            resourceInputs["labels"] = args ? args.labels : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["namespaceId"] = args ? args.namespaceId : undefined;
            resourceInputs["project"] = args ? args.project : undefined;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["uid"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        } else {
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["labels"] = undefined /*out*/;
            resourceInputs["location"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["namespaceId"] = undefined /*out*/;
            resourceInputs["project"] = undefined /*out*/;
            resourceInputs["uid"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["location", "namespaceId", "project"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Namespace.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Namespace resource.
 */
export interface NamespaceArgs {
    /**
     * Optional. Resource labels associated with this namespace. No more than 64 user labels can be associated with a given resource. Label keys and values can be no longer than 63 characters.
     */
    labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    location?: pulumi.Input<string>;
    /**
     * Immutable. The resource name for the namespace in the format `projects/*&#47;locations/*&#47;namespaces/*`.
     */
    name?: pulumi.Input<string>;
    /**
     * Required. The Resource ID must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
     */
    namespaceId: pulumi.Input<string>;
    project?: pulumi.Input<string>;
}
