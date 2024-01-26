# OwnedRepositories


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** |  | [optional] 
**owner** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.owned_repositories import OwnedRepositories

# TODO update the JSON string below
json = "{}"
# create an instance of OwnedRepositories from a JSON string
owned_repositories_instance = OwnedRepositories.from_json(json)
# print the JSON string representation of the object
print OwnedRepositories.to_json()

# convert the object into a dict
owned_repositories_dict = owned_repositories_instance.to_dict()
# create an instance of OwnedRepositories from a dict
owned_repositories_form_dict = owned_repositories.from_dict(owned_repositories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


