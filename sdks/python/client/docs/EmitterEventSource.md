# EmitterEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**broker** | **str** | Broker URI to connect to. | [optional] 
**channel_key** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**connection_backoff** | [**Backoff**](Backoff.md) |  | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**json_body** | **bool** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**password** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**tls** | [**TLSConfig**](TLSConfig.md) |  | [optional] 
**username** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.emitter_event_source import EmitterEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of EmitterEventSource from a JSON string
emitter_event_source_instance = EmitterEventSource.from_json(json)
# print the JSON string representation of the object
print EmitterEventSource.to_json()

# convert the object into a dict
emitter_event_source_dict = emitter_event_source_instance.to_dict()
# create an instance of EmitterEventSource from a dict
emitter_event_source_form_dict = emitter_event_source.from_dict(emitter_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


