A legal entity or groups of people associated with the production.. with a particular purpose relative to the production.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property         | Constraint        | Type                                                                                  | Description                                                                            |
| ---------------- | ----------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| entityType       | const<br>required | `"Organization"`                                                                      | Declares the entity type.                                                              |
| structuralType   | const             | `"organization"`                                                                      |                                                                                        |
| organizationName |                   | [basicName](../Utility/Utility.md#basicName)                                          | A canonical name and alternative name for the entity.                                  |
| contact          |                   | [contact](../Utility/Utility.md#contact)                                              | Means by which the subject of an entity may be contacted in the production.            |
| Location         | anyOf             | [Location](../Utility/Location.md) <br>[identifier](../Utility/Utility.md#identifier) | A particular place or position either in either the real world or the narrative world. |



## Examples

```JSON{  
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "Organization",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "ptsc/MFlCPsgmu_5xPCpQp7gGH"  
    }  
  ],  
  "name": "Organization",  
  "description": null,  
  "structuralType": "organization",  
  "organizationName": {  
    "fullName": "Labkoat Media LLC",  
    "altName": "Labkoat"  
  },  
  "Location": {  
    "identifier": [  
      {  
        "identifierScope": "labkoat",  
        "identifierValue": "loc/9MLbKNfnaUVj7u3n1Z4E6"  
      }  
    ]  
  },  
  "contact": {  
    "email": {  
      "business": "blank@labkoat.media",  
      "personal": "blank@gmail.com"  
    },  
    "telephone": {  
      "business": "213-555-1234",  
      "personal": "213-555-5678"  
    }  
  }  
}
```
