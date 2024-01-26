# WorkflowSuspendRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_suspend_request import WorkflowSuspendRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSuspendRequest from a JSON string
workflow_suspend_request_instance = WorkflowSuspendRequest.from_json(json)
# print the JSON string representation of the object
print WorkflowSuspendRequest.to_json()

# convert the object into a dict
workflow_suspend_request_dict = workflow_suspend_request_instance.to_dict()
# create an instance of WorkflowSuspendRequest from a dict
workflow_suspend_request_form_dict = workflow_suspend_request.from_dict(workflow_suspend_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


