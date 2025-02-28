// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Creates a new CertificateMapEntry in a given project and location.
 */
export class CertificateMapEntry extends pulumi.CustomResource {
    /**
     * Get an existing CertificateMapEntry resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): CertificateMapEntry {
        return new CertificateMapEntry(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'google-native:certificatemanager/v1:CertificateMapEntry';

    /**
     * Returns true if the given object is an instance of CertificateMapEntry.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CertificateMapEntry {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CertificateMapEntry.__pulumiType;
    }

    /**
     * Required. A user-provided name of the certificate map entry.
     */
    public readonly certificateMapEntryId!: pulumi.Output<string>;
    public readonly certificateMapId!: pulumi.Output<string>;
    /**
     * A set of Certificates defines for the given `hostname`. There can be defined up to four certificates in each Certificate Map Entry. Each certificate must match pattern `projects/*&#47;locations/*&#47;certificates/*`.
     */
    public readonly certificates!: pulumi.Output<string[]>;
    /**
     * The creation timestamp of a Certificate Map Entry.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * One or more paragraphs of text description of a certificate map entry.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * A Hostname (FQDN, e.g. `example.com`) or a wildcard hostname expression (`*.example.com`) for a set of hostnames with common suffix. Used as Server Name Indication (SNI) for selecting a proper certificate.
     */
    public readonly hostname!: pulumi.Output<string>;
    /**
     * Set of labels associated with a Certificate Map Entry.
     */
    public readonly labels!: pulumi.Output<{[key: string]: string}>;
    public readonly location!: pulumi.Output<string>;
    /**
     * A predefined matcher for particular cases, other than SNI selection.
     */
    public readonly matcher!: pulumi.Output<string>;
    /**
     * A user-defined name of the Certificate Map Entry. Certificate Map Entry names must be unique globally and match pattern `projects/*&#47;locations/*&#47;certificateMaps/*&#47;certificateMapEntries/*`.
     */
    public readonly name!: pulumi.Output<string>;
    public readonly project!: pulumi.Output<string>;
    /**
     * A serving state of this Certificate Map Entry.
     */
    public /*out*/ readonly state!: pulumi.Output<string>;
    /**
     * The update timestamp of a Certificate Map Entry.
     */
    public /*out*/ readonly updateTime!: pulumi.Output<string>;

    /**
     * Create a CertificateMapEntry resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CertificateMapEntryArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.certificateMapEntryId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'certificateMapEntryId'");
            }
            if ((!args || args.certificateMapId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'certificateMapId'");
            }
            resourceInputs["certificateMapEntryId"] = args ? args.certificateMapEntryId : undefined;
            resourceInputs["certificateMapId"] = args ? args.certificateMapId : undefined;
            resourceInputs["certificates"] = args ? args.certificates : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["hostname"] = args ? args.hostname : undefined;
            resourceInputs["labels"] = args ? args.labels : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["matcher"] = args ? args.matcher : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["project"] = args ? args.project : undefined;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        } else {
            resourceInputs["certificateMapEntryId"] = undefined /*out*/;
            resourceInputs["certificateMapId"] = undefined /*out*/;
            resourceInputs["certificates"] = undefined /*out*/;
            resourceInputs["createTime"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["hostname"] = undefined /*out*/;
            resourceInputs["labels"] = undefined /*out*/;
            resourceInputs["location"] = undefined /*out*/;
            resourceInputs["matcher"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["project"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["certificateMapEntryId", "certificateMapId", "location", "project"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(CertificateMapEntry.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a CertificateMapEntry resource.
 */
export interface CertificateMapEntryArgs {
    /**
     * Required. A user-provided name of the certificate map entry.
     */
    certificateMapEntryId: pulumi.Input<string>;
    certificateMapId: pulumi.Input<string>;
    /**
     * A set of Certificates defines for the given `hostname`. There can be defined up to four certificates in each Certificate Map Entry. Each certificate must match pattern `projects/*&#47;locations/*&#47;certificates/*`.
     */
    certificates?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * One or more paragraphs of text description of a certificate map entry.
     */
    description?: pulumi.Input<string>;
    /**
     * A Hostname (FQDN, e.g. `example.com`) or a wildcard hostname expression (`*.example.com`) for a set of hostnames with common suffix. Used as Server Name Indication (SNI) for selecting a proper certificate.
     */
    hostname?: pulumi.Input<string>;
    /**
     * Set of labels associated with a Certificate Map Entry.
     */
    labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    location?: pulumi.Input<string>;
    /**
     * A predefined matcher for particular cases, other than SNI selection.
     */
    matcher?: pulumi.Input<enums.certificatemanager.v1.CertificateMapEntryMatcher>;
    /**
     * A user-defined name of the Certificate Map Entry. Certificate Map Entry names must be unique globally and match pattern `projects/*&#47;locations/*&#47;certificateMaps/*&#47;certificateMapEntries/*`.
     */
    name?: pulumi.Input<string>;
    project?: pulumi.Input<string>;
}
