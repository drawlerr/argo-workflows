# MemoizationStatus

MemoizationStatus is the status of this memoized node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_name** | **str** | Cache is the name of the cache that was used | 
**hit** | **bool** | Hit indicates whether this node was created from a cache entry | 
**key** | **str** | Key is the name of the key used for this node&#39;s cache | 

## Example

```python
from argo_workflows.models.memoization_status import MemoizationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of MemoizationStatus from a JSON string
memoization_status_instance = MemoizationStatus.from_json(json)
# print the JSON string representation of the object
print MemoizationStatus.to_json()

# convert the object into a dict
memoization_status_dict = memoization_status_instance.to_dict()
# create an instance of MemoizationStatus from a dict
memoization_status_form_dict = memoization_status.from_dict(memoization_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


