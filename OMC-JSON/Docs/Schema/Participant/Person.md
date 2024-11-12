People are the individuals that are associated with the production.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property       | Constraint        | Type                                                                                  | Description                                                                             |
| -------------- | ----------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| entityType     | const<br>required | `"Person"`                                                                            | Declares the entity type.                                                               |
| structuralType | const             | `"Person"`                                                                            |                                                                                         |
| personName     |                   | [completeName](../Utility/Utility.md#completeName)                                    | A detailed description of a person, or other entities, name and variants of their name. |
| jobTitle       |                   | string, null                                                                          | A persons job title (as distinct from a specific role).                                 |
| gender         |                   | [gender](../Utility/Utility.md#gender)                                                | A person, or others, expressed or preferred gender and pronoun.                         |
| contact        |                   | [contact](../Utility/Utility.md#contact)                                              | Means by which the subject of an entity may be contacted in the production.             |
| Location       | oneOf             | [Location](../Utility/Location.md) <br>[identifier](../Utility/Utility.md#identifier) | A particular place or position either in either the real world or the narrative world.  |

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
