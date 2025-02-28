// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Compute.Beta.Outputs
{

    [OutputType]
    public sealed class RouterNatRuleResponse
    {
        /// <summary>
        /// The action to be enforced for traffic that matches this rule.
        /// </summary>
        public readonly Outputs.RouterNatRuleActionResponse Action;
        /// <summary>
        /// An optional description of this rule.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// CEL expression that specifies the match condition that egress traffic from a VM is evaluated against. If it evaluates to true, the corresponding `action` is enforced. The following examples are valid match expressions for public NAT: "inIpRange(destination.ip, '1.1.0.0/16') || inIpRange(destination.ip, '2.2.0.0/16')" "destination.ip == '1.1.0.1' || destination.ip == '8.8.8.8'" The following example is a valid match expression for private NAT: "nexthop.hub == '//networkconnectivity.googleapis.com/projects/my-project/locations/global/hubs/hub-1'"
        /// </summary>
        public readonly string Match;
        /// <summary>
        /// An integer uniquely identifying a rule in the list. The rule number must be a positive value between 0 and 65000, and must be unique among rules within a NAT.
        /// </summary>
        public readonly int RuleNumber;

        [OutputConstructor]
        private RouterNatRuleResponse(
            Outputs.RouterNatRuleActionResponse action,

            string description,

            string match,

            int ruleNumber)
        {
            Action = action;
            Description = description;
            Match = match;
            RuleNumber = ruleNumber;
        }
    }
}
