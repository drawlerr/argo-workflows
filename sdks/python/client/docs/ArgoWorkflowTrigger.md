# ArgoWorkflowTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **List[str]** |  | [optional] 
**operation** | **str** |  | [optional] 
**parameters** | [**List[TriggerParameter]**](TriggerParameter.md) |  | [optional] 
**source** | [**ArtifactLocation**](ArtifactLocation.md) |  | [optional] 

## Example

```python
from argo_workflows.models.argo_workflow_trigger import ArgoWorkflowTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of ArgoWorkflowTrigger from a JSON string
argo_workflow_trigger_instance = ArgoWorkflowTrigger.from_json(json)
# print the JSON string representation of the object
print ArgoWorkflowTrigger.to_json()

# convert the object into a dict
argo_workflow_trigger_dict = argo_workflow_trigger_instance.to_dict()
# create an instance of ArgoWorkflowTrigger from a dict
argo_workflow_trigger_form_dict = argo_workflow_trigger.from_dict(argo_workflow_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


