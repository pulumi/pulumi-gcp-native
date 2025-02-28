// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Creates an authorized orgs desc. The long-running operation from this RPC has a successful status after the authorized orgs desc propagates to long-lasting storage. If a authorized orgs desc contains errors, an error response is returned for the first error encountered. The name of this `AuthorizedOrgsDesc` will be assigned during creation.
 */
export class AuthorizedOrgsDesc extends pulumi.CustomResource {
    /**
     * Get an existing AuthorizedOrgsDesc resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): AuthorizedOrgsDesc {
        return new AuthorizedOrgsDesc(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:accesscontextmanager/v1:AuthorizedOrgsDesc';

    /**
     * Returns true if the given object is an instance of AuthorizedOrgsDesc.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AuthorizedOrgsDesc {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AuthorizedOrgsDesc.__pulumiType;
    }

    public readonly accessPolicyId!: pulumi.Output<string>;
    /**
     * The asset type of this authorized orgs desc. Valid values are `ASSET_TYPE_DEVICE`, and `ASSET_TYPE_CREDENTIAL_STRENGTH`.
     */
    public readonly assetType!: pulumi.Output<string>;
    /**
     * The direction of the authorization relationship between this organization and the organizations listed in the `orgs` field. The valid values for this field include the following: `AUTHORIZATION_DIRECTION_FROM`: Allows this organization to evaluate traffic in the organizations listed in the `orgs` field. `AUTHORIZATION_DIRECTION_TO`: Allows the organizations listed in the `orgs` field to evaluate the traffic in this organization. For the authorization relationship to take effect, all of the organizations must authorize and specify the appropriate relationship direction. For example, if organization A authorized organization B and C to evaluate its traffic, by specifying `AUTHORIZATION_DIRECTION_TO` as the authorization direction, organizations B and C must specify `AUTHORIZATION_DIRECTION_FROM` as the authorization direction in their `AuthorizedOrgsDesc` resource.
     */
    public readonly authorizationDirection!: pulumi.Output<string>;
    /**
     * A granular control type for authorization levels. Valid value is `AUTHORIZATION_TYPE_TRUST`.
     */
    public readonly authorizationType!: pulumi.Output<string>;
    /**
     * Resource name for the `AuthorizedOrgsDesc`. Format: `accessPolicies/{access_policy}/authorizedOrgsDescs/{authorized_orgs_desc}`. The `authorized_orgs_desc` component must begin with a letter, followed by alphanumeric characters or `_`. After you create an `AuthorizedOrgsDesc`, you cannot change its `name`.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The list of organization ids in this AuthorizedOrgsDesc. Format: `organizations/` Example: `organizations/123456`
     */
    public readonly orgs!: pulumi.Output<string[]>;

    /**
     * Create a AuthorizedOrgsDesc resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AuthorizedOrgsDescArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.accessPolicyId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'accessPolicyId'");
            }
            resourceInputs["accessPolicyId"] = args ? args.accessPolicyId : undefined;
            resourceInputs["assetType"] = args ? args.assetType : undefined;
            resourceInputs["authorizationDirection"] = args ? args.authorizationDirection : undefined;
            resourceInputs["authorizationType"] = args ? args.authorizationType : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["orgs"] = args ? args.orgs : undefined;
        } else {
            resourceInputs["accessPolicyId"] = undefined /*out*/;
            resourceInputs["assetType"] = undefined /*out*/;
            resourceInputs["authorizationDirection"] = undefined /*out*/;
            resourceInputs["authorizationType"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["orgs"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["accessPolicyId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(AuthorizedOrgsDesc.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a AuthorizedOrgsDesc resource.
 */
export interface AuthorizedOrgsDescArgs {
    accessPolicyId: pulumi.Input<string>;
    /**
     * The asset type of this authorized orgs desc. Valid values are `ASSET_TYPE_DEVICE`, and `ASSET_TYPE_CREDENTIAL_STRENGTH`.
     */
    assetType?: pulumi.Input<enums.accesscontextmanager.v1.AuthorizedOrgsDescAssetType>;
    /**
     * The direction of the authorization relationship between this organization and the organizations listed in the `orgs` field. The valid values for this field include the following: `AUTHORIZATION_DIRECTION_FROM`: Allows this organization to evaluate traffic in the organizations listed in the `orgs` field. `AUTHORIZATION_DIRECTION_TO`: Allows the organizations listed in the `orgs` field to evaluate the traffic in this organization. For the authorization relationship to take effect, all of the organizations must authorize and specify the appropriate relationship direction. For example, if organization A authorized organization B and C to evaluate its traffic, by specifying `AUTHORIZATION_DIRECTION_TO` as the authorization direction, organizations B and C must specify `AUTHORIZATION_DIRECTION_FROM` as the authorization direction in their `AuthorizedOrgsDesc` resource.
     */
    authorizationDirection?: pulumi.Input<enums.accesscontextmanager.v1.AuthorizedOrgsDescAuthorizationDirection>;
    /**
     * A granular control type for authorization levels. Valid value is `AUTHORIZATION_TYPE_TRUST`.
     */
    authorizationType?: pulumi.Input<enums.accesscontextmanager.v1.AuthorizedOrgsDescAuthorizationType>;
    /**
     * Resource name for the `AuthorizedOrgsDesc`. Format: `accessPolicies/{access_policy}/authorizedOrgsDescs/{authorized_orgs_desc}`. The `authorized_orgs_desc` component must begin with a letter, followed by alphanumeric characters or `_`. After you create an `AuthorizedOrgsDesc`, you cannot change its `name`.
     */
    name?: pulumi.Input<string>;
    /**
     * The list of organization ids in this AuthorizedOrgsDesc. Format: `organizations/` Example: `organizations/123456`
     */
    orgs?: pulumi.Input<pulumi.Input<string>[]>;
}
