# Sequence

Sequence expands a workflow step into numeric range

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **str** |  | [optional] 
**end** | **str** |  | [optional] 
**format** | **str** | Format is a printf format string to format the value in the sequence | [optional] 
**start** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.sequence import Sequence

# TODO update the JSON string below
json = "{}"
# create an instance of Sequence from a JSON string
sequence_instance = Sequence.from_json(json)
# print the JSON string representation of the object
print Sequence.to_json()

# convert the object into a dict
sequence_dict = sequence_instance.to_dict()
# create an instance of Sequence from a dict
sequence_form_dict = sequence.from_dict(sequence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


