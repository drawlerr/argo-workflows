# FileEventSource

FileEventSource describes an event-source for file related events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** |  | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**polling** | **bool** |  | [optional] 
**watch_path_config** | [**WatchPathConfig**](WatchPathConfig.md) |  | [optional] 

## Example

```python
from argo_workflows.models.file_event_source import FileEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of FileEventSource from a JSON string
file_event_source_instance = FileEventSource.from_json(json)
# print the JSON string representation of the object
print FileEventSource.to_json()

# convert the object into a dict
file_event_source_dict = file_event_source_instance.to_dict()
# create an instance of FileEventSource from a dict
file_event_source_form_dict = file_event_source.from_dict(file_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


