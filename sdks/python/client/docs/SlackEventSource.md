# SlackEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**signing_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**token** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**webhook** | [**WebhookContext**](WebhookContext.md) |  | [optional] 

## Example

```python
from argo_workflows.models.slack_event_source import SlackEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of SlackEventSource from a JSON string
slack_event_source_instance = SlackEventSource.from_json(json)
# print the JSON string representation of the object
print SlackEventSource.to_json()

# convert the object into a dict
slack_event_source_dict = slack_event_source_instance.to_dict()
# create an instance of SlackEventSource from a dict
slack_event_source_form_dict = slack_event_source.from_dict(slack_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


