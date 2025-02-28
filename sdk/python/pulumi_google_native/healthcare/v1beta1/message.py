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

__all__ = ['MessageArgs', 'Message']

@pulumi.input_type
class MessageArgs:
    def __init__(__self__, *,
                 dataset_id: pulumi.Input[str],
                 hl7_v2_store_id: pulumi.Input[str],
                 data: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 message_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 patient_ids: Optional[pulumi.Input[Sequence[pulumi.Input['PatientIdArgs']]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 schematized_data: Optional[pulumi.Input['SchematizedDataArgs']] = None,
                 send_facility: Optional[pulumi.Input[str]] = None,
                 send_time: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Message resource.
        :param pulumi.Input[str] data: Raw message bytes.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \\p{Ll}\\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\\p{Ll}\\p{Lo}\\p{N}_-]{0,63} No more than 64 labels can be associated with a given store.
        :param pulumi.Input[str] message_type: The message type for this message. MSH-9.1.
        :param pulumi.Input[str] name: Resource name of the Message, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7V2Stores/{hl7_v2_store_id}/messages/{message_id}`. Assigned by the server.
        :param pulumi.Input[Sequence[pulumi.Input['PatientIdArgs']]] patient_ids: All patient IDs listed in the PID-2, PID-3, and PID-4 segments of this message.
        :param pulumi.Input['SchematizedDataArgs'] schematized_data: The parsed version of the raw message data schematized according to this store's schemas and type definitions.
        :param pulumi.Input[str] send_facility: The hospital that this message came from. MSH-4.
        :param pulumi.Input[str] send_time: The datetime the sending application sent this message. MSH-7.
        """
        pulumi.set(__self__, "dataset_id", dataset_id)
        pulumi.set(__self__, "hl7_v2_store_id", hl7_v2_store_id)
        if data is not None:
            pulumi.set(__self__, "data", data)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if message_type is not None:
            pulumi.set(__self__, "message_type", message_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if patient_ids is not None:
            pulumi.set(__self__, "patient_ids", patient_ids)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if schematized_data is not None:
            pulumi.set(__self__, "schematized_data", schematized_data)
        if send_facility is not None:
            pulumi.set(__self__, "send_facility", send_facility)
        if send_time is not None:
            pulumi.set(__self__, "send_time", send_time)

    @property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "dataset_id")

    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "dataset_id", value)

    @property
    @pulumi.getter(name="hl7V2StoreId")
    def hl7_v2_store_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "hl7_v2_store_id")

    @hl7_v2_store_id.setter
    def hl7_v2_store_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "hl7_v2_store_id", value)

    @property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[str]]:
        """
        Raw message bytes.
        """
        return pulumi.get(self, "data")

    @data.setter
    def data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \\p{Ll}\\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\\p{Ll}\\p{Lo}\\p{N}_-]{0,63} No more than 64 labels can be associated with a given store.
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
    @pulumi.getter(name="messageType")
    def message_type(self) -> Optional[pulumi.Input[str]]:
        """
        The message type for this message. MSH-9.1.
        """
        return pulumi.get(self, "message_type")

    @message_type.setter
    def message_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Resource name of the Message, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7V2Stores/{hl7_v2_store_id}/messages/{message_id}`. Assigned by the server.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="patientIds")
    def patient_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PatientIdArgs']]]]:
        """
        All patient IDs listed in the PID-2, PID-3, and PID-4 segments of this message.
        """
        return pulumi.get(self, "patient_ids")

    @patient_ids.setter
    def patient_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PatientIdArgs']]]]):
        pulumi.set(self, "patient_ids", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="schematizedData")
    def schematized_data(self) -> Optional[pulumi.Input['SchematizedDataArgs']]:
        """
        The parsed version of the raw message data schematized according to this store's schemas and type definitions.
        """
        return pulumi.get(self, "schematized_data")

    @schematized_data.setter
    def schematized_data(self, value: Optional[pulumi.Input['SchematizedDataArgs']]):
        pulumi.set(self, "schematized_data", value)

    @property
    @pulumi.getter(name="sendFacility")
    def send_facility(self) -> Optional[pulumi.Input[str]]:
        """
        The hospital that this message came from. MSH-4.
        """
        return pulumi.get(self, "send_facility")

    @send_facility.setter
    def send_facility(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "send_facility", value)

    @property
    @pulumi.getter(name="sendTime")
    def send_time(self) -> Optional[pulumi.Input[str]]:
        """
        The datetime the sending application sent this message. MSH-7.
        """
        return pulumi.get(self, "send_time")

    @send_time.setter
    def send_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "send_time", value)


