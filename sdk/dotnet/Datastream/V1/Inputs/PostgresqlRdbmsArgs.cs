// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Datastream.V1.Inputs
{

    /// <summary>
    /// PostgreSQL database structure.
    /// </summary>
    public sealed class PostgresqlRdbmsArgs : global::Pulumi.ResourceArgs
    {
        [Input("postgresqlSchemas")]
        private InputList<Inputs.PostgresqlSchemaArgs>? _postgresqlSchemas;

        /// <summary>
        /// PostgreSQL schemas in the database server.
        /// </summary>
        public InputList<Inputs.PostgresqlSchemaArgs> PostgresqlSchemas
        {
            get => _postgresqlSchemas ?? (_postgresqlSchemas = new InputList<Inputs.PostgresqlSchemaArgs>());
            set => _postgresqlSchemas = value;
        }

        public PostgresqlRdbmsArgs()
        {
        }
        public static new PostgresqlRdbmsArgs Empty => new PostgresqlRdbmsArgs();
    }
}
