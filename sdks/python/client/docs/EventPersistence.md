# EventPersistence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catchup** | [**CatchupConfiguration**](CatchupConfiguration.md) |  | [optional] 
**config_map** | [**ConfigMapPersistence**](ConfigMapPersistence.md) |  | [optional] 

## Example

```python
from argo_workflows.models.event_persistence import EventPersistence

# TODO update the JSON string below
json = "{}"
# create an instance of EventPersistence from a JSON string
event_persistence_instance = EventPersistence.from_json(json)
# print the JSON string representation of the object
print EventPersistence.to_json()

# convert the object into a dict
event_persistence_dict = event_persistence_instance.to_dict()
# create an instance of EventPersistence from a dict
event_persistence_form_dict = event_persistence.from_dict(event_persistence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


