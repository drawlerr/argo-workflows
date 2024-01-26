# PodDisruptionBudgetSpec

PodDisruptionBudgetSpec is a description of a PodDisruptionBudget.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_unavailable** | **str** |  | [optional] 
**min_available** | **str** |  | [optional] 
**selector** | [**LabelSelector**](LabelSelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.pod_disruption_budget_spec import PodDisruptionBudgetSpec

# TODO update the JSON string below
json = "{}"
# create an instance of PodDisruptionBudgetSpec from a JSON string
pod_disruption_budget_spec_instance = PodDisruptionBudgetSpec.from_json(json)
# print the JSON string representation of the object
print PodDisruptionBudgetSpec.to_json()

# convert the object into a dict
pod_disruption_budget_spec_dict = pod_disruption_budget_spec_instance.to_dict()
# create an instance of PodDisruptionBudgetSpec from a dict
pod_disruption_budget_spec_form_dict = pod_disruption_budget_spec.from_dict(pod_disruption_budget_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


