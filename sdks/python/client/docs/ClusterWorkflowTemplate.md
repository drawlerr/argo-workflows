# ClusterWorkflowTemplate

ClusterWorkflowTemplate is the definition of a workflow template resource in cluster scope

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.io.k8s.community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.io.k8s.community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**ObjectMeta**](ObjectMeta.md) |  | 
**spec** | [**WorkflowSpec**](WorkflowSpec.md) |  | 

## Example

```python
from argo_workflows.models.cluster_workflow_template import ClusterWorkflowTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterWorkflowTemplate from a JSON string
cluster_workflow_template_instance = ClusterWorkflowTemplate.from_json(json)
# print the JSON string representation of the object
print ClusterWorkflowTemplate.to_json()

# convert the object into a dict
cluster_workflow_template_dict = cluster_workflow_template_instance.to_dict()
# create an instance of ClusterWorkflowTemplate from a dict
cluster_workflow_template_form_dict = cluster_workflow_template.from_dict(cluster_workflow_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


