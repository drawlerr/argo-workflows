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
from argo_workflows.models.io_argoproj_events_v1alpha1_bitbucket_auth import IoArgoprojEventsV1alpha1BitbucketAuth
from argo_workflows.models.io_argoproj_events_v1alpha1_bitbucket_repository import IoArgoprojEventsV1alpha1BitbucketRepository
from argo_workflows.models.io_argoproj_events_v1alpha1_event_source_filter import IoArgoprojEventsV1alpha1EventSourceFilter
from argo_workflows.models.io_argoproj_events_v1alpha1_webhook_context import IoArgoprojEventsV1alpha1WebhookContext
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IoArgoprojEventsV1alpha1BitbucketEventSource(BaseModel):
    """
    IoArgoprojEventsV1alpha1BitbucketEventSource
    """ # noqa: E501
    auth: Optional[IoArgoprojEventsV1alpha1BitbucketAuth] = None
    delete_hook_on_finish: Optional[StrictBool] = Field(default=None, alias="deleteHookOnFinish")
    events: Optional[List[StrictStr]] = Field(default=None, description="Events this webhook is subscribed to.")
    filter: Optional[IoArgoprojEventsV1alpha1EventSourceFilter] = None
    metadata: Optional[Dict[str, StrictStr]] = None
    owner: Optional[StrictStr] = None
    project_key: Optional[StrictStr] = Field(default=None, alias="projectKey")
    repositories: Optional[List[IoArgoprojEventsV1alpha1BitbucketRepository]] = None
    repository_slug: Optional[StrictStr] = Field(default=None, alias="repositorySlug")
    webhook: Optional[IoArgoprojEventsV1alpha1WebhookContext] = None
    __properties: ClassVar[List[str]] = ["auth", "deleteHookOnFinish", "events", "filter", "metadata", "owner", "projectKey", "repositories", "repositorySlug", "webhook"]

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
        """Create an instance of IoArgoprojEventsV1alpha1BitbucketEventSource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in repositories (list)
        _items = []
        if self.repositories:
            for _item in self.repositories:
                if _item:
                    _items.append(_item.to_dict())
            _dict['repositories'] = _items
        # override the default output from pydantic by calling `to_dict()` of webhook
        if self.webhook:
            _dict['webhook'] = self.webhook.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IoArgoprojEventsV1alpha1BitbucketEventSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "auth": IoArgoprojEventsV1alpha1BitbucketAuth.from_dict(obj.get("auth")) if obj.get("auth") is not None else None,
            "deleteHookOnFinish": obj.get("deleteHookOnFinish"),
            "events": obj.get("events"),
            "filter": IoArgoprojEventsV1alpha1EventSourceFilter.from_dict(obj.get("filter")) if obj.get("filter") is not None else None,
            "metadata": obj.get("metadata"),
            "owner": obj.get("owner"),
            "projectKey": obj.get("projectKey"),
            "repositories": [IoArgoprojEventsV1alpha1BitbucketRepository.from_dict(_item) for _item in obj.get("repositories")] if obj.get("repositories") is not None else None,
            "repositorySlug": obj.get("repositorySlug"),
            "webhook": IoArgoprojEventsV1alpha1WebhookContext.from_dict(obj.get("webhook")) if obj.get("webhook") is not None else None
        })
        return _obj


