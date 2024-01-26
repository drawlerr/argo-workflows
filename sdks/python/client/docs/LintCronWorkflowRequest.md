# LintCronWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron_workflow** | [**CronWorkflow**](CronWorkflow.md) |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.lint_cron_workflow_request import LintCronWorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LintCronWorkflowRequest from a JSON string
lint_cron_workflow_request_instance = LintCronWorkflowRequest.from_json(json)
# print the JSON string representation of the object
print LintCronWorkflowRequest.to_json()

# convert the object into a dict
lint_cron_workflow_request_dict = lint_cron_workflow_request_instance.to_dict()
# create an instance of LintCronWorkflowRequest from a dict
lint_cron_workflow_request_form_dict = lint_cron_workflow_request.from_dict(lint_cron_workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


