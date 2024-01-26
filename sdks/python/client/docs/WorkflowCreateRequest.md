# WorkflowCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_options** | [**CreateOptions**](CreateOptions.md) |  | [optional] 
**instance_id** | **str** | This field is no longer used. | [optional] 
**namespace** | **str** |  | [optional] 
**server_dry_run** | **bool** |  | [optional] 
**workflow** | [**Workflow**](Workflow.md) |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_create_request import WorkflowCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowCreateRequest from a JSON string
workflow_create_request_instance = WorkflowCreateRequest.from_json(json)
# print the JSON string representation of the object
print WorkflowCreateRequest.to_json()

# convert the object into a dict
workflow_create_request_dict = workflow_create_request_instance.to_dict()
# create an instance of WorkflowCreateRequest from a dict
workflow_create_request_form_dict = workflow_create_request.from_dict(workflow_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


