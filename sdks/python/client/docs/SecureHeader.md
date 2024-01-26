# SecureHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value_from** | [**ValueFromSource**](ValueFromSource.md) |  | [optional] 

## Example

```python
from argo_workflows.models.secure_header import SecureHeader

# TODO update the JSON string below
json = "{}"
# create an instance of SecureHeader from a JSON string
secure_header_instance = SecureHeader.from_json(json)
# print the JSON string representation of the object
print SecureHeader.to_json()

# convert the object into a dict
secure_header_dict = secure_header_instance.to_dict()
# create an instance of SecureHeader from a dict
secure_header_form_dict = secure_header.from_dict(secure_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


