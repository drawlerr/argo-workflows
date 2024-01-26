# CronWorkflowList

CronWorkflowList is list of CronWorkflow resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.io.k8s.community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**items** | [**List[CronWorkflow]**](CronWorkflow.md) |  | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.io.k8s.community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**ListMeta**](ListMeta.md) |  | 

## Example

```python
from argo_workflows.models.cron_workflow_list import CronWorkflowList

# TODO update the JSON string below
json = "{}"
# create an instance of CronWorkflowList from a JSON string
cron_workflow_list_instance = CronWorkflowList.from_json(json)
# print the JSON string representation of the object
print CronWorkflowList.to_json()

# convert the object into a dict
cron_workflow_list_dict = cron_workflow_list_instance.to_dict()
# create an instance of CronWorkflowList from a dict
cron_workflow_list_form_dict = cron_workflow_list.from_dict(cron_workflow_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


