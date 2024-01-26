# SASLConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mechanism** | **str** |  | [optional] 
**password** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**user** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.sasl_config import SASLConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SASLConfig from a JSON string
sasl_config_instance = SASLConfig.from_json(json)
# print the JSON string representation of the object
print SASLConfig.to_json()

# convert the object into a dict
sasl_config_dict = sasl_config_instance.to_dict()
# create an instance of SASLConfig from a dict
sasl_config_form_dict = sasl_config.from_dict(sasl_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


