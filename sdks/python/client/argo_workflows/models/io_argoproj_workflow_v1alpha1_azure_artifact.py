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
from argo_workflows.models.secret_key_selector import SecretKeySelector
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IoArgoprojWorkflowV1alpha1AzureArtifact(BaseModel):
    """
    AzureArtifact is the location of a an Azure Storage artifact
    """ # noqa: E501
    account_key_secret: Optional[SecretKeySelector] = Field(default=None, alias="accountKeySecret")
    blob: StrictStr = Field(description="Blob is the blob name (i.e., path) in the container where the artifact resides")
    container: StrictStr = Field(description="Container is the container where resources will be stored")
    endpoint: StrictStr = Field(description="Endpoint is the service url associated with an account. It is most likely \"https://<ACCOUNT_NAME>.blob.core.windows.net\"")
    use_sdk_creds: Optional[StrictBool] = Field(default=None, description="UseSDKCreds tells the driver to figure out credentials based on sdk defaults.", alias="useSDKCreds")
    __properties: ClassVar[List[str]] = ["accountKeySecret", "blob", "container", "endpoint", "useSDKCreds"]

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
        """Create an instance of IoArgoprojWorkflowV1alpha1AzureArtifact from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account_key_secret
        if self.account_key_secret:
            _dict['accountKeySecret'] = self.account_key_secret.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IoArgoprojWorkflowV1alpha1AzureArtifact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountKeySecret": SecretKeySelector.from_dict(obj.get("accountKeySecret")) if obj.get("accountKeySecret") is not None else None,
            "blob": obj.get("blob"),
            "container": obj.get("container"),
            "endpoint": obj.get("endpoint"),
            "useSDKCreds": obj.get("useSDKCreds")
        })
        return _obj


