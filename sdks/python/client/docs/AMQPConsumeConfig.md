# AMQPConsumeConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_ack** | **bool** |  | [optional] 
**consumer_tag** | **str** |  | [optional] 
**exclusive** | **bool** |  | [optional] 
**no_local** | **bool** |  | [optional] 
**no_wait** | **bool** |  | [optional] 

## Example

```python
from argo_workflows.models.amqp_consume_config import AMQPConsumeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AMQPConsumeConfig from a JSON string
amqp_consume_config_instance = AMQPConsumeConfig.from_json(json)
# print the JSON string representation of the object
print AMQPConsumeConfig.to_json()

# convert the object into a dict
amqp_consume_config_dict = amqp_consume_config_instance.to_dict()
# create an instance of AMQPConsumeConfig from a dict
amqp_consume_config_form_dict = amqp_consume_config.from_dict(amqp_consume_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


