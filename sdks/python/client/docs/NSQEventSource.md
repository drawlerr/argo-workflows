# NSQEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** |  | [optional] 
**connection_backoff** | [**Backoff**](Backoff.md) |  | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**host_address** | **str** |  | [optional] 
**json_body** | **bool** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**tls** | [**TLSConfig**](TLSConfig.md) |  | [optional] 
**topic** | **str** | Topic to subscribe to. | [optional] 

## Example

```python
from argo_workflows.models.nsq_event_source import NSQEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of NSQEventSource from a JSON string
nsq_event_source_instance = NSQEventSource.from_json(json)
# print the JSON string representation of the object
print NSQEventSource.to_json()

# convert the object into a dict
nsq_event_source_dict = nsq_event_source_instance.to_dict()
# create an instance of NSQEventSource from a dict
nsq_event_source_form_dict = nsq_event_source.from_dict(nsq_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


