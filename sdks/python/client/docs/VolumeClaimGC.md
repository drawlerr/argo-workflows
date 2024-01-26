# VolumeClaimGC

VolumeClaimGC describes how to delete volumes from completed Workflows

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | **str** | Strategy is the strategy to use. One of \&quot;OnWorkflowCompletion\&quot;, \&quot;OnWorkflowSuccess\&quot;. Defaults to \&quot;OnWorkflowSuccess\&quot; | [optional] 

## Example

```python
from argo_workflows.models.volume_claim_gc import VolumeClaimGC

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeClaimGC from a JSON string
volume_claim_gc_instance = VolumeClaimGC.from_json(json)
# print the JSON string representation of the object
print VolumeClaimGC.to_json()

# convert the object into a dict
volume_claim_gc_dict = volume_claim_gc_instance.to_dict()
# create an instance of VolumeClaimGC from a dict
volume_claim_gc_form_dict = volume_claim_gc.from_dict(volume_claim_gc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


