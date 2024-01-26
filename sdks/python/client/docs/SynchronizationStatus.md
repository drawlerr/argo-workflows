# SynchronizationStatus

SynchronizationStatus stores the status of semaphore and mutex.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mutex** | [**MutexStatus**](MutexStatus.md) |  | [optional] 
**semaphore** | [**SemaphoreStatus**](SemaphoreStatus.md) |  | [optional] 

## Example

```python
from argo_workflows.models.synchronization_status import SynchronizationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SynchronizationStatus from a JSON string
synchronization_status_instance = SynchronizationStatus.from_json(json)
# print the JSON string representation of the object
print SynchronizationStatus.to_json()

# convert the object into a dict
synchronization_status_dict = synchronization_status_instance.to_dict()
# create an instance of SynchronizationStatus from a dict
synchronization_status_form_dict = synchronization_status.from_dict(synchronization_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


