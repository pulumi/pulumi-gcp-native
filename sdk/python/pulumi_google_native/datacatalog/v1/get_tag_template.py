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

__all__ = [
    'GetTagTemplateResult',
    'AwaitableGetTagTemplateResult',
    'get_tag_template',
    'get_tag_template_output',
]

@pulumi.output_type
class GetTagTemplateResult:
    def __init__(__self__, display_name=None, fields=None, is_publicly_readable=None, name=None):
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if fields and not isinstance(fields, dict):
            raise TypeError("Expected argument 'fields' to be a dict")
        pulumi.set(__self__, "fields", fields)
        if is_publicly_readable and not isinstance(is_publicly_readable, bool):
            raise TypeError("Expected argument 'is_publicly_readable' to be a bool")
        pulumi.set(__self__, "is_publicly_readable", is_publicly_readable)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Display name for this template. Defaults to an empty string. The name must contain only Unicode letters, numbers (0-9), underscores (_), dashes (-), spaces ( ), and can't start or end with spaces. The maximum length is 200 characters.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def fields(self) -> Mapping[str, 'outputs.GoogleCloudDatacatalogV1TagTemplateFieldResponse']:
        """
        Map of tag template field IDs to the settings for the field. This map is an exhaustive list of the allowed fields. The map must contain at least one field and at most 500 fields. The keys to this map are tag template field IDs. The IDs have the following limitations: * Can contain uppercase and lowercase letters, numbers (0-9) and underscores (_). * Must be at least 1 character and at most 64 characters long. * Must start with a letter or underscore.
        """
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter(name="isPubliclyReadable")
    def is_publicly_readable(self) -> bool:
        """
        Indicates whether tags created with this template are public. Public tags do not require tag template access to appear in ListTags API response. Additionally, you can search for a public tag by value with a simple search query in addition to using a ``tag:`` predicate.
        """
        return pulumi.get(self, "is_publicly_readable")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the tag template in URL format. Note: The tag template itself and its child resources might not be stored in the location specified in its name.
        """
        return pulumi.get(self, "name")


class AwaitableGetTagTemplateResult(GetTagTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTagTemplateResult(
            display_name=self.display_name,
            fields=self.fields,
            is_publicly_readable=self.is_publicly_readable,
            name=self.name)


def get_tag_template(location: Optional[str] = None,
                     project: Optional[str] = None,
                     tag_template_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTagTemplateResult:
    """
    Gets a tag template.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    __args__['tagTemplateId'] = tag_template_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('google-native:datacatalog/v1:getTagTemplate', __args__, opts=opts, typ=GetTagTemplateResult).value

    return AwaitableGetTagTemplateResult(
        display_name=pulumi.get(__ret__, 'display_name'),
        fields=pulumi.get(__ret__, 'fields'),
        is_publicly_readable=pulumi.get(__ret__, 'is_publicly_readable'),
        name=pulumi.get(__ret__, 'name'))


@_utilities.lift_output_func(get_tag_template)
def get_tag_template_output(location: Optional[pulumi.Input[str]] = None,
                            project: Optional[pulumi.Input[Optional[str]]] = None,
                            tag_template_id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTagTemplateResult]:
    """
    Gets a tag template.
    """
    ...
