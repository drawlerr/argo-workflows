# K8SResourcePolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backoff** | [**Backoff**](Backoff.md) |  | [optional] 
**error_on_backoff_timeout** | **bool** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 

## Example

```python
from argo_workflows.models.k8_s_resource_policy import K8SResourcePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of K8SResourcePolicy from a JSON string
k8_s_resource_policy_instance = K8SResourcePolicy.from_json(json)
# print the JSON string representation of the object
print K8SResourcePolicy.to_json()

# convert the object into a dict
k8_s_resource_policy_dict = k8_s_resource_policy_instance.to_dict()
# create an instance of K8SResourcePolicy from a dict
k8_s_resource_policy_form_dict = k8_s_resource_policy.from_dict(k8_s_resource_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


