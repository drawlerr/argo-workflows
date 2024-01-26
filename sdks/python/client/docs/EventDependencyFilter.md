# EventDependencyFilter

EventDependencyFilter defines filters and constraints for a 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**EventContext**](EventContext.md) |  | [optional] 
**data** | [**List[DataFilter]**](DataFilter.md) |  | [optional] 
**data_logical_operator** | **str** | DataLogicalOperator defines how multiple Data filters (if defined) are evaluated together. Available values: and (&amp;&amp;), or (||) Is optional and if left blank treated as and (&amp;&amp;). | [optional] 
**expr_logical_operator** | **str** | ExprLogicalOperator defines how multiple Exprs filters (if defined) are evaluated together. Available values: and (&amp;&amp;), or (||) Is optional and if left blank treated as and (&amp;&amp;). | [optional] 
**exprs** | [**List[ExprFilter]**](ExprFilter.md) | Exprs contains the list of expressions evaluated against the event payload. | [optional] 
**script** | **str** | Script refers to a Lua script evaluated to determine the validity of an  | [optional] 
**time** | [**TimeFilter**](TimeFilter.md) |  | [optional] 

## Example

```python
from argo_workflows.models.event_dependency_filter import EventDependencyFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EventDependencyFilter from a JSON string
event_dependency_filter_instance = EventDependencyFilter.from_json(json)
# print the JSON string representation of the object
print EventDependencyFilter.to_json()

# convert the object into a dict
event_dependency_filter_dict = event_dependency_filter_instance.to_dict()
# create an instance of EventDependencyFilter from a dict
event_dependency_filter_form_dict = event_dependency_filter.from_dict(event_dependency_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


