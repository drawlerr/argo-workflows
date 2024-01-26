# WorkflowResumeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**node_field_selector** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_resume_request import WorkflowResumeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowResumeRequest from a JSON string
workflow_resume_request_instance = WorkflowResumeRequest.from_json(json)
# print the JSON string representation of the object
print WorkflowResumeRequest.to_json()

# convert the object into a dict
workflow_resume_request_dict = workflow_resume_request_instance.to_dict()
# create an instance of WorkflowResumeRequest from a dict
workflow_resume_request_form_dict = workflow_resume_request.from_dict(workflow_resume_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


