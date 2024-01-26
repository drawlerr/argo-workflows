# WorkflowLintRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | **str** |  | [optional] 
**workflow** | [**Workflow**](Workflow.md) |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_lint_request import WorkflowLintRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowLintRequest from a JSON string
workflow_lint_request_instance = WorkflowLintRequest.from_json(json)
# print the JSON string representation of the object
print WorkflowLintRequest.to_json()

# convert the object into a dict
workflow_lint_request_dict = workflow_lint_request_instance.to_dict()
# create an instance of WorkflowLintRequest from a dict
workflow_lint_request_form_dict = workflow_lint_request.from_dict(workflow_lint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


