# BitbucketServerEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**bitbucketserver_base_url** | **str** |  | [optional] 
**delete_hook_on_finish** | **bool** |  | [optional] 
**events** | **List[str]** |  | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**project_key** | **str** |  | [optional] 
**repositories** | [**List[BitbucketServerRepository]**](BitbucketServerRepository.md) |  | [optional] 
**repository_slug** | **str** |  | [optional] 
**webhook** | [**WebhookContext**](WebhookContext.md) |  | [optional] 
**webhook_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.bitbucket_server_event_source import BitbucketServerEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of BitbucketServerEventSource from a JSON string
bitbucket_server_event_source_instance = BitbucketServerEventSource.from_json(json)
# print the JSON string representation of the object
print BitbucketServerEventSource.to_json()

# convert the object into a dict
bitbucket_server_event_source_dict = bitbucket_server_event_source_instance.to_dict()
# create an instance of BitbucketServerEventSource from a dict
bitbucket_server_event_source_form_dict = bitbucket_server_event_source.from_dict(bitbucket_server_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


