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

__all__ = ['RepositoryArgs', 'Repository']

@pulumi.input_type
class RepositoryArgs:
    def __init__(__self__, *,
                 repository_id: pulumi.Input[str],
                 cleanup_policies: Optional[pulumi.Input[Mapping[str, pulumi.Input['CleanupPolicyArgs']]]] = None,
                 cleanup_policy_dry_run: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 docker_config: Optional[pulumi.Input['DockerRepositoryConfigArgs']] = None,
                 format: Optional[pulumi.Input['RepositoryFormat']] = None,
                 kms_key_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maven_config: Optional[pulumi.Input['MavenRepositoryConfigArgs']] = None,
                 mode: Optional[pulumi.Input['RepositoryMode']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 remote_repository_config: Optional[pulumi.Input['RemoteRepositoryConfigArgs']] = None,
                 virtual_repository_config: Optional[pulumi.Input['VirtualRepositoryConfigArgs']] = None):
        """
        The set of arguments for constructing a Repository resource.
        :param pulumi.Input[str] repository_id: Required. The repository id to use for this repository.
        :param pulumi.Input[Mapping[str, pulumi.Input['CleanupPolicyArgs']]] cleanup_policies: Optional. Cleanup policies for this repository. Cleanup policies indicate when certain package versions can be automatically deleted. Map keys are policy IDs supplied by users during policy creation. They must unique within a repository and be under 128 characters in length.
        :param pulumi.Input[bool] cleanup_policy_dry_run: Optional. If true, the cleanup pipeline is prevented from deleting versions in this repository.
        :param pulumi.Input[str] description: The user-provided description of the repository.
        :param pulumi.Input['DockerRepositoryConfigArgs'] docker_config: Docker repository config contains repository level configuration for the repositories of docker type.
        :param pulumi.Input['RepositoryFormat'] format: Optional. The format of packages that are stored in the repository.
        :param pulumi.Input[str] kms_key_name: The Cloud KMS resource name of the customer managed encryption key that's used to encrypt the contents of the Repository. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. This value may not be changed after the Repository has been created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels with user-defined metadata. This field may contain up to 64 entries. Label keys and values may be no longer than 63 characters. Label keys must begin with a lowercase letter and may only contain lowercase letters, numeric characters, underscores, and dashes.
        :param pulumi.Input['MavenRepositoryConfigArgs'] maven_config: Maven repository config contains repository level configuration for the repositories of maven type.
        :param pulumi.Input['RepositoryMode'] mode: Optional. The mode of the repository.
        :param pulumi.Input[str] name: The name of the repository, for example: `projects/p1/locations/us-central1/repositories/repo1`.
        :param pulumi.Input['RemoteRepositoryConfigArgs'] remote_repository_config: Configuration specific for a Remote Repository.
        :param pulumi.Input['VirtualRepositoryConfigArgs'] virtual_repository_config: Configuration specific for a Virtual Repository.
        """
        pulumi.set(__self__, "repository_id", repository_id)
        if cleanup_policies is not None:
            pulumi.set(__self__, "cleanup_policies", cleanup_policies)
        if cleanup_policy_dry_run is not None:
            pulumi.set(__self__, "cleanup_policy_dry_run", cleanup_policy_dry_run)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if docker_config is not None:
            pulumi.set(__self__, "docker_config", docker_config)
        if format is not None:
            pulumi.set(__self__, "format", format)
        if kms_key_name is not None:
            pulumi.set(__self__, "kms_key_name", kms_key_name)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if maven_config is not None:
            pulumi.set(__self__, "maven_config", maven_config)
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if remote_repository_config is not None:
            pulumi.set(__self__, "remote_repository_config", remote_repository_config)
        if virtual_repository_config is not None:
            pulumi.set(__self__, "virtual_repository_config", virtual_repository_config)

    @property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> pulumi.Input[str]:
        """
        Required. The repository id to use for this repository.
        """
        return pulumi.get(self, "repository_id")

    @repository_id.setter
    def repository_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "repository_id", value)

    @property
    @pulumi.getter(name="cleanupPolicies")
    def cleanup_policies(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['CleanupPolicyArgs']]]]:
        """
        Optional. Cleanup policies for this repository. Cleanup policies indicate when certain package versions can be automatically deleted. Map keys are policy IDs supplied by users during policy creation. They must unique within a repository and be under 128 characters in length.
        """
        return pulumi.get(self, "cleanup_policies")

    @cleanup_policies.setter
    def cleanup_policies(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['CleanupPolicyArgs']]]]):
        pulumi.set(self, "cleanup_policies", value)

    @property
    @pulumi.getter(name="cleanupPolicyDryRun")
    def cleanup_policy_dry_run(self) -> Optional[pulumi.Input[bool]]:
        """
        Optional. If true, the cleanup pipeline is prevented from deleting versions in this repository.
        """
        return pulumi.get(self, "cleanup_policy_dry_run")

    @cleanup_policy_dry_run.setter
    def cleanup_policy_dry_run(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "cleanup_policy_dry_run", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The user-provided description of the repository.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="dockerConfig")
    def docker_config(self) -> Optional[pulumi.Input['DockerRepositoryConfigArgs']]:
        """
        Docker repository config contains repository level configuration for the repositories of docker type.
        """
        return pulumi.get(self, "docker_config")

    @docker_config.setter
    def docker_config(self, value: Optional[pulumi.Input['DockerRepositoryConfigArgs']]):
        pulumi.set(self, "docker_config", value)

    @property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input['RepositoryFormat']]:
        """
        Optional. The format of packages that are stored in the repository.
        """
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: Optional[pulumi.Input['RepositoryFormat']]):
        pulumi.set(self, "format", value)

    @property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Cloud KMS resource name of the customer managed encryption key that's used to encrypt the contents of the Repository. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. This value may not be changed after the Repository has been created.
        """
        return pulumi.get(self, "kms_key_name")

    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_name", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Labels with user-defined metadata. This field may contain up to 64 entries. Label keys and values may be no longer than 63 characters. Label keys must begin with a lowercase letter and may only contain lowercase letters, numeric characters, underscores, and dashes.
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
    @pulumi.getter(name="mavenConfig")
    def maven_config(self) -> Optional[pulumi.Input['MavenRepositoryConfigArgs']]:
        """
        Maven repository config contains repository level configuration for the repositories of maven type.
        """
        return pulumi.get(self, "maven_config")

    @maven_config.setter
    def maven_config(self, value: Optional[pulumi.Input['MavenRepositoryConfigArgs']]):
        pulumi.set(self, "maven_config", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input['RepositoryMode']]:
        """
        Optional. The mode of the repository.
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input['RepositoryMode']]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the repository, for example: `projects/p1/locations/us-central1/repositories/repo1`.
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
    @pulumi.getter(name="remoteRepositoryConfig")
    def remote_repository_config(self) -> Optional[pulumi.Input['RemoteRepositoryConfigArgs']]:
        """
        Configuration specific for a Remote Repository.
        """
        return pulumi.get(self, "remote_repository_config")

    @remote_repository_config.setter
    def remote_repository_config(self, value: Optional[pulumi.Input['RemoteRepositoryConfigArgs']]):
        pulumi.set(self, "remote_repository_config", value)

    @property
    @pulumi.getter(name="virtualRepositoryConfig")
    def virtual_repository_config(self) -> Optional[pulumi.Input['VirtualRepositoryConfigArgs']]:
        """
        Configuration specific for a Virtual Repository.
        """
        return pulumi.get(self, "virtual_repository_config")

    @virtual_repository_config.setter
    def virtual_repository_config(self, value: Optional[pulumi.Input['VirtualRepositoryConfigArgs']]):
        pulumi.set(self, "virtual_repository_config", value)


