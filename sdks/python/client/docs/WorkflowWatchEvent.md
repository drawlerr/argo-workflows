# WorkflowWatchEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | [**Workflow**](Workflow.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_watch_event import WorkflowWatchEvent

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowWatchEvent from a JSON string
workflow_watch_event_instance = WorkflowWatchEvent.from_json(json)
# print the JSON string representation of the object
print WorkflowWatchEvent.to_json()

# convert the object into a dict
workflow_watch_event_dict = workflow_watch_event_instance.to_dict()
# create an instance of WorkflowWatchEvent from a dict
workflow_watch_event_form_dict = workflow_watch_event.from_dict(workflow_watch_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


