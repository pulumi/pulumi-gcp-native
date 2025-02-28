// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.BigQuery.V2.Inputs
{

    public sealed class QueryParameterValueArgs : global::Pulumi.ResourceArgs
    {
        [Input("arrayValues")]
        private InputList<Inputs.QueryParameterValueArgs>? _arrayValues;

        /// <summary>
        /// [Optional] The array values, if this is an array type.
        /// </summary>
        public InputList<Inputs.QueryParameterValueArgs> ArrayValues
        {
            get => _arrayValues ?? (_arrayValues = new InputList<Inputs.QueryParameterValueArgs>());
            set => _arrayValues = value;
        }

        [Input("structValues")]
        private InputMap<Inputs.QueryParameterValueArgs>? _structValues;

        /// <summary>
        /// [Optional] The struct field values, in order of the struct type's declaration.
        /// </summary>
        public InputMap<Inputs.QueryParameterValueArgs> StructValues
        {
            get => _structValues ?? (_structValues = new InputMap<Inputs.QueryParameterValueArgs>());
            set => _structValues = value;
        }

        /// <summary>
        /// [Optional] The value of this value, if a simple scalar type.
        /// </summary>
        [Input("value")]
        public Input<string>? Value { get; set; }

        public QueryParameterValueArgs()
        {
        }
        public static new QueryParameterValueArgs Empty => new QueryParameterValueArgs();
    }
}
