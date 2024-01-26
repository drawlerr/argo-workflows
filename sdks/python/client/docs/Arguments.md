# Arguments

Arguments to a template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifacts** | [**List[Artifact]**](Artifact.md) | Artifacts is the list of artifacts to pass to the template or workflow | [optional] 
**parameters** | [**List[Parameter]**](Parameter.md) | Parameters is the list of parameters to pass to the template or workflow | [optional] 

## Example

```python
from argo_workflows.models.arguments import Arguments

# TODO update the JSON string below
json = "{}"
# create an instance of Arguments from a JSON string
arguments_instance = Arguments.from_json(json)
# print the JSON string representation of the object
print Arguments.to_json()

# convert the object into a dict
arguments_dict = arguments_instance.to_dict()
# create an instance of Arguments from a dict
arguments_form_dict = arguments.from_dict(arguments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


