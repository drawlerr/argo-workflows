# WorkflowStopRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**node_field_selector** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_stop_request import WorkflowStopRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStopRequest from a JSON string
workflow_stop_request_instance = WorkflowStopRequest.from_json(json)
# print the JSON string representation of the object
print WorkflowStopRequest.to_json()

# convert the object into a dict
workflow_stop_request_dict = workflow_stop_request_instance.to_dict()
# create an instance of WorkflowStopRequest from a dict
workflow_stop_request_form_dict = workflow_stop_request.from_dict(workflow_stop_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


