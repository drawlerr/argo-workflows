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
from argo_workflows.models.secret_key_selector import SecretKeySelector
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ArtifactoryArtifact(BaseModel):
    """
    ArtifactoryArtifact is the location of an artifactory artifact
    """ # noqa: E501
    password_secret: Optional[SecretKeySelector] = Field(default=None, alias="passwordSecret")
    url: StrictStr = Field(description="URL of the artifact")
    username_secret: Optional[SecretKeySelector] = Field(default=None, alias="usernameSecret")
    __properties: ClassVar[List[str]] = ["passwordSecret", "url", "usernameSecret"]

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
        """Create an instance of ArtifactoryArtifact from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of password_secret
        if self.password_secret:
            _dict['passwordSecret'] = self.password_secret.to_dict()
        # override the default output from pydantic by calling `to_dict()` of username_secret
        if self.username_secret:
            _dict['usernameSecret'] = self.username_secret.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ArtifactoryArtifact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "passwordSecret": SecretKeySelector.from_dict(obj.get("passwordSecret")) if obj.get("passwordSecret") is not None else None,
            "url": obj.get("url"),
            "usernameSecret": SecretKeySelector.from_dict(obj.get("usernameSecret")) if obj.get("usernameSecret") is not None else None
        })
        return _obj


