# GCSArtifact

GCSArtifact is the location of a GCS artifact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** | Bucket is the name of the bucket | [optional] 
**key** | **str** | Key is the path in the bucket where the artifact resides | 
**service_account_key_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 

## Example

```python
from argo_workflows.models.gcs_artifact import GCSArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of GCSArtifact from a JSON string
gcs_artifact_instance = GCSArtifact.from_json(json)
# print the JSON string representation of the object
print GCSArtifact.to_json()

# convert the object into a dict
gcs_artifact_dict = gcs_artifact_instance.to_dict()
# create an instance of GCSArtifact from a dict
gcs_artifact_form_dict = gcs_artifact.from_dict(gcs_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


