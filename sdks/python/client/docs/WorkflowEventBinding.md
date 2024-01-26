# WorkflowEventBinding

WorkflowEventBinding is the definition of an event resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.io.k8s.community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.io.k8s.community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**ObjectMeta**](ObjectMeta.md) |  | 
**spec** | [**WorkflowEventBindingSpec**](WorkflowEventBindingSpec.md) |  | 

## Example

```python
from argo_workflows.models.workflow_event_binding import WorkflowEventBinding

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowEventBinding from a JSON string
workflow_event_binding_instance = WorkflowEventBinding.from_json(json)
# print the JSON string representation of the object
print WorkflowEventBinding.to_json()

# convert the object into a dict
workflow_event_binding_dict = workflow_event_binding_instance.to_dict()
# create an instance of WorkflowEventBinding from a dict
workflow_event_binding_form_dict = workflow_event_binding.from_dict(workflow_event_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


