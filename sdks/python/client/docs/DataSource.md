# DataSource

DataSource sources external data into a data template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_paths** | [**ArtifactPaths**](ArtifactPaths.md) |  | [optional] 

## Example

```python
from argo_workflows.models.data_source import DataSource

# TODO update the JSON string below
json = "{}"
# create an instance of DataSource from a JSON string
data_source_instance = DataSource.from_json(json)
# print the JSON string representation of the object
print DataSource.to_json()

# convert the object into a dict
data_source_dict = data_source_instance.to_dict()
# create an instance of DataSource from a dict
data_source_form_dict = data_source.from_dict(data_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


