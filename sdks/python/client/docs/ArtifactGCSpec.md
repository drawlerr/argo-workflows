# ArtifactGCSpec

ArtifactGCSpec specifies the Artifacts that need to be deleted

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifacts_by_node** | [**Dict[str, ArtifactNodeSpec]**](ArtifactNodeSpec.md) | ArtifactsByNode maps Node name to information pertaining to Artifacts on that Node | [optional] 

## Example

```python
from argo_workflows.models.artifact_gc_spec import ArtifactGCSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactGCSpec from a JSON string
artifact_gc_spec_instance = ArtifactGCSpec.from_json(json)
# print the JSON string representation of the object
print ArtifactGCSpec.to_json()

# convert the object into a dict
artifact_gc_spec_dict = artifact_gc_spec_instance.to_dict()
# create an instance of ArtifactGCSpec from a dict
artifact_gc_spec_form_dict = artifact_gc_spec.from_dict(artifact_gc_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


