# Histogram

Histogram is a Histogram prometheus metric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buckets** | **List[float]** | Buckets is a list of bucket divisors for the histogram | 
**value** | **str** | Value is the value of the metric | 

## Example

```python
from argo_workflows.models.histogram import Histogram

# TODO update the JSON string below
json = "{}"
# create an instance of Histogram from a JSON string
histogram_instance = Histogram.from_json(json)
# print the JSON string representation of the object
print Histogram.to_json()

# convert the object into a dict
histogram_dict = histogram_instance.to_dict()
# create an instance of Histogram from a dict
histogram_form_dict = histogram.from_dict(histogram_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


