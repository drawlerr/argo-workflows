# ValueFromSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_map_key_ref** | [**ConfigMapKeySelector**](ConfigMapKeySelector.md) |  | [optional] 
**secret_key_ref** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.value_from_source import ValueFromSource

# TODO update the JSON string below
json = "{}"
# create an instance of ValueFromSource from a JSON string
value_from_source_instance = ValueFromSource.from_json(json)
# print the JSON string representation of the object
print ValueFromSource.to_json()

# convert the object into a dict
value_from_source_dict = value_from_source_instance.to_dict()
# create an instance of ValueFromSource from a dict
value_from_source_form_dict = value_from_source.from_dict(value_from_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


