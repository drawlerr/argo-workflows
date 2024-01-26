# NATSTrigger

NATSTrigger refers to the specification of the NATS trigger.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**List[TriggerParameter]**](TriggerParameter.md) |  | [optional] 
**payload** | [**List[TriggerParameter]**](TriggerParameter.md) |  | [optional] 
**subject** | **str** | Name of the subject to put message on. | [optional] 
**tls** | [**TLSConfig**](TLSConfig.md) |  | [optional] 
**url** | **str** | URL of the NATS cluster. | [optional] 

## Example

```python
from argo_workflows.models.nats_trigger import NATSTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of NATSTrigger from a JSON string
nats_trigger_instance = NATSTrigger.from_json(json)
# print the JSON string representation of the object
print NATSTrigger.to_json()

# convert the object into a dict
nats_trigger_dict = nats_trigger_instance.to_dict()
# create an instance of NATSTrigger from a dict
nats_trigger_form_dict = nats_trigger.from_dict(nats_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


