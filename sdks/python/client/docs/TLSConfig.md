# TLSConfig

TLSConfig refers to TLS configuration for a client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_cert_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**client_cert_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**client_key_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**insecure_skip_verify** | **bool** |  | [optional] 

## Example

```python
from argo_workflows.models.tls_config import TLSConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TLSConfig from a JSON string
tls_config_instance = TLSConfig.from_json(json)
# print the JSON string representation of the object
print TLSConfig.to_json()

# convert the object into a dict
tls_config_dict = tls_config_instance.to_dict()
# create an instance of TLSConfig from a dict
tls_config_form_dict = tls_config.from_dict(tls_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


