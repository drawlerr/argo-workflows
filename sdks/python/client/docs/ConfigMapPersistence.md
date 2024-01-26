# ConfigMapPersistence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_if_not_exist** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.config_map_persistence import ConfigMapPersistence

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigMapPersistence from a JSON string
config_map_persistence_instance = ConfigMapPersistence.from_json(json)
# print the JSON string representation of the object
print ConfigMapPersistence.to_json()

# convert the object into a dict
config_map_persistence_dict = config_map_persistence_instance.to_dict()
# create an instance of ConfigMapPersistence from a dict
config_map_persistence_form_dict = config_map_persistence.from_dict(config_map_persistence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


