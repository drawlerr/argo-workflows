# GCSArtifactRepository

GCSArtifactRepository defines the controller configuration for a GCS artifact repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** | Bucket is the name of the bucket | [optional] 
**key_format** | **str** | KeyFormat defines the format of how to store keys and can reference workflow variables. | [optional] 
**service_account_key_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.gcs_artifact_repository import GCSArtifactRepository

# TODO update the JSON string below
json = "{}"
# create an instance of GCSArtifactRepository from a JSON string
gcs_artifact_repository_instance = GCSArtifactRepository.from_json(json)
# print the JSON string representation of the object
print GCSArtifactRepository.to_json()

# convert the object into a dict
gcs_artifact_repository_dict = gcs_artifact_repository_instance.to_dict()
# create an instance of GCSArtifactRepository from a dict
gcs_artifact_repository_form_dict = gcs_artifact_repository.from_dict(gcs_artifact_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


