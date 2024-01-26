# ClusterWorkflowTemplateUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | DEPRECATED: This field is ignored. | [optional] 
**template** | [**ClusterWorkflowTemplate**](ClusterWorkflowTemplate.md) |  | [optional] 

## Example

```python
from argo_workflows.models.cluster_workflow_template_update_request import ClusterWorkflowTemplateUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterWorkflowTemplateUpdateRequest from a JSON string
cluster_workflow_template_update_request_instance = ClusterWorkflowTemplateUpdateRequest.from_json(json)
# print the JSON string representation of the object
print ClusterWorkflowTemplateUpdateRequest.to_json()

# convert the object into a dict
cluster_workflow_template_update_request_dict = cluster_workflow_template_update_request_instance.to_dict()
# create an instance of ClusterWorkflowTemplateUpdateRequest from a dict
cluster_workflow_template_update_request_form_dict = cluster_workflow_template_update_request.from_dict(cluster_workflow_template_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


