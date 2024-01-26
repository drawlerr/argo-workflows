# EventDependency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_name** | **str** |  | [optional] 
**event_source_name** | **str** |  | [optional] 
**filters** | [**EventDependencyFilter**](EventDependencyFilter.md) |  | [optional] 
**filters_logical_operator** | **str** | FiltersLogicalOperator defines how different filters are evaluated together. Available values: and (&amp;&amp;), or (||) Is optional and if left blank treated as and (&amp;&amp;). | [optional] 
**name** | **str** |  | [optional] 
**transform** | [**EventDependencyTransformer**](EventDependencyTransformer.md) |  | [optional] 

## Example

```python
from argo_workflows.models.event_dependency import EventDependency

# TODO update the JSON string below
json = "{}"
# create an instance of EventDependency from a JSON string
event_dependency_instance = EventDependency.from_json(json)
# print the JSON string representation of the object
print EventDependency.to_json()

# convert the object into a dict
event_dependency_dict = event_dependency_instance.to_dict()
# create an instance of EventDependency from a dict
event_dependency_form_dict = event_dependency.from_dict(event_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


