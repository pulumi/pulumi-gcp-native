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
from ._enums import *
from ._inputs import *

__all__ = ['TestCaseArgs', 'TestCase']

@pulumi.input_type
class TestCaseArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 integration_id: pulumi.Input[str],
                 test_case_id: pulumi.Input[str],
                 trigger_id: pulumi.Input[str],
                 version_id: pulumi.Input[str],
                 create_time: Optional[pulumi.Input[str]] = None,
                 creator_email: Optional[pulumi.Input[str]] = None,
                 database_persistence_policy: Optional[pulumi.Input['TestCaseDatabasePersistencePolicy']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 last_modifier_email: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 lock_holder_email: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 test_input_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudIntegrationsV1alphaIntegrationParameterArgs']]]] = None,
                 test_task_configs: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudIntegrationsV1alphaTestTaskConfigArgs']]]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 workflow_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TestCase resource.
        :param pulumi.Input[str] display_name: The display name of test case.
        :param pulumi.Input[str] test_case_id: Required. Required
        :param pulumi.Input[str] trigger_id: This defines the trigger ID in workflow which is considered to be executed as starting point of the test case
        :param pulumi.Input[str] create_time: Auto-generated.
        :param pulumi.Input[str] creator_email: Optional. The creator's email address. Generated based on the End User Credentials/LOAS role of the user making the call.
        :param pulumi.Input['TestCaseDatabasePersistencePolicy'] database_persistence_policy: Optional. Various policies for how to persist the test execution info including execution info, execution export info, execution metadata index and execution param index..
        :param pulumi.Input[str] description: Optional. Description of the test case.
        :param pulumi.Input[str] last_modifier_email: The last modifer's email address. Generated based on the End User Credentials/LOAS role of the user making the call.
        :param pulumi.Input[str] lock_holder_email: Optional. The edit lock holder's email address. Generated based on the End User Credentials/LOAS role of the user making the call.
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudIntegrationsV1alphaIntegrationParameterArgs']]] test_input_parameters: Optional. Parameters that are expected to be passed to the test case when the test case is triggered. This gives the user the ability to provide default values. This should include all the output variables of the trigger as input variables.
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudIntegrationsV1alphaTestTaskConfigArgs']]] test_task_configs: Optional. However, the test case doesn't mock or assert anything without test_task_configs.
        :param pulumi.Input[str] update_time: Auto-generated.
        :param pulumi.Input[str] workflow_id: ID of the workflow with which this test case is associated
        """
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "integration_id", integration_id)
        pulumi.set(__self__, "test_case_id", test_case_id)
        pulumi.set(__self__, "trigger_id", trigger_id)
        pulumi.set(__self__, "version_id", version_id)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if creator_email is not None:
            pulumi.set(__self__, "creator_email", creator_email)
        if database_persistence_policy is not None:
            pulumi.set(__self__, "database_persistence_policy", database_persistence_policy)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if last_modifier_email is not None:
            pulumi.set(__self__, "last_modifier_email", last_modifier_email)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if lock_holder_email is not None:
            pulumi.set(__self__, "lock_holder_email", lock_holder_email)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if test_input_parameters is not None:
            pulumi.set(__self__, "test_input_parameters", test_input_parameters)
        if test_task_configs is not None:
            pulumi.set(__self__, "test_task_configs", test_task_configs)
        if update_time is not None:
            pulumi.set(__self__, "update_time", update_time)
        if workflow_id is not None:
            pulumi.set(__self__, "workflow_id", workflow_id)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The display name of test case.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="integrationId")
    def integration_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "integration_id")

    @integration_id.setter
    def integration_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "integration_id", value)

    @property
    @pulumi.getter(name="testCaseId")
    def test_case_id(self) -> pulumi.Input[str]:
        """
        Required. Required
        """
        return pulumi.get(self, "test_case_id")

    @test_case_id.setter
    def test_case_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "test_case_id", value)

    @property
    @pulumi.getter(name="triggerId")
    def trigger_id(self) -> pulumi.Input[str]:
        """
        This defines the trigger ID in workflow which is considered to be executed as starting point of the test case
        """
        return pulumi.get(self, "trigger_id")

    @trigger_id.setter
    def trigger_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "trigger_id", value)

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "version_id")

    @version_id.setter
    def version_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "version_id", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Auto-generated.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="creatorEmail")
    def creator_email(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The creator's email address. Generated based on the End User Credentials/LOAS role of the user making the call.
        """
        return pulumi.get(self, "creator_email")

    @creator_email.setter
    def creator_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "creator_email", value)

    @property
    @pulumi.getter(name="databasePersistencePolicy")
    def database_persistence_policy(self) -> Optional[pulumi.Input['TestCaseDatabasePersistencePolicy']]:
        """
        Optional. Various policies for how to persist the test execution info including execution info, execution export info, execution metadata index and execution param index..
        """
        return pulumi.get(self, "database_persistence_policy")

    @database_persistence_policy.setter
    def database_persistence_policy(self, value: Optional[pulumi.Input['TestCaseDatabasePersistencePolicy']]):
        pulumi.set(self, "database_persistence_policy", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Description of the test case.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="lastModifierEmail")
    def last_modifier_email(self) -> Optional[pulumi.Input[str]]:
        """
        The last modifer's email address. Generated based on the End User Credentials/LOAS role of the user making the call.
        """
        return pulumi.get(self, "last_modifier_email")

    @last_modifier_email.setter
    def last_modifier_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_modifier_email", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="lockHolderEmail")
    def lock_holder_email(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The edit lock holder's email address. Generated based on the End User Credentials/LOAS role of the user making the call.
        """
        return pulumi.get(self, "lock_holder_email")

    @lock_holder_email.setter
    def lock_holder_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lock_holder_email", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="testInputParameters")
    def test_input_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudIntegrationsV1alphaIntegrationParameterArgs']]]]:
        """
        Optional. Parameters that are expected to be passed to the test case when the test case is triggered. This gives the user the ability to provide default values. This should include all the output variables of the trigger as input variables.
        """
        return pulumi.get(self, "test_input_parameters")

    @test_input_parameters.setter
    def test_input_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudIntegrationsV1alphaIntegrationParameterArgs']]]]):
        pulumi.set(self, "test_input_parameters", value)

    @property
    @pulumi.getter(name="testTaskConfigs")
    def test_task_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudIntegrationsV1alphaTestTaskConfigArgs']]]]:
        """
        Optional. However, the test case doesn't mock or assert anything without test_task_configs.
        """
        return pulumi.get(self, "test_task_configs")

    @test_task_configs.setter
    def test_task_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudIntegrationsV1alphaTestTaskConfigArgs']]]]):
        pulumi.set(self, "test_task_configs", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        Auto-generated.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)

    @property
    @pulumi.getter(name="workflowId")
    def workflow_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the workflow with which this test case is associated
        """
        return pulumi.get(self, "workflow_id")

    @workflow_id.setter
    def workflow_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workflow_id", value)


class TestCase(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 creator_email: Optional[pulumi.Input[str]] = None,
                 database_persistence_policy: Optional[pulumi.Input['TestCaseDatabasePersistencePolicy']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 integration_id: Optional[pulumi.Input[str]] = None,
                 last_modifier_email: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 lock_holder_email: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 test_case_id: Optional[pulumi.Input[str]] = None,
                 test_input_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudIntegrationsV1alphaIntegrationParameterArgs']]]]] = None,
                 test_task_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudIntegrationsV1alphaTestTaskConfigArgs']]]]] = None,
                 trigger_id: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 version_id: Optional[pulumi.Input[str]] = None,
                 workflow_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new test case
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: Auto-generated.
        :param pulumi.Input[str] creator_email: Optional. The creator's email address. Generated based on the End User Credentials/LOAS role of the user making the call.
        :param pulumi.Input['TestCaseDatabasePersistencePolicy'] database_persistence_policy: Optional. Various policies for how to persist the test execution info including execution info, execution export info, execution metadata index and execution param index..
        :param pulumi.Input[str] description: Optional. Description of the test case.
        :param pulumi.Input[str] display_name: The display name of test case.
        :param pulumi.Input[str] last_modifier_email: The last modifer's email address. Generated based on the End User Credentials/LOAS role of the user making the call.
        :param pulumi.Input[str] lock_holder_email: Optional. The edit lock holder's email address. Generated based on the End User Credentials/LOAS role of the user making the call.
        :param pulumi.Input[str] test_case_id: Required. Required
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudIntegrationsV1alphaIntegrationParameterArgs']]]] test_input_parameters: Optional. Parameters that are expected to be passed to the test case when the test case is triggered. This gives the user the ability to provide default values. This should include all the output variables of the trigger as input variables.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudIntegrationsV1alphaTestTaskConfigArgs']]]] test_task_configs: Optional. However, the test case doesn't mock or assert anything without test_task_configs.
        :param pulumi.Input[str] trigger_id: This defines the trigger ID in workflow which is considered to be executed as starting point of the test case
        :param pulumi.Input[str] update_time: Auto-generated.
        :param pulumi.Input[str] workflow_id: ID of the workflow with which this test case is associated
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TestCaseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new test case
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param TestCaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TestCaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 creator_email: Optional[pulumi.Input[str]] = None,
                 database_persistence_policy: Optional[pulumi.Input['TestCaseDatabasePersistencePolicy']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 integration_id: Optional[pulumi.Input[str]] = None,
                 last_modifier_email: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 lock_holder_email: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 test_case_id: Optional[pulumi.Input[str]] = None,
                 test_input_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudIntegrationsV1alphaIntegrationParameterArgs']]]]] = None,
                 test_task_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudIntegrationsV1alphaTestTaskConfigArgs']]]]] = None,
                 trigger_id: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 version_id: Optional[pulumi.Input[str]] = None,
                 workflow_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TestCaseArgs.__new__(TestCaseArgs)

            __props__.__dict__["create_time"] = create_time
            __props__.__dict__["creator_email"] = creator_email
            __props__.__dict__["database_persistence_policy"] = database_persistence_policy
            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            if integration_id is None and not opts.urn:
                raise TypeError("Missing required property 'integration_id'")
            __props__.__dict__["integration_id"] = integration_id
            __props__.__dict__["last_modifier_email"] = last_modifier_email
            __props__.__dict__["location"] = location
            __props__.__dict__["lock_holder_email"] = lock_holder_email
            __props__.__dict__["project"] = project
            if test_case_id is None and not opts.urn:
                raise TypeError("Missing required property 'test_case_id'")
            __props__.__dict__["test_case_id"] = test_case_id
            __props__.__dict__["test_input_parameters"] = test_input_parameters
            __props__.__dict__["test_task_configs"] = test_task_configs
            if trigger_id is None and not opts.urn:
                raise TypeError("Missing required property 'trigger_id'")
            __props__.__dict__["trigger_id"] = trigger_id
            __props__.__dict__["update_time"] = update_time
            if version_id is None and not opts.urn:
                raise TypeError("Missing required property 'version_id'")
            __props__.__dict__["version_id"] = version_id
            __props__.__dict__["workflow_id"] = workflow_id
            __props__.__dict__["name"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["integrationId", "location", "project", "testCaseId", "versionId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(TestCase, __self__).__init__(
            'google-native:integrations/v1alpha:TestCase',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TestCase':
        """
        Get an existing TestCase resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TestCaseArgs.__new__(TestCaseArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["creator_email"] = None
        __props__.__dict__["database_persistence_policy"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["integration_id"] = None
        __props__.__dict__["last_modifier_email"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["lock_holder_email"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["test_case_id"] = None
        __props__.__dict__["test_input_parameters"] = None
        __props__.__dict__["test_task_configs"] = None
        __props__.__dict__["trigger_id"] = None
        __props__.__dict__["update_time"] = None
        __props__.__dict__["version_id"] = None
        __props__.__dict__["workflow_id"] = None
        return TestCase(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Auto-generated.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="creatorEmail")
    def creator_email(self) -> pulumi.Output[str]:
        """
        Optional. The creator's email address. Generated based on the End User Credentials/LOAS role of the user making the call.
        """
        return pulumi.get(self, "creator_email")

    @property
    @pulumi.getter(name="databasePersistencePolicy")
    def database_persistence_policy(self) -> pulumi.Output[str]:
        """
        Optional. Various policies for how to persist the test execution info including execution info, execution export info, execution metadata index and execution param index..
        """
        return pulumi.get(self, "database_persistence_policy")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Optional. Description of the test case.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The display name of test case.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="integrationId")
    def integration_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "integration_id")

    @property
    @pulumi.getter(name="lastModifierEmail")
    def last_modifier_email(self) -> pulumi.Output[str]:
        """
        The last modifer's email address. Generated based on the End User Credentials/LOAS role of the user making the call.
        """
        return pulumi.get(self, "last_modifier_email")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="lockHolderEmail")
    def lock_holder_email(self) -> pulumi.Output[str]:
        """
        Optional. The edit lock holder's email address. Generated based on the End User Credentials/LOAS role of the user making the call.
        """
        return pulumi.get(self, "lock_holder_email")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Auto-generated primary key.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="testCaseId")
    def test_case_id(self) -> pulumi.Output[str]:
        """
        Required. Required
        """
        return pulumi.get(self, "test_case_id")

    @property
    @pulumi.getter(name="testInputParameters")
    def test_input_parameters(self) -> pulumi.Output[Sequence['outputs.GoogleCloudIntegrationsV1alphaIntegrationParameterResponse']]:
        """
        Optional. Parameters that are expected to be passed to the test case when the test case is triggered. This gives the user the ability to provide default values. This should include all the output variables of the trigger as input variables.
        """
        return pulumi.get(self, "test_input_parameters")

    @property
    @pulumi.getter(name="testTaskConfigs")
    def test_task_configs(self) -> pulumi.Output[Sequence['outputs.GoogleCloudIntegrationsV1alphaTestTaskConfigResponse']]:
        """
        Optional. However, the test case doesn't mock or assert anything without test_task_configs.
        """
        return pulumi.get(self, "test_task_configs")

    @property
    @pulumi.getter(name="triggerId")
    def trigger_id(self) -> pulumi.Output[str]:
        """
        This defines the trigger ID in workflow which is considered to be executed as starting point of the test case
        """
        return pulumi.get(self, "trigger_id")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Auto-generated.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "version_id")

    @property
    @pulumi.getter(name="workflowId")
    def workflow_id(self) -> pulumi.Output[str]:
        """
        ID of the workflow with which this test case is associated
        """
        return pulumi.get(self, "workflow_id")

