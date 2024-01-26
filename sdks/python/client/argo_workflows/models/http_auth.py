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
from argo_workflows.models.basic_auth import BasicAuth
from argo_workflows.models.client_cert_auth import ClientCertAuth
from argo_workflows.models.o_auth2_auth import OAuth2Auth
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HTTPAuth(BaseModel):
    """
    HTTPAuth
    """ # noqa: E501
    basic_auth: Optional[BasicAuth] = Field(default=None, alias="basicAuth")
    client_cert: Optional[ClientCertAuth] = Field(default=None, alias="clientCert")
    oauth2: Optional[OAuth2Auth] = None
    __properties: ClassVar[List[str]] = ["basicAuth", "clientCert", "oauth2"]

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
        """Create an instance of HTTPAuth from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of basic_auth
        if self.basic_auth:
            _dict['basicAuth'] = self.basic_auth.to_dict()
        # override the default output from pydantic by calling `to_dict()` of client_cert
        if self.client_cert:
            _dict['clientCert'] = self.client_cert.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oauth2
        if self.oauth2:
            _dict['oauth2'] = self.oauth2.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of HTTPAuth from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "basicAuth": BasicAuth.from_dict(obj.get("basicAuth")) if obj.get("basicAuth") is not None else None,
            "clientCert": ClientCertAuth.from_dict(obj.get("clientCert")) if obj.get("clientCert") is not None else None,
            "oauth2": OAuth2Auth.from_dict(obj.get("oauth2")) if obj.get("oauth2") is not None else None
        })
        return _obj


