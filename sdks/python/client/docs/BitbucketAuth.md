# BitbucketAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic** | [**BitbucketBasicAuth**](BitbucketBasicAuth.md) |  | [optional] 
**oauth_token** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.bitbucket_auth import BitbucketAuth

# TODO update the JSON string below
json = "{}"
# create an instance of BitbucketAuth from a JSON string
bitbucket_auth_instance = BitbucketAuth.from_json(json)
# print the JSON string representation of the object
print BitbucketAuth.to_json()

# convert the object into a dict
bitbucket_auth_dict = bitbucket_auth_instance.to_dict()
# create an instance of BitbucketAuth from a dict
bitbucket_auth_form_dict = bitbucket_auth.from_dict(bitbucket_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


