# MutexHolding

MutexHolding describes the mutex and the object which is holding it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holder** | **str** | Holder is a reference to the object which holds the Mutex. Holding Scenario:   1. Current workflow&#39;s NodeID which is holding the lock.      e.g: ${NodeID} Waiting Scenario:   1. Current workflow or other workflow NodeID which is holding the lock.      e.g: ${WorkflowName}/${NodeID} | [optional] 
**mutex** | **str** | Reference for the mutex e.g: ${namespace}/mutex/${mutexName} | [optional] 

## Example

```python
from argo_workflows.models.mutex_holding import MutexHolding

# TODO update the JSON string below
json = "{}"
# create an instance of MutexHolding from a JSON string
mutex_holding_instance = MutexHolding.from_json(json)
# print the JSON string representation of the object
print MutexHolding.to_json()

# convert the object into a dict
mutex_holding_dict = mutex_holding_instance.to_dict()
# create an instance of MutexHolding from a dict
mutex_holding_form_dict = mutex_holding.from_dict(mutex_holding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


