# EventSourceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EventSource]**](EventSource.md) |  | [optional] 
**metadata** | [**ListMeta**](ListMeta.md) |  | [optional] 

## Example

```python
from argo_workflows.models.event_source_list import EventSourceList

# TODO update the JSON string below
json = "{}"
# create an instance of EventSourceList from a JSON string
event_source_list_instance = EventSourceList.from_json(json)
# print the JSON string representation of the object
print EventSourceList.to_json()

# convert the object into a dict
event_source_list_dict = event_source_list_instance.to_dict()
# create an instance of EventSourceList from a dict
event_source_list_form_dict = event_source_list.from_dict(event_source_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


