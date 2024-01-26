# WorkflowSubmitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | **str** |  | [optional] 
**resource_kind** | **str** |  | [optional] 
**resource_name** | **str** |  | [optional] 
**submit_options** | [**SubmitOpts**](SubmitOpts.md) |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_submit_request import WorkflowSubmitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSubmitRequest from a JSON string
workflow_submit_request_instance = WorkflowSubmitRequest.from_json(json)
# print the JSON string representation of the object
print WorkflowSubmitRequest.to_json()

# convert the object into a dict
workflow_submit_request_dict = workflow_submit_request_instance.to_dict()
# create an instance of WorkflowSubmitRequest from a dict
workflow_submit_request_form_dict = workflow_submit_request.from_dict(workflow_submit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


