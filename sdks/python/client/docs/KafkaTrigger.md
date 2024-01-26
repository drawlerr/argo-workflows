# KafkaTrigger

KafkaTrigger refers to the specification of the Kafka trigger.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compress** | **bool** |  | [optional] 
**flush_frequency** | **int** |  | [optional] 
**parameters** | [**List[TriggerParameter]**](TriggerParameter.md) | Parameters is the list of parameters that is applied to resolved Kafka trigger object. | [optional] 
**partition** | **int** | Partition to write data to. | [optional] 
**partitioning_key** | **str** | The partitioning key for the messages put on the Kafka topic. Defaults to broker url. +optional. | [optional] 
**payload** | [**List[TriggerParameter]**](TriggerParameter.md) | Payload is the list of key-value extracted from an event payload to construct the request payload. | [optional] 
**required_acks** | **int** | RequiredAcks used in producer to tell the broker how many replica acknowledgements Defaults to 1 (Only wait for the leader to ack). +optional. | [optional] 
**sasl** | [**SASLConfig**](SASLConfig.md) |  | [optional] 
**tls** | [**TLSConfig**](TLSConfig.md) |  | [optional] 
**topic** | **str** |  | [optional] 
**url** | **str** | URL of the Kafka broker, multiple URLs separated by comma. | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.kafka_trigger import KafkaTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of KafkaTrigger from a JSON string
kafka_trigger_instance = KafkaTrigger.from_json(json)
# print the JSON string representation of the object
print KafkaTrigger.to_json()

# convert the object into a dict
kafka_trigger_dict = kafka_trigger_instance.to_dict()
# create an instance of KafkaTrigger from a dict
kafka_trigger_form_dict = kafka_trigger.from_dict(kafka_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


