# WebhookContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**endpoint** | **str** |  | [optional] 
**max_payload_size** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**method** | **str** |  | [optional] 
**port** | **str** | Port on which HTTP server is listening for incoming events. | [optional] 
**server_cert_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**server_key_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**url** | **str** | URL is the url of the server. | [optional] 

## Example

```python
from argo_workflows.models.webhook_context import WebhookContext

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookContext from a JSON string
webhook_context_instance = WebhookContext.from_json(json)
# print the JSON string representation of the object
print WebhookContext.to_json()

# convert the object into a dict
webhook_context_dict = webhook_context_instance.to_dict()
# create an instance of WebhookContext from a dict
webhook_context_form_dict = webhook_context.from_dict(webhook_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


