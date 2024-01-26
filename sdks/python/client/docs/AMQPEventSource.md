# AMQPEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**BasicAuth**](BasicAuth.md) |  | [optional] 
**connection_backoff** | [**Backoff**](Backoff.md) |  | [optional] 
**consume** | [**AMQPConsumeConfig**](AMQPConsumeConfig.md) |  | [optional] 
**exchange_declare** | [**AMQPExchangeDeclareConfig**](AMQPExchangeDeclareConfig.md) |  | [optional] 
**exchange_name** | **str** |  | [optional] 
**exchange_type** | **str** |  | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**json_body** | **bool** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**queue_bind** | [**AMQPQueueBindConfig**](AMQPQueueBindConfig.md) |  | [optional] 
**queue_declare** | [**AMQPQueueDeclareConfig**](AMQPQueueDeclareConfig.md) |  | [optional] 
**routing_key** | **str** |  | [optional] 
**tls** | [**TLSConfig**](TLSConfig.md) |  | [optional] 
**url** | **str** |  | [optional] 
**url_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.amqp_event_source import AMQPEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of AMQPEventSource from a JSON string
amqp_event_source_instance = AMQPEventSource.from_json(json)
# print the JSON string representation of the object
print AMQPEventSource.to_json()

# convert the object into a dict
amqp_event_source_dict = amqp_event_source_instance.to_dict()
# create an instance of AMQPEventSource from a dict
amqp_event_source_form_dict = amqp_event_source.from_dict(amqp_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


