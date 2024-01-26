# EventSourceStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | [optional] 

## Example

```python
from argo_workflows.models.event_source_status import EventSourceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of EventSourceStatus from a JSON string
event_source_status_instance = EventSourceStatus.from_json(json)
# print the JSON string representation of the object
print EventSourceStatus.to_json()

# convert the object into a dict
event_source_status_dict = event_source_status_instance.to_dict()
# create an instance of EventSourceStatus from a dict
event_source_status_form_dict = event_source_status.from_dict(event_source_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


