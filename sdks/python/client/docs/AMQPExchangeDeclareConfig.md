# AMQPExchangeDeclareConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_delete** | **bool** |  | [optional] 
**durable** | **bool** |  | [optional] 
**internal** | **bool** |  | [optional] 
**no_wait** | **bool** |  | [optional] 

## Example

```python
from argo_workflows.models.amqp_exchange_declare_config import AMQPExchangeDeclareConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AMQPExchangeDeclareConfig from a JSON string
amqp_exchange_declare_config_instance = AMQPExchangeDeclareConfig.from_json(json)
# print the JSON string representation of the object
print AMQPExchangeDeclareConfig.to_json()

# convert the object into a dict
amqp_exchange_declare_config_dict = amqp_exchange_declare_config_instance.to_dict()
# create an instance of AMQPExchangeDeclareConfig from a dict
amqp_exchange_declare_config_form_dict = amqp_exchange_declare_config.from_dict(amqp_exchange_declare_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


