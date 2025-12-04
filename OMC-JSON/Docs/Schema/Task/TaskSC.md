# TaskSC

### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property             | Constraint        | Type                                                             | Description                                     |
| -------------------- | ----------------- | ---------------------------------------------------------------- | ----------------------------------------------- |
| entityType           | const<br>required | `"TaskSC"`                                                       | Declares the entity type.                       |
| strcuturalType       |                   | string, null                                                     | A structured description of the the Tasks form. |
| structuralProperties |                   |                                                                  |                                                 |
| customData           |                   | [&nbsp[customData](../Utility/Utility.md#customData)&nbsp], null |                                                 |

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