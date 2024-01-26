# WorkflowMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**labels_from** | [**Dict[str, LabelValueFrom]**](LabelValueFrom.md) |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_metadata import WorkflowMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowMetadata from a JSON string
workflow_metadata_instance = WorkflowMetadata.from_json(json)
# print the JSON string representation of the object
print WorkflowMetadata.to_json()

# convert the object into a dict
workflow_metadata_dict = workflow_metadata_instance.to_dict()
# create an instance of WorkflowMetadata from a dict
workflow_metadata_form_dict = workflow_metadata.from_dict(workflow_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


