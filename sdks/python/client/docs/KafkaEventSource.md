# KafkaEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **str** | Yaml format Sarama config for Kafka connection. It follows the struct of sarama.Config. See https://github.com/Shopify/sarama/blob/main/config.go e.g.  consumer:   fetch:     min: 1 net:   MaxOpenRequests: 5  +optional | [optional] 
**connection_backoff** | [**Backoff**](Backoff.md) |  | [optional] 
**consumer_group** | [**KafkaConsumerGroup**](KafkaConsumerGroup.md) |  | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**json_body** | **bool** |  | [optional] 
**limit_events_per_second** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**partition** | **str** |  | [optional] 
**sasl** | [**SASLConfig**](SASLConfig.md) |  | [optional] 
**tls** | [**TLSConfig**](TLSConfig.md) |  | [optional] 
**topic** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.kafka_event_source import KafkaEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of KafkaEventSource from a JSON string
kafka_event_source_instance = KafkaEventSource.from_json(json)
# print the JSON string representation of the object
print KafkaEventSource.to_json()

# convert the object into a dict
kafka_event_source_dict = kafka_event_source_instance.to_dict()
# create an instance of KafkaEventSource from a dict
kafka_event_source_form_dict = kafka_event_source.from_dict(kafka_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


