# PubSubEventSource

PubSubEventSource refers to event-source for GCP PubSub related events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**delete_subscription_on_finish** | **bool** |  | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**json_body** | **bool** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**project_id** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**topic** | **str** |  | [optional] 
**topic_project_id** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.pub_sub_event_source import PubSubEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of PubSubEventSource from a JSON string
pub_sub_event_source_instance = PubSubEventSource.from_json(json)
# print the JSON string representation of the object
print PubSubEventSource.to_json()

# convert the object into a dict
pub_sub_event_source_dict = pub_sub_event_source_instance.to_dict()
# create an instance of PubSubEventSource from a dict
pub_sub_event_source_form_dict = pub_sub_event_source.from_dict(pub_sub_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


