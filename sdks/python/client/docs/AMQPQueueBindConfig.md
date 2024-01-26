# AMQPQueueBindConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**no_wait** | **bool** |  | [optional] 

## Example

```python
from argo_workflows.models.amqp_queue_bind_config import AMQPQueueBindConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AMQPQueueBindConfig from a JSON string
amqp_queue_bind_config_instance = AMQPQueueBindConfig.from_json(json)
# print the JSON string representation of the object
print AMQPQueueBindConfig.to_json()

# convert the object into a dict
amqp_queue_bind_config_dict = amqp_queue_bind_config_instance.to_dict()
# create an instance of AMQPQueueBindConfig from a dict
amqp_queue_bind_config_form_dict = amqp_queue_bind_config.from_dict(amqp_queue_bind_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


