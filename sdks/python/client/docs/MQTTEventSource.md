# MQTTEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**connection_backoff** | [**Backoff**](Backoff.md) |  | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**json_body** | **bool** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**tls** | [**TLSConfig**](TLSConfig.md) |  | [optional] 
**topic** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.mqtt_event_source import MQTTEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of MQTTEventSource from a JSON string
mqtt_event_source_instance = MQTTEventSource.from_json(json)
# print the JSON string representation of the object
print MQTTEventSource.to_json()

# convert the object into a dict
mqtt_event_source_dict = mqtt_event_source_instance.to_dict()
# create an instance of MQTTEventSource from a dict
mqtt_event_source_form_dict = mqtt_event_source.from_dict(mqtt_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


