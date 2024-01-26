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
from argo_workflows.models.archive_strategy import ArchiveStrategy
from argo_workflows.models.artifact_gc import ArtifactGC
from argo_workflows.models.artifactory_artifact import ArtifactoryArtifact
from argo_workflows.models.azure_artifact import AzureArtifact
from argo_workflows.models.gcs_artifact import GCSArtifact
from argo_workflows.models.git_artifact import GitArtifact
from argo_workflows.models.hdfs_artifact import HDFSArtifact
from argo_workflows.models.http_artifact import HTTPArtifact
from argo_workflows.models.oss_artifact import OSSArtifact
from argo_workflows.models.raw_artifact import RawArtifact
from argo_workflows.models.s3_artifact import S3Artifact
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ArtifactPaths(BaseModel):
    """
    ArtifactPaths expands a step from a collection of artifacts
    """ # noqa: E501
    archive: Optional[ArchiveStrategy] = None
    archive_logs: Optional[StrictBool] = Field(default=None, description="ArchiveLogs indicates if the container logs should be archived", alias="archiveLogs")
    artifact_gc: Optional[ArtifactGC] = Field(default=None, alias="artifactGC")
    artifactory: Optional[ArtifactoryArtifact] = None
    azure: Optional[AzureArtifact] = None
    deleted: Optional[StrictBool] = Field(default=None, description="Has this been deleted?")
    var_from: Optional[StrictStr] = Field(default=None, description="From allows an artifact to reference an artifact from a previous step", alias="from")
    from_expression: Optional[StrictStr] = Field(default=None, description="FromExpression, if defined, is evaluated to specify the value for the artifact", alias="fromExpression")
    gcs: Optional[GCSArtifact] = None
    git: Optional[GitArtifact] = None
    global_name: Optional[StrictStr] = Field(default=None, description="GlobalName exports an output artifact to the global scope, making it available as '{{outputs.artifacts.XXXX}} and in workflow.status.outputs.artifacts", alias="globalName")
    hdfs: Optional[HDFSArtifact] = None
    http: Optional[HTTPArtifact] = None
    mode: Optional[StrictInt] = Field(default=None, description="mode bits to use on this file, must be a value between 0 and 0777 set when loading input artifacts.")
    name: StrictStr = Field(description="name of the artifact. must be unique within a template's inputs/outputs.")
    optional: Optional[StrictBool] = Field(default=None, description="Make Artifacts optional, if Artifacts doesn't generate or exist")
    oss: Optional[OSSArtifact] = None
    path: Optional[StrictStr] = Field(default=None, description="Path is the container path to the artifact")
    raw: Optional[RawArtifact] = None
    recurse_mode: Optional[StrictBool] = Field(default=None, description="If mode is set, apply the permission recursively into the artifact if it is a folder", alias="recurseMode")
    s3: Optional[S3Artifact] = None
    sub_path: Optional[StrictStr] = Field(default=None, description="SubPath allows an artifact to be sourced from a subpath within the specified source", alias="subPath")
    __properties: ClassVar[List[str]] = ["archive", "archiveLogs", "artifactGC", "artifactory", "azure", "deleted", "from", "fromExpression", "gcs", "git", "globalName", "hdfs", "http", "mode", "name", "optional", "oss", "path", "raw", "recurseMode", "s3", "subPath"]

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
        """Create an instance of ArtifactPaths from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of archive
        if self.archive:
            _dict['archive'] = self.archive.to_dict()
        # override the default output from pydantic by calling `to_dict()` of artifact_gc
        if self.artifact_gc:
            _dict['artifactGC'] = self.artifact_gc.to_dict()
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
        """Create an instance of ArtifactPaths from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "archive": ArchiveStrategy.from_dict(obj.get("archive")) if obj.get("archive") is not None else None,
            "archiveLogs": obj.get("archiveLogs"),
            "artifactGC": ArtifactGC.from_dict(obj.get("artifactGC")) if obj.get("artifactGC") is not None else None,
            "artifactory": ArtifactoryArtifact.from_dict(obj.get("artifactory")) if obj.get("artifactory") is not None else None,
            "azure": AzureArtifact.from_dict(obj.get("azure")) if obj.get("azure") is not None else None,
            "deleted": obj.get("deleted"),
            "from": obj.get("from"),
            "fromExpression": obj.get("fromExpression"),
            "gcs": GCSArtifact.from_dict(obj.get("gcs")) if obj.get("gcs") is not None else None,
            "git": GitArtifact.from_dict(obj.get("git")) if obj.get("git") is not None else None,
            "globalName": obj.get("globalName"),
            "hdfs": HDFSArtifact.from_dict(obj.get("hdfs")) if obj.get("hdfs") is not None else None,
            "http": HTTPArtifact.from_dict(obj.get("http")) if obj.get("http") is not None else None,
            "mode": obj.get("mode"),
            "name": obj.get("name"),
            "optional": obj.get("optional"),
            "oss": OSSArtifact.from_dict(obj.get("oss")) if obj.get("oss") is not None else None,
            "path": obj.get("path"),
            "raw": RawArtifact.from_dict(obj.get("raw")) if obj.get("raw") is not None else None,
            "recurseMode": obj.get("recurseMode"),
            "s3": S3Artifact.from_dict(obj.get("s3")) if obj.get("s3") is not None else None,
            "subPath": obj.get("subPath")
        })
        return _obj


