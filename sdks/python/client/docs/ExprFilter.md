# ExprFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expr** | **str** | Expr refers to the expression that determines the outcome of the filter. | [optional] 
**fields** | [**List[PayloadField]**](PayloadField.md) | Fields refers to set of keys that refer to the paths within event payload. | [optional] 

## Example

```python
from argo_workflows.models.expr_filter import ExprFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ExprFilter from a JSON string
expr_filter_instance = ExprFilter.from_json(json)
# print the JSON string representation of the object
print ExprFilter.to_json()

# convert the object into a dict
expr_filter_dict = expr_filter_instance.to_dict()
# create an instance of ExprFilter from a dict
expr_filter_form_dict = expr_filter.from_dict(expr_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


