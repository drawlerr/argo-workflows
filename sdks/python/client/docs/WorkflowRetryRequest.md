# WorkflowRetryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**node_field_selector** | **str** |  | [optional] 
**parameters** | **List[str]** |  | [optional] 
**restart_successful** | **bool** |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_retry_request import WorkflowRetryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowRetryRequest from a JSON string
workflow_retry_request_instance = WorkflowRetryRequest.from_json(json)
# print the JSON string representation of the object
print WorkflowRetryRequest.to_json()

# convert the object into a dict
workflow_retry_request_dict = workflow_retry_request_instance.to_dict()
# create an instance of WorkflowRetryRequest from a dict
workflow_retry_request_form_dict = workflow_retry_request.from_dict(workflow_retry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


