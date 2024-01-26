# ArtifactGC

ArtifactGC describes how to delete artifacts from completed Workflows - this is embedded into the WorkflowLevelArtifactGC, and also used for individual Artifacts to override that as needed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod_metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**service_account_name** | **str** | ServiceAccountName is an optional field for specifying the Service Account that should be assigned to the Pod doing the deletion | [optional] 
**strategy** | **str** | Strategy is the strategy to use. | [optional] 

## Example

```python
from argo_workflows.models.artifact_gc import ArtifactGC

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactGC from a JSON string
artifact_gc_instance = ArtifactGC.from_json(json)
# print the JSON string representation of the object
print ArtifactGC.to_json()

# convert the object into a dict
artifact_gc_dict = artifact_gc_instance.to_dict()
# create an instance of ArtifactGC from a dict
artifact_gc_form_dict = artifact_gc.from_dict(artifact_gc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


