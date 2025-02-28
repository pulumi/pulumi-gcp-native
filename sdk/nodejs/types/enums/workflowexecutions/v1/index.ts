// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const ExecutionCallLogLevel = {
    /**
     * No call logging level specified.
     */
    CallLogLevelUnspecified: "CALL_LOG_LEVEL_UNSPECIFIED",
    /**
     * Log all call steps within workflows, all call returns, and all exceptions raised.
     */
    LogAllCalls: "LOG_ALL_CALLS",
    /**
     * Log only exceptions that are raised from call steps within workflows.
     */
    LogErrorsOnly: "LOG_ERRORS_ONLY",
    /**
     * Explicitly log nothing.
     */
    LogNone: "LOG_NONE",
} as const;

/**
 * The call logging level associated to this execution.
 */
export type ExecutionCallLogLevel = (typeof ExecutionCallLogLevel)[keyof typeof ExecutionCallLogLevel];
