# URLArtifact

URLArtifact contains information about an artifact at an http endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**verify_cert** | **bool** |  | [optional] 

## Example

```python
from argo_workflows.models.url_artifact import URLArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of URLArtifact from a JSON string
url_artifact_instance = URLArtifact.from_json(json)
# print the JSON string representation of the object
print URLArtifact.to_json()

# convert the object into a dict
url_artifact_dict = url_artifact_instance.to_dict()
# create an instance of URLArtifact from a dict
url_artifact_form_dict = url_artifact.from_dict(url_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


