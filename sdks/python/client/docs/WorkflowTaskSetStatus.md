# WorkflowTaskSetStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**Dict[str, NodeResult]**](NodeResult.md) |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_task_set_status import WorkflowTaskSetStatus

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTaskSetStatus from a JSON string
workflow_task_set_status_instance = WorkflowTaskSetStatus.from_json(json)
# print the JSON string representation of the object
print WorkflowTaskSetStatus.to_json()

# convert the object into a dict
workflow_task_set_status_dict = workflow_task_set_status_instance.to_dict()
# create an instance of WorkflowTaskSetStatus from a dict
workflow_task_set_status_form_dict = workflow_task_set_status.from_dict(workflow_task_set_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


