# WatchPathConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directory** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**path_regexp** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.watch_path_config import WatchPathConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WatchPathConfig from a JSON string
watch_path_config_instance = WatchPathConfig.from_json(json)
# print the JSON string representation of the object
print WatchPathConfig.to_json()

# convert the object into a dict
watch_path_config_dict = watch_path_config_instance.to_dict()
# create an instance of WatchPathConfig from a dict
watch_path_config_form_dict = watch_path_config.from_dict(watch_path_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


