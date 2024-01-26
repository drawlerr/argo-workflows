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
from argo_workflows.models.io_argoproj_events_v1alpha1_trigger_parameter import IoArgoprojEventsV1alpha1TriggerParameter
from argo_workflows.models.secret_key_selector import SecretKeySelector
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IoArgoprojEventsV1alpha1SlackTrigger(BaseModel):
    """
    SlackTrigger refers to the specification of the slack notification trigger.
    """ # noqa: E501
    channel: Optional[StrictStr] = None
    message: Optional[StrictStr] = None
    parameters: Optional[List[IoArgoprojEventsV1alpha1TriggerParameter]] = None
    slack_token: Optional[SecretKeySelector] = Field(default=None, alias="slackToken")
    __properties: ClassVar[List[str]] = ["channel", "message", "parameters", "slackToken"]

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
        """Create an instance of IoArgoprojEventsV1alpha1SlackTrigger from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in parameters (list)
        _items = []
        if self.parameters:
            for _item in self.parameters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parameters'] = _items
        # override the default output from pydantic by calling `to_dict()` of slack_token
        if self.slack_token:
            _dict['slackToken'] = self.slack_token.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IoArgoprojEventsV1alpha1SlackTrigger from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "channel": obj.get("channel"),
            "message": obj.get("message"),
            "parameters": [IoArgoprojEventsV1alpha1TriggerParameter.from_dict(_item) for _item in obj.get("parameters")] if obj.get("parameters") is not None else None,
            "slackToken": SecretKeySelector.from_dict(obj.get("slackToken")) if obj.get("slackToken") is not None else None
        })
        return _obj


