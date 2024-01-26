# Inputs

Inputs are the mechanism for passing parameters, artifacts, volumes from one template to another

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifacts** | [**List[Artifact]**](Artifact.md) | Artifact are a list of artifacts passed as inputs | [optional] 
**parameters** | [**List[Parameter]**](Parameter.md) | Parameters are a list of parameters passed as inputs | [optional] 

## Example

```python
from argo_workflows.models.inputs import Inputs

# TODO update the JSON string below
json = "{}"
# create an instance of Inputs from a JSON string
inputs_instance = Inputs.from_json(json)
# print the JSON string representation of the object
print Inputs.to_json()

# convert the object into a dict
inputs_dict = inputs_instance.to_dict()
# create an instance of Inputs from a dict
inputs_form_dict = inputs.from_dict(inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


