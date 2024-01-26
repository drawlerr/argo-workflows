# ArchiveStrategy

ArchiveStrategy describes how to archive files/directory when saving artifacts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_none** | **object** | NoneStrategy indicates to skip tar process and upload the files or directory tree as independent files. Note that if the artifact is a directory, the artifact driver must support the ability to save/load the directory appropriately. | [optional] 
**tar** | [**TarStrategy**](TarStrategy.md) |  | [optional] 
**zip** | **object** | ZipStrategy will unzip zipped input artifacts | [optional] 

## Example

```python
from argo_workflows.models.archive_strategy import ArchiveStrategy

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveStrategy from a JSON string
archive_strategy_instance = ArchiveStrategy.from_json(json)
# print the JSON string representation of the object
print ArchiveStrategy.to_json()

# convert the object into a dict
archive_strategy_dict = archive_strategy_instance.to_dict()
# create an instance of ArchiveStrategy from a dict
archive_strategy_form_dict = archive_strategy.from_dict(archive_strategy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


