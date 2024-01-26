# RedisStreamEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer_group** | **str** |  | [optional] 
**db** | **int** |  | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**host_address** | **str** |  | [optional] 
**max_msg_count_per_read** | **int** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**password** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**streams** | **List[str]** | Streams to look for entries. XREADGROUP is used on all streams using a single consumer group. | [optional] 
**tls** | [**TLSConfig**](TLSConfig.md) |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.redis_stream_event_source import RedisStreamEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of RedisStreamEventSource from a JSON string
redis_stream_event_source_instance = RedisStreamEventSource.from_json(json)
# print the JSON string representation of the object
print RedisStreamEventSource.to_json()

# convert the object into a dict
redis_stream_event_source_dict = redis_stream_event_source_instance.to_dict()
# create an instance of RedisStreamEventSource from a dict
redis_stream_event_source_form_dict = redis_stream_event_source.from_dict(redis_stream_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


