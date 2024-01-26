# Submit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | [**Arguments**](Arguments.md) |  | [optional] 
**metadata** | [**ObjectMeta**](ObjectMeta.md) |  | [optional] 
**workflow_template_ref** | [**WorkflowTemplateRef**](WorkflowTemplateRef.md) |  | 

## Example

```python
from argo_workflows.models.submit import Submit

# TODO update the JSON string below
json = "{}"
# create an instance of Submit from a JSON string
submit_instance = Submit.from_json(json)
# print the JSON string representation of the object
print Submit.to_json()

# convert the object into a dict
submit_dict = submit_instance.to_dict()
# create an instance of Submit from a dict
submit_form_dict = submit.from_dict(submit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


