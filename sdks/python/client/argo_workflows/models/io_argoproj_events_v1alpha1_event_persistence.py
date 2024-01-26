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
from pydantic import BaseModel
from pydantic import Field
from argo_workflows.models.io_argoproj_events_v1alpha1_catchup_configuration import IoArgoprojEventsV1alpha1CatchupConfiguration
from argo_workflows.models.io_argoproj_events_v1alpha1_config_map_persistence import IoArgoprojEventsV1alpha1ConfigMapPersistence
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IoArgoprojEventsV1alpha1EventPersistence(BaseModel):
    """
    IoArgoprojEventsV1alpha1EventPersistence
    """ # noqa: E501
    catchup: Optional[IoArgoprojEventsV1alpha1CatchupConfiguration] = None
    config_map: Optional[IoArgoprojEventsV1alpha1ConfigMapPersistence] = Field(default=None, alias="configMap")
    __properties: ClassVar[List[str]] = ["catchup", "configMap"]

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
        """Create an instance of IoArgoprojEventsV1alpha1EventPersistence from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of catchup
        if self.catchup:
            _dict['catchup'] = self.catchup.to_dict()
        # override the default output from pydantic by calling `to_dict()` of config_map
        if self.config_map:
            _dict['configMap'] = self.config_map.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IoArgoprojEventsV1alpha1EventPersistence from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "catchup": IoArgoprojEventsV1alpha1CatchupConfiguration.from_dict(obj.get("catchup")) if obj.get("catchup") is not None else None,
            "configMap": IoArgoprojEventsV1alpha1ConfigMapPersistence.from_dict(obj.get("configMap")) if obj.get("configMap") is not None else None
        })
        return _obj


