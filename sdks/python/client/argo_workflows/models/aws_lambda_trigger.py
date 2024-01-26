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
from argo_workflows.models.trigger_parameter import TriggerParameter
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AWSLambdaTrigger(BaseModel):
    """
    AWSLambdaTrigger
    """ # noqa: E501
    access_key: Optional[SecretKeySelector] = Field(default=None, alias="accessKey")
    function_name: Optional[StrictStr] = Field(default=None, description="FunctionName refers to the name of the function to invoke.", alias="functionName")
    invocation_type: Optional[StrictStr] = Field(default=None, description="Choose from the following options.     * RequestResponse (default) - Invoke the function synchronously. Keep    the connection open until the function returns a response or times out.    The API response includes the function response and additional data.     * Event - Invoke the function asynchronously. Send events that fail multiple    times to the function's dead-letter queue (if it's configured). The API    response only includes a status code.     * DryRun - Validate parameter values and verify that the user or role    has permission to invoke the function. +optional", alias="invocationType")
    parameters: Optional[List[TriggerParameter]] = None
    payload: Optional[List[TriggerParameter]] = Field(default=None, description="Payload is the list of key-value extracted from an event payload to construct the request payload.")
    region: Optional[StrictStr] = None
    role_arn: Optional[StrictStr] = Field(default=None, alias="roleARN")
    secret_key: Optional[SecretKeySelector] = Field(default=None, alias="secretKey")
    __properties: ClassVar[List[str]] = ["accessKey", "functionName", "invocationType", "parameters", "payload", "region", "roleARN", "secretKey"]

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
        """Create an instance of AWSLambdaTrigger from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of access_key
        if self.access_key:
            _dict['accessKey'] = self.access_key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in parameters (list)
        _items = []
        if self.parameters:
            for _item in self.parameters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parameters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in payload (list)
        _items = []
        if self.payload:
            for _item in self.payload:
                if _item:
                    _items.append(_item.to_dict())
            _dict['payload'] = _items
        # override the default output from pydantic by calling `to_dict()` of secret_key
        if self.secret_key:
            _dict['secretKey'] = self.secret_key.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AWSLambdaTrigger from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessKey": SecretKeySelector.from_dict(obj.get("accessKey")) if obj.get("accessKey") is not None else None,
            "functionName": obj.get("functionName"),
            "invocationType": obj.get("invocationType"),
            "parameters": [TriggerParameter.from_dict(_item) for _item in obj.get("parameters")] if obj.get("parameters") is not None else None,
            "payload": [TriggerParameter.from_dict(_item) for _item in obj.get("payload")] if obj.get("payload") is not None else None,
            "region": obj.get("region"),
            "roleARN": obj.get("roleARN"),
            "secretKey": SecretKeySelector.from_dict(obj.get("secretKey")) if obj.get("secretKey") is not None else None
        })
        return _obj


