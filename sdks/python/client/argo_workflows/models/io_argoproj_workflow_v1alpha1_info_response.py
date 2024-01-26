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
from argo_workflows.models.io_argoproj_workflow_v1alpha1_column import IoArgoprojWorkflowV1alpha1Column
from argo_workflows.models.io_argoproj_workflow_v1alpha1_link import IoArgoprojWorkflowV1alpha1Link
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IoArgoprojWorkflowV1alpha1InfoResponse(BaseModel):
    """
    IoArgoprojWorkflowV1alpha1InfoResponse
    """ # noqa: E501
    columns: Optional[List[IoArgoprojWorkflowV1alpha1Column]] = None
    links: Optional[List[IoArgoprojWorkflowV1alpha1Link]] = None
    managed_namespace: Optional[StrictStr] = Field(default=None, alias="managedNamespace")
    modals: Optional[Dict[str, StrictBool]] = None
    nav_color: Optional[StrictStr] = Field(default=None, alias="navColor")
    __properties: ClassVar[List[str]] = ["columns", "links", "managedNamespace", "modals", "navColor"]

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
        """Create an instance of IoArgoprojWorkflowV1alpha1InfoResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in columns (list)
        _items = []
        if self.columns:
            for _item in self.columns:
                if _item:
                    _items.append(_item.to_dict())
            _dict['columns'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IoArgoprojWorkflowV1alpha1InfoResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "columns": [IoArgoprojWorkflowV1alpha1Column.from_dict(_item) for _item in obj.get("columns")] if obj.get("columns") is not None else None,
            "links": [IoArgoprojWorkflowV1alpha1Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "managedNamespace": obj.get("managedNamespace"),
            "modals": obj.get("modals"),
            "navColor": obj.get("navColor")
        })
        return _obj


