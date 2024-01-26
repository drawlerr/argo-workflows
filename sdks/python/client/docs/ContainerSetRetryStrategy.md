# ContainerSetRetryStrategy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | Duration is the time between each retry, examples values are \&quot;300ms\&quot;, \&quot;1s\&quot; or \&quot;5m\&quot;. Valid time units are \&quot;ns\&quot;, \&quot;us\&quot; (or \&quot;µs\&quot;), \&quot;ms\&quot;, \&quot;s\&quot;, \&quot;m\&quot;, \&quot;h\&quot;. | [optional] 
**retries** | **str** |  | 

## Example

```python
from argo_workflows.models.container_set_retry_strategy import ContainerSetRetryStrategy

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerSetRetryStrategy from a JSON string
container_set_retry_strategy_instance = ContainerSetRetryStrategy.from_json(json)
# print the JSON string representation of the object
print ContainerSetRetryStrategy.to_json()

# convert the object into a dict
container_set_retry_strategy_dict = container_set_retry_strategy_instance.to_dict()
# create an instance of ContainerSetRetryStrategy from a dict
container_set_retry_strategy_form_dict = container_set_retry_strategy.from_dict(container_set_retry_strategy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


