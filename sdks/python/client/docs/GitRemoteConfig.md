# GitRemoteConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the remote to fetch from. | [optional] 
**urls** | **List[str]** | URLs the URLs of a remote repository. It must be non-empty. Fetch will always use the first URL, while push will use all of them. | [optional] 

## Example

```python
from argo_workflows.models.git_remote_config import GitRemoteConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GitRemoteConfig from a JSON string
git_remote_config_instance = GitRemoteConfig.from_json(json)
# print the JSON string representation of the object
print GitRemoteConfig.to_json()

# convert the object into a dict
git_remote_config_dict = git_remote_config_instance.to_dict()
# create an instance of GitRemoteConfig from a dict
git_remote_config_form_dict = git_remote_config.from_dict(git_remote_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


