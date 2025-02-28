# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['WorkflowArgs', 'Workflow']

@pulumi.input_type
class WorkflowArgs:
    def __init__(__self__, *,
                 workflow_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service_account: Optional[pulumi.Input[str]] = None,
                 source_contents: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Workflow resource.
        :param pulumi.Input[str] workflow_id: Required. The ID of the workflow to be created. It has to fulfill the following requirements: * Must contain only letters, numbers, underscores and hyphens. * Must start with a letter. * Must be between 1-64 characters. * Must end with a number or a letter. * Must be unique within the customer project and location.
        :param pulumi.Input[str] description: Description of the workflow provided by the user. Must be at most 1000 unicode characters long.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with this workflow. Labels can contain at most 64 entries. Keys and values can be no longer than 63 characters and can only contain lowercase letters, numeric characters, underscores and dashes. Label keys must start with a letter. International characters are allowed.
        :param pulumi.Input[str] name: The resource name of the workflow. Format: projects/{project}/locations/{location}/workflows/{workflow}
        :param pulumi.Input[str] service_account: The service account associated with the latest workflow version. This service account represents the identity of the workflow and determines what permissions the workflow has. Format: projects/{project}/serviceAccounts/{account} or {account} Using `-` as a wildcard for the `{project}` or not providing one at all will infer the project from the account. The `{account}` value can be the `email` address or the `unique_id` of the service account. If not provided, workflow will use the project's default service account. Modifying this field for an existing workflow results in a new workflow revision.
        :param pulumi.Input[str] source_contents: Workflow code to be executed. The size limit is 128KB.
        """
        pulumi.set(__self__, "workflow_id", workflow_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if service_account is not None:
            pulumi.set(__self__, "service_account", service_account)
        if source_contents is not None:
            pulumi.set(__self__, "source_contents", source_contents)

    @property
    @pulumi.getter(name="workflowId")
    def workflow_id(self) -> pulumi.Input[str]:
        """
        Required. The ID of the workflow to be created. It has to fulfill the following requirements: * Must contain only letters, numbers, underscores and hyphens. * Must start with a letter. * Must be between 1-64 characters. * Must end with a number or a letter. * Must be unique within the customer project and location.
        """
        return pulumi.get(self, "workflow_id")

    @workflow_id.setter
    def workflow_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "workflow_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the workflow provided by the user. Must be at most 1000 unicode characters long.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Labels associated with this workflow. Labels can contain at most 64 entries. Keys and values can be no longer than 63 characters and can only contain lowercase letters, numeric characters, underscores and dashes. Label keys must start with a letter. International characters are allowed.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the workflow. Format: projects/{project}/locations/{location}/workflows/{workflow}
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[str]]:
        """
        The service account associated with the latest workflow version. This service account represents the identity of the workflow and determines what permissions the workflow has. Format: projects/{project}/serviceAccounts/{account} or {account} Using `-` as a wildcard for the `{project}` or not providing one at all will infer the project from the account. The `{account}` value can be the `email` address or the `unique_id` of the service account. If not provided, workflow will use the project's default service account. Modifying this field for an existing workflow results in a new workflow revision.
        """
        return pulumi.get(self, "service_account")

    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_account", value)

    @property
    @pulumi.getter(name="sourceContents")
    def source_contents(self) -> Optional[pulumi.Input[str]]:
        """
        Workflow code to be executed. The size limit is 128KB.
        """
        return pulumi.get(self, "source_contents")

    @source_contents.setter
    def source_contents(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_contents", value)


class Workflow(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service_account: Optional[pulumi.Input[str]] = None,
                 source_contents: Optional[pulumi.Input[str]] = None,
                 workflow_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new workflow. If a workflow with the specified name already exists in the specified project and location, the long running operation will return ALREADY_EXISTS error.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the workflow provided by the user. Must be at most 1000 unicode characters long.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with this workflow. Labels can contain at most 64 entries. Keys and values can be no longer than 63 characters and can only contain lowercase letters, numeric characters, underscores and dashes. Label keys must start with a letter. International characters are allowed.
        :param pulumi.Input[str] name: The resource name of the workflow. Format: projects/{project}/locations/{location}/workflows/{workflow}
        :param pulumi.Input[str] service_account: The service account associated with the latest workflow version. This service account represents the identity of the workflow and determines what permissions the workflow has. Format: projects/{project}/serviceAccounts/{account} or {account} Using `-` as a wildcard for the `{project}` or not providing one at all will infer the project from the account. The `{account}` value can be the `email` address or the `unique_id` of the service account. If not provided, workflow will use the project's default service account. Modifying this field for an existing workflow results in a new workflow revision.
        :param pulumi.Input[str] source_contents: Workflow code to be executed. The size limit is 128KB.
        :param pulumi.Input[str] workflow_id: Required. The ID of the workflow to be created. It has to fulfill the following requirements: * Must contain only letters, numbers, underscores and hyphens. * Must start with a letter. * Must be between 1-64 characters. * Must end with a number or a letter. * Must be unique within the customer project and location.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkflowArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new workflow. If a workflow with the specified name already exists in the specified project and location, the long running operation will return ALREADY_EXISTS error.

        :param str resource_name: The name of the resource.
        :param WorkflowArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkflowArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service_account: Optional[pulumi.Input[str]] = None,
                 source_contents: Optional[pulumi.Input[str]] = None,
                 workflow_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkflowArgs.__new__(WorkflowArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["service_account"] = service_account
            __props__.__dict__["source_contents"] = source_contents
            if workflow_id is None and not opts.urn:
                raise TypeError("Missing required property 'workflow_id'")
            __props__.__dict__["workflow_id"] = workflow_id
            __props__.__dict__["create_time"] = None
            __props__.__dict__["revision_create_time"] = None
            __props__.__dict__["revision_id"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["location", "project", "workflowId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Workflow, __self__).__init__(
            'google-native:workflows/v1beta:Workflow',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Workflow':
        """
        Get an existing Workflow resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkflowArgs.__new__(WorkflowArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["revision_create_time"] = None
        __props__.__dict__["revision_id"] = None
        __props__.__dict__["service_account"] = None
        __props__.__dict__["source_contents"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["update_time"] = None
        __props__.__dict__["workflow_id"] = None
        return Workflow(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The timestamp of when the workflow was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Description of the workflow provided by the user. Must be at most 1000 unicode characters long.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Labels associated with this workflow. Labels can contain at most 64 entries. Keys and values can be no longer than 63 characters and can only contain lowercase letters, numeric characters, underscores and dashes. Label keys must start with a letter. International characters are allowed.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the workflow. Format: projects/{project}/locations/{location}/workflows/{workflow}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="revisionCreateTime")
    def revision_create_time(self) -> pulumi.Output[str]:
        """
        The timestamp that the latest revision of the workflow was created.
        """
        return pulumi.get(self, "revision_create_time")

    @property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> pulumi.Output[str]:
        """
        The revision of the workflow. A new revision of a workflow is created as a result of updating the following properties of a workflow: - Service account - Workflow code to be executed The format is "000001-a4d", where the first 6 characters define the zero-padded revision ordinal number. They are followed by a hyphen and 3 hexadecimal random characters.
        """
        return pulumi.get(self, "revision_id")

    @property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Output[str]:
        """
        The service account associated with the latest workflow version. This service account represents the identity of the workflow and determines what permissions the workflow has. Format: projects/{project}/serviceAccounts/{account} or {account} Using `-` as a wildcard for the `{project}` or not providing one at all will infer the project from the account. The `{account}` value can be the `email` address or the `unique_id` of the service account. If not provided, workflow will use the project's default service account. Modifying this field for an existing workflow results in a new workflow revision.
        """
        return pulumi.get(self, "service_account")

    @property
    @pulumi.getter(name="sourceContents")
    def source_contents(self) -> pulumi.Output[str]:
        """
        Workflow code to be executed. The size limit is 128KB.
        """
        return pulumi.get(self, "source_contents")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the workflow deployment.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The last update timestamp of the workflow.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="workflowId")
    def workflow_id(self) -> pulumi.Output[str]:
        """
        Required. The ID of the workflow to be created. It has to fulfill the following requirements: * Must contain only letters, numbers, underscores and hyphens. * Must start with a letter. * Must be between 1-64 characters. * Must end with a number or a letter. * Must be unique within the customer project and location.
        """
        return pulumi.get(self, "workflow_id")

