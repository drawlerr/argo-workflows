# WorkflowStep

WorkflowStep is a reference to a template to execute in a series of step

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | [**Arguments**](Arguments.md) |  | [optional] 
**continue_on** | [**ContinueOn**](ContinueOn.md) |  | [optional] 
**hooks** | [**Dict[str, LifecycleHook]**](LifecycleHook.md) | Hooks holds the lifecycle hook which is invoked at lifecycle of step, irrespective of the success, failure, or error status of the primary step | [optional] 
**inline** | [**Template**](Template.md) |  | [optional] 
**name** | **str** | Name of the step | [optional] 
**on_exit** | **str** | OnExit is a template reference which is invoked at the end of the template, irrespective of the success, failure, or error of the primary template. DEPRECATED: Use Hooks[exit].Template instead. | [optional] 
**template** | **str** | Template is the name of the template to execute as the step | [optional] 
**template_ref** | [**TemplateRef**](TemplateRef.md) |  | [optional] 
**when** | **str** | When is an expression in which the step should conditionally execute | [optional] 
**with_items** | **List[object]** | WithItems expands a step into multiple parallel steps from the items in the list | [optional] 
**with_param** | **str** | WithParam expands a step into multiple parallel steps from the value in the parameter, which is expected to be a JSON list. | [optional] 
**with_sequence** | [**Sequence**](Sequence.md) |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_step import WorkflowStep

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStep from a JSON string
workflow_step_instance = WorkflowStep.from_json(json)
# print the JSON string representation of the object
print WorkflowStep.to_json()

# convert the object into a dict
workflow_step_dict = workflow_step_instance.to_dict()
# create an instance of WorkflowStep from a dict
workflow_step_form_dict = workflow_step.from_dict(workflow_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


