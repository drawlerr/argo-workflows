# HTTPTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_auth** | [**BasicAuth**](BasicAuth.md) |  | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 
**method** | **str** |  | [optional] 
**parameters** | [**List[TriggerParameter]**](TriggerParameter.md) | Parameters is the list of key-value extracted from event&#39;s payload that are applied to the HTTP trigger resource. | [optional] 
**payload** | [**List[TriggerParameter]**](TriggerParameter.md) |  | [optional] 
**secure_headers** | [**List[SecureHeader]**](SecureHeader.md) |  | [optional] 
**timeout** | **str** |  | [optional] 
**tls** | [**TLSConfig**](TLSConfig.md) |  | [optional] 
**url** | **str** | URL refers to the URL to send HTTP request to. | [optional] 

## Example

```python
from argo_workflows.models.http_trigger import HTTPTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPTrigger from a JSON string
http_trigger_instance = HTTPTrigger.from_json(json)
# print the JSON string representation of the object
print HTTPTrigger.to_json()

# convert the object into a dict
http_trigger_dict = http_trigger_instance.to_dict()
# create an instance of HTTPTrigger from a dict
http_trigger_form_dict = http_trigger.from_dict(http_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


