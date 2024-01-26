# WorkflowResubmitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memoized** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**parameters** | **List[str]** |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_resubmit_request import WorkflowResubmitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowResubmitRequest from a JSON string
workflow_resubmit_request_instance = WorkflowResubmitRequest.from_json(json)
# print the JSON string representation of the object
print WorkflowResubmitRequest.to_json()

# convert the object into a dict
workflow_resubmit_request_dict = workflow_resubmit_request_instance.to_dict()
# create an instance of WorkflowResubmitRequest from a dict
workflow_resubmit_request_form_dict = workflow_resubmit_request.from_dict(workflow_resubmit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


