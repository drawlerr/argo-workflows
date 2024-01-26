# RetryStrategy

RetryStrategy provides controls on how to retry a workflow step

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinity** | [**RetryAffinity**](RetryAffinity.md) |  | [optional] 
**backoff** | [**Backoff**](Backoff.md) |  | [optional] 
**expression** | **str** | Expression is a condition expression for when a node will be retried. If it evaluates to false, the node will not be retried and the retry strategy will be ignored | [optional] 
**limit** | **str** |  | [optional] 
**retry_policy** | **str** | RetryPolicy is a policy of NodePhase statuses that will be retried | [optional] 

## Example

```python
from argo_workflows.models.retry_strategy import RetryStrategy

# TODO update the JSON string below
json = "{}"
# create an instance of RetryStrategy from a JSON string
retry_strategy_instance = RetryStrategy.from_json(json)
# print the JSON string representation of the object
print RetryStrategy.to_json()

# convert the object into a dict
retry_strategy_dict = retry_strategy_instance.to_dict()
# create an instance of RetryStrategy from a dict
retry_strategy_form_dict = retry_strategy.from_dict(retry_strategy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


