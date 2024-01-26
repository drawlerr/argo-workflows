# LogTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval_seconds** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.log_trigger import LogTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of LogTrigger from a JSON string
log_trigger_instance = LogTrigger.from_json(json)
# print the JSON string representation of the object
print LogTrigger.to_json()

# convert the object into a dict
log_trigger_dict = log_trigger_instance.to_dict()
# create an instance of LogTrigger from a dict
log_trigger_form_dict = log_trigger.from_dict(log_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


