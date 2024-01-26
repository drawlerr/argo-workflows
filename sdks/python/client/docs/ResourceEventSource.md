# ResourceEventSource

ResourceEventSource refers to a event-source for K8s resource related events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_types** | **List[str]** | EventTypes is the list of event type to watch. Possible values are - ADD, UPDATE and DELETE. | [optional] 
**filter** | [**ResourceFilter**](ResourceFilter.md) |  | [optional] 
**group_version_resource** | [**GroupVersionResource**](GroupVersionResource.md) |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.resource_event_source import ResourceEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceEventSource from a JSON string
resource_event_source_instance = ResourceEventSource.from_json(json)
# print the JSON string representation of the object
print ResourceEventSource.to_json()

# convert the object into a dict
resource_event_source_dict = resource_event_source_instance.to_dict()
# create an instance of ResourceEventSource from a dict
resource_event_source_form_dict = resource_event_source.from_dict(resource_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


