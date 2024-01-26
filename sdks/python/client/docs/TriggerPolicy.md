# TriggerPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**k8s** | [**K8SResourcePolicy**](K8SResourcePolicy.md) |  | [optional] 
**status** | [**StatusPolicy**](StatusPolicy.md) |  | [optional] 

## Example

```python
from argo_workflows.models.trigger_policy import TriggerPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerPolicy from a JSON string
trigger_policy_instance = TriggerPolicy.from_json(json)
# print the JSON string representation of the object
print TriggerPolicy.to_json()

# convert the object into a dict
trigger_policy_dict = trigger_policy_instance.to_dict()
# create an instance of TriggerPolicy from a dict
trigger_policy_form_dict = trigger_policy.from_dict(trigger_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


