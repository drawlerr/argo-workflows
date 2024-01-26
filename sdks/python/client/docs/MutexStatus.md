# MutexStatus

MutexStatus contains which objects hold  mutex locks, and which objects this workflow is waiting on to release locks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding** | [**List[MutexHolding]**](MutexHolding.md) | Holding is a list of mutexes and their respective objects that are held by mutex lock for this  | [optional] 
**waiting** | [**List[MutexHolding]**](MutexHolding.md) | Waiting is a list of mutexes and their respective objects this workflow is waiting for. | [optional] 

## Example

```python
from argo_workflows.models.mutex_status import MutexStatus

# TODO update the JSON string below
json = "{}"
# create an instance of MutexStatus from a JSON string
mutex_status_instance = MutexStatus.from_json(json)
# print the JSON string representation of the object
print MutexStatus.to_json()

# convert the object into a dict
mutex_status_dict = mutex_status_instance.to_dict()
# create an instance of MutexStatus from a dict
mutex_status_form_dict = mutex_status.from_dict(mutex_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


