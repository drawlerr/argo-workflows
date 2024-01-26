# BitbucketServerRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_key** | **str** |  | [optional] 
**repository_slug** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.bitbucket_server_repository import BitbucketServerRepository

# TODO update the JSON string below
json = "{}"
# create an instance of BitbucketServerRepository from a JSON string
bitbucket_server_repository_instance = BitbucketServerRepository.from_json(json)
# print the JSON string representation of the object
print BitbucketServerRepository.to_json()

# convert the object into a dict
bitbucket_server_repository_dict = bitbucket_server_repository_instance.to_dict()
# create an instance of BitbucketServerRepository from a dict
bitbucket_server_repository_form_dict = bitbucket_server_repository.from_dict(bitbucket_server_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


