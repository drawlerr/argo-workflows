# CronWorkflowStatus

CronWorkflowStatus is the status of a CronWorkflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | [**List[ObjectReference]**](ObjectReference.md) | Active is a list of active workflows stemming from this CronWorkflow | 
**conditions** | [**List[Condition]**](Condition.md) | Conditions is a list of conditions the CronWorkflow may have | 
**failed** | **int** | Failed is a counter of how many times a child workflow terminated in failed or errored state | 
**last_scheduled_time** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | 
**phase** | **str** | Phase defines the cron workflow phase. It is changed to Stopped when the stopping condition is achieved which stops new CronWorkflows from running | 
**succeeded** | **int** | Succeeded is a counter of how many times the child workflows had success | 

## Example

```python
from argo_workflows.models.cron_workflow_status import CronWorkflowStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CronWorkflowStatus from a JSON string
cron_workflow_status_instance = CronWorkflowStatus.from_json(json)
# print the JSON string representation of the object
print CronWorkflowStatus.to_json()

# convert the object into a dict
cron_workflow_status_dict = cron_workflow_status_instance.to_dict()
# create an instance of CronWorkflowStatus from a dict
cron_workflow_status_form_dict = cron_workflow_status.from_dict(cron_workflow_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


