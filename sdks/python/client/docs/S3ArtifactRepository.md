# S3ArtifactRepository

S3ArtifactRepository defines the controller configuration for an S3 artifact repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**bucket** | **str** | Bucket is the name of the bucket | [optional] 
**ca_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**create_bucket_if_not_present** | [**CreateS3BucketOptions**](CreateS3BucketOptions.md) |  | [optional] 
**encryption_options** | [**S3EncryptionOptions**](S3EncryptionOptions.md) |  | [optional] 
**endpoint** | **str** | Endpoint is the hostname of the bucket endpoint | [optional] 
**insecure** | **bool** | Insecure will connect to the service with TLS | [optional] 
**key_format** | **str** | KeyFormat defines the format of how to store keys and can reference workflow variables. | [optional] 
**key_prefix** | **str** | KeyPrefix is prefix used as part of the bucket key in which the controller will store artifacts. DEPRECATED. Use KeyFormat instead | [optional] 
**region** | **str** | Region contains the optional bucket region | [optional] 
**role_arn** | **str** | RoleARN is the Amazon Resource Name (ARN) of the role to assume. | [optional] 
**secret_key_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**use_sdk_creds** | **bool** | UseSDKCreds tells the driver to figure out credentials based on sdk defaults. | [optional] 

## Example

```python
from argo_workflows.models.s3_artifact_repository import S3ArtifactRepository

# TODO update the JSON string below
json = "{}"
# create an instance of S3ArtifactRepository from a JSON string
s3_artifact_repository_instance = S3ArtifactRepository.from_json(json)
# print the JSON string representation of the object
print S3ArtifactRepository.to_json()

# convert the object into a dict
s3_artifact_repository_dict = s3_artifact_repository_instance.to_dict()
# create an instance of S3ArtifactRepository from a dict
s3_artifact_repository_form_dict = s3_artifact_repository.from_dict(s3_artifact_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


