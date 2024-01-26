# Header

Header indicate a key-value request header to be used when fetching artifacts over HTTP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name is the header name | 
**value** | **str** | Value is the literal value to use for the header | 

## Example

```python
from argo_workflows.models.header import Header

# TODO update the JSON string below
json = "{}"
# create an instance of Header from a JSON string
header_instance = Header.from_json(json)
# print the JSON string representation of the object
print Header.to_json()

# convert the object into a dict
header_dict = header_instance.to_dict()
# create an instance of Header from a dict
header_form_dict = header.from_dict(header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


