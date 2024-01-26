# StopStrategy

StopStrategy defines if the cron workflow will stop being triggered once a certain condition has been reached, involving a number of runs of the workflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **str** | Condition defines a condition that stops scheduling workflows when evaluates to true. Use the keywords &#x60;failed&#x60; or &#x60;succeeded&#x60; to access the number of failed or successful child workflows. | 

## Example

```python
from argo_workflows.models.stop_strategy import StopStrategy

# TODO update the JSON string below
json = "{}"
# create an instance of StopStrategy from a JSON string
stop_strategy_instance = StopStrategy.from_json(json)
# print the JSON string representation of the object
print StopStrategy.to_json()

# convert the object into a dict
stop_strategy_dict = stop_strategy_instance.to_dict()
# create an instance of StopStrategy from a dict
stop_strategy_form_dict = stop_strategy.from_dict(stop_strategy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


