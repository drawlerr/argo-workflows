# CronWorkflowResumeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.cron_workflow_resume_request import CronWorkflowResumeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CronWorkflowResumeRequest from a JSON string
cron_workflow_resume_request_instance = CronWorkflowResumeRequest.from_json(json)
# print the JSON string representation of the object
print CronWorkflowResumeRequest.to_json()

# convert the object into a dict
cron_workflow_resume_request_dict = cron_workflow_resume_request_instance.to_dict()
# create an instance of CronWorkflowResumeRequest from a dict
cron_workflow_resume_request_form_dict = cron_workflow_resume_request.from_dict(cron_workflow_resume_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


