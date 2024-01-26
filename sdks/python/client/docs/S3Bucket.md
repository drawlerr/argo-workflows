# S3Bucket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.s3_bucket import S3Bucket

# TODO update the JSON string below
json = "{}"
# create an instance of S3Bucket from a JSON string
s3_bucket_instance = S3Bucket.from_json(json)
# print the JSON string representation of the object
print S3Bucket.to_json()

# convert the object into a dict
s3_bucket_dict = s3_bucket_instance.to_dict()
# create an instance of S3Bucket from a dict
s3_bucket_form_dict = s3_bucket.from_dict(s3_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


