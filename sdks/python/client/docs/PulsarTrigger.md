# PulsarTrigger

PulsarTrigger refers to the specification of the Pulsar trigger.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_token_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**connection_backoff** | [**Backoff**](Backoff.md) |  | [optional] 
**parameters** | [**List[TriggerParameter]**](TriggerParameter.md) | Parameters is the list of parameters that is applied to resolved Kafka trigger object. | [optional] 
**payload** | [**List[TriggerParameter]**](TriggerParameter.md) | Payload is the list of key-value extracted from an event payload to construct the request payload. | [optional] 
**tls** | [**TLSConfig**](TLSConfig.md) |  | [optional] 
**tls_allow_insecure_connection** | **bool** |  | [optional] 
**tls_trust_certs_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**tls_validate_hostname** | **bool** |  | [optional] 
**topic** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from argo_workflows.models.pulsar_trigger import PulsarTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of PulsarTrigger from a JSON string
pulsar_trigger_instance = PulsarTrigger.from_json(json)
# print the JSON string representation of the object
print PulsarTrigger.to_json()

# convert the object into a dict
pulsar_trigger_dict = pulsar_trigger_instance.to_dict()
# create an instance of PulsarTrigger from a dict
pulsar_trigger_form_dict = pulsar_trigger.from_dict(pulsar_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


