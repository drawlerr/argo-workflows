# S3Filter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** |  | [optional] 
**suffix** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.s3_filter import S3Filter

# TODO update the JSON string below
json = "{}"
# create an instance of S3Filter from a JSON string
s3_filter_instance = S3Filter.from_json(json)
# print the JSON string representation of the object
print S3Filter.to_json()

# convert the object into a dict
s3_filter_dict = s3_filter_instance.to_dict()
# create an instance of S3Filter from a dict
s3_filter_form_dict = s3_filter.from_dict(s3_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


