# StreamResultOfWorkflowWatchEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**GrpcGatewayRuntimeStreamError**](GrpcGatewayRuntimeStreamError.md) |  | [optional] 
**result** | [**WorkflowWatchEvent**](WorkflowWatchEvent.md) |  | [optional] 

## Example

```python
from argo_workflows.models.stream_result_of_workflow_watch_event import StreamResultOfWorkflowWatchEvent

# TODO update the JSON string below
json = "{}"
# create an instance of StreamResultOfWorkflowWatchEvent from a JSON string
stream_result_of_workflow_watch_event_instance = StreamResultOfWorkflowWatchEvent.from_json(json)
# print the JSON string representation of the object
print StreamResultOfWorkflowWatchEvent.to_json()

# convert the object into a dict
stream_result_of_workflow_watch_event_dict = stream_result_of_workflow_watch_event_instance.to_dict()
# create an instance of StreamResultOfWorkflowWatchEvent from a dict
stream_result_of_workflow_watch_event_form_dict = stream_result_of_workflow_watch_event.from_dict(stream_result_of_workflow_watch_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


