# BitbucketRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | **str** |  | [optional] 
**repository_slug** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.bitbucket_repository import BitbucketRepository

# TODO update the JSON string below
json = "{}"
# create an instance of BitbucketRepository from a JSON string
bitbucket_repository_instance = BitbucketRepository.from_json(json)
# print the JSON string representation of the object
print BitbucketRepository.to_json()

# convert the object into a dict
bitbucket_repository_dict = bitbucket_repository_instance.to_dict()
# create an instance of BitbucketRepository from a dict
bitbucket_repository_form_dict = bitbucket_repository.from_dict(bitbucket_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


