# Parameter

Parameter indicate a passed string parameter to a service template with an optional default value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Default is the default value to use for an input parameter if a value was not supplied | [optional] 
**description** | **str** | Description is the parameter description | [optional] 
**enum** | **List[str]** | Enum holds a list of string values to choose from, for the actual value of the parameter | [optional] 
**global_name** | **str** | GlobalName exports an output parameter to the global scope, making it available as &#39;{{outputs.parameters.XXXX}} and in workflow.status.outputs.parameters | [optional] 
**name** | **str** | Name is the parameter name | 
**value** | **str** | Value is the literal value to use for the parameter. If specified in the context of an input parameter, the value takes precedence over any passed values | [optional] 
**value_from** | [**ValueFrom**](ValueFrom.md) |  | [optional] 

## Example

```python
from argo_workflows.models.parameter import Parameter

# TODO update the JSON string below
json = "{}"
# create an instance of Parameter from a JSON string
parameter_instance = Parameter.from_json(json)
# print the JSON string representation of the object
print Parameter.to_json()

# convert the object into a dict
parameter_dict = parameter_instance.to_dict()
# create an instance of Parameter from a dict
parameter_form_dict = parameter.from_dict(parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


