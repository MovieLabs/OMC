Describes the form of the Infrastructure along with the attributes specific to that infrastructures' form.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property         | Operator          | Type                                                                           | Description               |
| ---------------- | ----------------- | ------------------------------------------------------------------------------ | ------------------------- |
| entityType       | const<br>required | `"InfrastructureSC"`                                                           | Declares the entity type. |
| InfrastructureSC |                   |                                                                                |                           |
| infrastructureFC |                   |                                                                                |                           |
| Context          | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ] |                           |

## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "InfrastructureSC",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "infc/7EdFxI0xaHHruB97KA9Ni"  
    }  
  ],  
  "structuralType": "camera",  
  "structuralProperties": null  
}
```