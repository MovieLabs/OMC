Describes the form of the Infrastructure along with the attributes specific to that infrastructures' form.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property             | Constraint        | Type                 | Description               |
| -------------------- | ----------------- | -------------------- | ------------------------- |
| entityType           | const<br>required | `"InfrastructureSC"` | Declares the entity type. |
| strcuturalType       |                   |                      |                           |
| strcuturalProperties |                   |                      |                           |

#### Object Properties
| Property             | Constraint | Type         | Description               |
| -------------------- | ---------- | ------------ | ------------------------- |
| structuralProperties |            | object, null | Declares the entity type. |



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