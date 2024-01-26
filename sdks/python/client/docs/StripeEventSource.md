# StripeEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**create_webhook** | **bool** |  | [optional] 
**event_filter** | **List[str]** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**webhook** | [**WebhookContext**](WebhookContext.md) |  | [optional] 

## Example

```python
from argo_workflows.models.stripe_event_source import StripeEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of StripeEventSource from a JSON string
stripe_event_source_instance = StripeEventSource.from_json(json)
# print the JSON string representation of the object
print StripeEventSource.to_json()

# convert the object into a dict
stripe_event_source_dict = stripe_event_source_instance.to_dict()
# create an instance of StripeEventSource from a dict
stripe_event_source_form_dict = stripe_event_source.from_dict(stripe_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


