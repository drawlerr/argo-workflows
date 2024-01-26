# StatusPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow** | **List[int]** |  | [optional] 

## Example

```python
from argo_workflows.models.status_policy import StatusPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of StatusPolicy from a JSON string
status_policy_instance = StatusPolicy.from_json(json)
# print the JSON string representation of the object
print StatusPolicy.to_json()

# convert the object into a dict
status_policy_dict = status_policy_instance.to_dict()
# create an instance of StatusPolicy from a dict
status_policy_form_dict = status_policy.from_dict(status_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


