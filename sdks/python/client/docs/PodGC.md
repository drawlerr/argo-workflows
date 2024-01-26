# PodGC

PodGC describes how to delete completed pods as they complete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_delay_duration** | [**Duration**](Duration.md) |  | [optional] 
**label_selector** | [**LabelSelector**](LabelSelector.md) |  | [optional] 
**strategy** | **str** | Strategy is the strategy to use. One of \&quot;OnPodCompletion\&quot;, \&quot;OnPodSuccess\&quot;, \&quot;OnWorkflowCompletion\&quot;, \&quot;OnWorkflowSuccess\&quot;. If unset, does not delete Pods | [optional] 

## Example

```python
from argo_workflows.models.pod_gc import PodGC

# TODO update the JSON string below
json = "{}"
# create an instance of PodGC from a JSON string
pod_gc_instance = PodGC.from_json(json)
# print the JSON string representation of the object
print PodGC.to_json()

# convert the object into a dict
pod_gc_dict = pod_gc_instance.to_dict()
# create an instance of PodGC from a dict
pod_gc_form_dict = pod_gc.from_dict(pod_gc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


