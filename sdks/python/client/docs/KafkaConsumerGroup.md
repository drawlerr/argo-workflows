# KafkaConsumerGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** |  | [optional] 
**oldest** | **bool** |  | [optional] 
**rebalance_strategy** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.kafka_consumer_group import KafkaConsumerGroup

# TODO update the JSON string below
json = "{}"
# create an instance of KafkaConsumerGroup from a JSON string
kafka_consumer_group_instance = KafkaConsumerGroup.from_json(json)
# print the JSON string representation of the object
print KafkaConsumerGroup.to_json()

# convert the object into a dict
kafka_consumer_group_dict = kafka_consumer_group_instance.to_dict()
# create an instance of KafkaConsumerGroup from a dict
kafka_consumer_group_form_dict = kafka_consumer_group.from_dict(kafka_consumer_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


