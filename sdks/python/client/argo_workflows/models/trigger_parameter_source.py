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
from pydantic import BaseModel, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TriggerParameterSource(BaseModel):
    """
    TriggerParameterSource
    """ # noqa: E501
    context_key: Optional[StrictStr] = Field(default=None, description="ContextKey is the JSONPath of the event's (JSON decoded) context key ContextKey is a series of keys separated by a dot. A key may contain wildcard characters '*' and '?'. To access an array value use the index as the key. The dot and wildcard characters can be escaped with '\\\\'. See https://github.com/tidwall/gjson#path-syntax for more information on how to use this.", alias="contextKey")
    context_template: Optional[StrictStr] = Field(default=None, alias="contextTemplate")
    data_key: Optional[StrictStr] = Field(default=None, description="DataKey is the JSONPath of the event's (JSON decoded) data key DataKey is a series of keys separated by a dot. A key may contain wildcard characters '*' and '?'. To access an array value use the index as the key. The dot and wildcard characters can be escaped with '\\\\'. See https://github.com/tidwall/gjson#path-syntax for more information on how to use this.", alias="dataKey")
    data_template: Optional[StrictStr] = Field(default=None, alias="dataTemplate")
    dependency_name: Optional[StrictStr] = Field(default=None, description="DependencyName refers to the name of the dependency. The event which is stored for this dependency is used as payload for the parameterization. Make sure to refer to one of the dependencies you have defined under Dependencies list.", alias="dependencyName")
    value: Optional[StrictStr] = Field(default=None, description="Value is the default literal value to use for this parameter source This is only used if the DataKey is invalid. If the DataKey is invalid and this is not defined, this param source will produce an error.")
    __properties: ClassVar[List[str]] = ["contextKey", "contextTemplate", "dataKey", "dataTemplate", "dependencyName", "value"]

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
        """Create an instance of TriggerParameterSource from a JSON string"""
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
        """Create an instance of TriggerParameterSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contextKey": obj.get("contextKey"),
            "contextTemplate": obj.get("contextTemplate"),
            "dataKey": obj.get("dataKey"),
            "dataTemplate": obj.get("dataTemplate"),
            "dependencyName": obj.get("dependencyName"),
            "value": obj.get("value")
        })
        return _obj


