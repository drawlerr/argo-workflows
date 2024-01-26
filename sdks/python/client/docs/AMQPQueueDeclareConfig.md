# AMQPQueueDeclareConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | **str** |  | [optional] 
**auto_delete** | **bool** |  | [optional] 
**durable** | **bool** |  | [optional] 
**exclusive** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**no_wait** | **bool** |  | [optional] 

## Example

```python
from argo_workflows.models.amqp_queue_declare_config import AMQPQueueDeclareConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AMQPQueueDeclareConfig from a JSON string
amqp_queue_declare_config_instance = AMQPQueueDeclareConfig.from_json(json)
# print the JSON string representation of the object
print AMQPQueueDeclareConfig.to_json()

# convert the object into a dict
amqp_queue_declare_config_dict = amqp_queue_declare_config_instance.to_dict()
# create an instance of AMQPQueueDeclareConfig from a dict
amqp_queue_declare_config_form_dict = amqp_queue_declare_config.from_dict(amqp_queue_declare_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


