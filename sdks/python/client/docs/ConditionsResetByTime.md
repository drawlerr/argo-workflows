# ConditionsResetByTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.conditions_reset_by_time import ConditionsResetByTime

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionsResetByTime from a JSON string
conditions_reset_by_time_instance = ConditionsResetByTime.from_json(json)
# print the JSON string representation of the object
print ConditionsResetByTime.to_json()

# convert the object into a dict
conditions_reset_by_time_dict = conditions_reset_by_time_instance.to_dict()
# create an instance of ConditionsResetByTime from a dict
conditions_reset_by_time_form_dict = conditions_reset_by_time.from_dict(conditions_reset_by_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


