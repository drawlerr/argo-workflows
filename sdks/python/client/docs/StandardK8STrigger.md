# StandardK8STrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**live_object** | **bool** |  | [optional] 
**operation** | **str** |  | [optional] 
**parameters** | [**List[TriggerParameter]**](TriggerParameter.md) | Parameters is the list of parameters that is applied to resolved K8s trigger object. | [optional] 
**patch_strategy** | **str** |  | [optional] 
**source** | [**ArtifactLocation**](ArtifactLocation.md) |  | [optional] 

## Example

```python
from argo_workflows.models.standard_k8_s_trigger import StandardK8STrigger

# TODO update the JSON string below
json = "{}"
# create an instance of StandardK8STrigger from a JSON string
standard_k8_s_trigger_instance = StandardK8STrigger.from_json(json)
# print the JSON string representation of the object
print StandardK8STrigger.to_json()

# convert the object into a dict
standard_k8_s_trigger_dict = standard_k8_s_trigger_instance.to_dict()
# create an instance of StandardK8STrigger from a dict
standard_k8_s_trigger_form_dict = standard_k8_s_trigger.from_dict(standard_k8_s_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


