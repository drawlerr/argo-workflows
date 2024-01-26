# WorkflowSpec

WorkflowSpec is the specification of a Workflow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_deadline_seconds** | **int** | Optional duration in seconds relative to the workflow start time which the workflow is allowed to run before the controller terminates the  A value of zero is used to terminate a Running workflow | [optional] 
**affinity** | [**Affinity**](Affinity.md) |  | [optional] 
**archive_logs** | **bool** | ArchiveLogs indicates if the container logs should be archived | [optional] 
**arguments** | [**Arguments**](Arguments.md) |  | [optional] 
**artifact_gc** | [**WorkflowLevelArtifactGC**](WorkflowLevelArtifactGC.md) |  | [optional] 
**artifact_repository_ref** | [**ArtifactRepositoryRef**](ArtifactRepositoryRef.md) |  | [optional] 
**automount_service_account_token** | **bool** | AutomountServiceAccountToken indicates whether a service account token should be automatically mounted in pods. ServiceAccountName of ExecutorConfig must be specified if this value is false. | [optional] 
**dns_config** | [**PodDNSConfig**](PodDNSConfig.md) |  | [optional] 
**dns_policy** | **str** | Set DNS policy for the pod. Defaults to \&quot;ClusterFirst\&quot;. Valid values are &#39;ClusterFirstWithHostNet&#39;, &#39;ClusterFirst&#39;, &#39;Default&#39; or &#39;None&#39;. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to &#39;ClusterFirstWithHostNet&#39;. | [optional] 
**entrypoint** | **str** | Entrypoint is a template reference to the starting point of the  | [optional] 
**executor** | [**ExecutorConfig**](ExecutorConfig.md) |  | [optional] 
**hooks** | [**Dict[str, LifecycleHook]**](LifecycleHook.md) | Hooks holds the lifecycle hook which is invoked at lifecycle of step, irrespective of the success, failure, or error status of the primary step | [optional] 
**host_aliases** | [**List[HostAlias]**](HostAlias.md) |  | [optional] 
**host_network** | **bool** | Host networking requested for this workflow pod. Default to false. | [optional] 
**image_pull_secrets** | [**List[LocalObjectReference]**](LocalObjectReference.md) | ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod | [optional] 
**metrics** | [**Metrics**](Metrics.md) |  | [optional] 
**node_selector** | **Dict[str, str]** | NodeSelector is a selector which will result in all pods of the workflow to be scheduled on the selected node(s). This is able to be overridden by a nodeSelector specified in the template. | [optional] 
**on_exit** | **str** | OnExit is a template reference which is invoked at the end of the workflow, irrespective of the success, failure, or error of the primary  | [optional] 
**parallelism** | **int** | Parallelism limits the max total parallel pods that can execute at the same time in a workflow | [optional] 
**pod_disruption_budget** | [**PodDisruptionBudgetSpec**](PodDisruptionBudgetSpec.md) |  | [optional] 
**pod_gc** | [**PodGC**](PodGC.md) |  | [optional] 
**pod_metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**pod_priority** | **int** | Priority to apply to workflow pods. DEPRECATED: Use PodPriorityClassName instead. | [optional] 
**pod_priority_class_name** | **str** | PriorityClassName to apply to workflow pods. | [optional] 
**pod_spec_patch** | **str** | PodSpecPatch holds strategic merge patch to apply against the pod spec. Allows parameterization of container fields which are not strings (e.g. resource limits). | [optional] 
**priority** | **int** | Priority is used if controller is configured to process limited number of workflows in parallel. Workflows with higher priority are processed first. | [optional] 
**retry_strategy** | [**RetryStrategy**](RetryStrategy.md) |  | [optional] 
**scheduler_name** | **str** | Set scheduler name for all pods. Will be overridden if container/script template&#39;s scheduler name is set. Default scheduler will be used if neither specified. | [optional] 
**security_context** | [**PodSecurityContext**](PodSecurityContext.md) |  | [optional] 
**service_account_name** | **str** | ServiceAccountName is the name of the ServiceAccount to run all pods of the workflow as. | [optional] 
**shutdown** | **str** | Shutdown will shutdown the workflow according to its ShutdownStrategy | [optional] 
**suspend** | **bool** | Suspend will suspend the workflow and prevent execution of any future steps in the workflow | [optional] 
**synchronization** | [**Synchronization**](Synchronization.md) |  | [optional] 
**template_defaults** | [**Template**](Template.md) |  | [optional] 
**templates** | [**List[Template]**](Template.md) | Templates is a list of workflow templates used in a workflow | [optional] 
**tolerations** | [**List[Toleration]**](Toleration.md) | Tolerations to apply to workflow pods. | [optional] 
**ttl_strategy** | [**TTLStrategy**](TTLStrategy.md) |  | [optional] 
**volume_claim_gc** | [**VolumeClaimGC**](VolumeClaimGC.md) |  | [optional] 
**volume_claim_templates** | [**List[PersistentVolumeClaim]**](PersistentVolumeClaim.md) | VolumeClaimTemplates is a list of claims that containers are allowed to reference. The Workflow controller will create the claims at the beginning of the workflow and delete the claims upon completion of the workflow | [optional] 
**volumes** | [**List[Volume]**](Volume.md) | Volumes is a list of volumes that can be mounted by containers in a  | [optional] 
**workflow_metadata** | [**WorkflowMetadata**](WorkflowMetadata.md) |  | [optional] 
**workflow_template_ref** | [**WorkflowTemplateRef**](WorkflowTemplateRef.md) |  | [optional] 

## Example

```python
from argo_workflows.models.workflow_spec import WorkflowSpec

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSpec from a JSON string
workflow_spec_instance = WorkflowSpec.from_json(json)
# print the JSON string representation of the object
print WorkflowSpec.to_json()

# convert the object into a dict
workflow_spec_dict = workflow_spec_instance.to_dict()
# create an instance of WorkflowSpec from a dict
workflow_spec_form_dict = workflow_spec.from_dict(workflow_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


