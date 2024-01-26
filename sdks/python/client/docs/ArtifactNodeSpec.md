# ArtifactNodeSpec

ArtifactNodeSpec specifies the Artifacts that need to be deleted for a given Node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_location** | [**ArtifactLocation**](ArtifactLocation.md) |  | [optional] 
**artifacts** | [**Dict[str, Artifact]**](Artifact.md) | Artifacts maps artifact name to Artifact description | [optional] 

## Example

```python
from argo_workflows.models.artifact_node_spec import ArtifactNodeSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactNodeSpec from a JSON string
artifact_node_spec_instance = ArtifactNodeSpec.from_json(json)
# print the JSON string representation of the object
print ArtifactNodeSpec.to_json()

# convert the object into a dict
artifact_node_spec_dict = artifact_node_spec_instance.to_dict()
# create an instance of ArtifactNodeSpec from a dict
artifact_node_spec_form_dict = artifact_node_spec.from_dict(artifact_node_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


