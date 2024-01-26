# ArtifactRepositoryRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_map** | **str** | The name of the config map. Defaults to \&quot;artifact-repositories\&quot;. | [optional] 
**key** | **str** | The config map key. Defaults to the value of the \&quot;workflows.argoproj.io/default-artifact-repository\&quot; annotation. | [optional] 

## Example

```python
from argo_workflows.models.artifact_repository_ref import ArtifactRepositoryRef

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactRepositoryRef from a JSON string
artifact_repository_ref_instance = ArtifactRepositoryRef.from_json(json)
# print the JSON string representation of the object
print ArtifactRepositoryRef.to_json()

# convert the object into a dict
artifact_repository_ref_dict = artifact_repository_ref_instance.to_dict()
# create an instance of ArtifactRepositoryRef from a dict
artifact_repository_ref_form_dict = artifact_repository_ref.from_dict(artifact_repository_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


