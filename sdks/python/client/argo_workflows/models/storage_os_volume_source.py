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
from argo_workflows.models.local_object_reference import LocalObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class StorageOSVolumeSource(BaseModel):
    """
    Represents a StorageOS persistent volume resource.
    """ # noqa: E501
    fs_type: Optional[StrictStr] = Field(default=None, description="Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.", alias="fsType")
    read_only: Optional[StrictBool] = Field(default=None, description="Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.", alias="readOnly")
    secret_ref: Optional[LocalObjectReference] = Field(default=None, alias="secretRef")
    volume_name: Optional[StrictStr] = Field(default=None, description="VolumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.", alias="volumeName")
    volume_namespace: Optional[StrictStr] = Field(default=None, description="VolumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to \"default\" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.", alias="volumeNamespace")
    __properties: ClassVar[List[str]] = ["fsType", "readOnly", "secretRef", "volumeName", "volumeNamespace"]

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
        """Create an instance of StorageOSVolumeSource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of secret_ref
        if self.secret_ref:
            _dict['secretRef'] = self.secret_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of StorageOSVolumeSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fsType": obj.get("fsType"),
            "readOnly": obj.get("readOnly"),
            "secretRef": LocalObjectReference.from_dict(obj.get("secretRef")) if obj.get("secretRef") is not None else None,
            "volumeName": obj.get("volumeName"),
            "volumeNamespace": obj.get("volumeNamespace")
        })
        return _obj


