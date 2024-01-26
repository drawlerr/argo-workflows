# ParallelSteps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from argo_workflows.models.parallel_steps import ParallelSteps

# TODO update the JSON string below
json = "{}"
# create an instance of ParallelSteps from a JSON string
parallel_steps_instance = ParallelSteps.from_json(json)
# print the JSON string representation of the object
print ParallelSteps.to_json()

# convert the object into a dict
parallel_steps_dict = parallel_steps_instance.to_dict()
# create an instance of ParallelSteps from a dict
parallel_steps_form_dict = parallel_steps.from_dict(parallel_steps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


