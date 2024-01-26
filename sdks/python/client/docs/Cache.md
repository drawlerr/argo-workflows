# Cache

Cache is the configuration for the type of cache to be used

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_map** | [**ConfigMapKeySelector**](ConfigMapKeySelector.md) |  | 

## Example

```python
from argo_workflows.models.cache import Cache

# TODO update the JSON string below
json = "{}"
# create an instance of Cache from a JSON string
cache_instance = Cache.from_json(json)
# print the JSON string representation of the object
print Cache.to_json()

# convert the object into a dict
cache_dict = cache_instance.to_dict()
# create an instance of Cache from a dict
cache_form_dict = cache.from_dict(cache_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


