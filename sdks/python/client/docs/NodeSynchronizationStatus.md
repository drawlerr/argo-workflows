# NodeSynchronizationStatus

NodeSynchronizationStatus stores the status of a node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**waiting** | **str** | Waiting is the name of the lock that this node is waiting for | [optional] 

## Example

```python
from argo_workflows.models.node_synchronization_status import NodeSynchronizationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NodeSynchronizationStatus from a JSON string
node_synchronization_status_instance = NodeSynchronizationStatus.from_json(json)
# print the JSON string representation of the object
print NodeSynchronizationStatus.to_json()

# convert the object into a dict
node_synchronization_status_dict = node_synchronization_status_instance.to_dict()
# create an instance of NodeSynchronizationStatus from a dict
node_synchronization_status_form_dict = node_synchronization_status.from_dict(node_synchronization_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


