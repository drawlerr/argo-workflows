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
from argo_workflows.models.group_version_resource import GroupVersionResource
from argo_workflows.models.io_argoproj_events_v1alpha1_resource_filter import IoArgoprojEventsV1alpha1ResourceFilter
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IoArgoprojEventsV1alpha1ResourceEventSource(BaseModel):
    """
    ResourceEventSource refers to a event-source for K8s resource related events.
    """ # noqa: E501
    event_types: Optional[List[StrictStr]] = Field(default=None, description="EventTypes is the list of event type to watch. Possible values are - ADD, UPDATE and DELETE.", alias="eventTypes")
    filter: Optional[IoArgoprojEventsV1alpha1ResourceFilter] = None
    group_version_resource: Optional[GroupVersionResource] = Field(default=None, alias="groupVersionResource")
    metadata: Optional[Dict[str, StrictStr]] = None
    namespace: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["eventTypes", "filter", "groupVersionResource", "metadata", "namespace"]

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
        """Create an instance of IoArgoprojEventsV1alpha1ResourceEventSource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of group_version_resource
        if self.group_version_resource:
            _dict['groupVersionResource'] = self.group_version_resource.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IoArgoprojEventsV1alpha1ResourceEventSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "eventTypes": obj.get("eventTypes"),
            "filter": IoArgoprojEventsV1alpha1ResourceFilter.from_dict(obj.get("filter")) if obj.get("filter") is not None else None,
            "groupVersionResource": GroupVersionResource.from_dict(obj.get("groupVersionResource")) if obj.get("groupVersionResource") is not None else None,
            "metadata": obj.get("metadata"),
            "namespace": obj.get("namespace")
        })
        return _obj


