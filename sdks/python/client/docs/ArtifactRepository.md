# ArtifactRepository

ArtifactRepository represents an artifact repository in which a controller will store its artifacts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_logs** | **bool** | ArchiveLogs enables log archiving | [optional] 
**artifactory** | [**ArtifactoryArtifactRepository**](ArtifactoryArtifactRepository.md) |  | [optional] 
**azure** | [**AzureArtifactRepository**](AzureArtifactRepository.md) |  | [optional] 
**gcs** | [**GCSArtifactRepository**](GCSArtifactRepository.md) |  | [optional] 
**hdfs** | [**HDFSArtifactRepository**](HDFSArtifactRepository.md) |  | [optional] 
**oss** | [**OSSArtifactRepository**](OSSArtifactRepository.md) |  | [optional] 
**s3** | [**S3ArtifactRepository**](S3ArtifactRepository.md) |  | [optional] 

## Example

```python
from argo_workflows.models.artifact_repository import ArtifactRepository

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactRepository from a JSON string
artifact_repository_instance = ArtifactRepository.from_json(json)
# print the JSON string representation of the object
print ArtifactRepository.to_json()

# convert the object into a dict
artifact_repository_dict = artifact_repository_instance.to_dict()
# create an instance of ArtifactRepository from a dict
artifact_repository_form_dict = artifact_repository.from_dict(artifact_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


