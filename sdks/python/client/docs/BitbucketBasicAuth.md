# BitbucketBasicAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**username** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.bitbucket_basic_auth import BitbucketBasicAuth

# TODO update the JSON string below
json = "{}"
# create an instance of BitbucketBasicAuth from a JSON string
bitbucket_basic_auth_instance = BitbucketBasicAuth.from_json(json)
# print the JSON string representation of the object
print BitbucketBasicAuth.to_json()

# convert the object into a dict
bitbucket_basic_auth_dict = bitbucket_basic_auth_instance.to_dict()
# create an instance of BitbucketBasicAuth from a dict
bitbucket_basic_auth_form_dict = bitbucket_basic_auth.from_dict(bitbucket_basic_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


