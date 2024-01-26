# HDFSArtifact

HDFSArtifact is the location of an HDFS artifact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | Addresses is accessible addresses of HDFS name nodes | [optional] 
**force** | **bool** | Force copies a file forcibly even if it exists | [optional] 
**hdfs_user** | **str** | HDFSUser is the user to access HDFS file system. It is ignored if either ccache or keytab is used. | [optional] 
**krb_c_cache_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**krb_config_config_map** | [**ConfigMapKeySelector**](ConfigMapKeySelector.md) |  | [optional] 
**krb_keytab_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**krb_realm** | **str** | KrbRealm is the Kerberos realm used with Kerberos keytab It must be set if keytab is used. | [optional] 
**krb_service_principal_name** | **str** | KrbServicePrincipalName is the principal name of Kerberos service It must be set if either ccache or keytab is used. | [optional] 
**krb_username** | **str** | KrbUsername is the Kerberos username used with Kerberos keytab It must be set if keytab is used. | [optional] 
**path** | **str** | Path is a file path in HDFS | 

## Example

```python
from argo_workflows.models.hdfs_artifact import HDFSArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of HDFSArtifact from a JSON string
hdfs_artifact_instance = HDFSArtifact.from_json(json)
# print the JSON string representation of the object
print HDFSArtifact.to_json()

# convert the object into a dict
hdfs_artifact_dict = hdfs_artifact_instance.to_dict()
# create an instance of HDFSArtifact from a dict
hdfs_artifact_form_dict = hdfs_artifact.from_dict(hdfs_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


