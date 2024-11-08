
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property   | Operator          | Type                                                                           | Description               |
| ---------- | ----------------- | ------------------------------------------------------------------------------ | ------------------------- |
| entityType | const<br>required | `"TaskSC"`                                                                     | Declares the entity type. |
| TaskSC     |                   |                                                                                |                           |
| taskFC     |                   |                                                                                |                           |
| Context    | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ] |                           |

## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "TaskSC",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "tsksc/7EdFxI0xaHHruB97KA9Ni"  
    }  
  ],  
  "structuralType": null,  
  "structuralProperties": null  
}
```