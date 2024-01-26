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
from argo_workflows.models.create_options import CreateOptions
from argo_workflows.models.io_argoproj_workflow_v1alpha1_workflow import IoArgoprojWorkflowV1alpha1Workflow
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IoArgoprojWorkflowV1alpha1WorkflowCreateRequest(BaseModel):
    """
    IoArgoprojWorkflowV1alpha1WorkflowCreateRequest
    """ # noqa: E501
    create_options: Optional[CreateOptions] = Field(default=None, alias="createOptions")
    instance_id: Optional[StrictStr] = Field(default=None, description="This field is no longer used.", alias="instanceID")
    namespace: Optional[StrictStr] = None
    server_dry_run: Optional[StrictBool] = Field(default=None, alias="serverDryRun")
    workflow: Optional[IoArgoprojWorkflowV1alpha1Workflow] = None
    __properties: ClassVar[List[str]] = ["createOptions", "instanceID", "namespace", "serverDryRun", "workflow"]

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
        """Create an instance of IoArgoprojWorkflowV1alpha1WorkflowCreateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of create_options
        if self.create_options:
            _dict['createOptions'] = self.create_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of workflow
        if self.workflow:
            _dict['workflow'] = self.workflow.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IoArgoprojWorkflowV1alpha1WorkflowCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createOptions": CreateOptions.from_dict(obj.get("createOptions")) if obj.get("createOptions") is not None else None,
            "instanceID": obj.get("instanceID"),
            "namespace": obj.get("namespace"),
            "serverDryRun": obj.get("serverDryRun"),
            "workflow": IoArgoprojWorkflowV1alpha1Workflow.from_dict(obj.get("workflow")) if obj.get("workflow") is not None else None
        })
        return _obj


