# ResourceFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_start** | **bool** |  | [optional] 
**created_by** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**fields** | [**List[Selector]**](Selector.md) |  | [optional] 
**labels** | [**List[Selector]**](Selector.md) |  | [optional] 
**prefix** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.resource_filter import ResourceFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceFilter from a JSON string
resource_filter_instance = ResourceFilter.from_json(json)
# print the JSON string representation of the object
print ResourceFilter.to_json()

# convert the object into a dict
resource_filter_dict = resource_filter_instance.to_dict()
# create an instance of ResourceFilter from a dict
resource_filter_form_dict = resource_filter.from_dict(resource_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


