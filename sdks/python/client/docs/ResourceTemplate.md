# ResourceTemplate

ResourceTemplate is a template subtype to manipulate kubernetes resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action is the action to perform to the resource. Must be one of: get, create, apply, delete, replace, patch | 
**failure_condition** | **str** | FailureCondition is a label selector expression which describes the conditions of the k8s resource in which the step was considered failed | [optional] 
**flags** | **List[str]** | Flags is a set of additional options passed to kubectl before submitting a resource I.e. to disable resource validation: flags: [  \&quot;--validate&#x3D;false\&quot;  # disable resource validation ] | [optional] 
**manifest** | **str** | Manifest contains the kubernetes manifest | [optional] 
**manifest_from** | [**ManifestFrom**](ManifestFrom.md) |  | [optional] 
**merge_strategy** | **str** | MergeStrategy is the strategy used to merge a patch. It defaults to \&quot;strategic\&quot; Must be one of: strategic, merge, json | [optional] 
**set_owner_reference** | **bool** | SetOwnerReference sets the reference to the workflow on the OwnerReference of generated resource. | [optional] 
**success_condition** | **str** | SuccessCondition is a label selector expression which describes the conditions of the k8s resource in which it is acceptable to proceed to the following step | [optional] 

## Example

```python
from argo_workflows.models.resource_template import ResourceTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceTemplate from a JSON string
resource_template_instance = ResourceTemplate.from_json(json)
# print the JSON string representation of the object
print ResourceTemplate.to_json()

# convert the object into a dict
resource_template_dict = resource_template_instance.to_dict()
# create an instance of ResourceTemplate from a dict
resource_template_form_dict = resource_template.from_dict(resource_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


