# OSSLifecycleRule

OSSLifecycleRule specifies how to manage bucket's lifecycle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mark_deletion_after_days** | **int** | MarkDeletionAfterDays is the number of days before we delete objects in the bucket | [optional] 
**mark_infrequent_access_after_days** | **int** | MarkInfrequentAccessAfterDays is the number of days before we convert the objects in the bucket to Infrequent Access (IA) storage type | [optional] 

## Example

```python
from argo_workflows.models.oss_lifecycle_rule import OSSLifecycleRule

# TODO update the JSON string below
json = "{}"
# create an instance of OSSLifecycleRule from a JSON string
oss_lifecycle_rule_instance = OSSLifecycleRule.from_json(json)
# print the JSON string representation of the object
print OSSLifecycleRule.to_json()

# convert the object into a dict
oss_lifecycle_rule_dict = oss_lifecycle_rule_instance.to_dict()
# create an instance of OSSLifecycleRule from a dict
oss_lifecycle_rule_form_dict = oss_lifecycle_rule.from_dict(oss_lifecycle_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


