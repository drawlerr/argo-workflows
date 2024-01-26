# GithubAppCreds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] 
**installation_id** | **str** |  | [optional] 
**private_key** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.github_app_creds import GithubAppCreds

# TODO update the JSON string below
json = "{}"
# create an instance of GithubAppCreds from a JSON string
github_app_creds_instance = GithubAppCreds.from_json(json)
# print the JSON string representation of the object
print GithubAppCreds.to_json()

# convert the object into a dict
github_app_creds_dict = github_app_creds_instance.to_dict()
# create an instance of GithubAppCreds from a dict
github_app_creds_form_dict = github_app_creds.from_dict(github_app_creds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


