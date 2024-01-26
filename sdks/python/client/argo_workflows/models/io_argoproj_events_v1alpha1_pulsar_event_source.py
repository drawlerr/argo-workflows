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
from argo_workflows.models.io_argoproj_events_v1alpha1_backoff import IoArgoprojEventsV1alpha1Backoff
from argo_workflows.models.io_argoproj_events_v1alpha1_event_source_filter import IoArgoprojEventsV1alpha1EventSourceFilter
from argo_workflows.models.io_argoproj_events_v1alpha1_tls_config import IoArgoprojEventsV1alpha1TLSConfig
from argo_workflows.models.secret_key_selector import SecretKeySelector
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IoArgoprojEventsV1alpha1PulsarEventSource(BaseModel):
    """
    IoArgoprojEventsV1alpha1PulsarEventSource
    """ # noqa: E501
    auth_token_secret: Optional[SecretKeySelector] = Field(default=None, alias="authTokenSecret")
    connection_backoff: Optional[IoArgoprojEventsV1alpha1Backoff] = Field(default=None, alias="connectionBackoff")
    filter: Optional[IoArgoprojEventsV1alpha1EventSourceFilter] = None
    json_body: Optional[StrictBool] = Field(default=None, alias="jsonBody")
    metadata: Optional[Dict[str, StrictStr]] = None
    tls: Optional[IoArgoprojEventsV1alpha1TLSConfig] = None
    tls_allow_insecure_connection: Optional[StrictBool] = Field(default=None, alias="tlsAllowInsecureConnection")
    tls_trust_certs_secret: Optional[SecretKeySelector] = Field(default=None, alias="tlsTrustCertsSecret")
    tls_validate_hostname: Optional[StrictBool] = Field(default=None, alias="tlsValidateHostname")
    topics: Optional[List[StrictStr]] = None
    type: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["authTokenSecret", "connectionBackoff", "filter", "jsonBody", "metadata", "tls", "tlsAllowInsecureConnection", "tlsTrustCertsSecret", "tlsValidateHostname", "topics", "type", "url"]

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
        """Create an instance of IoArgoprojEventsV1alpha1PulsarEventSource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of auth_token_secret
        if self.auth_token_secret:
            _dict['authTokenSecret'] = self.auth_token_secret.to_dict()
        # override the default output from pydantic by calling `to_dict()` of connection_backoff
        if self.connection_backoff:
            _dict['connectionBackoff'] = self.connection_backoff.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tls
        if self.tls:
            _dict['tls'] = self.tls.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tls_trust_certs_secret
        if self.tls_trust_certs_secret:
            _dict['tlsTrustCertsSecret'] = self.tls_trust_certs_secret.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IoArgoprojEventsV1alpha1PulsarEventSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authTokenSecret": SecretKeySelector.from_dict(obj.get("authTokenSecret")) if obj.get("authTokenSecret") is not None else None,
            "connectionBackoff": IoArgoprojEventsV1alpha1Backoff.from_dict(obj.get("connectionBackoff")) if obj.get("connectionBackoff") is not None else None,
            "filter": IoArgoprojEventsV1alpha1EventSourceFilter.from_dict(obj.get("filter")) if obj.get("filter") is not None else None,
            "jsonBody": obj.get("jsonBody"),
            "metadata": obj.get("metadata"),
            "tls": IoArgoprojEventsV1alpha1TLSConfig.from_dict(obj.get("tls")) if obj.get("tls") is not None else None,
            "tlsAllowInsecureConnection": obj.get("tlsAllowInsecureConnection"),
            "tlsTrustCertsSecret": SecretKeySelector.from_dict(obj.get("tlsTrustCertsSecret")) if obj.get("tlsTrustCertsSecret") is not None else None,
            "tlsValidateHostname": obj.get("tlsValidateHostname"),
            "topics": obj.get("topics"),
            "type": obj.get("type"),
            "url": obj.get("url")
        })
        return _obj


