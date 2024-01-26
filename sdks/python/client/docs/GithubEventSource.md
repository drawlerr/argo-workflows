# GithubEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**api_token** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**content_type** | **str** |  | [optional] 
**delete_hook_on_finish** | **bool** |  | [optional] 
**events** | **List[str]** |  | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**github_app** | [**GithubAppCreds**](GithubAppCreds.md) |  | [optional] 
**github_base_url** | **str** |  | [optional] 
**github_upload_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**insecure** | **bool** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**organizations** | **List[str]** | Organizations holds the names of organizations (used for organization level webhooks). Not required if Repositories is set. | [optional] 
**owner** | **str** |  | [optional] 
**repositories** | [**List[OwnedRepositories]**](OwnedRepositories.md) | Repositories holds the information of repositories, which uses repo owner as the key, and list of repo names as the value. Not required if Organizations is set. | [optional] 
**repository** | **str** |  | [optional] 
**webhook** | [**WebhookContext**](WebhookContext.md) |  | [optional] 
**webhook_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.github_event_source import GithubEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of GithubEventSource from a JSON string
github_event_source_instance = GithubEventSource.from_json(json)
# print the JSON string representation of the object
print GithubEventSource.to_json()

# convert the object into a dict
github_event_source_dict = github_event_source_instance.to_dict()
# create an instance of GithubEventSource from a dict
github_event_source_form_dict = github_event_source.from_dict(github_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


