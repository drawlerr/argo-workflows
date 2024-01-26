# ArtifactResultNodeStatus

ArtifactResultNodeStatus describes the result of the deletion on a given node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_results** | [**Dict[str, ArtifactResult]**](ArtifactResult.md) | ArtifactResults maps Artifact name to result of the deletion | [optional] 

## Example

```python
from argo_workflows.models.artifact_result_node_status import ArtifactResultNodeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactResultNodeStatus from a JSON string
artifact_result_node_status_instance = ArtifactResultNodeStatus.from_json(json)
# print the JSON string representation of the object
print ArtifactResultNodeStatus.to_json()

# convert the object into a dict
artifact_result_node_status_dict = artifact_result_node_status_instance.to_dict()
# create an instance of ArtifactResultNodeStatus from a dict
artifact_result_node_status_form_dict = artifact_result_node_status.from_dict(artifact_result_node_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


