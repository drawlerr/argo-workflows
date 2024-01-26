# RawArtifact

RawArtifact allows raw string content to be placed as an artifact in a container

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Data is the string contents of the artifact | 

## Example

```python
from argo_workflows.models.raw_artifact import RawArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of RawArtifact from a JSON string
raw_artifact_instance = RawArtifact.from_json(json)
# print the JSON string representation of the object
print RawArtifact.to_json()

# convert the object into a dict
raw_artifact_dict = raw_artifact_instance.to_dict()
# create an instance of RawArtifact from a dict
raw_artifact_form_dict = raw_artifact.from_dict(raw_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


