# CreateS3BucketOptions

CreateS3BucketOptions options used to determine automatic automatic bucket-creation process

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_locking** | **bool** | ObjectLocking Enable object locking | [optional] 

## Example

```python
from argo_workflows.models.create_s3_bucket_options import CreateS3BucketOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CreateS3BucketOptions from a JSON string
create_s3_bucket_options_instance = CreateS3BucketOptions.from_json(json)
# print the JSON string representation of the object
print CreateS3BucketOptions.to_json()

# convert the object into a dict
create_s3_bucket_options_dict = create_s3_bucket_options_instance.to_dict()
# create an instance of CreateS3BucketOptions from a dict
create_s3_bucket_options_form_dict = create_s3_bucket_options.from_dict(create_s3_bucket_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


