# GenericEventSource

GenericEventSource refers to a generic event source. It can be used to implement a custom event source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**config** | **str** |  | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**insecure** | **bool** | Insecure determines the type of connection. | [optional] 
**json_body** | **bool** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**url** | **str** | URL of the gRPC server that implements the event source. | [optional] 

## Example

```python
from argo_workflows.models.generic_event_source import GenericEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of GenericEventSource from a JSON string
generic_event_source_instance = GenericEventSource.from_json(json)
# print the JSON string representation of the object
print GenericEventSource.to_json()

# convert the object into a dict
generic_event_source_dict = generic_event_source_instance.to_dict()
# create an instance of GenericEventSource from a dict
generic_event_source_form_dict = generic_event_source.from_dict(generic_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


