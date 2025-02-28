# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['QueryArgs', 'Query']

@pulumi.input_type
class QueryArgs:
    def __init__(__self__, *,
                 environment_id: pulumi.Input[str],
                 organization_id: pulumi.Input[str],
                 time_range: Any,
                 csv_delimiter: Optional[pulumi.Input[str]] = None,
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 envgroup_hostname: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 group_by_time_unit: Optional[pulumi.Input[str]] = None,
                 limit: Optional[pulumi.Input[int]] = None,
                 metrics: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1QueryMetricArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 output_format: Optional[pulumi.Input[str]] = None,
                 report_definition_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Query resource.
        :param Any time_range: Time range for the query. Can use the following predefined strings to specify the time range: `last60minutes` `last24hours` `last7days` Or, specify the timeRange as a structure describing start and end timestamps in the ISO format: yyyy-mm-ddThh:mm:ssZ. Example: "timeRange": { "start": "2018-07-29T00:13:00Z", "end": "2018-08-01T00:18:00Z" }
        :param pulumi.Input[str] csv_delimiter: Delimiter used in the CSV file, if `outputFormat` is set to `csv`. Defaults to the `,` (comma) character. Supported delimiter characters include comma (`,`), pipe (`|`), and tab (`\\t`).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dimensions: A list of dimensions. https://docs.apigee.com/api-platform/analytics/analytics-reference#dimensions
        :param pulumi.Input[str] envgroup_hostname: Hostname needs to be specified if query intends to run at host level. This field is only allowed when query is submitted by CreateHostAsyncQuery where analytics data will be grouped by organization and hostname.
        :param pulumi.Input[str] filter: Boolean expression that can be used to filter data. Filter expressions can be combined using AND/OR terms and should be fully parenthesized to avoid ambiguity. See Analytics metrics, dimensions, and filters reference https://docs.apigee.com/api-platform/analytics/analytics-reference for more information on the fields available to filter on. For more information on the tokens that you use to build filter expressions, see Filter expression syntax. https://docs.apigee.com/api-platform/analytics/asynch-reports-api#filter-expression-syntax
        :param pulumi.Input[str] group_by_time_unit: Time unit used to group the result set. Valid values include: second, minute, hour, day, week, or month. If a query includes groupByTimeUnit, then the result is an aggregation based on the specified time unit and the resultant timestamp does not include milliseconds precision. If a query omits groupByTimeUnit, then the resultant timestamp includes milliseconds precision.
        :param pulumi.Input[int] limit: Maximum number of rows that can be returned in the result.
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1QueryMetricArgs']]] metrics: A list of Metrics.
        :param pulumi.Input[str] name: Asynchronous Query Name.
        :param pulumi.Input[str] output_format: Valid values include: `csv` or `json`. Defaults to `json`. Note: Configure the delimiter for CSV output using the csvDelimiter property.
        :param pulumi.Input[str] report_definition_id: Asynchronous Report ID.
        """
        pulumi.set(__self__, "environment_id", environment_id)
        pulumi.set(__self__, "organization_id", organization_id)
        pulumi.set(__self__, "time_range", time_range)
        if csv_delimiter is not None:
            pulumi.set(__self__, "csv_delimiter", csv_delimiter)
        if dimensions is not None:
            pulumi.set(__self__, "dimensions", dimensions)
        if envgroup_hostname is not None:
            pulumi.set(__self__, "envgroup_hostname", envgroup_hostname)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if group_by_time_unit is not None:
            pulumi.set(__self__, "group_by_time_unit", group_by_time_unit)
        if limit is not None:
            pulumi.set(__self__, "limit", limit)
        if metrics is not None:
            pulumi.set(__self__, "metrics", metrics)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if output_format is not None:
            pulumi.set(__self__, "output_format", output_format)
        if report_definition_id is not None:
            pulumi.set(__self__, "report_definition_id", report_definition_id)

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "environment_id")

    @environment_id.setter
    def environment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment_id", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> Any:
        """
        Time range for the query. Can use the following predefined strings to specify the time range: `last60minutes` `last24hours` `last7days` Or, specify the timeRange as a structure describing start and end timestamps in the ISO format: yyyy-mm-ddThh:mm:ssZ. Example: "timeRange": { "start": "2018-07-29T00:13:00Z", "end": "2018-08-01T00:18:00Z" }
        """
        return pulumi.get(self, "time_range")

    @time_range.setter
    def time_range(self, value: Any):
        pulumi.set(self, "time_range", value)

    @property
    @pulumi.getter(name="csvDelimiter")
    def csv_delimiter(self) -> Optional[pulumi.Input[str]]:
        """
        Delimiter used in the CSV file, if `outputFormat` is set to `csv`. Defaults to the `,` (comma) character. Supported delimiter characters include comma (`,`), pipe (`|`), and tab (`\\t`).
        """
        return pulumi.get(self, "csv_delimiter")

    @csv_delimiter.setter
    def csv_delimiter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "csv_delimiter", value)

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of dimensions. https://docs.apigee.com/api-platform/analytics/analytics-reference#dimensions
        """
        return pulumi.get(self, "dimensions")

    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "dimensions", value)

    @property
    @pulumi.getter(name="envgroupHostname")
    def envgroup_hostname(self) -> Optional[pulumi.Input[str]]:
        """
        Hostname needs to be specified if query intends to run at host level. This field is only allowed when query is submitted by CreateHostAsyncQuery where analytics data will be grouped by organization and hostname.
        """
        return pulumi.get(self, "envgroup_hostname")

    @envgroup_hostname.setter
    def envgroup_hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "envgroup_hostname", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[str]]:
        """
        Boolean expression that can be used to filter data. Filter expressions can be combined using AND/OR terms and should be fully parenthesized to avoid ambiguity. See Analytics metrics, dimensions, and filters reference https://docs.apigee.com/api-platform/analytics/analytics-reference for more information on the fields available to filter on. For more information on the tokens that you use to build filter expressions, see Filter expression syntax. https://docs.apigee.com/api-platform/analytics/asynch-reports-api#filter-expression-syntax
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter(name="groupByTimeUnit")
    def group_by_time_unit(self) -> Optional[pulumi.Input[str]]:
        """
        Time unit used to group the result set. Valid values include: second, minute, hour, day, week, or month. If a query includes groupByTimeUnit, then the result is an aggregation based on the specified time unit and the resultant timestamp does not include milliseconds precision. If a query omits groupByTimeUnit, then the resultant timestamp includes milliseconds precision.
        """
        return pulumi.get(self, "group_by_time_unit")

    @group_by_time_unit.setter
    def group_by_time_unit(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_by_time_unit", value)

    @property
    @pulumi.getter
    def limit(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum number of rows that can be returned in the result.
        """
        return pulumi.get(self, "limit")

    @limit.setter
    def limit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "limit", value)

    @property
    @pulumi.getter
    def metrics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1QueryMetricArgs']]]]:
        """
        A list of Metrics.
        """
        return pulumi.get(self, "metrics")

    @metrics.setter
    def metrics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudApigeeV1QueryMetricArgs']]]]):
        pulumi.set(self, "metrics", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Asynchronous Query Name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[pulumi.Input[str]]:
        """
        Valid values include: `csv` or `json`. Defaults to `json`. Note: Configure the delimiter for CSV output using the csvDelimiter property.
        """
        return pulumi.get(self, "output_format")

    @output_format.setter
    def output_format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "output_format", value)

    @property
    @pulumi.getter(name="reportDefinitionId")
    def report_definition_id(self) -> Optional[pulumi.Input[str]]:
        """
        Asynchronous Report ID.
        """
        return pulumi.get(self, "report_definition_id")

    @report_definition_id.setter
    def report_definition_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "report_definition_id", value)


