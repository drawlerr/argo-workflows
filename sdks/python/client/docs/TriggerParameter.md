# TriggerParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest** | **str** | Dest is the JSONPath of a resource key. A path is a series of keys separated by a dot. The colon character can be escaped with &#39;.&#39; The -1 key can be used to append a value to an existing array. See https://github.com/tidwall/sjson#path-syntax for more information about how this is used. | [optional] 
**operation** | **str** | Operation is what to do with the existing value at Dest, whether to &#39;prepend&#39;, &#39;overwrite&#39;, or &#39;append&#39; it. | [optional] 
**src** | [**TriggerParameterSource**](TriggerParameterSource.md) |  | [optional] 

## Example

```python
from argo_workflows.models.trigger_parameter import TriggerParameter

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerParameter from a JSON string
trigger_parameter_instance = TriggerParameter.from_json(json)
# print the JSON string representation of the object
print TriggerParameter.to_json()

# convert the object into a dict
trigger_parameter_dict = trigger_parameter_instance.to_dict()
# create an instance of TriggerParameter from a dict
trigger_parameter_form_dict = trigger_parameter.from_dict(trigger_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


