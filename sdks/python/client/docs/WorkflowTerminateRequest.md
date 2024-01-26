# WorkflowTerminateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_terminate_request import WorkflowTerminateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTerminateRequest from a JSON string
workflow_terminate_request_instance = WorkflowTerminateRequest.from_json(json)
# print the JSON string representation of the object
print WorkflowTerminateRequest.to_json()

# convert the object into a dict
workflow_terminate_request_dict = workflow_terminate_request_instance.to_dict()
# create an instance of WorkflowTerminateRequest from a dict
workflow_terminate_request_form_dict = workflow_terminate_request.from_dict(workflow_terminate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


