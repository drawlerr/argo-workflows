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
from argo_workflows.models.event_source_filter import EventSourceFilter
from argo_workflows.models.secret_key_selector import SecretKeySelector
from argo_workflows.models.webhook_context import WebhookContext
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GitlabEventSource(BaseModel):
    """
    GitlabEventSource
    """ # noqa: E501
    access_token: Optional[SecretKeySelector] = Field(default=None, alias="accessToken")
    delete_hook_on_finish: Optional[StrictBool] = Field(default=None, alias="deleteHookOnFinish")
    enable_ssl_verification: Optional[StrictBool] = Field(default=None, alias="enableSSLVerification")
    events: Optional[List[StrictStr]] = Field(default=None, description="Events are gitlab event to listen to. Refer https://github.com/xanzy/go-gitlab/blob/bf34eca5d13a9f4c3f501d8a97b8ac226d55e4d9/projects.go#L794.")
    filter: Optional[EventSourceFilter] = None
    gitlab_base_url: Optional[StrictStr] = Field(default=None, alias="gitlabBaseURL")
    metadata: Optional[Dict[str, StrictStr]] = None
    project_id: Optional[StrictStr] = Field(default=None, alias="projectID")
    projects: Optional[List[StrictStr]] = None
    secret_token: Optional[SecretKeySelector] = Field(default=None, alias="secretToken")
    webhook: Optional[WebhookContext] = None
    __properties: ClassVar[List[str]] = ["accessToken", "deleteHookOnFinish", "enableSSLVerification", "events", "filter", "gitlabBaseURL", "metadata", "projectID", "projects", "secretToken", "webhook"]

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
        """Create an instance of GitlabEventSource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of access_token
        if self.access_token:
            _dict['accessToken'] = self.access_token.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secret_token
        if self.secret_token:
            _dict['secretToken'] = self.secret_token.to_dict()
        # override the default output from pydantic by calling `to_dict()` of webhook
        if self.webhook:
            _dict['webhook'] = self.webhook.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GitlabEventSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessToken": SecretKeySelector.from_dict(obj.get("accessToken")) if obj.get("accessToken") is not None else None,
            "deleteHookOnFinish": obj.get("deleteHookOnFinish"),
            "enableSSLVerification": obj.get("enableSSLVerification"),
            "events": obj.get("events"),
            "filter": EventSourceFilter.from_dict(obj.get("filter")) if obj.get("filter") is not None else None,
            "gitlabBaseURL": obj.get("gitlabBaseURL"),
            "metadata": obj.get("metadata"),
            "projectID": obj.get("projectID"),
            "projects": obj.get("projects"),
            "secretToken": SecretKeySelector.from_dict(obj.get("secretToken")) if obj.get("secretToken") is not None else None,
            "webhook": WebhookContext.from_dict(obj.get("webhook")) if obj.get("webhook") is not None else None
        })
        return _obj


