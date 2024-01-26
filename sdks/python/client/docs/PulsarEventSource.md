# PulsarEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_token_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**connection_backoff** | [**Backoff**](Backoff.md) |  | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**json_body** | **bool** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**tls** | [**TLSConfig**](TLSConfig.md) |  | [optional] 
**tls_allow_insecure_connection** | **bool** |  | [optional] 
**tls_trust_certs_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**tls_validate_hostname** | **bool** |  | [optional] 
**topics** | **List[str]** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.pulsar_event_source import PulsarEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of PulsarEventSource from a JSON string
pulsar_event_source_instance = PulsarEventSource.from_json(json)
# print the JSON string representation of the object
print PulsarEventSource.to_json()

# convert the object into a dict
pulsar_event_source_dict = pulsar_event_source_instance.to_dict()
# create an instance of PulsarEventSource from a dict
pulsar_event_source_form_dict = pulsar_event_source.from_dict(pulsar_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


