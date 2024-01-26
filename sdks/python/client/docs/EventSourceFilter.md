# EventSourceFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.event_source_filter import EventSourceFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EventSourceFilter from a JSON string
event_source_filter_instance = EventSourceFilter.from_json(json)
# print the JSON string representation of the object
print EventSourceFilter.to_json()

# convert the object into a dict
event_source_filter_dict = event_source_filter_instance.to_dict()
# create an instance of EventSourceFilter from a dict
event_source_filter_form_dict = event_source_filter.from_dict(event_source_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


