# NATSEventsSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**NATSAuth**](NATSAuth.md) |  | [optional] 
**connection_backoff** | [**Backoff**](Backoff.md) |  | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**json_body** | **bool** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**subject** | **str** |  | [optional] 
**tls** | [**TLSConfig**](TLSConfig.md) |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.nats_events_source import NATSEventsSource

# TODO update the JSON string below
json = "{}"
# create an instance of NATSEventsSource from a JSON string
nats_events_source_instance = NATSEventsSource.from_json(json)
# print the JSON string representation of the object
print NATSEventsSource.to_json()

# convert the object into a dict
nats_events_source_dict = nats_events_source_instance.to_dict()
# create an instance of NATSEventsSource from a dict
nats_events_source_form_dict = nats_events_source.from_dict(nats_events_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


