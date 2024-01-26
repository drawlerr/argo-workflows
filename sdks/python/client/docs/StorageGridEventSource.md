# StorageGridEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_url** | **str** | APIURL is the url of the storagegrid api. | [optional] 
**auth_token** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**bucket** | **str** | Name of the bucket to register notifications for. | [optional] 
**events** | **List[str]** |  | [optional] 
**filter** | [**StorageGridFilter**](StorageGridFilter.md) |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**region** | **str** |  | [optional] 
**topic_arn** | **str** |  | [optional] 
**webhook** | [**WebhookContext**](WebhookContext.md) |  | [optional] 

## Example

```python
from argo_workflows.models.storage_grid_event_source import StorageGridEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of StorageGridEventSource from a JSON string
storage_grid_event_source_instance = StorageGridEventSource.from_json(json)
# print the JSON string representation of the object
print StorageGridEventSource.to_json()

# convert the object into a dict
storage_grid_event_source_dict = storage_grid_event_source_instance.to_dict()
# create an instance of StorageGridEventSource from a dict
storage_grid_event_source_form_dict = storage_grid_event_source.from_dict(storage_grid_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


