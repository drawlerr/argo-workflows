# coding: utf-8

"""
    Argo Workflows API

    Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argo-workflows.readthedocs.io/en/latest/

    The version of the OpenAPI document: VERSION
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from argo_workflows.models.container_port import ContainerPort
from argo_workflows.models.env_from_source import EnvFromSource
from argo_workflows.models.env_var import EnvVar
from argo_workflows.models.lifecycle import Lifecycle
from argo_workflows.models.probe import Probe
from argo_workflows.models.resource_requirements import ResourceRequirements
from argo_workflows.models.security_context import SecurityContext
from argo_workflows.models.volume_device import VolumeDevice
from argo_workflows.models.volume_mount import VolumeMount
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UserContainer(BaseModel):
    """
    UserContainer is a container specified by a user.
    """ # noqa: E501
    args: Optional[List[StrictStr]] = Field(default=None, description="Arguments to the entrypoint. The container image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell")
    command: Optional[List[StrictStr]] = Field(default=None, description="Entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell")
    env: Optional[List[EnvVar]] = Field(default=None, description="List of environment variables to set in the container. Cannot be updated.")
    env_from: Optional[List[EnvFromSource]] = Field(default=None, description="List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.", alias="envFrom")
    image: Optional[StrictStr] = Field(default=None, description="Container image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.")
    image_pull_policy: Optional[StrictStr] = Field(default=None, description="Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images", alias="imagePullPolicy")
    lifecycle: Optional[Lifecycle] = None
    liveness_probe: Optional[Probe] = Field(default=None, alias="livenessProbe")
    mirror_volume_mounts: Optional[StrictBool] = Field(default=None, description="MirrorVolumeMounts will mount the same volumes specified in the main container to the container (including artifacts), at the same mountPaths. This enables dind daemon to partially see the same filesystem as the main container in order to use features such as docker volume binding", alias="mirrorVolumeMounts")
    name: StrictStr = Field(description="Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.")
    ports: Optional[List[ContainerPort]] = Field(default=None, description="List of ports to expose from the container. Exposing a port here gives the system additional information about the network connections a container uses, but is primarily informational. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default \"0.0.0.0\" address inside a container will be accessible from the network. Cannot be updated.")
    readiness_probe: Optional[Probe] = Field(default=None, alias="readinessProbe")
    resources: Optional[ResourceRequirements] = None
    security_context: Optional[SecurityContext] = Field(default=None, alias="securityContext")
    startup_probe: Optional[Probe] = Field(default=None, alias="startupProbe")
    stdin: Optional[StrictBool] = Field(default=None, description="Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.")
    stdin_once: Optional[StrictBool] = Field(default=None, description="Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false", alias="stdinOnce")
    termination_message_path: Optional[StrictStr] = Field(default=None, description="Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.", alias="terminationMessagePath")
    termination_message_policy: Optional[StrictStr] = Field(default=None, description="Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.", alias="terminationMessagePolicy")
    tty: Optional[StrictBool] = Field(default=None, description="Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.")
    volume_devices: Optional[List[VolumeDevice]] = Field(default=None, description="volumeDevices is the list of block devices to be used by the container.", alias="volumeDevices")
    volume_mounts: Optional[List[VolumeMount]] = Field(default=None, description="Pod volumes to mount into the container's filesystem. Cannot be updated.", alias="volumeMounts")
    working_dir: Optional[StrictStr] = Field(default=None, description="Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.", alias="workingDir")
    __properties: ClassVar[List[str]] = ["args", "command", "env", "envFrom", "image", "imagePullPolicy", "lifecycle", "livenessProbe", "mirrorVolumeMounts", "name", "ports", "readinessProbe", "resources", "securityContext", "startupProbe", "stdin", "stdinOnce", "terminationMessagePath", "terminationMessagePolicy", "tty", "volumeDevices", "volumeMounts", "workingDir"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UserContainer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in env (list)
        _items = []
        if self.env:
            for _item in self.env:
                if _item:
                    _items.append(_item.to_dict())
            _dict['env'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in env_from (list)
        _items = []
        if self.env_from:
            for _item in self.env_from:
                if _item:
                    _items.append(_item.to_dict())
            _dict['envFrom'] = _items
        # override the default output from pydantic by calling `to_dict()` of lifecycle
        if self.lifecycle:
            _dict['lifecycle'] = self.lifecycle.to_dict()
        # override the default output from pydantic by calling `to_dict()` of liveness_probe
        if self.liveness_probe:
            _dict['livenessProbe'] = self.liveness_probe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ports (list)
        _items = []
        if self.ports:
            for _item in self.ports:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ports'] = _items
        # override the default output from pydantic by calling `to_dict()` of readiness_probe
        if self.readiness_probe:
            _dict['readinessProbe'] = self.readiness_probe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resources
        if self.resources:
            _dict['resources'] = self.resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of security_context
        if self.security_context:
            _dict['securityContext'] = self.security_context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of startup_probe
        if self.startup_probe:
            _dict['startupProbe'] = self.startup_probe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in volume_devices (list)
        _items = []
        if self.volume_devices:
            for _item in self.volume_devices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['volumeDevices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in volume_mounts (list)
        _items = []
        if self.volume_mounts:
            for _item in self.volume_mounts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['volumeMounts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UserContainer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "args": obj.get("args"),
            "command": obj.get("command"),
            "env": [EnvVar.from_dict(_item) for _item in obj.get("env")] if obj.get("env") is not None else None,
            "envFrom": [EnvFromSource.from_dict(_item) for _item in obj.get("envFrom")] if obj.get("envFrom") is not None else None,
            "image": obj.get("image"),
            "imagePullPolicy": obj.get("imagePullPolicy"),
            "lifecycle": Lifecycle.from_dict(obj.get("lifecycle")) if obj.get("lifecycle") is not None else None,
            "livenessProbe": Probe.from_dict(obj.get("livenessProbe")) if obj.get("livenessProbe") is not None else None,
            "mirrorVolumeMounts": obj.get("mirrorVolumeMounts"),
            "name": obj.get("name"),
            "ports": [ContainerPort.from_dict(_item) for _item in obj.get("ports")] if obj.get("ports") is not None else None,
            "readinessProbe": Probe.from_dict(obj.get("readinessProbe")) if obj.get("readinessProbe") is not None else None,
            "resources": ResourceRequirements.from_dict(obj.get("resources")) if obj.get("resources") is not None else None,
            "securityContext": SecurityContext.from_dict(obj.get("securityContext")) if obj.get("securityContext") is not None else None,
            "startupProbe": Probe.from_dict(obj.get("startupProbe")) if obj.get("startupProbe") is not None else None,
            "stdin": obj.get("stdin"),
            "stdinOnce": obj.get("stdinOnce"),
            "terminationMessagePath": obj.get("terminationMessagePath"),
            "terminationMessagePolicy": obj.get("terminationMessagePolicy"),
            "tty": obj.get("tty"),
            "volumeDevices": [VolumeDevice.from_dict(_item) for _item in obj.get("volumeDevices")] if obj.get("volumeDevices") is not None else None,
            "volumeMounts": [VolumeMount.from_dict(_item) for _item in obj.get("volumeMounts")] if obj.get("volumeMounts") is not None else None,
            "workingDir": obj.get("workingDir")
        })
        return _obj


