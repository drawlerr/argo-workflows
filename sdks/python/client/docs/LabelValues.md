# LabelValues

Labels is list of workflow labels

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** |  | [optional] 

## Example

```python
from argo_workflows.models.label_values import LabelValues

# TODO update the JSON string below
json = "{}"
# create an instance of LabelValues from a JSON string
label_values_instance = LabelValues.from_json(json)
# print the JSON string representation of the object
print LabelValues.to_json()

# convert the object into a dict
label_values_dict = label_values_instance.to_dict()
# create an instance of LabelValues from a dict
label_values_form_dict = label_values.from_dict(label_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


