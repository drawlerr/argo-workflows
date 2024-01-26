# CreateCronWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_options** | [**CreateOptions**](CreateOptions.md) |  | [optional] 
**cron_workflow** | [**CronWorkflow**](CronWorkflow.md) |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.create_cron_workflow_request import CreateCronWorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCronWorkflowRequest from a JSON string
create_cron_workflow_request_instance = CreateCronWorkflowRequest.from_json(json)
# print the JSON string representation of the object
print CreateCronWorkflowRequest.to_json()

# convert the object into a dict
create_cron_workflow_request_dict = create_cron_workflow_request_instance.to_dict()
# create an instance of CreateCronWorkflowRequest from a dict
create_cron_workflow_request_form_dict = create_cron_workflow_request.from_dict(create_cron_workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


