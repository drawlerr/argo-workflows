# CatchupConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**max_duration** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.catchup_configuration import CatchupConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CatchupConfiguration from a JSON string
catchup_configuration_instance = CatchupConfiguration.from_json(json)
# print the JSON string representation of the object
print CatchupConfiguration.to_json()

# convert the object into a dict
catchup_configuration_dict = catchup_configuration_instance.to_dict()
# create an instance of CatchupConfiguration from a dict
catchup_configuration_form_dict = catchup_configuration.from_dict(catchup_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


