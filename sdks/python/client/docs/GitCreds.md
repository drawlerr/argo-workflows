# GitCreds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**username** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.git_creds import GitCreds

# TODO update the JSON string below
json = "{}"
# create an instance of GitCreds from a JSON string
git_creds_instance = GitCreds.from_json(json)
# print the JSON string representation of the object
print GitCreds.to_json()

# convert the object into a dict
git_creds_dict = git_creds_instance.to_dict()
# create an instance of GitCreds from a dict
git_creds_form_dict = git_creds.from_dict(git_creds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


