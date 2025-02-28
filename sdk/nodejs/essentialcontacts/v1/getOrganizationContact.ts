// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Gets a single contact.
 */
export function getOrganizationContact(args: GetOrganizationContactArgs, opts?: pulumi.InvokeOptions): Promise<GetOrganizationContactResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:essentialcontacts/v1:getOrganizationContact", {
        "contactId": args.contactId,
        "organizationId": args.organizationId,
    }, opts);
}

export interface GetOrganizationContactArgs {
    contactId: string;
    organizationId: string;
}

export interface GetOrganizationContactResult {
    /**
     * The email address to send notifications to. The email address does not need to be a Google Account.
     */
    readonly email: string;
    /**
     * The preferred language for notifications, as a ISO 639-1 language code. See [Supported languages](https://cloud.google.com/resource-manager/docs/managing-notification-contacts#supported-languages) for a list of supported languages.
     */
    readonly languageTag: string;
    /**
     * The identifier for the contact. Format: {resource_type}/{resource_id}/contacts/{contact_id}
     */
    readonly name: string;
    /**
     * The categories of notifications that the contact will receive communications for.
     */
    readonly notificationCategorySubscriptions: string[];
    /**
     * The last time the validation_state was updated, either manually or automatically. A contact is considered stale if its validation state was updated more than 1 year ago.
     */
    readonly validateTime: string;
    /**
     * The validity of the contact. A contact is considered valid if it is the correct recipient for notifications for a particular resource.
     */
    readonly validationState: string;
}
/**
 * Gets a single contact.
 */
export function getOrganizationContactOutput(args: GetOrganizationContactOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetOrganizationContactResult> {
    return pulumi.output(args).apply((a: any) => getOrganizationContact(a, opts))
}

export interface GetOrganizationContactOutputArgs {
    contactId: pulumi.Input<string>;
    organizationId: pulumi.Input<string>;
}
