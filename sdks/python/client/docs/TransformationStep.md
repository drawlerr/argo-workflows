# TransformationStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | Expression defines an expr expression to apply | 

## Example

```python
from argo_workflows.models.transformation_step import TransformationStep

# TODO update the JSON string below
json = "{}"
# create an instance of TransformationStep from a JSON string
transformation_step_instance = TransformationStep.from_json(json)
# print the JSON string representation of the object
print TransformationStep.to_json()

# convert the object into a dict
transformation_step_dict = transformation_step_instance.to_dict()
# create an instance of TransformationStep from a dict
transformation_step_form_dict = transformation_step.from_dict(transformation_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