class Query(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 csv_delimiter: Optional[pulumi.Input[str]] = None,
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 envgroup_hostname: Optional[pulumi.Input[str]] = None,
                 environment_id: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 group_by_time_unit: Optional[pulumi.Input[str]] = None,
                 limit: Optional[pulumi.Input[int]] = None,
                 metrics: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1QueryMetricArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 output_format: Optional[pulumi.Input[str]] = None,
                 report_definition_id: Optional[pulumi.Input[str]] = None,
                 time_range: Optional[Any] = None,
                 __props__=None):
        """
        Submit a query to be processed in the background. If the submission of the query succeeds, the API returns a 201 status and an ID that refer to the query. In addition to the HTTP status 201, the `state` of "enqueued" means that the request succeeded.
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] csv_delimiter: Delimiter used in the CSV file, if `outputFormat` is set to `csv`. Defaults to the `,` (comma) character. Supported delimiter characters include comma (`,`), pipe (`|`), and tab (`\\t`).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dimensions: A list of dimensions. https://docs.apigee.com/api-platform/analytics/analytics-reference#dimensions
        :param pulumi.Input[str] envgroup_hostname: Hostname needs to be specified if query intends to run at host level. This field is only allowed when query is submitted by CreateHostAsyncQuery where analytics data will be grouped by organization and hostname.
        :param pulumi.Input[str] filter: Boolean expression that can be used to filter data. Filter expressions can be combined using AND/OR terms and should be fully parenthesized to avoid ambiguity. See Analytics metrics, dimensions, and filters reference https://docs.apigee.com/api-platform/analytics/analytics-reference for more information on the fields available to filter on. For more information on the tokens that you use to build filter expressions, see Filter expression syntax. https://docs.apigee.com/api-platform/analytics/asynch-reports-api#filter-expression-syntax
        :param pulumi.Input[str] group_by_time_unit: Time unit used to group the result set. Valid values include: second, minute, hour, day, week, or month. If a query includes groupByTimeUnit, then the result is an aggregation based on the specified time unit and the resultant timestamp does not include milliseconds precision. If a query omits groupByTimeUnit, then the resultant timestamp includes milliseconds precision.
        :param pulumi.Input[int] limit: Maximum number of rows that can be returned in the result.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1QueryMetricArgs']]]] metrics: A list of Metrics.
        :param pulumi.Input[str] name: Asynchronous Query Name.
        :param pulumi.Input[str] output_format: Valid values include: `csv` or `json`. Defaults to `json`. Note: Configure the delimiter for CSV output using the csvDelimiter property.
        :param pulumi.Input[str] report_definition_id: Asynchronous Report ID.
        :param Any time_range: Time range for the query. Can use the following predefined strings to specify the time range: `last60minutes` `last24hours` `last7days` Or, specify the timeRange as a structure describing start and end timestamps in the ISO format: yyyy-mm-ddThh:mm:ssZ. Example: "timeRange": { "start": "2018-07-29T00:13:00Z", "end": "2018-08-01T00:18:00Z" }
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: QueryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Submit a query to be processed in the background. If the submission of the query succeeds, the API returns a 201 status and an ID that refer to the query. In addition to the HTTP status 201, the `state` of "enqueued" means that the request succeeded.
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param QueryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(QueryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 csv_delimiter: Optional[pulumi.Input[str]] = None,
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 envgroup_hostname: Optional[pulumi.Input[str]] = None,
                 environment_id: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 group_by_time_unit: Optional[pulumi.Input[str]] = None,
                 limit: Optional[pulumi.Input[int]] = None,
                 metrics: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1QueryMetricArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 output_format: Optional[pulumi.Input[str]] = None,
                 report_definition_id: Optional[pulumi.Input[str]] = None,
                 time_range: Optional[Any] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = QueryArgs.__new__(QueryArgs)

            __props__.__dict__["csv_delimiter"] = csv_delimiter
            __props__.__dict__["dimensions"] = dimensions
            __props__.__dict__["envgroup_hostname"] = envgroup_hostname
            if environment_id is None and not opts.urn:
                raise TypeError("Missing required property 'environment_id'")
            __props__.__dict__["environment_id"] = environment_id
            __props__.__dict__["filter"] = filter
            __props__.__dict__["group_by_time_unit"] = group_by_time_unit
            __props__.__dict__["limit"] = limit
            __props__.__dict__["metrics"] = metrics
            __props__.__dict__["name"] = name
            if organization_id is None and not opts.urn:
                raise TypeError("Missing required property 'organization_id'")
            __props__.__dict__["organization_id"] = organization_id
            __props__.__dict__["output_format"] = output_format
            __props__.__dict__["report_definition_id"] = report_definition_id
            if time_range is None and not opts.urn:
                raise TypeError("Missing required property 'time_range'")
            __props__.__dict__["time_range"] = time_range
            __props__.__dict__["created"] = None
            __props__.__dict__["error"] = None
            __props__.__dict__["execution_time"] = None
            __props__.__dict__["query_params"] = None
            __props__.__dict__["result"] = None
            __props__.__dict__["result_file_size"] = None
            __props__.__dict__["result_rows"] = None
            __props__.__dict__["self"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["updated"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["environmentId", "organizationId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Query, __self__).__init__(
            'google-native:apigee/v1:Query',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Query':
        """
        Get an existing Query resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = QueryArgs.__new__(QueryArgs)

        __props__.__dict__["created"] = None
        __props__.__dict__["envgroup_hostname"] = None
        __props__.__dict__["environment_id"] = None
        __props__.__dict__["error"] = None
        __props__.__dict__["execution_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["organization_id"] = None
        __props__.__dict__["query_params"] = None
        __props__.__dict__["report_definition_id"] = None
        __props__.__dict__["result"] = None
        __props__.__dict__["result_file_size"] = None
        __props__.__dict__["result_rows"] = None
        __props__.__dict__["self"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["updated"] = None
        return Query(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[str]:
        """
        Creation time of the query.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="envgroupHostname")
    def envgroup_hostname(self) -> pulumi.Output[str]:
        """
        Hostname is available only when query is executed at host level.
        """
        return pulumi.get(self, "envgroup_hostname")

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "environment_id")

    @property
    @pulumi.getter
    def error(self) -> pulumi.Output[str]:
        """
        Error is set when query fails.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter(name="executionTime")
    def execution_time(self) -> pulumi.Output[str]:
        """
        ExecutionTime is available only after the query is completed.
        """
        return pulumi.get(self, "execution_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Asynchronous Query Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="queryParams")
    def query_params(self) -> pulumi.Output['outputs.GoogleCloudApigeeV1QueryMetadataResponse']:
        """
        Contains information like metrics, dimenstions etc of the AsyncQuery.
        """
        return pulumi.get(self, "query_params")

    @property
    @pulumi.getter(name="reportDefinitionId")
    def report_definition_id(self) -> pulumi.Output[str]:
        """
        Asynchronous Report ID.
        """
        return pulumi.get(self, "report_definition_id")

    @property
    @pulumi.getter
    def result(self) -> pulumi.Output['outputs.GoogleCloudApigeeV1AsyncQueryResultResponse']:
        """
        Result is available only after the query is completed.
        """
        return pulumi.get(self, "result")

    @property
    @pulumi.getter(name="resultFileSize")
    def result_file_size(self) -> pulumi.Output[str]:
        """
        ResultFileSize is available only after the query is completed.
        """
        return pulumi.get(self, "result_file_size")

    @property
    @pulumi.getter(name="resultRows")
    def result_rows(self) -> pulumi.Output[str]:
        """
        ResultRows is available only after the query is completed.
        """
        return pulumi.get(self, "result_rows")

    @property
    @pulumi.getter
    def self(self) -> pulumi.Output[str]:
        """
        Self link of the query. Example: `/organizations/myorg/environments/myenv/queries/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd` or following format if query is running at host level: `/organizations/myorg/hostQueries/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd`
        """
        return pulumi.get(self, "self")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Query state could be "enqueued", "running", "completed", "failed".
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def updated(self) -> pulumi.Output[str]:
        """
        Last updated timestamp for the query.
        """
        return pulumi.get(self, "updated")

