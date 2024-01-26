# AzureEventsHubEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**fqdn** | **str** |  | [optional] 
**hub_name** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**shared_access_key** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**shared_access_key_name** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.azure_events_hub_event_source import AzureEventsHubEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of AzureEventsHubEventSource from a JSON string
azure_events_hub_event_source_instance = AzureEventsHubEventSource.from_json(json)
# print the JSON string representation of the object
print AzureEventsHubEventSource.to_json()

# convert the object into a dict
azure_events_hub_event_source_dict = azure_events_hub_event_source_instance.to_dict()
# create an instance of AzureEventsHubEventSource from a dict
azure_events_hub_event_source_form_dict = azure_events_hub_event_source.from_dict(azure_events_hub_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


