# WorkflowTemplateRef

WorkflowTemplateRef is a reference to a WorkflowTemplate resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_scope** | **bool** | ClusterScope indicates the referred template is cluster scoped (i.e. a ClusterWorkflowTemplate). | [optional] 
**name** | **str** | Name is the resource name of the workflow template. | [optional] 

## Example

```python
from argo_workflows.models.workflow_template_ref import WorkflowTemplateRef

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTemplateRef from a JSON string
workflow_template_ref_instance = WorkflowTemplateRef.from_json(json)
# print the JSON string representation of the object
print WorkflowTemplateRef.to_json()

# convert the object into a dict
workflow_template_ref_dict = workflow_template_ref_instance.to_dict()
# create an instance of WorkflowTemplateRef from a dict
workflow_template_ref_form_dict = workflow_template_ref.from_dict(workflow_template_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


