# Mutex

Mutex holds Mutex configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the mutex | [optional] 
**namespace** | **str** | Namespace is the namespace of the mutex, default: [namespace of workflow] | [optional] 

## Example

```python
from argo_workflows.models.mutex import Mutex

# TODO update the JSON string below
json = "{}"
# create an instance of Mutex from a JSON string
mutex_instance = Mutex.from_json(json)
# print the JSON string representation of the object
print Mutex.to_json()

# convert the object into a dict
mutex_dict = mutex_instance.to_dict()
# create an instance of Mutex from a dict
mutex_form_dict = mutex.from_dict(mutex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


