People are the individuals that are associated with the production.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property       | Operator          | Type                                                                           | Description               |
| -------------- | ----------------- | ------------------------------------------------------------------------------ | ------------------------- |
| entityType     | const<br>required | `"Person"`                                                                     | Declares the entity type. |
| structuralType | const             | `"Person"`                                                                     |                           |
| personName     |                   |                                                                                |                           |
| jobTitle       |                   |                                                                                |                           |
| gender         |                   |                                                                                |                           |
| contact        |                   |                                                                                |                           |
| Location       | anyOf             | [Location](./Location.md) <br>[identifier](../Utility/Utility.md#identifier) ] |                           |



## Examples

```JSON{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "Person",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "ptsc/MFlCPsgmu_5xPCpQp7gGH"  
    }  
  ],  
  "name": "John Rene",  
  "description": null,  
  "personName": {  
    "firstGivenName": "John",  
    "familyName": "Rene"  
  },  
  "contact": {  
    "email": {  
      "business": "rene@labkoat.media",  
      "personal": "blank@gmail.com"  
    },  
    "telephone": {  
      "business": "213-555-0161",  
      "personal": "213-555-5678"  
    }  
  },  
  "gender": null  
}
```
