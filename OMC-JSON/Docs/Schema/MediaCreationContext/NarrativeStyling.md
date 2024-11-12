Styling required to prepare an actor for their role.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property      | Constraint        | Type                                                                               | Description                                                                                                                              |
| ------------- | ----------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| entityType    | const<br>required | `"NarrativeScene"`                                                                 | Declares the entity type.                                                                                                                |
| narrativeType | enum              | [narrativeType](#narrativeType)                                                    | The specific type of narrative styling                                                                                                   |
| Context       | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]     | Informs scope within the construction process of a Creative Work.                                                                        |
| Depiction     | anyOf             | [ [Depiction](./Depiction.md) <br>[identifier](../Utility/Utility.md#identifier) ] | The representation of something from a narrative entity by a production entity in the Creative Work, specified or implied by the Script. |

### Controlled & Enumerated Values

#### narrativeType
| Value | Description |
|-------|-------------|
| narrativeHair | Hair requirements, procuring and maintaining wigs, and styling and cutting the hair of Participants in Portrayals.  |
| narrativeMakeup | Application and Maintenance of make-up for anyone appearing on-screen.  |
| narrativeProsthetics | N/A |
| narrativeStyling | N/A |

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
