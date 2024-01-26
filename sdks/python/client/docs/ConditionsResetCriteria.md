# ConditionsResetCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**by_time** | [**ConditionsResetByTime**](ConditionsResetByTime.md) |  | [optional] 

## Example

```python
from argo_workflows.models.conditions_reset_criteria import ConditionsResetCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionsResetCriteria from a JSON string
conditions_reset_criteria_instance = ConditionsResetCriteria.from_json(json)
# print the JSON string representation of the object
print ConditionsResetCriteria.to_json()

# convert the object into a dict
conditions_reset_criteria_dict = conditions_reset_criteria_instance.to_dict()
# create an instance of ConditionsResetCriteria from a dict
conditions_reset_criteria_form_dict = conditions_reset_criteria.from_dict(conditions_reset_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


