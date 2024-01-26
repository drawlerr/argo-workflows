# RetryArchivedWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**node_field_selector** | **str** |  | [optional] 
**parameters** | **List[str]** |  | [optional] 
**restart_successful** | **bool** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.retry_archived_workflow_request import RetryArchivedWorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RetryArchivedWorkflowRequest from a JSON string
retry_archived_workflow_request_instance = RetryArchivedWorkflowRequest.from_json(json)
# print the JSON string representation of the object
print RetryArchivedWorkflowRequest.to_json()

# convert the object into a dict
retry_archived_workflow_request_dict = retry_archived_workflow_request_instance.to_dict()
# create an instance of RetryArchivedWorkflowRequest from a dict
retry_archived_workflow_request_form_dict = retry_archived_workflow_request.from_dict(retry_archived_workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


