// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Gets a tag template.
 */
export function getTagTemplate(args: GetTagTemplateArgs, opts?: pulumi.InvokeOptions): Promise<GetTagTemplateResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:datacatalog/v1beta1:getTagTemplate", {
        "location": args.location,
        "project": args.project,
        "tagTemplateId": args.tagTemplateId,
    }, opts);
}

export interface GetTagTemplateArgs {
    location: string;
    project?: string;
    tagTemplateId: string;
}

export interface GetTagTemplateResult {
    /**
     * The display name for this template. Defaults to an empty string.
     */
    readonly displayName: string;
    /**
     * Map of tag template field IDs to the settings for the field. This map is an exhaustive list of the allowed fields. This map must contain at least one field and at most 500 fields. The keys to this map are tag template field IDs. Field IDs can contain letters (both uppercase and lowercase), numbers (0-9) and underscores (_). Field IDs must be at least 1 character long and at most 64 characters long. Field IDs must start with a letter or underscore.
     */
    readonly fields: {[key: string]: outputs.datacatalog.v1beta1.GoogleCloudDatacatalogV1beta1TagTemplateFieldResponse};
    /**
     * The resource name of the tag template in URL format. Example: * projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id} Note that this TagTemplate and its child resources may not actually be stored in the location in this name.
     */
    readonly name: string;
}
/**
 * Gets a tag template.
 */
export function getTagTemplateOutput(args: GetTagTemplateOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetTagTemplateResult> {
    return pulumi.output(args).apply((a: any) => getTagTemplate(a, opts))
}

export interface GetTagTemplateOutputArgs {
    location: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    tagTemplateId: pulumi.Input<string>;
}
