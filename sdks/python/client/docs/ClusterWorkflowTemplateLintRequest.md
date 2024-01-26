# ClusterWorkflowTemplateLintRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_options** | [**CreateOptions**](CreateOptions.md) |  | [optional] 
**template** | [**ClusterWorkflowTemplate**](ClusterWorkflowTemplate.md) |  | [optional] 

## Example

```python
from argo_workflows.models.cluster_workflow_template_lint_request import ClusterWorkflowTemplateLintRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterWorkflowTemplateLintRequest from a JSON string
cluster_workflow_template_lint_request_instance = ClusterWorkflowTemplateLintRequest.from_json(json)
# print the JSON string representation of the object
print ClusterWorkflowTemplateLintRequest.to_json()

# convert the object into a dict
cluster_workflow_template_lint_request_dict = cluster_workflow_template_lint_request_instance.to_dict()
# create an instance of ClusterWorkflowTemplateLintRequest from a dict
cluster_workflow_template_lint_request_form_dict = cluster_workflow_template_lint_request.from_dict(cluster_workflow_template_lint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


