// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Gets a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more.
 */
export function getOrganizationJobTrigger(args: GetOrganizationJobTriggerArgs, opts?: pulumi.InvokeOptions): Promise<GetOrganizationJobTriggerResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("google-native:dlp/v2:getOrganizationJobTrigger", {
        "jobTriggerId": args.jobTriggerId,
        "location": args.location,
        "organizationId": args.organizationId,
    }, opts);
}

export interface GetOrganizationJobTriggerArgs {
    jobTriggerId: string;
    location: string;
    organizationId: string;
}

export interface GetOrganizationJobTriggerResult {
    /**
     * The creation timestamp of a triggeredJob.
     */
    readonly createTime: string;
    /**
     * User provided description (max 256 chars)
     */
    readonly description: string;
    /**
     * Display name (max 100 chars)
     */
    readonly displayName: string;
    /**
     * A stream of errors encountered when the trigger was activated. Repeated errors may result in the JobTrigger automatically being paused. Will return the last 100 errors. Whenever the JobTrigger is modified this list will be cleared.
     */
    readonly errors: outputs.dlp.v2.GooglePrivacyDlpV2ErrorResponse[];
    /**
     * For inspect jobs, a snapshot of the configuration.
     */
    readonly inspectJob: outputs.dlp.v2.GooglePrivacyDlpV2InspectJobConfigResponse;
    /**
     * The timestamp of the last time this trigger executed.
     */
    readonly lastRunTime: string;
    /**
     * Unique resource name for the triggeredJob, assigned by the service when the triggeredJob is created, for example `projects/dlp-test-project/jobTriggers/53234423`.
     */
    readonly name: string;
    /**
     * A status for this trigger.
     */
    readonly status: string;
    /**
     * A list of triggers which will be OR'ed together. Only one in the list needs to trigger for a job to be started. The list may contain only a single Schedule trigger and must have at least one object.
     */
    readonly triggers: outputs.dlp.v2.GooglePrivacyDlpV2TriggerResponse[];
    /**
     * The last update timestamp of a triggeredJob.
     */
    readonly updateTime: string;
}
/**
 * Gets a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more.
 */
export function getOrganizationJobTriggerOutput(args: GetOrganizationJobTriggerOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetOrganizationJobTriggerResult> {
    return pulumi.output(args).apply((a: any) => getOrganizationJobTrigger(a, opts))
}

export interface GetOrganizationJobTriggerOutputArgs {
    jobTriggerId: pulumi.Input<string>;
    location: pulumi.Input<string>;
    organizationId: pulumi.Input<string>;
}
