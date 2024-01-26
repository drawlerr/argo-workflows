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
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Toleration(BaseModel):
    """
    The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.
    """ # noqa: E501
    effect: Optional[StrictStr] = Field(default=None, description="Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.  Possible enum values:  - `\"NoExecute\"` Evict any already-running pods that do not tolerate the taint. Currently enforced by NodeController.  - `\"NoSchedule\"` Do not allow new pods to schedule onto the node unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. Enforced by the scheduler.  - `\"PreferNoSchedule\"` Like TaintEffectNoSchedule, but the scheduler tries not to schedule new pods onto the node, rather than prohibiting new pods from scheduling onto the node entirely. Enforced by the scheduler.")
    key: Optional[StrictStr] = Field(default=None, description="Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.")
    operator: Optional[StrictStr] = Field(default=None, description="Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.  Possible enum values:  - `\"Equal\"`  - `\"Exists\"`")
    toleration_seconds: Optional[StrictInt] = Field(default=None, description="TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.", alias="tolerationSeconds")
    value: Optional[StrictStr] = Field(default=None, description="Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.")
    __properties: ClassVar[List[str]] = ["effect", "key", "operator", "tolerationSeconds", "value"]

    @field_validator('effect')
    def effect_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NoExecute', 'NoSchedule', 'PreferNoSchedule'):
            raise ValueError("must be one of enum values ('NoExecute', 'NoSchedule', 'PreferNoSchedule')")
        return value

    @field_validator('operator')
    def operator_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Equal', 'Exists'):
            raise ValueError("must be one of enum values ('Equal', 'Exists')")
        return value

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
        """Create an instance of Toleration from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Toleration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "effect": obj.get("effect"),
            "key": obj.get("key"),
            "operator": obj.get("operator"),
            "tolerationSeconds": obj.get("tolerationSeconds"),
            "value": obj.get("value")
        })
        return _obj


