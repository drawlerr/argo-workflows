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

class ScaleIOVolumeSource(BaseModel):
    """
    ScaleIOVolumeSource represents a persistent ScaleIO volume
    """ # noqa: E501
    fs_type: Optional[StrictStr] = Field(default=None, description="Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Default is \"xfs\".", alias="fsType")
    gateway: StrictStr = Field(description="The host address of the ScaleIO API Gateway.")
    protection_domain: Optional[StrictStr] = Field(default=None, description="The name of the ScaleIO Protection Domain for the configured storage.", alias="protectionDomain")
    read_only: Optional[StrictBool] = Field(default=None, description="Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.", alias="readOnly")
    secret_ref: LocalObjectReference = Field(alias="secretRef")
    ssl_enabled: Optional[StrictBool] = Field(default=None, description="Flag to enable/disable SSL communication with Gateway, default false", alias="sslEnabled")
    storage_mode: Optional[StrictStr] = Field(default=None, description="Indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.", alias="storageMode")
    storage_pool: Optional[StrictStr] = Field(default=None, description="The ScaleIO Storage Pool associated with the protection domain.", alias="storagePool")
    system: StrictStr = Field(description="The name of the storage system as configured in ScaleIO.")
    volume_name: Optional[StrictStr] = Field(default=None, description="The name of a volume already created in the ScaleIO system that is associated with this volume source.", alias="volumeName")
    __properties: ClassVar[List[str]] = ["fsType", "gateway", "protectionDomain", "readOnly", "secretRef", "sslEnabled", "storageMode", "storagePool", "system", "volumeName"]

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
        """Create an instance of ScaleIOVolumeSource from a JSON string"""
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
        """Create an instance of ScaleIOVolumeSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fsType": obj.get("fsType"),
            "gateway": obj.get("gateway"),
            "protectionDomain": obj.get("protectionDomain"),
            "readOnly": obj.get("readOnly"),
            "secretRef": LocalObjectReference.from_dict(obj.get("secretRef")) if obj.get("secretRef") is not None else None,
            "sslEnabled": obj.get("sslEnabled"),
            "storageMode": obj.get("storageMode"),
            "storagePool": obj.get("storagePool"),
            "system": obj.get("system"),
            "volumeName": obj.get("volumeName")
        })
        return _obj


