# SemaphoreHolding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holders** | **List[str]** | Holders stores the list of current holder names in the  | [optional] 
**semaphore** | **str** | Semaphore stores the semaphore name. | [optional] 

## Example

```python
from argo_workflows.models.semaphore_holding import SemaphoreHolding

# TODO update the JSON string below
json = "{}"
# create an instance of SemaphoreHolding from a JSON string
semaphore_holding_instance = SemaphoreHolding.from_json(json)
# print the JSON string representation of the object
print SemaphoreHolding.to_json()

# convert the object into a dict
semaphore_holding_dict = semaphore_holding_instance.to_dict()
# create an instance of SemaphoreHolding from a dict
semaphore_holding_form_dict = semaphore_holding.from_dict(semaphore_holding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


