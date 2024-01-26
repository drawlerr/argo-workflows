# Outputs

Outputs hold parameters, artifacts, and results from a step

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifacts** | [**List[Artifact]**](Artifact.md) | Artifacts holds the list of output artifacts produced by a step | [optional] 
**exit_code** | **str** | ExitCode holds the exit code of a script template | [optional] 
**parameters** | [**List[Parameter]**](Parameter.md) | Parameters holds the list of output parameters produced by a step | [optional] 
**result** | **str** | Result holds the result (stdout) of a script template | [optional] 

## Example

```python
from argo_workflows.models.outputs import Outputs

# TODO update the JSON string below
json = "{}"
# create an instance of Outputs from a JSON string
outputs_instance = Outputs.from_json(json)
# print the JSON string representation of the object
print Outputs.to_json()

# convert the object into a dict
outputs_dict = outputs_instance.to_dict()
# create an instance of Outputs from a dict
outputs_form_dict = outputs.from_dict(outputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


