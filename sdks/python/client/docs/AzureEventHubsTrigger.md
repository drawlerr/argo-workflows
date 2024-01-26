# AzureEventHubsTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** |  | [optional] 
**hub_name** | **str** |  | [optional] 
**parameters** | [**List[TriggerParameter]**](TriggerParameter.md) |  | [optional] 
**payload** | [**List[TriggerParameter]**](TriggerParameter.md) | Payload is the list of key-value extracted from an event payload to construct the request payload. | [optional] 
**shared_access_key** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**shared_access_key_name** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.azure_event_hubs_trigger import AzureEventHubsTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of AzureEventHubsTrigger from a JSON string
azure_event_hubs_trigger_instance = AzureEventHubsTrigger.from_json(json)
# print the JSON string representation of the object
print AzureEventHubsTrigger.to_json()

# convert the object into a dict
azure_event_hubs_trigger_dict = azure_event_hubs_trigger_instance.to_dict()
# create an instance of AzureEventHubsTrigger from a dict
azure_event_hubs_trigger_form_dict = azure_event_hubs_trigger.from_dict(azure_event_hubs_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


