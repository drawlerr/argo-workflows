# ArtifactGCStatus

ArtifactGCStatus describes the result of the deletion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_results_by_node** | [**Dict[str, ArtifactResultNodeStatus]**](ArtifactResultNodeStatus.md) | ArtifactResultsByNode maps Node name to result | [optional] 

## Example

```python
from argo_workflows.models.artifact_gc_status import ArtifactGCStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactGCStatus from a JSON string
artifact_gc_status_instance = ArtifactGCStatus.from_json(json)
# print the JSON string representation of the object
print ArtifactGCStatus.to_json()

# convert the object into a dict
artifact_gc_status_dict = artifact_gc_status_instance.to_dict()
# create an instance of ArtifactGCStatus from a dict
artifact_gc_status_form_dict = artifact_gc_status.from_dict(artifact_gc_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


