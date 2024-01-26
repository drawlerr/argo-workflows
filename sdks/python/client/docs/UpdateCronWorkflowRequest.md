# UpdateCronWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron_workflow** | [**CronWorkflow**](CronWorkflow.md) |  | [optional] 
**name** | **str** | DEPRECATED: This field is ignored. | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.update_cron_workflow_request import UpdateCronWorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCronWorkflowRequest from a JSON string
update_cron_workflow_request_instance = UpdateCronWorkflowRequest.from_json(json)
# print the JSON string representation of the object
print UpdateCronWorkflowRequest.to_json()

# convert the object into a dict
update_cron_workflow_request_dict = update_cron_workflow_request_instance.to_dict()
# create an instance of UpdateCronWorkflowRequest from a dict
update_cron_workflow_request_form_dict = update_cron_workflow_request.from_dict(update_cron_workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


