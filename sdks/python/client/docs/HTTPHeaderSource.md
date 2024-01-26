# HTTPHeaderSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_key_ref** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.http_header_source import HTTPHeaderSource

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPHeaderSource from a JSON string
http_header_source_instance = HTTPHeaderSource.from_json(json)
# print the JSON string representation of the object
print HTTPHeaderSource.to_json()

# convert the object into a dict
http_header_source_dict = http_header_source_instance.to_dict()
# create an instance of HTTPHeaderSource from a dict
http_header_source_form_dict = http_header_source.from_dict(http_header_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


