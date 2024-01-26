# TarStrategy

TarStrategy will tar and gzip the file or directory when saving

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compression_level** | **int** | CompressionLevel specifies the gzip compression level to use for the artifact. Defaults to gzip.DefaultCompression. | [optional] 

## Example

```python
from argo_workflows.models.tar_strategy import TarStrategy

# TODO update the JSON string below
json = "{}"
# create an instance of TarStrategy from a JSON string
tar_strategy_instance = TarStrategy.from_json(json)
# print the JSON string representation of the object
print TarStrategy.to_json()

# convert the object into a dict
tar_strategy_dict = tar_strategy_instance.to_dict()
# create an instance of TarStrategy from a dict
tar_strategy_form_dict = tar_strategy.from_dict(tar_strategy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


