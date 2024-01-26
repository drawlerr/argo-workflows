# ManifestFrom


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact** | [**Artifact**](Artifact.md) |  | 

## Example

```python
from argo_workflows.models.manifest_from import ManifestFrom

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestFrom from a JSON string
manifest_from_instance = ManifestFrom.from_json(json)
# print the JSON string representation of the object
print ManifestFrom.to_json()

# convert the object into a dict
manifest_from_dict = manifest_from_instance.to_dict()
# create an instance of ManifestFrom from a dict
manifest_from_form_dict = manifest_from.from_dict(manifest_from_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


