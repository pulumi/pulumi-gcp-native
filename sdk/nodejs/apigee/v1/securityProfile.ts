// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * CreateSecurityProfile create a new custom security profile.
 */
export class SecurityProfile extends pulumi.CustomResource {
    /**
     * Get an existing SecurityProfile resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): SecurityProfile {
        return new SecurityProfile(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:apigee/v1:SecurityProfile';

    /**
     * Returns true if the given object is an instance of SecurityProfile.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SecurityProfile {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SecurityProfile.__pulumiType;
    }

    /**
     * Description of the security profile.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * DEPRECATED: DO NOT USE Display name of the security profile.
     *
     * @deprecated DEPRECATED: DO NOT USE Display name of the security profile.
     */
    public readonly displayName!: pulumi.Output<string>;
    /**
     * List of environments attached to security profile.
     */
    public readonly environments!: pulumi.Output<outputs.apigee.v1.GoogleCloudApigeeV1SecurityProfileEnvironmentResponse[]>;
    /**
     * Maximum security score that can be generated by this profile.
     */
    public /*out*/ readonly maxScore!: pulumi.Output<number>;
    /**
     * Minimum security score that can be generated by this profile.
     */
    public /*out*/ readonly minScore!: pulumi.Output<number>;
    /**
     * Immutable. Name of the security profile resource. Format: organizations/{org}/securityProfiles/{profile}
     */
    public readonly name!: pulumi.Output<string>;
    public readonly organizationId!: pulumi.Output<string>;
    /**
     * Customized profile configuration that computes the security score.
     */
    public readonly profileConfig!: pulumi.Output<outputs.apigee.v1.GoogleCloudApigeeV1ProfileConfigResponse>;
    /**
     * The time when revision was created.
     */
    public /*out*/ readonly revisionCreateTime!: pulumi.Output<string>;
    /**
     * Revision ID of the security profile.
     */
    public /*out*/ readonly revisionId!: pulumi.Output<string>;
    /**
     * DEPRECATED: DO NOT USE The time when revision was published. Once published, the security profile revision cannot be updated further and can be attached to environments.
     *
     * @deprecated Output only. DEPRECATED: DO NOT USE The time when revision was published. Once published, the security profile revision cannot be updated further and can be attached to environments.
     */
    public /*out*/ readonly revisionPublishTime!: pulumi.Output<string>;
    /**
     * The time when revision was updated.
     */
    public /*out*/ readonly revisionUpdateTime!: pulumi.Output<string>;
    /**
     * List of profile scoring configs in this revision.
     */
    public readonly scoringConfigs!: pulumi.Output<outputs.apigee.v1.GoogleCloudApigeeV1SecurityProfileScoringConfigResponse[]>;
    /**
     * Required. The ID to use for the SecurityProfile, which will become the final component of the action's resource name. This value should be 1-63 characters and validated by "(^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$)".
     */
    public readonly securityProfileId!: pulumi.Output<string>;

    /**
     * Create a SecurityProfile resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SecurityProfileArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.organizationId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'organizationId'");
            }
            if ((!args || args.profileConfig === undefined) && !opts.urn) {
                throw new Error("Missing required property 'profileConfig'");
            }
            if ((!args || args.securityProfileId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'securityProfileId'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["displayName"] = args ? args.displayName : undefined;
            resourceInputs["environments"] = args ? args.environments : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["organizationId"] = args ? args.organizationId : undefined;
            resourceInputs["profileConfig"] = args ? args.profileConfig : undefined;
            resourceInputs["scoringConfigs"] = args ? args.scoringConfigs : undefined;
            resourceInputs["securityProfileId"] = args ? args.securityProfileId : undefined;
            resourceInputs["maxScore"] = undefined /*out*/;
            resourceInputs["minScore"] = undefined /*out*/;
            resourceInputs["revisionCreateTime"] = undefined /*out*/;
            resourceInputs["revisionId"] = undefined /*out*/;
            resourceInputs["revisionPublishTime"] = undefined /*out*/;
            resourceInputs["revisionUpdateTime"] = undefined /*out*/;
        } else {
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["displayName"] = undefined /*out*/;
            resourceInputs["environments"] = undefined /*out*/;
            resourceInputs["maxScore"] = undefined /*out*/;
            resourceInputs["minScore"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["organizationId"] = undefined /*out*/;
            resourceInputs["profileConfig"] = undefined /*out*/;
            resourceInputs["revisionCreateTime"] = undefined /*out*/;
            resourceInputs["revisionId"] = undefined /*out*/;
            resourceInputs["revisionPublishTime"] = undefined /*out*/;
            resourceInputs["revisionUpdateTime"] = undefined /*out*/;
            resourceInputs["scoringConfigs"] = undefined /*out*/;
            resourceInputs["securityProfileId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["organizationId", "securityProfileId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(SecurityProfile.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a SecurityProfile resource.
 */
export interface SecurityProfileArgs {
    /**
     * Description of the security profile.
     */
    description?: pulumi.Input<string>;
    /**
     * DEPRECATED: DO NOT USE Display name of the security profile.
     *
     * @deprecated DEPRECATED: DO NOT USE Display name of the security profile.
     */
    displayName?: pulumi.Input<string>;
    /**
     * List of environments attached to security profile.
     */
    environments?: pulumi.Input<pulumi.Input<inputs.apigee.v1.GoogleCloudApigeeV1SecurityProfileEnvironmentArgs>[]>;
    /**
     * Immutable. Name of the security profile resource. Format: organizations/{org}/securityProfiles/{profile}
     */
    name?: pulumi.Input<string>;
    organizationId: pulumi.Input<string>;
    /**
     * Customized profile configuration that computes the security score.
     */
    profileConfig: pulumi.Input<inputs.apigee.v1.GoogleCloudApigeeV1ProfileConfigArgs>;
    /**
     * List of profile scoring configs in this revision.
     */
    scoringConfigs?: pulumi.Input<pulumi.Input<inputs.apigee.v1.GoogleCloudApigeeV1SecurityProfileScoringConfigArgs>[]>;
    /**
     * Required. The ID to use for the SecurityProfile, which will become the final component of the action's resource name. This value should be 1-63 characters and validated by "(^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$)".
     */
    securityProfileId: pulumi.Input<string>;
}