class Repository(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cleanup_policies: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['CleanupPolicyArgs']]]]] = None,
                 cleanup_policy_dry_run: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 docker_config: Optional[pulumi.Input[pulumi.InputType['DockerRepositoryConfigArgs']]] = None,
                 format: Optional[pulumi.Input['RepositoryFormat']] = None,
                 kms_key_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maven_config: Optional[pulumi.Input[pulumi.InputType['MavenRepositoryConfigArgs']]] = None,
                 mode: Optional[pulumi.Input['RepositoryMode']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 remote_repository_config: Optional[pulumi.Input[pulumi.InputType['RemoteRepositoryConfigArgs']]] = None,
                 repository_id: Optional[pulumi.Input[str]] = None,
                 virtual_repository_config: Optional[pulumi.Input[pulumi.InputType['VirtualRepositoryConfigArgs']]] = None,
                 __props__=None):
        """
        Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['CleanupPolicyArgs']]]] cleanup_policies: Optional. Cleanup policies for this repository. Cleanup policies indicate when certain package versions can be automatically deleted. Map keys are policy IDs supplied by users during policy creation. They must unique within a repository and be under 128 characters in length.
        :param pulumi.Input[bool] cleanup_policy_dry_run: Optional. If true, the cleanup pipeline is prevented from deleting versions in this repository.
        :param pulumi.Input[str] description: The user-provided description of the repository.
        :param pulumi.Input[pulumi.InputType['DockerRepositoryConfigArgs']] docker_config: Docker repository config contains repository level configuration for the repositories of docker type.
        :param pulumi.Input['RepositoryFormat'] format: Optional. The format of packages that are stored in the repository.
        :param pulumi.Input[str] kms_key_name: The Cloud KMS resource name of the customer managed encryption key that's used to encrypt the contents of the Repository. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. This value may not be changed after the Repository has been created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels with user-defined metadata. This field may contain up to 64 entries. Label keys and values may be no longer than 63 characters. Label keys must begin with a lowercase letter and may only contain lowercase letters, numeric characters, underscores, and dashes.
        :param pulumi.Input[pulumi.InputType['MavenRepositoryConfigArgs']] maven_config: Maven repository config contains repository level configuration for the repositories of maven type.
        :param pulumi.Input['RepositoryMode'] mode: Optional. The mode of the repository.
        :param pulumi.Input[str] name: The name of the repository, for example: `projects/p1/locations/us-central1/repositories/repo1`.
        :param pulumi.Input[pulumi.InputType['RemoteRepositoryConfigArgs']] remote_repository_config: Configuration specific for a Remote Repository.
        :param pulumi.Input[str] repository_id: Required. The repository id to use for this repository.
        :param pulumi.Input[pulumi.InputType['VirtualRepositoryConfigArgs']] virtual_repository_config: Configuration specific for a Virtual Repository.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RepositoryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository.

        :param str resource_name: The name of the resource.
        :param RepositoryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RepositoryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cleanup_policies: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['CleanupPolicyArgs']]]]] = None,
                 cleanup_policy_dry_run: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 docker_config: Optional[pulumi.Input[pulumi.InputType['DockerRepositoryConfigArgs']]] = None,
                 format: Optional[pulumi.Input['RepositoryFormat']] = None,
                 kms_key_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maven_config: Optional[pulumi.Input[pulumi.InputType['MavenRepositoryConfigArgs']]] = None,
                 mode: Optional[pulumi.Input['RepositoryMode']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 remote_repository_config: Optional[pulumi.Input[pulumi.InputType['RemoteRepositoryConfigArgs']]] = None,
                 repository_id: Optional[pulumi.Input[str]] = None,
                 virtual_repository_config: Optional[pulumi.Input[pulumi.InputType['VirtualRepositoryConfigArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RepositoryArgs.__new__(RepositoryArgs)

            __props__.__dict__["cleanup_policies"] = cleanup_policies
            __props__.__dict__["cleanup_policy_dry_run"] = cleanup_policy_dry_run
            __props__.__dict__["description"] = description
            __props__.__dict__["docker_config"] = docker_config
            __props__.__dict__["format"] = format
            __props__.__dict__["kms_key_name"] = kms_key_name
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["maven_config"] = maven_config
            __props__.__dict__["mode"] = mode
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["remote_repository_config"] = remote_repository_config
            if repository_id is None and not opts.urn:
                raise TypeError("Missing required property 'repository_id'")
            __props__.__dict__["repository_id"] = repository_id
            __props__.__dict__["virtual_repository_config"] = virtual_repository_config
            __props__.__dict__["create_time"] = None
            __props__.__dict__["satisfies_pzs"] = None
            __props__.__dict__["size_bytes"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["location", "project", "repositoryId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Repository, __self__).__init__(
            'google-native:artifactregistry/v1:Repository',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Repository':
        """
        Get an existing Repository resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RepositoryArgs.__new__(RepositoryArgs)

        __props__.__dict__["cleanup_policies"] = None
        __props__.__dict__["cleanup_policy_dry_run"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["docker_config"] = None
        __props__.__dict__["format"] = None
        __props__.__dict__["kms_key_name"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["maven_config"] = None
        __props__.__dict__["mode"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["remote_repository_config"] = None
        __props__.__dict__["repository_id"] = None
        __props__.__dict__["satisfies_pzs"] = None
        __props__.__dict__["size_bytes"] = None
        __props__.__dict__["update_time"] = None
        __props__.__dict__["virtual_repository_config"] = None
        return Repository(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cleanupPolicies")
    def cleanup_policies(self) -> pulumi.Output[Mapping[str, 'outputs.CleanupPolicyResponse']]:
        """
        Optional. Cleanup policies for this repository. Cleanup policies indicate when certain package versions can be automatically deleted. Map keys are policy IDs supplied by users during policy creation. They must unique within a repository and be under 128 characters in length.
        """
        return pulumi.get(self, "cleanup_policies")

    @property
    @pulumi.getter(name="cleanupPolicyDryRun")
    def cleanup_policy_dry_run(self) -> pulumi.Output[bool]:
        """
        Optional. If true, the cleanup pipeline is prevented from deleting versions in this repository.
        """
        return pulumi.get(self, "cleanup_policy_dry_run")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time when the repository was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The user-provided description of the repository.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dockerConfig")
    def docker_config(self) -> pulumi.Output['outputs.DockerRepositoryConfigResponse']:
        """
        Docker repository config contains repository level configuration for the repositories of docker type.
        """
        return pulumi.get(self, "docker_config")

    @property
    @pulumi.getter
    def format(self) -> pulumi.Output[str]:
        """
        Optional. The format of packages that are stored in the repository.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Output[str]:
        """
        The Cloud KMS resource name of the customer managed encryption key that's used to encrypt the contents of the Repository. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. This value may not be changed after the Repository has been created.
        """
        return pulumi.get(self, "kms_key_name")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Labels with user-defined metadata. This field may contain up to 64 entries. Label keys and values may be no longer than 63 characters. Label keys must begin with a lowercase letter and may only contain lowercase letters, numeric characters, underscores, and dashes.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mavenConfig")
    def maven_config(self) -> pulumi.Output['outputs.MavenRepositoryConfigResponse']:
        """
        Maven repository config contains repository level configuration for the repositories of maven type.
        """
        return pulumi.get(self, "maven_config")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[str]:
        """
        Optional. The mode of the repository.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the repository, for example: `projects/p1/locations/us-central1/repositories/repo1`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="remoteRepositoryConfig")
    def remote_repository_config(self) -> pulumi.Output['outputs.RemoteRepositoryConfigResponse']:
        """
        Configuration specific for a Remote Repository.
        """
        return pulumi.get(self, "remote_repository_config")

    @property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> pulumi.Output[str]:
        """
        Required. The repository id to use for this repository.
        """
        return pulumi.get(self, "repository_id")

    @property
    @pulumi.getter(name="satisfiesPzs")
    def satisfies_pzs(self) -> pulumi.Output[bool]:
        """
        If set, the repository satisfies physical zone separation.
        """
        return pulumi.get(self, "satisfies_pzs")

    @property
    @pulumi.getter(name="sizeBytes")
    def size_bytes(self) -> pulumi.Output[str]:
        """
        The size, in bytes, of all artifact storage in this repository. Repositories that are generally available or in public preview use this to calculate storage costs.
        """
        return pulumi.get(self, "size_bytes")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The time when the repository was last updated.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="virtualRepositoryConfig")
    def virtual_repository_config(self) -> pulumi.Output['outputs.VirtualRepositoryConfigResponse']:
        """
        Configuration specific for a Virtual Repository.
        """
        return pulumi.get(self, "virtual_repository_config")

