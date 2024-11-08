Transcoding service or transfer service.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property       | Operator          | Type                                                                           | Description               |
| -------------- | ----------------- | ------------------------------------------------------------------------------ | ------------------------- |
| entityType     | const<br>required | `"Service"`                                                                    | Declares the entity type. |
| structuralType | const             | `"service"`                                                                    |                           |
| serviceName    |                   |                                                                                |                           |
| contact        |                   |                                                                                |                           |
| Location       | anyOf             | [Location](./Location.md) <br>[identifier](../Utility/Utility.md#identifier) ] |                           |



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
