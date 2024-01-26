# Prometheus

Prometheus is a prometheus metric to be emitted

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counter** | [**Counter**](Counter.md) |  | [optional] 
**gauge** | [**Gauge**](Gauge.md) |  | [optional] 
**help** | **str** | Help is a string that describes the metric | 
**histogram** | [**Histogram**](Histogram.md) |  | [optional] 
**labels** | [**List[MetricLabel]**](MetricLabel.md) | Labels is a list of metric labels | [optional] 
**name** | **str** | Name is the name of the metric | 
**when** | **str** | When is a conditional statement that decides when to emit the metric | [optional] 

## Example

```python
from argo_workflows.models.prometheus import Prometheus

# TODO update the JSON string below
json = "{}"
# create an instance of Prometheus from a JSON string
prometheus_instance = Prometheus.from_json(json)
# print the JSON string representation of the object
print Prometheus.to_json()

# convert the object into a dict
prometheus_dict = prometheus_instance.to_dict()
# create an instance of Prometheus from a dict
prometheus_form_dict = prometheus.from_dict(prometheus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


