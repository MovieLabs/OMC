# NarrativeStyling
Styling required to prepare an actor for their role.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property      | Constraint        | Type                                                                               | Description                                                       |
| ------------- | ----------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| entityType    | const<br>required | `"NarrativeScene"`                                                                 | Declares the entity type.                                         |
| narrativeType | enum              | [narrativeType](#narrativeType)                                                    | The specific type of narrative styling.                           |
| Context       | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]     | Informs scope within the construction process of a Creative Work. |
| Depiction     | anyOf             | [ [Depiction](./Depiction.md) <br>[identifier](../Utility/Utility.md#identifier) ] | A set of Depictions for this Narrative Entity                     |

### Controlled & Enumerated Values

#### narrativeType
| Value                | Description                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------ |
| narrativeHair        | Hair requirements, procuring and maintaining wigs, and styling and cutting the hair of Participants in Portrayals. |
| narrativeMakeup      | Application and Maintenance of make-up for anyone appearing on-screen.                                             |
| narrativeProsthetics | The use of molding, casting, and sculpting techniques to create the required look for a Character.                 |
| narrativeStyling     | Styling required to prepare an actor for their role.                                                               |

## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "NarrativeStyling",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "psd/CtrVXKgNDDME9aKy8EAqX"  
    }  
  ],  
  "name": "Kiera's hair",  
  "description": "Blue streak",  
  "narrativeType": "narrativeHair",  
  "Context": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "cxt/Q7RfaXCaI8fUyZuvddPFJ"  
        }  
      ]  
    }  
  ]  
}
```
