# HTTPBodySource

HTTPBodySource contains the source of the HTTP body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes** | **bytearray** |  | [optional] 

## Example

```python
from argo_workflows.models.http_body_source import HTTPBodySource

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPBodySource from a JSON string
http_body_source_instance = HTTPBodySource.from_json(json)
# print the JSON string representation of the object
print HTTPBodySource.to_json()

# convert the object into a dict
http_body_source_dict = http_body_source_instance.to_dict()
# create an instance of HTTPBodySource from a dict
http_body_source_form_dict = http_body_source.from_dict(http_body_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


