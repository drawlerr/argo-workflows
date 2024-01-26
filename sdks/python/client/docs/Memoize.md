# Memoize

Memoization enables caching for the Outputs of the template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache** | [**Cache**](Cache.md) |  | 
**key** | **str** | Key is the key to use as the caching key | 
**max_age** | **str** | MaxAge is the maximum age (e.g. \&quot;180s\&quot;, \&quot;24h\&quot;) of an entry that is still considered valid. If an entry is older than the MaxAge, it will be ignored. | 

## Example

```python
from argo_workflows.models.memoize import Memoize

# TODO update the JSON string below
json = "{}"
# create an instance of Memoize from a JSON string
memoize_instance = Memoize.from_json(json)
# print the JSON string representation of the object
print Memoize.to_json()

# convert the object into a dict
memoize_dict = memoize_instance.to_dict()
# create an instance of Memoize from a dict
memoize_form_dict = memoize.from_dict(memoize_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


