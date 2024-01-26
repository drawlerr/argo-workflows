# RetryAffinity

RetryAffinity prevents running steps on the same host.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_anti_affinity** | **object** | RetryNodeAntiAffinity is a placeholder for future expansion, only empty nodeAntiAffinity is allowed. In order to prevent running steps on the same host, it uses \&quot;kubernetes.io/hostname\&quot;. | [optional] 

## Example

```python
from argo_workflows.models.retry_affinity import RetryAffinity

# TODO update the JSON string below
json = "{}"
# create an instance of RetryAffinity from a JSON string
retry_affinity_instance = RetryAffinity.from_json(json)
# print the JSON string representation of the object
print RetryAffinity.to_json()

# convert the object into a dict
retry_affinity_dict = retry_affinity_instance.to_dict()
# create an instance of RetryAffinity from a dict
retry_affinity_form_dict = retry_affinity.from_dict(retry_affinity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


