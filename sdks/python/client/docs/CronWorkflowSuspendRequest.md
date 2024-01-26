# CronWorkflowSuspendRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.cron_workflow_suspend_request import CronWorkflowSuspendRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CronWorkflowSuspendRequest from a JSON string
cron_workflow_suspend_request_instance = CronWorkflowSuspendRequest.from_json(json)
# print the JSON string representation of the object
print CronWorkflowSuspendRequest.to_json()

# convert the object into a dict
cron_workflow_suspend_request_dict = cron_workflow_suspend_request_instance.to_dict()
# create an instance of CronWorkflowSuspendRequest from a dict
cron_workflow_suspend_request_form_dict = cron_workflow_suspend_request.from_dict(cron_workflow_suspend_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


