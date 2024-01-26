# WorkflowTemplateCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_options** | [**CreateOptions**](CreateOptions.md) |  | [optional] 
**namespace** | **str** |  | [optional] 
**template** | [**WorkflowTemplate**](WorkflowTemplate.md) |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_template_create_request import WorkflowTemplateCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTemplateCreateRequest from a JSON string
workflow_template_create_request_instance = WorkflowTemplateCreateRequest.from_json(json)
# print the JSON string representation of the object
print WorkflowTemplateCreateRequest.to_json()

# convert the object into a dict
workflow_template_create_request_dict = workflow_template_create_request_instance.to_dict()
# create an instance of WorkflowTemplateCreateRequest from a dict
workflow_template_create_request_form_dict = workflow_template_create_request.from_dict(workflow_template_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


