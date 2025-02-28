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

__all__ = ['AuthorizedCertificateArgs', 'AuthorizedCertificate']

@pulumi.input_type
class AuthorizedCertificateArgs:
    def __init__(__self__, *,
                 app_id: pulumi.Input[str],
                 certificate_raw_data: Optional[pulumi.Input['CertificateRawDataArgs']] = None,
                 display_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AuthorizedCertificate resource.
        :param pulumi.Input['CertificateRawDataArgs'] certificate_raw_data: The SSL certificate serving the AuthorizedCertificate resource. This must be obtained independently from a certificate authority.
        :param pulumi.Input[str] display_name: The user-specified display name of the certificate. This is not guaranteed to be unique. Example: My Certificate.
        """
        pulumi.set(__self__, "app_id", app_id)
        if certificate_raw_data is not None:
            pulumi.set(__self__, "certificate_raw_data", certificate_raw_data)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter(name="certificateRawData")
    def certificate_raw_data(self) -> Optional[pulumi.Input['CertificateRawDataArgs']]:
        """
        The SSL certificate serving the AuthorizedCertificate resource. This must be obtained independently from a certificate authority.
        """
        return pulumi.get(self, "certificate_raw_data")

    @certificate_raw_data.setter
    def certificate_raw_data(self, value: Optional[pulumi.Input['CertificateRawDataArgs']]):
        pulumi.set(self, "certificate_raw_data", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The user-specified display name of the certificate. This is not guaranteed to be unique. Example: My Certificate.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)


class AuthorizedCertificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 certificate_raw_data: Optional[pulumi.Input[pulumi.InputType['CertificateRawDataArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Uploads the specified SSL certificate.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['CertificateRawDataArgs']] certificate_raw_data: The SSL certificate serving the AuthorizedCertificate resource. This must be obtained independently from a certificate authority.
        :param pulumi.Input[str] display_name: The user-specified display name of the certificate. This is not guaranteed to be unique. Example: My Certificate.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AuthorizedCertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Uploads the specified SSL certificate.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param AuthorizedCertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AuthorizedCertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 certificate_raw_data: Optional[pulumi.Input[pulumi.InputType['CertificateRawDataArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AuthorizedCertificateArgs.__new__(AuthorizedCertificateArgs)

            if app_id is None and not opts.urn:
                raise TypeError("Missing required property 'app_id'")
            __props__.__dict__["app_id"] = app_id
            __props__.__dict__["certificate_raw_data"] = certificate_raw_data
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["domain_mappings_count"] = None
            __props__.__dict__["domain_names"] = None
            __props__.__dict__["expire_time"] = None
            __props__.__dict__["managed_certificate"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["visible_domain_mappings"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["appId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(AuthorizedCertificate, __self__).__init__(
            'google-native:appengine/v1alpha:AuthorizedCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AuthorizedCertificate':
        """
        Get an existing AuthorizedCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AuthorizedCertificateArgs.__new__(AuthorizedCertificateArgs)

        __props__.__dict__["app_id"] = None
        __props__.__dict__["certificate_raw_data"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["domain_mappings_count"] = None
        __props__.__dict__["domain_names"] = None
        __props__.__dict__["expire_time"] = None
        __props__.__dict__["managed_certificate"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["visible_domain_mappings"] = None
        return AuthorizedCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter(name="certificateRawData")
    def certificate_raw_data(self) -> pulumi.Output['outputs.CertificateRawDataResponse']:
        """
        The SSL certificate serving the AuthorizedCertificate resource. This must be obtained independently from a certificate authority.
        """
        return pulumi.get(self, "certificate_raw_data")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The user-specified display name of the certificate. This is not guaranteed to be unique. Example: My Certificate.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="domainMappingsCount")
    def domain_mappings_count(self) -> pulumi.Output[int]:
        """
        Aggregate count of the domain mappings with this certificate mapped. This count includes domain mappings on applications for which the user does not have VIEWER permissions.Only returned by GET or LIST requests when specifically requested by the view=FULL_CERTIFICATE option.
        """
        return pulumi.get(self, "domain_mappings_count")

    @property
    @pulumi.getter(name="domainNames")
    def domain_names(self) -> pulumi.Output[Sequence[str]]:
        """
        Topmost applicable domains of this certificate. This certificate applies to these domains and their subdomains. Example: example.com.
        """
        return pulumi.get(self, "domain_names")

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[str]:
        """
        The time when this certificate expires. To update the renewal time on this certificate, upload an SSL certificate with a different expiration time using AuthorizedCertificates.UpdateAuthorizedCertificate.
        """
        return pulumi.get(self, "expire_time")

    @property
    @pulumi.getter(name="managedCertificate")
    def managed_certificate(self) -> pulumi.Output['outputs.ManagedCertificateResponse']:
        """
        Only applicable if this certificate is managed by App Engine. Managed certificates are tied to the lifecycle of a DomainMapping and cannot be updated or deleted via the AuthorizedCertificates API. If this certificate is manually administered by the user, this field will be empty.
        """
        return pulumi.get(self, "managed_certificate")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Full path to the AuthorizedCertificate resource in the API. Example: apps/myapp/authorizedCertificates/12345.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="visibleDomainMappings")
    def visible_domain_mappings(self) -> pulumi.Output[Sequence[str]]:
        """
        The full paths to user visible Domain Mapping resources that have this certificate mapped. Example: apps/myapp/domainMappings/example.com.This may not represent the full list of mapped domain mappings if the user does not have VIEWER permissions on all of the applications that have this certificate mapped. See domain_mappings_count for a complete count.Only returned by GET or LIST requests when specifically requested by the view=FULL_CERTIFICATE option.
        """
        return pulumi.get(self, "visible_domain_mappings")

