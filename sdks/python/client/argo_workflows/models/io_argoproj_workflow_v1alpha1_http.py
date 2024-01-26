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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from argo_workflows.models.io_argoproj_workflow_v1alpha1_http_body_source import IoArgoprojWorkflowV1alpha1HTTPBodySource
from argo_workflows.models.io_argoproj_workflow_v1alpha1_http_header import IoArgoprojWorkflowV1alpha1HTTPHeader
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IoArgoprojWorkflowV1alpha1HTTP(BaseModel):
    """
    IoArgoprojWorkflowV1alpha1HTTP
    """ # noqa: E501
    body: Optional[StrictStr] = Field(default=None, description="Body is content of the HTTP Request")
    body_from: Optional[IoArgoprojWorkflowV1alpha1HTTPBodySource] = Field(default=None, alias="bodyFrom")
    headers: Optional[List[IoArgoprojWorkflowV1alpha1HTTPHeader]] = Field(default=None, description="Headers are an optional list of headers to send with HTTP requests")
    insecure_skip_verify: Optional[StrictBool] = Field(default=None, description="InsecureSkipVerify is a bool when if set to true will skip TLS verification for the HTTP client", alias="insecureSkipVerify")
    method: Optional[StrictStr] = Field(default=None, description="Method is HTTP methods for HTTP Request")
    success_condition: Optional[StrictStr] = Field(default=None, description="SuccessCondition is an expression if evaluated to true is considered successful", alias="successCondition")
    timeout_seconds: Optional[StrictInt] = Field(default=None, description="TimeoutSeconds is request timeout for HTTP Request. Default is 30 seconds", alias="timeoutSeconds")
    url: StrictStr = Field(description="URL of the HTTP Request")
    __properties: ClassVar[List[str]] = ["body", "bodyFrom", "headers", "insecureSkipVerify", "method", "successCondition", "timeoutSeconds", "url"]

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
        """Create an instance of IoArgoprojWorkflowV1alpha1HTTP from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of body_from
        if self.body_from:
            _dict['bodyFrom'] = self.body_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in headers (list)
        _items = []
        if self.headers:
            for _item in self.headers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['headers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IoArgoprojWorkflowV1alpha1HTTP from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "body": obj.get("body"),
            "bodyFrom": IoArgoprojWorkflowV1alpha1HTTPBodySource.from_dict(obj.get("bodyFrom")) if obj.get("bodyFrom") is not None else None,
            "headers": [IoArgoprojWorkflowV1alpha1HTTPHeader.from_dict(_item) for _item in obj.get("headers")] if obj.get("headers") is not None else None,
            "insecureSkipVerify": obj.get("insecureSkipVerify"),
            "method": obj.get("method"),
            "successCondition": obj.get("successCondition"),
            "timeoutSeconds": obj.get("timeoutSeconds"),
            "url": obj.get("url")
        })
        return _obj


