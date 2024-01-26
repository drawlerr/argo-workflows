# ArtGCStatus

ArtGCStatus maintains state related to ArtifactGC

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**not_specified** | **bool** | if this is true, we already checked to see if we need to do it and we don&#39;t | [optional] 
**pods_recouped** | **Dict[str, bool]** | have completed Pods been processed? (mapped by Pod name) used to prevent re-processing the Status of a Pod more than once | [optional] 
**strategies_processed** | **Dict[str, bool]** | have Pods been started to perform this strategy? (enables us not to re-process what we&#39;ve already done) | [optional] 

## Example

```python
from argo_workflows.models.art_gc_status import ArtGCStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ArtGCStatus from a JSON string
art_gc_status_instance = ArtGCStatus.from_json(json)
# print the JSON string representation of the object
print ArtGCStatus.to_json()

# convert the object into a dict
art_gc_status_dict = art_gc_status_instance.to_dict()
# create an instance of ArtGCStatus from a dict
art_gc_status_form_dict = art_gc_status.from_dict(art_gc_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


