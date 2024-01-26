# ContainerSetTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containers** | [**List[ContainerNode]**](ContainerNode.md) |  | 
**retry_strategy** | [**ContainerSetRetryStrategy**](ContainerSetRetryStrategy.md) |  | [optional] 
**volume_mounts** | [**List[VolumeMount]**](VolumeMount.md) |  | [optional] 

## Example

```python
from argo_workflows.models.container_set_template import ContainerSetTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerSetTemplate from a JSON string
container_set_template_instance = ContainerSetTemplate.from_json(json)
# print the JSON string representation of the object
print ContainerSetTemplate.to_json()

# convert the object into a dict
container_set_template_dict = container_set_template_instance.to_dict()
# create an instance of ContainerSetTemplate from a dict
container_set_template_form_dict = container_set_template.from_dict(container_set_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


