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
from argo_workflows.models.backoff import Backoff
from argo_workflows.models.event_source_filter import EventSourceFilter
from argo_workflows.models.nats_auth import NATSAuth
from argo_workflows.models.tls_config import TLSConfig
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class NATSEventsSource(BaseModel):
    """
    NATSEventsSource
    """ # noqa: E501
    auth: Optional[NATSAuth] = None
    connection_backoff: Optional[Backoff] = Field(default=None, alias="connectionBackoff")
    filter: Optional[EventSourceFilter] = None
    json_body: Optional[StrictBool] = Field(default=None, alias="jsonBody")
    metadata: Optional[Dict[str, StrictStr]] = None
    subject: Optional[StrictStr] = None
    tls: Optional[TLSConfig] = None
    url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["auth", "connectionBackoff", "filter", "jsonBody", "metadata", "subject", "tls", "url"]

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
        """Create an instance of NATSEventsSource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of auth
        if self.auth:
            _dict['auth'] = self.auth.to_dict()
        # override the default output from pydantic by calling `to_dict()` of connection_backoff
        if self.connection_backoff:
            _dict['connectionBackoff'] = self.connection_backoff.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tls
        if self.tls:
            _dict['tls'] = self.tls.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of NATSEventsSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "auth": NATSAuth.from_dict(obj.get("auth")) if obj.get("auth") is not None else None,
            "connectionBackoff": Backoff.from_dict(obj.get("connectionBackoff")) if obj.get("connectionBackoff") is not None else None,
            "filter": EventSourceFilter.from_dict(obj.get("filter")) if obj.get("filter") is not None else None,
            "jsonBody": obj.get("jsonBody"),
            "metadata": obj.get("metadata"),
            "subject": obj.get("subject"),
            "tls": TLSConfig.from_dict(obj.get("tls")) if obj.get("tls") is not None else None,
            "url": obj.get("url")
        })
        return _obj


