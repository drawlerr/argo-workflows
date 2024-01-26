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
from argo_workflows.models.io_argoproj_workflow_v1alpha1_artifact_repository import IoArgoprojWorkflowV1alpha1ArtifactRepository
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IoArgoprojWorkflowV1alpha1ArtifactRepositoryRefStatus(BaseModel):
    """
    IoArgoprojWorkflowV1alpha1ArtifactRepositoryRefStatus
    """ # noqa: E501
    artifact_repository: Optional[IoArgoprojWorkflowV1alpha1ArtifactRepository] = Field(default=None, alias="artifactRepository")
    config_map: Optional[StrictStr] = Field(default=None, description="The name of the config map. Defaults to \"artifact-repositories\".", alias="configMap")
    default: Optional[StrictBool] = Field(default=None, description="If this ref represents the default artifact repository, rather than a config map.")
    key: Optional[StrictStr] = Field(default=None, description="The config map key. Defaults to the value of the \"workflows.argoproj.io/default-artifact-repository\" annotation.")
    namespace: Optional[StrictStr] = Field(default=None, description="The namespace of the config map. Defaults to the workflow's namespace, or the controller's namespace (if found).")
    __properties: ClassVar[List[str]] = ["artifactRepository", "configMap", "default", "key", "namespace"]

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
        """Create an instance of IoArgoprojWorkflowV1alpha1ArtifactRepositoryRefStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of artifact_repository
        if self.artifact_repository:
            _dict['artifactRepository'] = self.artifact_repository.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IoArgoprojWorkflowV1alpha1ArtifactRepositoryRefStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "artifactRepository": IoArgoprojWorkflowV1alpha1ArtifactRepository.from_dict(obj.get("artifactRepository")) if obj.get("artifactRepository") is not None else None,
            "configMap": obj.get("configMap"),
            "default": obj.get("default"),
            "key": obj.get("key"),
            "namespace": obj.get("namespace")
        })
        return _obj


