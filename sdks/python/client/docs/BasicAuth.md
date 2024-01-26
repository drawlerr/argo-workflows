# BasicAuth

BasicAuth describes the secret selectors required for basic authentication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**username_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.basic_auth import BasicAuth

# TODO update the JSON string below
json = "{}"
# create an instance of BasicAuth from a JSON string
basic_auth_instance = BasicAuth.from_json(json)
# print the JSON string representation of the object
print BasicAuth.to_json()

# convert the object into a dict
basic_auth_dict = basic_auth_instance.to_dict()
# create an instance of BasicAuth from a dict
basic_auth_form_dict = basic_auth.from_dict(basic_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


