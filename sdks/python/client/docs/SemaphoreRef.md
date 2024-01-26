# SemaphoreRef

SemaphoreRef is a reference of Semaphore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_map_key_ref** | [**ConfigMapKeySelector**](ConfigMapKeySelector.md) |  | [optional] 
**namespace** | **str** | Namespace is the namespace of the configmap, default: [namespace of workflow] | [optional] 

## Example

```python
from argo_workflows.models.semaphore_ref import SemaphoreRef

# TODO update the JSON string below
json = "{}"
# create an instance of SemaphoreRef from a JSON string
semaphore_ref_instance = SemaphoreRef.from_json(json)
# print the JSON string representation of the object
print SemaphoreRef.to_json()

# convert the object into a dict
semaphore_ref_dict = semaphore_ref_instance.to_dict()
# create an instance of SemaphoreRef from a dict
semaphore_ref_form_dict = semaphore_ref.from_dict(semaphore_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


