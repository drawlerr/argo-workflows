# ArtifactLocation

ArtifactLocation describes a location for a single or multiple artifacts. It is used as single artifact in the context of inputs/outputs (e.g. outputs.artifacts.artname). It is also used to describe the location of multiple artifacts such as the archive location of a single workflow step, which the executor will use as a default location to store its files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_logs** | **bool** | ArchiveLogs indicates if the container logs should be archived | [optional] 
**artifactory** | [**ArtifactoryArtifact**](ArtifactoryArtifact.md) |  | [optional] 
**azure** | [**AzureArtifact**](AzureArtifact.md) |  | [optional] 
**gcs** | [**GCSArtifact**](GCSArtifact.md) |  | [optional] 
**git** | [**GitArtifact**](GitArtifact.md) |  | [optional] 
**hdfs** | [**HDFSArtifact**](HDFSArtifact.md) |  | [optional] 
**http** | [**HTTPArtifact**](HTTPArtifact.md) |  | [optional] 
**oss** | [**OSSArtifact**](OSSArtifact.md) |  | [optional] 
**raw** | [**RawArtifact**](RawArtifact.md) |  | [optional] 
**s3** | [**S3Artifact**](S3Artifact.md) |  | [optional] 

## Example

```python
from argo_workflows.models.artifact_location import ArtifactLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactLocation from a JSON string
artifact_location_instance = ArtifactLocation.from_json(json)
# print the JSON string representation of the object
print ArtifactLocation.to_json()

# convert the object into a dict
artifact_location_dict = artifact_location_instance.to_dict()
# create an instance of ArtifactLocation from a dict
artifact_location_form_dict = artifact_location.from_dict(artifact_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


