Part of a larger Organization with a particular set of responsibilities on the production.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property       | Constraint        | Type                                                                                  | Description                                                                            |
| -------------- | ----------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| entityType     | const<br>required | `"Department"`                                                                        | Declares the entity type.                                                              |
| structuralType | const             | `"department"`                                                                        |                                                                                        |
| departmentName |                   | [basicName](../Utility/Utility.md#basicName)                                          | A canonical name and alternative name for the entity.                                  |
| contact        |                   | [contact](../Utility/Utility.md#contact)                                              | Means by which the subject of an entity may be contacted in the production.            |
| Location       | anyOf             | [Location](../Utility/Location.md) <br>[identifier](../Utility/Utility.md#identifier) | A particular place or position either in either the real world or the narrative world. |



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
