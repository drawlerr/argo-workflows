# SemaphoreStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding** | [**List[SemaphoreHolding]**](SemaphoreHolding.md) | Holding stores the list of resource acquired synchronization lock for workflows. | [optional] 
**waiting** | [**List[SemaphoreHolding]**](SemaphoreHolding.md) | Waiting indicates the list of current synchronization lock holders. | [optional] 

## Example

```python
from argo_workflows.models.semaphore_status import SemaphoreStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SemaphoreStatus from a JSON string
semaphore_status_instance = SemaphoreStatus.from_json(json)
# print the JSON string representation of the object
print SemaphoreStatus.to_json()

# convert the object into a dict
semaphore_status_dict = semaphore_status_instance.to_dict()
# create an instance of SemaphoreStatus from a dict
semaphore_status_form_dict = semaphore_status.from_dict(semaphore_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


