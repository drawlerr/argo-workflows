# OpenWhiskTrigger

OpenWhiskTrigger refers to the specification of the OpenWhisk trigger.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_name** | **str** | Name of the action/function. | [optional] 
**auth_token** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**host** | **str** | Host URL of the OpenWhisk. | [optional] 
**namespace** | **str** | Namespace for the action. Defaults to \&quot;_\&quot;. +optional. | [optional] 
**parameters** | [**List[TriggerParameter]**](TriggerParameter.md) |  | [optional] 
**payload** | [**List[TriggerParameter]**](TriggerParameter.md) | Payload is the list of key-value extracted from an event payload to construct the request payload. | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.open_whisk_trigger import OpenWhiskTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of OpenWhiskTrigger from a JSON string
open_whisk_trigger_instance = OpenWhiskTrigger.from_json(json)
# print the JSON string representation of the object
print OpenWhiskTrigger.to_json()

# convert the object into a dict
open_whisk_trigger_dict = open_whisk_trigger_instance.to_dict()
# create an instance of OpenWhiskTrigger from a dict
open_whisk_trigger_form_dict = open_whisk_trigger.from_dict(open_whisk_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


