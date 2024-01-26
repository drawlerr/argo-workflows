# InfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[Column]**](Column.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**managed_namespace** | **str** |  | [optional] 
**modals** | **Dict[str, bool]** |  | [optional] 
**nav_color** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.info_response import InfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InfoResponse from a JSON string
info_response_instance = InfoResponse.from_json(json)
# print the JSON string representation of the object
print InfoResponse.to_json()

# convert the object into a dict
info_response_dict = info_response_instance.to_dict()
# create an instance of InfoResponse from a dict
info_response_form_dict = info_response.from_dict(info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


