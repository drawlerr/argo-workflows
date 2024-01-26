# NATSAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic** | [**BasicAuth**](BasicAuth.md) |  | [optional] 
**credential** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**nkey** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**token** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.nats_auth import NATSAuth

# TODO update the JSON string below
json = "{}"
# create an instance of NATSAuth from a JSON string
nats_auth_instance = NATSAuth.from_json(json)
# print the JSON string representation of the object
print NATSAuth.to_json()

# convert the object into a dict
nats_auth_dict = nats_auth_instance.to_dict()
# create an instance of NATSAuth from a dict
nats_auth_form_dict = nats_auth.from_dict(nats_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


