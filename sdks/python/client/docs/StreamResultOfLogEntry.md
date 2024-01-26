# StreamResultOfLogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**GrpcGatewayRuntimeStreamError**](GrpcGatewayRuntimeStreamError.md) |  | [optional] 
**result** | [**LogEntry**](LogEntry.md) |  | [optional] 

## Example

```python
from argo_workflows.models.stream_result_of_log_entry import StreamResultOfLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of StreamResultOfLogEntry from a JSON string
stream_result_of_log_entry_instance = StreamResultOfLogEntry.from_json(json)
# print the JSON string representation of the object
print StreamResultOfLogEntry.to_json()

# convert the object into a dict
stream_result_of_log_entry_dict = stream_result_of_log_entry_instance.to_dict()
# create an instance of StreamResultOfLogEntry from a dict
stream_result_of_log_entry_form_dict = stream_result_of_log_entry.from_dict(stream_result_of_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


