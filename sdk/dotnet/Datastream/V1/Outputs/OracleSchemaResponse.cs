// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Datastream.V1.Outputs
{

    /// <summary>
    /// Oracle schema.
    /// </summary>
    [OutputType]
    public sealed class OracleSchemaResponse
    {
        /// <summary>
        /// Tables in the schema.
        /// </summary>
        public readonly ImmutableArray<Outputs.OracleTableResponse> OracleTables;
        /// <summary>
        /// Schema name.
        /// </summary>
        public readonly string Schema;

        [OutputConstructor]
        private OracleSchemaResponse(
            ImmutableArray<Outputs.OracleTableResponse> oracleTables,

            string schema)
        {
            OracleTables = oracleTables;
            Schema = schema;
        }
    }
}
