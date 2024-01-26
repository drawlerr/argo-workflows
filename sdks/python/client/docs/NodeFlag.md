# NodeFlag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hooked** | **bool** | Hooked tracks whether or not this node was triggered by hook or onExit | [optional] 
**retried** | **bool** | Retried tracks whether or not this node was retried by retryStrategy | [optional] 

## Example

```python
from argo_workflows.models.node_flag import NodeFlag

# TODO update the JSON string below
json = "{}"
# create an instance of NodeFlag from a JSON string
node_flag_instance = NodeFlag.from_json(json)
# print the JSON string representation of the object
print NodeFlag.to_json()

# convert the object into a dict
node_flag_dict = node_flag_instance.to_dict()
# create an instance of NodeFlag from a dict
node_flag_form_dict = node_flag.from_dict(node_flag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


