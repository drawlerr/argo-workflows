# SensorStatus

SensorStatus contains information about the status of a sensor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | [optional] 

## Example

```python
from argo_workflows.models.sensor_status import SensorStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SensorStatus from a JSON string
sensor_status_instance = SensorStatus.from_json(json)
# print the JSON string representation of the object
print SensorStatus.to_json()

# convert the object into a dict
sensor_status_dict = sensor_status_instance.to_dict()
# create an instance of SensorStatus from a dict
sensor_status_form_dict = sensor_status.from_dict(sensor_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


