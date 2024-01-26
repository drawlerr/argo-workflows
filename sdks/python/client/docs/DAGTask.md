# DAGTask

DAGTask represents a node in the graph during DAG execution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | [**Arguments**](Arguments.md) |  | [optional] 
**continue_on** | [**ContinueOn**](ContinueOn.md) |  | [optional] 
**dependencies** | **List[str]** | Dependencies are name of other targets which this depends on | [optional] 
**depends** | **str** | Depends are name of other targets which this depends on | [optional] 
**hooks** | [**Dict[str, LifecycleHook]**](LifecycleHook.md) | Hooks hold the lifecycle hook which is invoked at lifecycle of task, irrespective of the success, failure, or error status of the primary task | [optional] 
**inline** | [**Template**](Template.md) |  | [optional] 
**name** | **str** | Name is the name of the target | 
**on_exit** | **str** | OnExit is a template reference which is invoked at the end of the template, irrespective of the success, failure, or error of the primary template. DEPRECATED: Use Hooks[exit].Template instead. | [optional] 
**template** | **str** | Name of template to execute | [optional] 
**template_ref** | [**TemplateRef**](TemplateRef.md) |  | [optional] 
**when** | **str** | When is an expression in which the task should conditionally execute | [optional] 
**with_items** | **List[object]** | WithItems expands a task into multiple parallel tasks from the items in the list | [optional] 
**with_param** | **str** | WithParam expands a task into multiple parallel tasks from the value in the parameter, which is expected to be a JSON list. | [optional] 
**with_sequence** | [**Sequence**](Sequence.md) |  | [optional] 

## Example

```python
from argo_workflows.models.dag_task import DAGTask

# TODO update the JSON string below
json = "{}"
# create an instance of DAGTask from a JSON string
dag_task_instance = DAGTask.from_json(json)
# print the JSON string representation of the object
print DAGTask.to_json()

# convert the object into a dict
dag_task_dict = dag_task_instance.to_dict()
# create an instance of DAGTask from a dict
dag_task_form_dict = dag_task.from_dict(dag_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


