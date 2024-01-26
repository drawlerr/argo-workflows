# Template

Template is a reusable and composable unit of execution in a workflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_deadline_seconds** | **str** |  | [optional] 
**affinity** | [**Affinity**](Affinity.md) |  | [optional] 
**archive_location** | [**ArtifactLocation**](ArtifactLocation.md) |  | [optional] 
**automount_service_account_token** | **bool** | AutomountServiceAccountToken indicates whether a service account token should be automatically mounted in pods. ServiceAccountName of ExecutorConfig must be specified if this value is false. | [optional] 
**container** | [**Container**](Container.md) |  | [optional] 
**container_set** | [**ContainerSetTemplate**](ContainerSetTemplate.md) |  | [optional] 
**daemon** | **bool** | Daemon will allow a workflow to proceed to the next step so long as the container reaches readiness | [optional] 
**dag** | [**DAGTemplate**](DAGTemplate.md) |  | [optional] 
**data** | [**Data**](Data.md) |  | [optional] 
**executor** | [**ExecutorConfig**](ExecutorConfig.md) |  | [optional] 
**fail_fast** | **bool** | FailFast, if specified, will fail this template if any of its child pods has failed. This is useful for when this template is expanded with &#x60;withItems&#x60;, etc. | [optional] 
**host_aliases** | [**List[HostAlias]**](HostAlias.md) | HostAliases is an optional list of hosts and IPs that will be injected into the pod spec | [optional] 
**http** | [**HTTP**](HTTP.md) |  | [optional] 
**init_containers** | [**List[UserContainer]**](UserContainer.md) | InitContainers is a list of containers which run before the main container. | [optional] 
**inputs** | [**Inputs**](Inputs.md) |  | [optional] 
**memoize** | [**Memoize**](Memoize.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**metrics** | [**Metrics**](Metrics.md) |  | [optional] 
**name** | **str** | Name is the name of the template | [optional] 
**node_selector** | **Dict[str, str]** | NodeSelector is a selector to schedule this step of the workflow to be run on the selected node(s). Overrides the selector set at the workflow level. | [optional] 
**outputs** | [**Outputs**](Outputs.md) |  | [optional] 
**parallelism** | **int** | Parallelism limits the max total parallel pods that can execute at the same time within the boundaries of this template invocation. If additional steps/dag templates are invoked, the pods created by those templates will not be counted towards this total. | [optional] 
**plugin** | **object** | Plugin is an Object with exactly one key | [optional] 
**pod_spec_patch** | **str** | PodSpecPatch holds strategic merge patch to apply against the pod spec. Allows parameterization of container fields which are not strings (e.g. resource limits). | [optional] 
**priority** | **int** | Priority to apply to workflow pods. | [optional] 
**priority_class_name** | **str** | PriorityClassName to apply to workflow pods. | [optional] 
**resource** | [**ResourceTemplate**](ResourceTemplate.md) |  | [optional] 
**retry_strategy** | [**RetryStrategy**](RetryStrategy.md) |  | [optional] 
**scheduler_name** | **str** | If specified, the pod will be dispatched by specified scheduler. Or it will be dispatched by workflow scope scheduler if specified. If neither specified, the pod will be dispatched by default scheduler. | [optional] 
**script** | [**ScriptTemplate**](ScriptTemplate.md) |  | [optional] 
**security_context** | [**PodSecurityContext**](PodSecurityContext.md) |  | [optional] 
**service_account_name** | **str** | ServiceAccountName to apply to workflow pods | [optional] 
**sidecars** | [**List[UserContainer]**](UserContainer.md) | Sidecars is a list of containers which run alongside the main container Sidecars are automatically killed when the main container completes | [optional] 
**steps** | [**List[ParallelSteps]**](ParallelSteps.md) | Steps define a series of sequential/parallel workflow steps | [optional] 
**suspend** | [**SuspendTemplate**](SuspendTemplate.md) |  | [optional] 
**synchronization** | [**Synchronization**](Synchronization.md) |  | [optional] 
**timeout** | **str** | Timeout allows to set the total node execution timeout duration counting from the node&#39;s start time. This duration also includes time in which the node spends in Pending state. This duration may not be applied to Step or DAG templates. | [optional] 
**tolerations** | [**List[Toleration]**](Toleration.md) | Tolerations to apply to workflow pods. | [optional] 
**volumes** | [**List[Volume]**](Volume.md) | Volumes is a list of volumes that can be mounted by containers in a template. | [optional] 

## Example

```python
from argo_workflows.models.template import Template

# TODO update the JSON string below
json = "{}"
# create an instance of Template from a JSON string
template_instance = Template.from_json(json)
# print the JSON string representation of the object
print Template.to_json()

# convert the object into a dict
template_dict = template_instance.to_dict()
# create an instance of Template from a dict
template_form_dict = template.from_dict(template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


