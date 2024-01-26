# PayloadField

PayloadField binds a value at path within the event payload against a name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name acts as key that holds the value at the path. | [optional] 
**path** | **str** | Path is the JSONPath of the event&#39;s (JSON decoded) data key Path is a series of keys separated by a dot. A key may contain wildcard characters &#39;*&#39; and &#39;?&#39;. To access an array value use the index as the key. The dot and wildcard characters can be escaped with &#39;\\\\&#39;. See https://github.com/tidwall/gjson#path-syntax for more information on how to use this. | [optional] 

## Example

```python
from argo_workflows.models.payload_field import PayloadField

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadField from a JSON string
payload_field_instance = PayloadField.from_json(json)
# print the JSON string representation of the object
print PayloadField.to_json()

# convert the object into a dict
payload_field_dict = payload_field_instance.to_dict()
# create an instance of PayloadField from a dict
payload_field_form_dict = payload_field.from_dict(payload_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


