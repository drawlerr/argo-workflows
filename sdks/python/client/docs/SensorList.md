# SensorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Sensor]**](Sensor.md) |  | [optional] 
**metadata** | [**ListMeta**](ListMeta.md) |  | [optional] 

## Example

```python
from argo_workflows.models.sensor_list import SensorList

# TODO update the JSON string below
json = "{}"
# create an instance of SensorList from a JSON string
sensor_list_instance = SensorList.from_json(json)
# print the JSON string representation of the object
print SensorList.to_json()

# convert the object into a dict
sensor_list_dict = sensor_list_instance.to_dict()
# create an instance of SensorList from a dict
sensor_list_form_dict = sensor_list.from_dict(sensor_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


