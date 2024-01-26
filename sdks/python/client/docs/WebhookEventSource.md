# WebhookEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**webhook_context** | [**WebhookContext**](WebhookContext.md) |  | [optional] 

## Example

```python
from argo_workflows.models.webhook_event_source import WebhookEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEventSource from a JSON string
webhook_event_source_instance = WebhookEventSource.from_json(json)
# print the JSON string representation of the object
print WebhookEventSource.to_json()

# convert the object into a dict
webhook_event_source_dict = webhook_event_source_instance.to_dict()
# create an instance of WebhookEventSource from a dict
webhook_event_source_form_dict = webhook_event_source.from_dict(webhook_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


