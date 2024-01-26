# CustomTrigger

CustomTrigger refers to the specification of the custom trigger.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**parameters** | [**List[TriggerParameter]**](TriggerParameter.md) | Parameters is the list of parameters that is applied to resolved custom trigger trigger object. | [optional] 
**payload** | [**List[TriggerParameter]**](TriggerParameter.md) | Payload is the list of key-value extracted from an event payload to construct the request payload. | [optional] 
**secure** | **bool** |  | [optional] 
**server_name_override** | **str** | ServerNameOverride for the secure connection between sensor and custom trigger gRPC server. | [optional] 
**server_url** | **str** |  | [optional] 
**spec** | **Dict[str, str]** | Spec is the custom trigger resource specification that custom trigger gRPC server knows how to interpret. | [optional] 

## Example

```python
from argo_workflows.models.custom_trigger import CustomTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of CustomTrigger from a JSON string
custom_trigger_instance = CustomTrigger.from_json(json)
# print the JSON string representation of the object
print CustomTrigger.to_json()

# convert the object into a dict
custom_trigger_dict = custom_trigger_instance.to_dict()
# create an instance of CustomTrigger from a dict
custom_trigger_form_dict = custom_trigger.from_dict(custom_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


