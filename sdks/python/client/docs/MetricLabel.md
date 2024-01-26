# MetricLabel

MetricLabel is a single label for a prometheus metric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from argo_workflows.models.metric_label import MetricLabel

# TODO update the JSON string below
json = "{}"
# create an instance of MetricLabel from a JSON string
metric_label_instance = MetricLabel.from_json(json)
# print the JSON string representation of the object
print MetricLabel.to_json()

# convert the object into a dict
metric_label_dict = metric_label_instance.to_dict()
# create an instance of MetricLabel from a dict
metric_label_form_dict = metric_label.from_dict(metric_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


