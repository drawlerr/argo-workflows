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
from argo_workflows.models.io_argoproj_events_v1alpha1_event_source_filter import IoArgoprojEventsV1alpha1EventSourceFilter
from argo_workflows.models.io_argoproj_events_v1alpha1_webhook_context import IoArgoprojEventsV1alpha1WebhookContext
from argo_workflows.models.secret_key_selector import SecretKeySelector
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IoArgoprojEventsV1alpha1SlackEventSource(BaseModel):
    """
    IoArgoprojEventsV1alpha1SlackEventSource
    """ # noqa: E501
    filter: Optional[IoArgoprojEventsV1alpha1EventSourceFilter] = None
    metadata: Optional[Dict[str, StrictStr]] = None
    signing_secret: Optional[SecretKeySelector] = Field(default=None, alias="signingSecret")
    token: Optional[SecretKeySelector] = None
    webhook: Optional[IoArgoprojEventsV1alpha1WebhookContext] = None
    __properties: ClassVar[List[str]] = ["filter", "metadata", "signingSecret", "token", "webhook"]

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
        """Create an instance of IoArgoprojEventsV1alpha1SlackEventSource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of signing_secret
        if self.signing_secret:
            _dict['signingSecret'] = self.signing_secret.to_dict()
        # override the default output from pydantic by calling `to_dict()` of token
        if self.token:
            _dict['token'] = self.token.to_dict()
        # override the default output from pydantic by calling `to_dict()` of webhook
        if self.webhook:
            _dict['webhook'] = self.webhook.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IoArgoprojEventsV1alpha1SlackEventSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "filter": IoArgoprojEventsV1alpha1EventSourceFilter.from_dict(obj.get("filter")) if obj.get("filter") is not None else None,
            "metadata": obj.get("metadata"),
            "signingSecret": SecretKeySelector.from_dict(obj.get("signingSecret")) if obj.get("signingSecret") is not None else None,
            "token": SecretKeySelector.from_dict(obj.get("token")) if obj.get("token") is not None else None,
            "webhook": IoArgoprojEventsV1alpha1WebhookContext.from_dict(obj.get("webhook")) if obj.get("webhook") is not None else None
        })
        return _obj


