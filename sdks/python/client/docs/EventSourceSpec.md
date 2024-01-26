# EventSourceSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amqp** | [**Dict[str, AMQPEventSource]**](AMQPEventSource.md) |  | [optional] 
**azure_events_hub** | [**Dict[str, AzureEventsHubEventSource]**](AzureEventsHubEventSource.md) |  | [optional] 
**bitbucket** | [**Dict[str, BitbucketEventSource]**](BitbucketEventSource.md) |  | [optional] 
**bitbucketserver** | [**Dict[str, BitbucketServerEventSource]**](BitbucketServerEventSource.md) |  | [optional] 
**calendar** | [**Dict[str, CalendarEventSource]**](CalendarEventSource.md) |  | [optional] 
**emitter** | [**Dict[str, EmitterEventSource]**](EmitterEventSource.md) |  | [optional] 
**event_bus_name** | **str** |  | [optional] 
**file** | [**Dict[str, FileEventSource]**](FileEventSource.md) |  | [optional] 
**generic** | [**Dict[str, GenericEventSource]**](GenericEventSource.md) |  | [optional] 
**github** | [**Dict[str, GithubEventSource]**](GithubEventSource.md) |  | [optional] 
**gitlab** | [**Dict[str, GitlabEventSource]**](GitlabEventSource.md) |  | [optional] 
**hdfs** | [**Dict[str, HDFSEventSource]**](HDFSEventSource.md) |  | [optional] 
**kafka** | [**Dict[str, KafkaEventSource]**](KafkaEventSource.md) |  | [optional] 
**minio** | [**Dict[str, S3Artifact]**](S3Artifact.md) |  | [optional] 
**mqtt** | [**Dict[str, MQTTEventSource]**](MQTTEventSource.md) |  | [optional] 
**nats** | [**Dict[str, NATSEventsSource]**](NATSEventsSource.md) |  | [optional] 
**nsq** | [**Dict[str, NSQEventSource]**](NSQEventSource.md) |  | [optional] 
**pub_sub** | [**Dict[str, PubSubEventSource]**](PubSubEventSource.md) |  | [optional] 
**pulsar** | [**Dict[str, PulsarEventSource]**](PulsarEventSource.md) |  | [optional] 
**redis** | [**Dict[str, RedisEventSource]**](RedisEventSource.md) |  | [optional] 
**redis_stream** | [**Dict[str, RedisStreamEventSource]**](RedisStreamEventSource.md) |  | [optional] 
**replicas** | **int** |  | [optional] 
**resource** | [**Dict[str, ResourceEventSource]**](ResourceEventSource.md) |  | [optional] 
**service** | [**Service**](Service.md) |  | [optional] 
**slack** | [**Dict[str, SlackEventSource]**](SlackEventSource.md) |  | [optional] 
**sns** | [**Dict[str, SNSEventSource]**](SNSEventSource.md) |  | [optional] 
**sqs** | [**Dict[str, SQSEventSource]**](SQSEventSource.md) |  | [optional] 
**storage_grid** | [**Dict[str, StorageGridEventSource]**](StorageGridEventSource.md) |  | [optional] 
**stripe** | [**Dict[str, StripeEventSource]**](StripeEventSource.md) |  | [optional] 
**template** | [**Template**](Template.md) |  | [optional] 
**webhook** | [**Dict[str, WebhookEventSource]**](WebhookEventSource.md) |  | [optional] 

## Example

```python
from argo_workflows.models.event_source_spec import EventSourceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of EventSourceSpec from a JSON string
event_source_spec_instance = EventSourceSpec.from_json(json)
# print the JSON string representation of the object
print EventSourceSpec.to_json()

# convert the object into a dict
event_source_spec_dict = event_source_spec_instance.to_dict()
# create an instance of EventSourceSpec from a dict
event_source_spec_form_dict = event_source_spec.from_dict(event_source_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


