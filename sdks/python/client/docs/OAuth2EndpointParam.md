# OAuth2EndpointParam

EndpointParam is for requesting optional fields that should be sent in the oauth request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Name is the header name | 
**value** | **str** | Value is the literal value to use for the header | [optional] 

## Example

```python
from argo_workflows.models.o_auth2_endpoint_param import OAuth2EndpointParam

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2EndpointParam from a JSON string
o_auth2_endpoint_param_instance = OAuth2EndpointParam.from_json(json)
# print the JSON string representation of the object
print OAuth2EndpointParam.to_json()

# convert the object into a dict
o_auth2_endpoint_param_dict = o_auth2_endpoint_param_instance.to_dict()
# create an instance of OAuth2EndpointParam from a dict
o_auth2_endpoint_param_form_dict = o_auth2_endpoint_param.from_dict(o_auth2_endpoint_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


