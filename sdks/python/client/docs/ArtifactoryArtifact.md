# ArtifactoryArtifact

ArtifactoryArtifact is the location of an artifactory artifact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**url** | **str** | URL of the artifact | 
**username_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.artifactory_artifact import ArtifactoryArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactoryArtifact from a JSON string
artifactory_artifact_instance = ArtifactoryArtifact.from_json(json)
# print the JSON string representation of the object
print ArtifactoryArtifact.to_json()

# convert the object into a dict
artifactory_artifact_dict = artifactory_artifact_instance.to_dict()
# create an instance of ArtifactoryArtifact from a dict
artifactory_artifact_form_dict = artifactory_artifact.from_dict(artifactory_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


