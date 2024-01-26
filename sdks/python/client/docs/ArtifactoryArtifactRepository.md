# ArtifactoryArtifactRepository

ArtifactoryArtifactRepository defines the controller configuration for an artifactory artifact repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_format** | **str** | KeyFormat defines the format of how to store keys and can reference workflow variables. | [optional] 
**password_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**repo_url** | **str** | RepoURL is the url for artifactory repo. | [optional] 
**username_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.artifactory_artifact_repository import ArtifactoryArtifactRepository

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactoryArtifactRepository from a JSON string
artifactory_artifact_repository_instance = ArtifactoryArtifactRepository.from_json(json)
# print the JSON string representation of the object
print ArtifactoryArtifactRepository.to_json()

# convert the object into a dict
artifactory_artifact_repository_dict = artifactory_artifact_repository_instance.to_dict()
# create an instance of ArtifactoryArtifactRepository from a dict
artifactory_artifact_repository_form_dict = artifactory_artifact_repository.from_dict(artifactory_artifact_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


