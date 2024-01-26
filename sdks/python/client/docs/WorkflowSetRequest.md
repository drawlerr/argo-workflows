# WorkflowSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**node_field_selector** | **str** |  | [optional] 
**output_parameters** | **str** |  | [optional] 
**phase** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_set_request import WorkflowSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSetRequest from a JSON string
workflow_set_request_instance = WorkflowSetRequest.from_json(json)
# print the JSON string representation of the object
print WorkflowSetRequest.to_json()

# convert the object into a dict
workflow_set_request_dict = workflow_set_request_instance.to_dict()
# create an instance of WorkflowSetRequest from a dict
workflow_set_request_form_dict = workflow_set_request.from_dict(workflow_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


