# ArtifactResult

ArtifactResult describes the result of attempting to delete a given Artifact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error is an optional error message which should be set if Success&#x3D;&#x3D;false | [optional] 
**name** | **str** | Name is the name of the Artifact | 
**success** | **bool** | Success describes whether the deletion succeeded | [optional] 

## Example

```python
from argo_workflows.models.artifact_result import ArtifactResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactResult from a JSON string
artifact_result_instance = ArtifactResult.from_json(json)
# print the JSON string representation of the object
print ArtifactResult.to_json()

# convert the object into a dict
artifact_result_dict = artifact_result_instance.to_dict()
# create an instance of ArtifactResult from a dict
artifact_result_form_dict = artifact_result.from_dict(artifact_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


