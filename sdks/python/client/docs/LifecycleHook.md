# LifecycleHook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | [**Arguments**](Arguments.md) |  | [optional] 
**expression** | **str** | Expression is a condition expression for when a node will be retried. If it evaluates to false, the node will not be retried and the retry strategy will be ignored | [optional] 
**template** | **str** | Template is the name of the template to execute by the hook | [optional] 
**template_ref** | [**TemplateRef**](TemplateRef.md) |  | [optional] 

## Example

```python
from argo_workflows.models.lifecycle_hook import LifecycleHook

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleHook from a JSON string
lifecycle_hook_instance = LifecycleHook.from_json(json)
# print the JSON string representation of the object
print LifecycleHook.to_json()

# convert the object into a dict
lifecycle_hook_dict = lifecycle_hook_instance.to_dict()
# create an instance of LifecycleHook from a dict
lifecycle_hook_form_dict = lifecycle_hook.from_dict(lifecycle_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


