# Version


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_date** | **str** |  | 
**compiler** | **str** |  | 
**git_commit** | **str** |  | 
**git_tag** | **str** |  | 
**git_tree_state** | **str** |  | 
**go_version** | **str** |  | 
**platform** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from argo_workflows.models.version import Version

# TODO update the JSON string below
json = "{}"
# create an instance of Version from a JSON string
version_instance = Version.from_json(json)
# print the JSON string representation of the object
print Version.to_json()

# convert the object into a dict
version_dict = version_instance.to_dict()
# create an instance of Version from a dict
version_form_dict = version.from_dict(version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


