# Int64OrString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**int64_val** | **str** |  | [optional] 
**str_val** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.int64_or_string import Int64OrString

# TODO update the JSON string below
json = "{}"
# create an instance of Int64OrString from a JSON string
int64_or_string_instance = Int64OrString.from_json(json)
# print the JSON string representation of the object
print Int64OrString.to_json()

# convert the object into a dict
int64_or_string_dict = int64_or_string_instance.to_dict()
# create an instance of Int64OrString from a dict
int64_or_string_form_dict = int64_or_string.from_dict(int64_or_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


