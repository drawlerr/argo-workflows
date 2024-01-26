# ContinueOn

ContinueOn defines if a workflow should continue even if a task or step fails/errors. It can be specified if the workflow should continue when the pod errors, fails or both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **bool** |  | [optional] 
**failed** | **bool** |  | [optional] 

## Example

```python
from argo_workflows.models.continue_on import ContinueOn

# TODO update the JSON string below
json = "{}"
# create an instance of ContinueOn from a JSON string
continue_on_instance = ContinueOn.from_json(json)
# print the JSON string representation of the object
print ContinueOn.to_json()

# convert the object into a dict
continue_on_dict = continue_on_instance.to_dict()
# create an instance of ContinueOn from a dict
continue_on_form_dict = continue_on.from_dict(continue_on_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


