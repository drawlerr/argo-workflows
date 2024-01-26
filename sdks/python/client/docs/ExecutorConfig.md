# ExecutorConfig

ExecutorConfig holds configurations of an executor container.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_account_name** | **str** | ServiceAccountName specifies the service account name of the executor container. | [optional] 

## Example

```python
from argo_workflows.models.executor_config import ExecutorConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutorConfig from a JSON string
executor_config_instance = ExecutorConfig.from_json(json)
# print the JSON string representation of the object
print ExecutorConfig.to_json()

# convert the object into a dict
executor_config_dict = executor_config_instance.to_dict()
# create an instance of ExecutorConfig from a dict
executor_config_form_dict = executor_config.from_dict(executor_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


