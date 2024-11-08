Part of a larger Organization with a particular set of responsibilities on the production.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property       | Operator          | Type                                                                           | Description               |
| -------------- | ----------------- | ------------------------------------------------------------------------------ | ------------------------- |
| entityType     | const<br>required | `"Department"`                                                                 | Declares the entity type. |
| structuralType | const             | `"department"`                                                                 |                           |
| departmentName |                   |                                                                                |                           |
| contact        |                   |                                                                                |                           |
| Location       | anyOf             | [Location](./Location.md) <br>[identifier](../Utility/Utility.md#identifier) ] |                           |



## Examples

```JSON{  
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "Department",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "ptsc/MFlCPsgmu_5xPCpQp7gGH"  
    }  
  ],  
  "name": "Wardrobe",  
  "description": null,  
  "structuralType": "department",  
  "departmentName": {  
    "fullName": "Production Wardrobe",  
    "altName": "Wardrobe"  
  },  
  "Location": {  
    "identifier": [  
      {  
        "identifierScope": "labkoat",  
        "identifierValue": "loc/9MLbKNfnaUVj7u3n1Z4E6"  
      }  
    ]  
  }
```
