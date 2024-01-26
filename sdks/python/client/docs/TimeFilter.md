# TimeFilter

TimeFilter describes a window in time. It filters out events that occur outside the time limits. In other words, only events that occur after Start and before Stop will pass this filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | Start is the beginning of a time window in UTC. Before this time, events for this dependency are ignored. Format is hh:mm:ss. | [optional] 
**stop** | **str** | Stop is the end of a time window in UTC. After or equal to this time, events for this dependency are ignored and Format is hh:mm:ss. If it is smaller than Start, it is treated as next day of Start (e.g.: 22:00:00-01:00:00 means 22:00:00-25:00:00). | [optional] 

## Example

```python
from argo_workflows.models.time_filter import TimeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TimeFilter from a JSON string
time_filter_instance = TimeFilter.from_json(json)
# print the JSON string representation of the object
print TimeFilter.to_json()

# convert the object into a dict
time_filter_dict = time_filter_instance.to_dict()
# create an instance of TimeFilter from a dict
time_filter_form_dict = time_filter.from_dict(time_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


