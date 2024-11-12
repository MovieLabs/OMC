Transcoding service or transfer service.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property       | Constraint        | Type                                                                                  | Description                                                                            |
| -------------- | ----------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| entityType     | const<br>required | `"Service"`                                                                           | Declares the entity type.                                                              |
| structuralType | const             | `"service"`                                                                           |                                                                                        |
| serviceName    |                   | [basicName](../Utility/Utility.md#basicName)                                          | A canonical name and alternative name for the entity.                                  |
| contact        |                   | [contact](../Utility/Utility.md#contact)                                              | Means by which the subject of an entity may be contacted in the production.            |
| Location       | anyOf             | [Location](../Utility/Location.md) <br>[identifier](../Utility/Utility.md#identifier) | A particular place or position either in either the real world or the narrative world. |



## Examples

```JSON{  
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "Service",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "ptsc/MFlCPsgmu_5xPCpQp7gGH"  
    }  
  ],  
  "structuralType": "service",  
  "serviceName": {  
    "fullName": "Movielabs fMam",  
    "altName": "fMam"  
  },  
  "contact": {  
    "email": {  
      "business": "fmam@movielabs.com",  
      "personal": "blank@gmail.com"  
    },  
    "telephone": {  
      "business": "213-555-1234",  
      "personal": "213-555-5678"  
    }  
  }  
}
```
