# ResubmitArchivedWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memoized** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**parameters** | **List[str]** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.resubmit_archived_workflow_request import ResubmitArchivedWorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResubmitArchivedWorkflowRequest from a JSON string
resubmit_archived_workflow_request_instance = ResubmitArchivedWorkflowRequest.from_json(json)
# print the JSON string representation of the object
print ResubmitArchivedWorkflowRequest.to_json()

# convert the object into a dict
resubmit_archived_workflow_request_dict = resubmit_archived_workflow_request_instance.to_dict()
# create an instance of ResubmitArchivedWorkflowRequest from a dict
resubmit_archived_workflow_request_form_dict = resubmit_archived_workflow_request.from_dict(resubmit_archived_workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


