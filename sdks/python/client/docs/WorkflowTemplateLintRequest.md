# WorkflowTemplateLintRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_options** | [**CreateOptions**](CreateOptions.md) |  | [optional] 
**namespace** | **str** |  | [optional] 
**template** | [**WorkflowTemplate**](WorkflowTemplate.md) |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_template_lint_request import WorkflowTemplateLintRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTemplateLintRequest from a JSON string
workflow_template_lint_request_instance = WorkflowTemplateLintRequest.from_json(json)
# print the JSON string representation of the object
print WorkflowTemplateLintRequest.to_json()

# convert the object into a dict
workflow_template_lint_request_dict = workflow_template_lint_request_instance.to_dict()
# create an instance of WorkflowTemplateLintRequest from a dict
workflow_template_lint_request_form_dict = workflow_template_lint_request.from_dict(workflow_template_lint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


