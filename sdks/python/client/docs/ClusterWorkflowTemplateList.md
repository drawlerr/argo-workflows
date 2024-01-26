# ClusterWorkflowTemplateList

ClusterWorkflowTemplateList is list of ClusterWorkflowTemplate resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.io.k8s.community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**items** | [**List[ClusterWorkflowTemplate]**](ClusterWorkflowTemplate.md) |  | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.io.k8s.community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**ListMeta**](ListMeta.md) |  | 

## Example

```python
from argo_workflows.models.cluster_workflow_template_list import ClusterWorkflowTemplateList

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterWorkflowTemplateList from a JSON string
cluster_workflow_template_list_instance = ClusterWorkflowTemplateList.from_json(json)
# print the JSON string representation of the object
print ClusterWorkflowTemplateList.to_json()

# convert the object into a dict
cluster_workflow_template_list_dict = cluster_workflow_template_list_instance.to_dict()
# create an instance of ClusterWorkflowTemplateList from a dict
cluster_workflow_template_list_form_dict = cluster_workflow_template_list.from_dict(cluster_workflow_template_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


