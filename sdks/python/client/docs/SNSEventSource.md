# SNSEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**endpoint** | **str** |  | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**region** | **str** |  | [optional] 
**role_arn** | **str** |  | [optional] 
**secret_key** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**topic_arn** | **str** |  | [optional] 
**validate_signature** | **bool** |  | [optional] 
**webhook** | [**WebhookContext**](WebhookContext.md) |  | [optional] 

## Example

```python
from argo_workflows.models.sns_event_source import SNSEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of SNSEventSource from a JSON string
sns_event_source_instance = SNSEventSource.from_json(json)
# print the JSON string representation of the object
print SNSEventSource.to_json()

# convert the object into a dict
sns_event_source_dict = sns_event_source_instance.to_dict()
# create an instance of SNSEventSource from a dict
sns_event_source_form_dict = sns_event_source.from_dict(sns_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


