# AzureArtifact

AzureArtifact is the location of a an Azure Storage artifact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_key_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**blob** | **str** | Blob is the blob name (i.e., path) in the container where the artifact resides | 
**container** | **str** | Container is the container where resources will be stored | 
**endpoint** | **str** | Endpoint is the service url associated with an account. It is most likely \&quot;https://&lt;ACCOUNT_NAME&gt;.blob.core.windows.net\&quot; | 
**use_sdk_creds** | **bool** | UseSDKCreds tells the driver to figure out credentials based on sdk defaults. | [optional] 

## Example

```python
from argo_workflows.models.azure_artifact import AzureArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of AzureArtifact from a JSON string
azure_artifact_instance = AzureArtifact.from_json(json)
# print the JSON string representation of the object
print AzureArtifact.to_json()

# convert the object into a dict
azure_artifact_dict = azure_artifact_instance.to_dict()
# create an instance of AzureArtifact from a dict
azure_artifact_form_dict = azure_artifact.from_dict(azure_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


