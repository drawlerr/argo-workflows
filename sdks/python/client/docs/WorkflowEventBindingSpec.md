# WorkflowEventBindingSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**Event**](Event.md) |  | 
**submit** | [**Submit**](Submit.md) |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_event_binding_spec import WorkflowEventBindingSpec

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowEventBindingSpec from a JSON string
workflow_event_binding_spec_instance = WorkflowEventBindingSpec.from_json(json)
# print the JSON string representation of the object
print WorkflowEventBindingSpec.to_json()

# convert the object into a dict
workflow_event_binding_spec_dict = workflow_event_binding_spec_instance.to_dict()
# create an instance of WorkflowEventBindingSpec from a dict
workflow_event_binding_spec_form_dict = workflow_event_binding_spec.from_dict(workflow_event_binding_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


