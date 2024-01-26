# SensorSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependencies** | [**List[EventDependency]**](EventDependency.md) | Dependencies is a list of the events that this sensor is dependent on. | [optional] 
**error_on_failed_round** | **bool** | ErrorOnFailedRound if set to true, marks sensor state as &#x60;error&#x60; if the previous trigger round fails. Once sensor state is set to &#x60;error&#x60;, no further triggers will be processed. | [optional] 
**event_bus_name** | **str** |  | [optional] 
**replicas** | **int** |  | [optional] 
**template** | [**Template**](Template.md) |  | [optional] 
**triggers** | [**List[Trigger]**](Trigger.md) | Triggers is a list of the things that this sensor evokes. These are the outputs from this sensor. | [optional] 

## Example

```python
from argo_workflows.models.sensor_spec import SensorSpec

# TODO update the JSON string below
json = "{}"
# create an instance of SensorSpec from a JSON string
sensor_spec_instance = SensorSpec.from_json(json)
# print the JSON string representation of the object
print SensorSpec.to_json()

# convert the object into a dict
sensor_spec_dict = sensor_spec_instance.to_dict()
# create an instance of SensorSpec from a dict
sensor_spec_form_dict = sensor_spec.from_dict(sensor_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


