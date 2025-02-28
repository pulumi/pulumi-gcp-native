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

__all__ = ['CaseArgs', 'Case']

@pulumi.input_type
class CaseArgs:
    def __init__(__self__, *,
                 v2beta_id1: pulumi.Input[str],
                 v2betum_id: pulumi.Input[str],
                 classification: Optional[pulumi.Input['CaseClassificationArgs']] = None,
                 contact_email: Optional[pulumi.Input[str]] = None,
                 creator: Optional[pulumi.Input['ActorArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 escalated: Optional[pulumi.Input[bool]] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input['CasePriority']] = None,
                 severity: Optional[pulumi.Input['CaseSeverity']] = None,
                 subscriber_email_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 test_case: Optional[pulumi.Input[bool]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Case resource.
        :param pulumi.Input['CaseClassificationArgs'] classification: The issue classification applicable to this case.
        :param pulumi.Input[str] contact_email: A user-supplied email address to send case update notifications for. This should only be used in BYOID flows, where we cannot infer the user's email address directly from their EUCs.
        :param pulumi.Input['ActorArgs'] creator: The user who created the case. Note: The name and email will be obfuscated if the case was created by Google Support.
        :param pulumi.Input[str] description: A broad description of the issue.
        :param pulumi.Input[str] display_name: The short summary of the issue reported in this case.
        :param pulumi.Input[bool] escalated: Whether the case is currently escalated.
        :param pulumi.Input[str] language_code: The language the user has requested to receive support in. This should be a BCP 47 language code (e.g., `"en"`, `"zh-CN"`, `"zh-TW"`, `"ja"`, `"ko"`). If no language or an unsupported language is specified, this field defaults to English (en). Language selection during case creation may affect your available support options. For a list of supported languages and their support working hours, see: https://cloud.google.com/support/docs/language-working-hours
        :param pulumi.Input[str] name: The resource name for the case.
        :param pulumi.Input['CasePriority'] priority: The priority of this case.
        :param pulumi.Input['CaseSeverity'] severity: REMOVED. The severity of this case. Use priority instead.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subscriber_email_addresses: The email addresses to receive updates on this case.
        :param pulumi.Input[bool] test_case: Whether this case was created for internal API testing and should not be acted on by the support team.
        :param pulumi.Input[str] time_zone: The timezone of the user who created the support case. It should be in a format IANA recognizes: https://www.iana.org/time-zones. There is no additional validation done by the API.
        """
        pulumi.set(__self__, "v2beta_id1", v2beta_id1)
        pulumi.set(__self__, "v2betum_id", v2betum_id)
        if classification is not None:
            pulumi.set(__self__, "classification", classification)
        if contact_email is not None:
            pulumi.set(__self__, "contact_email", contact_email)
        if creator is not None:
            pulumi.set(__self__, "creator", creator)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if escalated is not None:
            pulumi.set(__self__, "escalated", escalated)
        if language_code is not None:
            pulumi.set(__self__, "language_code", language_code)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if severity is not None:
            pulumi.set(__self__, "severity", severity)
        if subscriber_email_addresses is not None:
            pulumi.set(__self__, "subscriber_email_addresses", subscriber_email_addresses)
        if test_case is not None:
            pulumi.set(__self__, "test_case", test_case)
        if time_zone is not None:
            pulumi.set(__self__, "time_zone", time_zone)

    @property
    @pulumi.getter(name="v2betaId1")
    def v2beta_id1(self) -> pulumi.Input[str]:
        return pulumi.get(self, "v2beta_id1")

    @v2beta_id1.setter
    def v2beta_id1(self, value: pulumi.Input[str]):
        pulumi.set(self, "v2beta_id1", value)

    @property
    @pulumi.getter(name="v2betumId")
    def v2betum_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "v2betum_id")

    @v2betum_id.setter
    def v2betum_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "v2betum_id", value)

    @property
    @pulumi.getter
    def classification(self) -> Optional[pulumi.Input['CaseClassificationArgs']]:
        """
        The issue classification applicable to this case.
        """
        return pulumi.get(self, "classification")

    @classification.setter
    def classification(self, value: Optional[pulumi.Input['CaseClassificationArgs']]):
        pulumi.set(self, "classification", value)

    @property
    @pulumi.getter(name="contactEmail")
    def contact_email(self) -> Optional[pulumi.Input[str]]:
        """
        A user-supplied email address to send case update notifications for. This should only be used in BYOID flows, where we cannot infer the user's email address directly from their EUCs.
        """
        return pulumi.get(self, "contact_email")

    @contact_email.setter
    def contact_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "contact_email", value)

    @property
    @pulumi.getter
    def creator(self) -> Optional[pulumi.Input['ActorArgs']]:
        """
        The user who created the case. Note: The name and email will be obfuscated if the case was created by Google Support.
        """
        return pulumi.get(self, "creator")

    @creator.setter
    def creator(self, value: Optional[pulumi.Input['ActorArgs']]):
        pulumi.set(self, "creator", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A broad description of the issue.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The short summary of the issue reported in this case.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def escalated(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the case is currently escalated.
        """
        return pulumi.get(self, "escalated")

    @escalated.setter
    def escalated(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "escalated", value)

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[str]]:
        """
        The language the user has requested to receive support in. This should be a BCP 47 language code (e.g., `"en"`, `"zh-CN"`, `"zh-TW"`, `"ja"`, `"ko"`). If no language or an unsupported language is specified, this field defaults to English (en). Language selection during case creation may affect your available support options. For a list of supported languages and their support working hours, see: https://cloud.google.com/support/docs/language-working-hours
        """
        return pulumi.get(self, "language_code")

    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "language_code", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name for the case.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input['CasePriority']]:
        """
        The priority of this case.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input['CasePriority']]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input['CaseSeverity']]:
        """
        REMOVED. The severity of this case. Use priority instead.
        """
        return pulumi.get(self, "severity")

    @severity.setter
    def severity(self, value: Optional[pulumi.Input['CaseSeverity']]):
        pulumi.set(self, "severity", value)

    @property
    @pulumi.getter(name="subscriberEmailAddresses")
    def subscriber_email_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The email addresses to receive updates on this case.
        """
        return pulumi.get(self, "subscriber_email_addresses")

    @subscriber_email_addresses.setter
    def subscriber_email_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subscriber_email_addresses", value)

    @property
    @pulumi.getter(name="testCase")
    def test_case(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this case was created for internal API testing and should not be acted on by the support team.
        """
        return pulumi.get(self, "test_case")

    @test_case.setter
    def test_case(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "test_case", value)

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[str]]:
        """
        The timezone of the user who created the support case. It should be in a format IANA recognizes: https://www.iana.org/time-zones. There is no additional validation done by the API.
        """
        return pulumi.get(self, "time_zone")

    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_zone", value)


class Case(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 classification: Optional[pulumi.Input[pulumi.InputType['CaseClassificationArgs']]] = None,
                 contact_email: Optional[pulumi.Input[str]] = None,
                 creator: Optional[pulumi.Input[pulumi.InputType['ActorArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 escalated: Optional[pulumi.Input[bool]] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input['CasePriority']] = None,
                 severity: Optional[pulumi.Input['CaseSeverity']] = None,
                 subscriber_email_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 test_case: Optional[pulumi.Input[bool]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 v2beta_id1: Optional[pulumi.Input[str]] = None,
                 v2betum_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a new case and associate it with a parent. It must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`. EXAMPLES: cURL: ``` shell parent="projects/some-project" curl \\ --request POST \\ --header "Authorization: Bearer $(gcloud auth print-access-token)" \\ --header 'Content-Type: application/json' \\ --data '{ "display_name": "Test case created by me.", "description": "a random test case, feel free to close", "classification": { "id": "100IK2AKCLHMGRJ9CDGMOCGP8DM6UTB4BT262T31BT1M2T31DHNMENPO6KS36CPJ786L2TBFEHGN6NPI64R3CDHN8880G08I1H3MURR7DHII0GRCDTQM8" }, "time_zone": "-07:00", "subscriber_email_addresses": [ "foo@domain.com", "bar@domain.com" ], "testCase": true, "priority": "P3" }' \\ "https://cloudsupport.googleapis.com/v2/$parent/cases"  ``` Python: ``` python import googleapiclient.discovery api_version = "v2" supportApiService = googleapiclient.discovery.build( serviceName="cloudsupport", version=api_version, discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={api_version}", ) request = supportApiService.cases().create( parent="projects/some-project", body={ "displayName": "A Test Case", "description": "This is a test case.", "testCase": True, "priority": "P2", "classification": { "id": "100IK2AKCLHMGRJ9CDGMOCGP8DM6UTB4BT262T31BT1M2T31DHNMENPO6KS36CPJ786L2TBFEHGN6NPI64R3CDHN8880G08I1H3MURR7DHII0GRCDTQM8" }, }, ) print(request.execute())  ```
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['CaseClassificationArgs']] classification: The issue classification applicable to this case.
        :param pulumi.Input[str] contact_email: A user-supplied email address to send case update notifications for. This should only be used in BYOID flows, where we cannot infer the user's email address directly from their EUCs.
        :param pulumi.Input[pulumi.InputType['ActorArgs']] creator: The user who created the case. Note: The name and email will be obfuscated if the case was created by Google Support.
        :param pulumi.Input[str] description: A broad description of the issue.
        :param pulumi.Input[str] display_name: The short summary of the issue reported in this case.
        :param pulumi.Input[bool] escalated: Whether the case is currently escalated.
        :param pulumi.Input[str] language_code: The language the user has requested to receive support in. This should be a BCP 47 language code (e.g., `"en"`, `"zh-CN"`, `"zh-TW"`, `"ja"`, `"ko"`). If no language or an unsupported language is specified, this field defaults to English (en). Language selection during case creation may affect your available support options. For a list of supported languages and their support working hours, see: https://cloud.google.com/support/docs/language-working-hours
        :param pulumi.Input[str] name: The resource name for the case.
        :param pulumi.Input['CasePriority'] priority: The priority of this case.
        :param pulumi.Input['CaseSeverity'] severity: REMOVED. The severity of this case. Use priority instead.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subscriber_email_addresses: The email addresses to receive updates on this case.
        :param pulumi.Input[bool] test_case: Whether this case was created for internal API testing and should not be acted on by the support team.
        :param pulumi.Input[str] time_zone: The timezone of the user who created the support case. It should be in a format IANA recognizes: https://www.iana.org/time-zones. There is no additional validation done by the API.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CaseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a new case and associate it with a parent. It must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`. EXAMPLES: cURL: ``` shell parent="projects/some-project" curl \\ --request POST \\ --header "Authorization: Bearer $(gcloud auth print-access-token)" \\ --header 'Content-Type: application/json' \\ --data '{ "display_name": "Test case created by me.", "description": "a random test case, feel free to close", "classification": { "id": "100IK2AKCLHMGRJ9CDGMOCGP8DM6UTB4BT262T31BT1M2T31DHNMENPO6KS36CPJ786L2TBFEHGN6NPI64R3CDHN8880G08I1H3MURR7DHII0GRCDTQM8" }, "time_zone": "-07:00", "subscriber_email_addresses": [ "foo@domain.com", "bar@domain.com" ], "testCase": true, "priority": "P3" }' \\ "https://cloudsupport.googleapis.com/v2/$parent/cases"  ``` Python: ``` python import googleapiclient.discovery api_version = "v2" supportApiService = googleapiclient.discovery.build( serviceName="cloudsupport", version=api_version, discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={api_version}", ) request = supportApiService.cases().create( parent="projects/some-project", body={ "displayName": "A Test Case", "description": "This is a test case.", "testCase": True, "priority": "P2", "classification": { "id": "100IK2AKCLHMGRJ9CDGMOCGP8DM6UTB4BT262T31BT1M2T31DHNMENPO6KS36CPJ786L2TBFEHGN6NPI64R3CDHN8880G08I1H3MURR7DHII0GRCDTQM8" }, }, ) print(request.execute())  ```
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param CaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 classification: Optional[pulumi.Input[pulumi.InputType['CaseClassificationArgs']]] = None,
                 contact_email: Optional[pulumi.Input[str]] = None,
                 creator: Optional[pulumi.Input[pulumi.InputType['ActorArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 escalated: Optional[pulumi.Input[bool]] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input['CasePriority']] = None,
                 severity: Optional[pulumi.Input['CaseSeverity']] = None,
                 subscriber_email_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 test_case: Optional[pulumi.Input[bool]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 v2beta_id1: Optional[pulumi.Input[str]] = None,
                 v2betum_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CaseArgs.__new__(CaseArgs)

            __props__.__dict__["classification"] = classification
            __props__.__dict__["contact_email"] = contact_email
            __props__.__dict__["creator"] = creator
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["escalated"] = escalated
            __props__.__dict__["language_code"] = language_code
            __props__.__dict__["name"] = name
            __props__.__dict__["priority"] = priority
            __props__.__dict__["severity"] = severity
            __props__.__dict__["subscriber_email_addresses"] = subscriber_email_addresses
            __props__.__dict__["test_case"] = test_case
            __props__.__dict__["time_zone"] = time_zone
            if v2beta_id1 is None and not opts.urn:
                raise TypeError("Missing required property 'v2beta_id1'")
            __props__.__dict__["v2beta_id1"] = v2beta_id1
            if v2betum_id is None and not opts.urn:
                raise TypeError("Missing required property 'v2betum_id'")
            __props__.__dict__["v2betum_id"] = v2betum_id
            __props__.__dict__["create_time"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["v2betaId1", "v2betumId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Case, __self__).__init__(
            'google-native:cloudsupport/v2beta:Case',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Case':
        """
        Get an existing Case resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CaseArgs.__new__(CaseArgs)

        __props__.__dict__["classification"] = None
        __props__.__dict__["contact_email"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["creator"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["escalated"] = None
        __props__.__dict__["language_code"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["priority"] = None
        __props__.__dict__["severity"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["subscriber_email_addresses"] = None
        __props__.__dict__["test_case"] = None
        __props__.__dict__["time_zone"] = None
        __props__.__dict__["update_time"] = None
        __props__.__dict__["v2beta_id1"] = None
        __props__.__dict__["v2betum_id"] = None
        return Case(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def classification(self) -> pulumi.Output['outputs.CaseClassificationResponse']:
        """
        The issue classification applicable to this case.
        """
        return pulumi.get(self, "classification")

    @property
    @pulumi.getter(name="contactEmail")
    def contact_email(self) -> pulumi.Output[str]:
        """
        A user-supplied email address to send case update notifications for. This should only be used in BYOID flows, where we cannot infer the user's email address directly from their EUCs.
        """
        return pulumi.get(self, "contact_email")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time this case was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def creator(self) -> pulumi.Output['outputs.ActorResponse']:
        """
        The user who created the case. Note: The name and email will be obfuscated if the case was created by Google Support.
        """
        return pulumi.get(self, "creator")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        A broad description of the issue.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The short summary of the issue reported in this case.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def escalated(self) -> pulumi.Output[bool]:
        """
        Whether the case is currently escalated.
        """
        return pulumi.get(self, "escalated")

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Output[str]:
        """
        The language the user has requested to receive support in. This should be a BCP 47 language code (e.g., `"en"`, `"zh-CN"`, `"zh-TW"`, `"ja"`, `"ko"`). If no language or an unsupported language is specified, this field defaults to English (en). Language selection during case creation may affect your available support options. For a list of supported languages and their support working hours, see: https://cloud.google.com/support/docs/language-working-hours
        """
        return pulumi.get(self, "language_code")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name for the case.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[str]:
        """
        The priority of this case.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def severity(self) -> pulumi.Output[str]:
        """
        REMOVED. The severity of this case. Use priority instead.
        """
        return pulumi.get(self, "severity")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current status of the support case.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subscriberEmailAddresses")
    def subscriber_email_addresses(self) -> pulumi.Output[Sequence[str]]:
        """
        The email addresses to receive updates on this case.
        """
        return pulumi.get(self, "subscriber_email_addresses")

    @property
    @pulumi.getter(name="testCase")
    def test_case(self) -> pulumi.Output[bool]:
        """
        Whether this case was created for internal API testing and should not be acted on by the support team.
        """
        return pulumi.get(self, "test_case")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[str]:
        """
        The timezone of the user who created the support case. It should be in a format IANA recognizes: https://www.iana.org/time-zones. There is no additional validation done by the API.
        """
        return pulumi.get(self, "time_zone")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The time this case was last updated.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="v2betaId1")
    def v2beta_id1(self) -> pulumi.Output[str]:
        return pulumi.get(self, "v2beta_id1")

    @property
    @pulumi.getter(name="v2betumId")
    def v2betum_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "v2betum_id")

