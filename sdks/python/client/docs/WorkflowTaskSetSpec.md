# WorkflowTaskSetSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tasks** | [**Dict[str, Template]**](Template.md) |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_task_set_spec import WorkflowTaskSetSpec

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTaskSetSpec from a JSON string
workflow_task_set_spec_instance = WorkflowTaskSetSpec.from_json(json)
# print the JSON string representation of the object
print WorkflowTaskSetSpec.to_json()

# convert the object into a dict
workflow_task_set_spec_dict = workflow_task_set_spec_instance.to_dict()
# create an instance of WorkflowTaskSetSpec from a dict
workflow_task_set_spec_form_dict = workflow_task_set_spec.from_dict(workflow_task_set_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


