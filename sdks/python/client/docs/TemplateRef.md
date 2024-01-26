# TemplateRef

TemplateRef is a reference of template resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_scope** | **bool** | ClusterScope indicates the referred template is cluster scoped (i.e. a ClusterWorkflowTemplate). | [optional] 
**name** | **str** | Name is the resource name of the template. | [optional] 
**template** | **str** | Template is the name of referred template in the resource. | [optional] 

## Example

```python
from argo_workflows.models.template_ref import TemplateRef

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateRef from a JSON string
template_ref_instance = TemplateRef.from_json(json)
# print the JSON string representation of the object
print TemplateRef.to_json()

# convert the object into a dict
template_ref_dict = template_ref_instance.to_dict()
# create an instance of TemplateRef from a dict
template_ref_form_dict = template_ref.from_dict(template_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


