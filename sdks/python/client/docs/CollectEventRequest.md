# CollectEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.collect_event_request import CollectEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CollectEventRequest from a JSON string
collect_event_request_instance = CollectEventRequest.from_json(json)
# print the JSON string representation of the object
print CollectEventRequest.to_json()

# convert the object into a dict
collect_event_request_dict = collect_event_request_instance.to_dict()
# create an instance of CollectEventRequest from a dict
collect_event_request_form_dict = collect_event_request.from_dict(collect_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


