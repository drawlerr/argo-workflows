# CalendarEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclusion_dates** | **List[str]** | ExclusionDates defines the list of DATE-TIME exceptions for recurring events. | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**interval** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**persistence** | [**EventPersistence**](EventPersistence.md) |  | [optional] 
**schedule** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.calendar_event_source import CalendarEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventSource from a JSON string
calendar_event_source_instance = CalendarEventSource.from_json(json)
# print the JSON string representation of the object
print CalendarEventSource.to_json()

# convert the object into a dict
calendar_event_source_dict = calendar_event_source_instance.to_dict()
# create an instance of CalendarEventSource from a dict
calendar_event_source_form_dict = calendar_event_source.from_dict(calendar_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