class Message(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data: Optional[pulumi.Input[str]] = None,
                 dataset_id: Optional[pulumi.Input[str]] = None,
                 hl7_v2_store_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 message_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 patient_ids: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PatientIdArgs']]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 schematized_data: Optional[pulumi.Input[pulumi.InputType['SchematizedDataArgs']]] = None,
                 send_facility: Optional[pulumi.Input[str]] = None,
                 send_time: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Parses and stores an HL7v2 message. This method triggers an asynchronous notification to any Pub/Sub topic configured in Hl7V2Store.Hl7V2NotificationConfig, if the filtering matches the message. If an MLLP adapter is configured to listen to a Pub/Sub topic, the adapter transmits the message when a notification is received.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data: Raw message bytes.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \\p{Ll}\\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\\p{Ll}\\p{Lo}\\p{N}_-]{0,63} No more than 64 labels can be associated with a given store.
        :param pulumi.Input[str] message_type: The message type for this message. MSH-9.1.
        :param pulumi.Input[str] name: Resource name of the Message, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7V2Stores/{hl7_v2_store_id}/messages/{message_id}`. Assigned by the server.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PatientIdArgs']]]] patient_ids: All patient IDs listed in the PID-2, PID-3, and PID-4 segments of this message.
        :param pulumi.Input[pulumi.InputType['SchematizedDataArgs']] schematized_data: The parsed version of the raw message data schematized according to this store's schemas and type definitions.
        :param pulumi.Input[str] send_facility: The hospital that this message came from. MSH-4.
        :param pulumi.Input[str] send_time: The datetime the sending application sent this message. MSH-7.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MessageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Parses and stores an HL7v2 message. This method triggers an asynchronous notification to any Pub/Sub topic configured in Hl7V2Store.Hl7V2NotificationConfig, if the filtering matches the message. If an MLLP adapter is configured to listen to a Pub/Sub topic, the adapter transmits the message when a notification is received.

        :param str resource_name: The name of the resource.
        :param MessageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MessageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data: Optional[pulumi.Input[str]] = None,
                 dataset_id: Optional[pulumi.Input[str]] = None,
                 hl7_v2_store_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 message_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 patient_ids: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PatientIdArgs']]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 schematized_data: Optional[pulumi.Input[pulumi.InputType['SchematizedDataArgs']]] = None,
                 send_facility: Optional[pulumi.Input[str]] = None,
                 send_time: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MessageArgs.__new__(MessageArgs)

            __props__.__dict__["data"] = data
            if dataset_id is None and not opts.urn:
                raise TypeError("Missing required property 'dataset_id'")
            __props__.__dict__["dataset_id"] = dataset_id
            if hl7_v2_store_id is None and not opts.urn:
                raise TypeError("Missing required property 'hl7_v2_store_id'")
            __props__.__dict__["hl7_v2_store_id"] = hl7_v2_store_id
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["message_type"] = message_type
            __props__.__dict__["name"] = name
            __props__.__dict__["patient_ids"] = patient_ids
            __props__.__dict__["project"] = project
            __props__.__dict__["schematized_data"] = schematized_data
            __props__.__dict__["send_facility"] = send_facility
            __props__.__dict__["send_time"] = send_time
            __props__.__dict__["create_time"] = None
            __props__.__dict__["parsed_data"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["datasetId", "hl7V2StoreId", "location", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Message, __self__).__init__(
            'google-native:healthcare/v1beta1:Message',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Message':
        """
        Get an existing Message resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MessageArgs.__new__(MessageArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["data"] = None
        __props__.__dict__["dataset_id"] = None
        __props__.__dict__["hl7_v2_store_id"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["message_type"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parsed_data"] = None
        __props__.__dict__["patient_ids"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["schematized_data"] = None
        __props__.__dict__["send_facility"] = None
        __props__.__dict__["send_time"] = None
        return Message(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The datetime when the message was created. Set by the server.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def data(self) -> pulumi.Output[str]:
        """
        Raw message bytes.
        """
        return pulumi.get(self, "data")

    @property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "dataset_id")

    @property
    @pulumi.getter(name="hl7V2StoreId")
    def hl7_v2_store_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "hl7_v2_store_id")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \\p{Ll}\\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\\p{Ll}\\p{Lo}\\p{N}_-]{0,63} No more than 64 labels can be associated with a given store.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="messageType")
    def message_type(self) -> pulumi.Output[str]:
        """
        The message type for this message. MSH-9.1.
        """
        return pulumi.get(self, "message_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name of the Message, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7V2Stores/{hl7_v2_store_id}/messages/{message_id}`. Assigned by the server.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parsedData")
    def parsed_data(self) -> pulumi.Output['outputs.ParsedDataResponse']:
        """
        The parsed version of the raw message data.
        """
        return pulumi.get(self, "parsed_data")

    @property
    @pulumi.getter(name="patientIds")
    def patient_ids(self) -> pulumi.Output[Sequence['outputs.PatientIdResponse']]:
        """
        All patient IDs listed in the PID-2, PID-3, and PID-4 segments of this message.
        """
        return pulumi.get(self, "patient_ids")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="schematizedData")
    def schematized_data(self) -> pulumi.Output['outputs.SchematizedDataResponse']:
        """
        The parsed version of the raw message data schematized according to this store's schemas and type definitions.
        """
        return pulumi.get(self, "schematized_data")

    @property
    @pulumi.getter(name="sendFacility")
    def send_facility(self) -> pulumi.Output[str]:
        """
        The hospital that this message came from. MSH-4.
        """
        return pulumi.get(self, "send_facility")

    @property
    @pulumi.getter(name="sendTime")
    def send_time(self) -> pulumi.Output[str]:
        """
        The datetime the sending application sent this message. MSH-7.
        """
        return pulumi.get(self, "send_time")

