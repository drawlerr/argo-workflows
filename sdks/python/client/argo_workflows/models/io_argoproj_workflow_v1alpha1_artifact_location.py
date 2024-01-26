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
from pydantic import BaseModel, StrictBool
from pydantic import Field
from argo_workflows.models.io_argoproj_workflow_v1alpha1_artifactory_artifact import IoArgoprojWorkflowV1alpha1ArtifactoryArtifact
from argo_workflows.models.io_argoproj_workflow_v1alpha1_azure_artifact import IoArgoprojWorkflowV1alpha1AzureArtifact
from argo_workflows.models.io_argoproj_workflow_v1alpha1_gcs_artifact import IoArgoprojWorkflowV1alpha1GCSArtifact
from argo_workflows.models.io_argoproj_workflow_v1alpha1_git_artifact import IoArgoprojWorkflowV1alpha1GitArtifact
from argo_workflows.models.io_argoproj_workflow_v1alpha1_hdfs_artifact import IoArgoprojWorkflowV1alpha1HDFSArtifact
from argo_workflows.models.io_argoproj_workflow_v1alpha1_http_artifact import IoArgoprojWorkflowV1alpha1HTTPArtifact
from argo_workflows.models.io_argoproj_workflow_v1alpha1_oss_artifact import IoArgoprojWorkflowV1alpha1OSSArtifact
from argo_workflows.models.io_argoproj_workflow_v1alpha1_raw_artifact import IoArgoprojWorkflowV1alpha1RawArtifact
from argo_workflows.models.io_argoproj_workflow_v1alpha1_s3_artifact import IoArgoprojWorkflowV1alpha1S3Artifact
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IoArgoprojWorkflowV1alpha1ArtifactLocation(BaseModel):
    """
    ArtifactLocation describes a location for a single or multiple artifacts. It is used as single artifact in the context of inputs/outputs (e.g. outputs.artifacts.artname). It is also used to describe the location of multiple artifacts such as the archive location of a single workflow step, which the executor will use as a default location to store its files.
    """ # noqa: E501
    archive_logs: Optional[StrictBool] = Field(default=None, description="ArchiveLogs indicates if the container logs should be archived", alias="archiveLogs")
    artifactory: Optional[IoArgoprojWorkflowV1alpha1ArtifactoryArtifact] = None
    azure: Optional[IoArgoprojWorkflowV1alpha1AzureArtifact] = None
    gcs: Optional[IoArgoprojWorkflowV1alpha1GCSArtifact] = None
    git: Optional[IoArgoprojWorkflowV1alpha1GitArtifact] = None
    hdfs: Optional[IoArgoprojWorkflowV1alpha1HDFSArtifact] = None
    http: Optional[IoArgoprojWorkflowV1alpha1HTTPArtifact] = None
    oss: Optional[IoArgoprojWorkflowV1alpha1OSSArtifact] = None
    raw: Optional[IoArgoprojWorkflowV1alpha1RawArtifact] = None
    s3: Optional[IoArgoprojWorkflowV1alpha1S3Artifact] = None
    __properties: ClassVar[List[str]] = ["archiveLogs", "artifactory", "azure", "gcs", "git", "hdfs", "http", "oss", "raw", "s3"]

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
        """Create an instance of IoArgoprojWorkflowV1alpha1ArtifactLocation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of artifactory
        if self.artifactory:
            _dict['artifactory'] = self.artifactory.to_dict()
        # override the default output from pydantic by calling `to_dict()` of azure
        if self.azure:
            _dict['azure'] = self.azure.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gcs
        if self.gcs:
            _dict['gcs'] = self.gcs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of git
        if self.git:
            _dict['git'] = self.git.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hdfs
        if self.hdfs:
            _dict['hdfs'] = self.hdfs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of http
        if self.http:
            _dict['http'] = self.http.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oss
        if self.oss:
            _dict['oss'] = self.oss.to_dict()
        # override the default output from pydantic by calling `to_dict()` of raw
        if self.raw:
            _dict['raw'] = self.raw.to_dict()
        # override the default output from pydantic by calling `to_dict()` of s3
        if self.s3:
            _dict['s3'] = self.s3.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IoArgoprojWorkflowV1alpha1ArtifactLocation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "archiveLogs": obj.get("archiveLogs"),
            "artifactory": IoArgoprojWorkflowV1alpha1ArtifactoryArtifact.from_dict(obj.get("artifactory")) if obj.get("artifactory") is not None else None,
            "azure": IoArgoprojWorkflowV1alpha1AzureArtifact.from_dict(obj.get("azure")) if obj.get("azure") is not None else None,
            "gcs": IoArgoprojWorkflowV1alpha1GCSArtifact.from_dict(obj.get("gcs")) if obj.get("gcs") is not None else None,
            "git": IoArgoprojWorkflowV1alpha1GitArtifact.from_dict(obj.get("git")) if obj.get("git") is not None else None,
            "hdfs": IoArgoprojWorkflowV1alpha1HDFSArtifact.from_dict(obj.get("hdfs")) if obj.get("hdfs") is not None else None,
            "http": IoArgoprojWorkflowV1alpha1HTTPArtifact.from_dict(obj.get("http")) if obj.get("http") is not None else None,
            "oss": IoArgoprojWorkflowV1alpha1OSSArtifact.from_dict(obj.get("oss")) if obj.get("oss") is not None else None,
            "raw": IoArgoprojWorkflowV1alpha1RawArtifact.from_dict(obj.get("raw")) if obj.get("raw") is not None else None,
            "s3": IoArgoprojWorkflowV1alpha1S3Artifact.from_dict(obj.get("s3")) if obj.get("s3") is not None else None
        })
        return _obj


