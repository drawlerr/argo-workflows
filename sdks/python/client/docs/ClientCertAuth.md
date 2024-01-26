# ClientCertAuth

ClientCertAuth holds necessary information for client authentication via certificates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_cert_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**client_key_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.client_cert_auth import ClientCertAuth

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCertAuth from a JSON string
client_cert_auth_instance = ClientCertAuth.from_json(json)
# print the JSON string representation of the object
print ClientCertAuth.to_json()

# convert the object into a dict
client_cert_auth_dict = client_cert_auth_instance.to_dict()
# create an instance of ClientCertAuth from a dict
client_cert_auth_form_dict = client_cert_auth.from_dict(client_cert_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


