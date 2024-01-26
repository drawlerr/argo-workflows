# OSSArtifactRepository

OSSArtifactRepository defines the controller configuration for an OSS artifact repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**bucket** | **str** | Bucket is the name of the bucket | [optional] 
**create_bucket_if_not_present** | **bool** | CreateBucketIfNotPresent tells the driver to attempt to create the OSS bucket for output artifacts, if it doesn&#39;t exist | [optional] 
**endpoint** | **str** | Endpoint is the hostname of the bucket endpoint | [optional] 
**key_format** | **str** | KeyFormat defines the format of how to store keys and can reference workflow variables. | [optional] 
**lifecycle_rule** | [**OSSLifecycleRule**](OSSLifecycleRule.md) |  | [optional] 
**secret_key_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**security_token** | **str** | SecurityToken is the user&#39;s temporary security token. For more details, check out: https://www.alibabacloud.com/help/doc-detail/100624.htm | [optional] 
**use_sdk_creds** | **bool** | UseSDKCreds tells the driver to figure out credentials based on sdk defaults. | [optional] 

## Example

```python
from argo_workflows.models.oss_artifact_repository import OSSArtifactRepository

# TODO update the JSON string below
json = "{}"
# create an instance of OSSArtifactRepository from a JSON string
oss_artifact_repository_instance = OSSArtifactRepository.from_json(json)
# print the JSON string representation of the object
print OSSArtifactRepository.to_json()

# convert the object into a dict
oss_artifact_repository_dict = oss_artifact_repository_instance.to_dict()
# create an instance of OSSArtifactRepository from a dict
oss_artifact_repository_form_dict = oss_artifact_repository.from_dict(oss_artifact_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


