# HTTPArtifact

HTTPArtifact allows a file served on HTTP to be placed as an input artifact in a container

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**HTTPAuth**](HTTPAuth.md) |  | [optional] 
**headers** | [**List[Header]**](Header.md) | Headers are an optional list of headers to send with HTTP requests for artifacts | [optional] 
**url** | **str** | URL of the artifact | 

## Example

```python
from argo_workflows.models.http_artifact import HTTPArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPArtifact from a JSON string
http_artifact_instance = HTTPArtifact.from_json(json)
# print the JSON string representation of the object
print HTTPArtifact.to_json()

# convert the object into a dict
http_artifact_dict = http_artifact_instance.to_dict()
# create an instance of HTTPArtifact from a dict
http_artifact_form_dict = http_artifact.from_dict(http_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


