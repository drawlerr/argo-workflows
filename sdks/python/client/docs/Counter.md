# Counter

Counter is a Counter prometheus metric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value is the value of the metric | 

## Example

```python
from argo_workflows.models.counter import Counter

# TODO update the JSON string below
json = "{}"
# create an instance of Counter from a JSON string
counter_instance = Counter.from_json(json)
# print the JSON string representation of the object
print Counter.to_json()

# convert the object into a dict
counter_dict = counter_instance.to_dict()
# create an instance of Counter from a dict
counter_form_dict = counter.from_dict(counter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


