# FileArtifact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.file_artifact import FileArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of FileArtifact from a JSON string
file_artifact_instance = FileArtifact.from_json(json)
# print the JSON string representation of the object
print FileArtifact.to_json()

# convert the object into a dict
file_artifact_dict = file_artifact_instance.to_dict()
# create an instance of FileArtifact from a dict
file_artifact_form_dict = file_artifact.from_dict(file_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


