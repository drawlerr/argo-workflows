# Synchronization

Synchronization holds synchronization lock configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mutex** | [**Mutex**](Mutex.md) |  | [optional] 
**semaphore** | [**SemaphoreRef**](SemaphoreRef.md) |  | [optional] 

## Example

```python
from argo_workflows.models.synchronization import Synchronization

# TODO update the JSON string below
json = "{}"
# create an instance of Synchronization from a JSON string
synchronization_instance = Synchronization.from_json(json)
# print the JSON string representation of the object
print Synchronization.to_json()

# convert the object into a dict
synchronization_dict = synchronization_instance.to_dict()
# create an instance of Synchronization from a dict
synchronization_form_dict = synchronization.from_dict(synchronization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


