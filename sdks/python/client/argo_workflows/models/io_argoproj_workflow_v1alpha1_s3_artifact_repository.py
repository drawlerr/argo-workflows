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
from argo_workflows.models.io_argoproj_workflow_v1alpha1_create_s3_bucket_options import IoArgoprojWorkflowV1alpha1CreateS3BucketOptions
from argo_workflows.models.io_argoproj_workflow_v1alpha1_s3_encryption_options import IoArgoprojWorkflowV1alpha1S3EncryptionOptions
from argo_workflows.models.secret_key_selector import SecretKeySelector
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IoArgoprojWorkflowV1alpha1S3ArtifactRepository(BaseModel):
    """
    S3ArtifactRepository defines the controller configuration for an S3 artifact repository
    """ # noqa: E501
    access_key_secret: Optional[SecretKeySelector] = Field(default=None, alias="accessKeySecret")
    bucket: Optional[StrictStr] = Field(default=None, description="Bucket is the name of the bucket")
    ca_secret: Optional[SecretKeySelector] = Field(default=None, alias="caSecret")
    create_bucket_if_not_present: Optional[IoArgoprojWorkflowV1alpha1CreateS3BucketOptions] = Field(default=None, alias="createBucketIfNotPresent")
    encryption_options: Optional[IoArgoprojWorkflowV1alpha1S3EncryptionOptions] = Field(default=None, alias="encryptionOptions")
    endpoint: Optional[StrictStr] = Field(default=None, description="Endpoint is the hostname of the bucket endpoint")
    insecure: Optional[StrictBool] = Field(default=None, description="Insecure will connect to the service with TLS")
    key_format: Optional[StrictStr] = Field(default=None, description="KeyFormat defines the format of how to store keys and can reference workflow variables.", alias="keyFormat")
    key_prefix: Optional[StrictStr] = Field(default=None, description="KeyPrefix is prefix used as part of the bucket key in which the controller will store artifacts. DEPRECATED. Use KeyFormat instead", alias="keyPrefix")
    region: Optional[StrictStr] = Field(default=None, description="Region contains the optional bucket region")
    role_arn: Optional[StrictStr] = Field(default=None, description="RoleARN is the Amazon Resource Name (ARN) of the role to assume.", alias="roleARN")
    secret_key_secret: Optional[SecretKeySelector] = Field(default=None, alias="secretKeySecret")
    use_sdk_creds: Optional[StrictBool] = Field(default=None, description="UseSDKCreds tells the driver to figure out credentials based on sdk defaults.", alias="useSDKCreds")
    __properties: ClassVar[List[str]] = ["accessKeySecret", "bucket", "caSecret", "createBucketIfNotPresent", "encryptionOptions", "endpoint", "insecure", "keyFormat", "keyPrefix", "region", "roleARN", "secretKeySecret", "useSDKCreds"]

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
        """Create an instance of IoArgoprojWorkflowV1alpha1S3ArtifactRepository from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of access_key_secret
        if self.access_key_secret:
            _dict['accessKeySecret'] = self.access_key_secret.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ca_secret
        if self.ca_secret:
            _dict['caSecret'] = self.ca_secret.to_dict()
        # override the default output from pydantic by calling `to_dict()` of create_bucket_if_not_present
        if self.create_bucket_if_not_present:
            _dict['createBucketIfNotPresent'] = self.create_bucket_if_not_present.to_dict()
        # override the default output from pydantic by calling `to_dict()` of encryption_options
        if self.encryption_options:
            _dict['encryptionOptions'] = self.encryption_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secret_key_secret
        if self.secret_key_secret:
            _dict['secretKeySecret'] = self.secret_key_secret.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IoArgoprojWorkflowV1alpha1S3ArtifactRepository from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessKeySecret": SecretKeySelector.from_dict(obj.get("accessKeySecret")) if obj.get("accessKeySecret") is not None else None,
            "bucket": obj.get("bucket"),
            "caSecret": SecretKeySelector.from_dict(obj.get("caSecret")) if obj.get("caSecret") is not None else None,
            "createBucketIfNotPresent": IoArgoprojWorkflowV1alpha1CreateS3BucketOptions.from_dict(obj.get("createBucketIfNotPresent")) if obj.get("createBucketIfNotPresent") is not None else None,
            "encryptionOptions": IoArgoprojWorkflowV1alpha1S3EncryptionOptions.from_dict(obj.get("encryptionOptions")) if obj.get("encryptionOptions") is not None else None,
            "endpoint": obj.get("endpoint"),
            "insecure": obj.get("insecure"),
            "keyFormat": obj.get("keyFormat"),
            "keyPrefix": obj.get("keyPrefix"),
            "region": obj.get("region"),
            "roleARN": obj.get("roleARN"),
            "secretKeySecret": SecretKeySelector.from_dict(obj.get("secretKeySecret")) if obj.get("secretKeySecret") is not None else None,
            "useSDKCreds": obj.get("useSDKCreds")
        })
        return _obj


