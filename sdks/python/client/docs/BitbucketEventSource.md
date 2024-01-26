# BitbucketEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**BitbucketAuth**](BitbucketAuth.md) |  | [optional] 
**delete_hook_on_finish** | **bool** |  | [optional] 
**events** | **List[str]** | Events this webhook is subscribed to. | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**owner** | **str** |  | [optional] 
**project_key** | **str** |  | [optional] 
**repositories** | [**List[BitbucketRepository]**](BitbucketRepository.md) |  | [optional] 
**repository_slug** | **str** |  | [optional] 
**webhook** | [**WebhookContext**](WebhookContext.md) |  | [optional] 

## Example

```python
from argo_workflows.models.bitbucket_event_source import BitbucketEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of BitbucketEventSource from a JSON string
bitbucket_event_source_instance = BitbucketEventSource.from_json(json)
# print the JSON string representation of the object
print BitbucketEventSource.to_json()

# convert the object into a dict
bitbucket_event_source_dict = bitbucket_event_source_instance.to_dict()
# create an instance of BitbucketEventSource from a dict
bitbucket_event_source_form_dict = bitbucket_event_source.from_dict(bitbucket_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


