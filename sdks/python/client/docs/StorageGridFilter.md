# StorageGridFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** |  | [optional] 
**suffix** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.storage_grid_filter import StorageGridFilter

# TODO update the JSON string below
json = "{}"
# create an instance of StorageGridFilter from a JSON string
storage_grid_filter_instance = StorageGridFilter.from_json(json)
# print the JSON string representation of the object
print StorageGridFilter.to_json()

# convert the object into a dict
storage_grid_filter_dict = storage_grid_filter_instance.to_dict()
# create an instance of StorageGridFilter from a dict
storage_grid_filter_form_dict = storage_grid_filter.from_dict(storage_grid_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


