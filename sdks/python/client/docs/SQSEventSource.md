# SQSEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**dlq** | **bool** |  | [optional] 
**endpoint** | **str** |  | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**json_body** | **bool** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**queue** | **str** |  | [optional] 
**queue_account_id** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**role_arn** | **str** |  | [optional] 
**secret_key** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**session_token** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**wait_time_seconds** | **str** | WaitTimeSeconds is The duration (in seconds) for which the call waits for a message to arrive in the queue before returning. | [optional] 

## Example

```python
from argo_workflows.models.sqs_event_source import SQSEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of SQSEventSource from a JSON string
sqs_event_source_instance = SQSEventSource.from_json(json)
# print the JSON string representation of the object
print SQSEventSource.to_json()

# convert the object into a dict
sqs_event_source_dict = sqs_event_source_instance.to_dict()
# create an instance of SQSEventSource from a dict
sqs_event_source_form_dict = sqs_event_source.from_dict(sqs_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


