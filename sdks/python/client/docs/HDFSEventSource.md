# HDFSEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** |  | [optional] 
**check_interval** | **str** |  | [optional] 
**filter** | [**EventSourceFilter**](EventSourceFilter.md) |  | [optional] 
**hdfs_user** | **str** | HDFSUser is the user to access HDFS file system. It is ignored if either ccache or keytab is used. | [optional] 
**krb_c_cache_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**krb_config_config_map** | [**ConfigMapKeySelector**](ConfigMapKeySelector.md) |  | [optional] 
**krb_keytab_secret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**krb_realm** | **str** | KrbRealm is the Kerberos realm used with Kerberos keytab It must be set if keytab is used. | [optional] 
**krb_service_principal_name** | **str** | KrbServicePrincipalName is the principal name of Kerberos service It must be set if either ccache or keytab is used. | [optional] 
**krb_username** | **str** | KrbUsername is the Kerberos username used with Kerberos keytab It must be set if keytab is used. | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**type** | **str** |  | [optional] 
**watch_path_config** | [**WatchPathConfig**](WatchPathConfig.md) |  | [optional] 

## Example

```python
from argo_workflows.models.hdfs_event_source import HDFSEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of HDFSEventSource from a JSON string
hdfs_event_source_instance = HDFSEventSource.from_json(json)
# print the JSON string representation of the object
print HDFSEventSource.to_json()

# convert the object into a dict
hdfs_event_source_dict = hdfs_event_source_instance.to_dict()
# create an instance of HDFSEventSource from a dict
hdfs_event_source_form_dict = hdfs_event_source.from_dict(hdfs_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


