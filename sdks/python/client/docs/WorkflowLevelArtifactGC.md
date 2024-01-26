# WorkflowLevelArtifactGC

WorkflowLevelArtifactGC describes how to delete artifacts from completed Workflows - this spec is used on the Workflow level

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_finalizer_removal** | **bool** | ForceFinalizerRemoval: if set to true, the finalizer will be removed in the case that Artifact GC fails | [optional] 
**pod_metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**pod_spec_patch** | **str** | PodSpecPatch holds strategic merge patch to apply against the artgc pod spec. | [optional] 
**service_account_name** | **str** | ServiceAccountName is an optional field for specifying the Service Account that should be assigned to the Pod doing the deletion | [optional] 
**strategy** | **str** | Strategy is the strategy to use. | [optional] 

## Example

```python
from argo_workflows.models.workflow_level_artifact_gc import WorkflowLevelArtifactGC

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowLevelArtifactGC from a JSON string
workflow_level_artifact_gc_instance = WorkflowLevelArtifactGC.from_json(json)
# print the JSON string representation of the object
print WorkflowLevelArtifactGC.to_json()

# convert the object into a dict
workflow_level_artifact_gc_dict = workflow_level_artifact_gc_instance.to_dict()
# create an instance of WorkflowLevelArtifactGC from a dict
workflow_level_artifact_gc_form_dict = workflow_level_artifact_gc.from_dict(workflow_level_artifact_gc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


