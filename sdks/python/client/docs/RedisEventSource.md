# RedisEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | **List[str]** |  | [optional] 
**db** | **int** |  | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**host_address** | **str** |  | [optional] 
**json_body** | **bool** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**namespace** | **str** |  | [optional] 
**password** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**tls** | [**TLSConfig**](TLSConfig.md) |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.redis_event_source import RedisEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of RedisEventSource from a JSON string
redis_event_source_instance = RedisEventSource.from_json(json)
# print the JSON string representation of the object
print RedisEventSource.to_json()

# convert the object into a dict
redis_event_source_dict = redis_event_source_instance.to_dict()
# create an instance of RedisEventSource from a dict
redis_event_source_form_dict = redis_event_source.from_dict(redis_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


