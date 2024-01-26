# NodeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**outputs** | [**Outputs**](Outputs.md) |  | [optional] 
**phase** | **str** |  | [optional] 
**progress** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.node_result import NodeResult

# TODO update the JSON string below
json = "{}"
# create an instance of NodeResult from a JSON string
node_result_instance = NodeResult.from_json(json)
# print the JSON string representation of the object
print NodeResult.to_json()

# convert the object into a dict
node_result_dict = node_result_instance.to_dict()
# create an instance of NodeResult from a dict
node_result_form_dict = node_result.from_dict(node_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


