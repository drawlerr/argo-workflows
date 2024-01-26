# GitlabEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**delete_hook_on_finish** | **bool** |  | [optional] 
**enable_ssl_verification** | **bool** |  | [optional] 
**events** | **List[str]** | Events are gitlab event to listen to. Refer https://github.com/xanzy/go-gitlab/blob/bf34eca5d13a9f4c3f501d8a97b8ac226d55e4d9/projects.go#L794. | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**gitlab_base_url** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**project_id** | **str** |  | [optional] 
**projects** | **List[str]** |  | [optional] 
**secret_token** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**webhook** | [**WebhookContext**](WebhookContext.md) |  | [optional] 

## Example

```python
from argo_workflows.models.gitlab_event_source import GitlabEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of GitlabEventSource from a JSON string
gitlab_event_source_instance = GitlabEventSource.from_json(json)
# print the JSON string representation of the object
print GitlabEventSource.to_json()

# convert the object into a dict
gitlab_event_source_dict = gitlab_event_source_instance.to_dict()
# create an instance of GitlabEventSource from a dict
gitlab_event_source_form_dict = gitlab_event_source.from_dict(gitlab_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


