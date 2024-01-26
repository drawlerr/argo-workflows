# EventDependencyTransformer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jq** | **str** |  | [optional] 
**script** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.event_dependency_transformer import EventDependencyTransformer

# TODO update the JSON string below
json = "{}"
# create an instance of EventDependencyTransformer from a JSON string
event_dependency_transformer_instance = EventDependencyTransformer.from_json(json)
# print the JSON string representation of the object
print EventDependencyTransformer.to_json()

# convert the object into a dict
event_dependency_transformer_dict = event_dependency_transformer_instance.to_dict()
# create an instance of EventDependencyTransformer from a dict
event_dependency_transformer_form_dict = event_dependency_transformer.from_dict(event_dependency_transformer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


