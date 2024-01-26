# SlackTrigger

SlackTrigger refers to the specification of the slack notification trigger.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**parameters** | [**List[TriggerParameter]**](TriggerParameter.md) |  | [optional] 
**slack_token** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.slack_trigger import SlackTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of SlackTrigger from a JSON string
slack_trigger_instance = SlackTrigger.from_json(json)
# print the JSON string representation of the object
print SlackTrigger.to_json()

# convert the object into a dict
slack_trigger_dict = slack_trigger_instance.to_dict()
# create an instance of SlackTrigger from a dict
slack_trigger_form_dict = slack_trigger.from_dict(slack_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


