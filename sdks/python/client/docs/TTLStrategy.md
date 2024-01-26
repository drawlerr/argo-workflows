# TTLStrategy

TTLStrategy is the strategy for the time to live depending on if the workflow succeeded or failed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds_after_completion** | **int** | SecondsAfterCompletion is the number of seconds to live after completion | [optional] 
**seconds_after_failure** | **int** | SecondsAfterFailure is the number of seconds to live after failure | [optional] 
**seconds_after_success** | **int** | SecondsAfterSuccess is the number of seconds to live after success | [optional] 

## Example

```python
from argo_workflows.models.ttl_strategy import TTLStrategy

# TODO update the JSON string below
json = "{}"
# create an instance of TTLStrategy from a JSON string
ttl_strategy_instance = TTLStrategy.from_json(json)
# print the JSON string representation of the object
print TTLStrategy.to_json()

# convert the object into a dict
ttl_strategy_dict = ttl_strategy_instance.to_dict()
# create an instance of TTLStrategy from a dict
ttl_strategy_form_dict = ttl_strategy.from_dict(ttl_strategy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


