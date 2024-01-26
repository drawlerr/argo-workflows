# WorkflowTemplateUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | DEPRECATED: This field is ignored. | [optional] 
**namespace** | **str** |  | [optional] 
**template** | [**WorkflowTemplate**](WorkflowTemplate.md) |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_template_update_request import WorkflowTemplateUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTemplateUpdateRequest from a JSON string
workflow_template_update_request_instance = WorkflowTemplateUpdateRequest.from_json(json)
# print the JSON string representation of the object
print WorkflowTemplateUpdateRequest.to_json()

# convert the object into a dict
workflow_template_update_request_dict = workflow_template_update_request_instance.to_dict()
# create an instance of WorkflowTemplateUpdateRequest from a dict
workflow_template_update_request_form_dict = workflow_template_update_request.from_dict(workflow_template_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


