# TriggerTemplate

TriggerTemplate is the template that describes trigger specification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**argo_workflow** | [**ArgoWorkflowTrigger**](ArgoWorkflowTrigger.md) |  | [optional] 
**aws_lambda** | [**AWSLambdaTrigger**](AWSLambdaTrigger.md) |  | [optional] 
**azure_event_hubs** | [**AzureEventHubsTrigger**](AzureEventHubsTrigger.md) |  | [optional] 
**conditions** | **str** |  | [optional] 
**conditions_reset** | [**List[ConditionsResetCriteria]**](ConditionsResetCriteria.md) |  | [optional] 
**custom** | [**CustomTrigger**](CustomTrigger.md) |  | [optional] 
**http** | [**HTTPTrigger**](HTTPTrigger.md) |  | [optional] 
**k8s** | [**StandardK8STrigger**](StandardK8STrigger.md) |  | [optional] 
**kafka** | [**KafkaTrigger**](KafkaTrigger.md) |  | [optional] 
**log** | [**LogTrigger**](LogTrigger.md) |  | [optional] 
**name** | **str** | Name is a unique name of the action to take. | [optional] 
**nats** | [**NATSTrigger**](NATSTrigger.md) |  | [optional] 
**open_whisk** | [**OpenWhiskTrigger**](OpenWhiskTrigger.md) |  | [optional] 
**pulsar** | [**PulsarTrigger**](PulsarTrigger.md) |  | [optional] 
**slack** | [**SlackTrigger**](SlackTrigger.md) |  | [optional] 

## Example

```python
from argo_workflows.models.trigger_template import TriggerTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerTemplate from a JSON string
trigger_template_instance = TriggerTemplate.from_json(json)
# print the JSON string representation of the object
print TriggerTemplate.to_json()

# convert the object into a dict
trigger_template_dict = trigger_template_instance.to_dict()
# create an instance of TriggerTemplate from a dict
trigger_template_form_dict = trigger_template.from_dict(trigger_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


