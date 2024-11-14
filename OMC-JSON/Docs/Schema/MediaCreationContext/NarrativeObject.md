# NarrativeObject
A named object related to or interacting with characters that is implied or understood to be necessary for the narrative. Includes items like props, wardrobe, set dressing and vehicles.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property      | Constraint        | Type                                                                               | Description                                                       |
| ------------- | ----------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| entityType    | const<br>required | `"NarrativeObject"`                                                                | Declares the entity type.                                         |
| narrativeType | enum              | [narrativeType](#narrativeType)                                                    | The specific type of narrative object                             |
| quantity      |                   | string<br>number<br>null                                                           | Indicates the number of these narrative objects required.         |
| size          |                   | string<br>null                                                                     | Indicates a size of the narrative object required.                |
| Context       | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]     | Informs scope within the construction process of a Creative Work. |
| Depiction     | anyOf             | [ [Depiction](./Depiction.md) <br>[identifier](../Utility/Utility.md#identifier) ] | A set of Depictions for this Narrative Entity                     |

### Controlled & Enumerated Values

#### narrativeType
| Value | Description |
|-------|-------------|
| narrativeGreenery | Plant material and terrain-building material described or implied in the narrative, |
| narrativeObject | A significant tangible thing in the narrative. |
| narrativeProp | A Prop as specified or implied by the narrative. |
| narrativeSetDressing | Set Dressing as implied or specified by the narrative. |
| narrativeVehicle | Any mode of transport specified or implied by the narrative.  |

## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "NarrativeObject",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "psd/CtrVXKgNDDME9aKy8EAqX"  
    }  
  ],  
  "name": "Beach rocks",  
  "description": "Various types of rocks that can be found on the beaches of SR 232",  
  "narrativeType": "narrativeSetDressing",  
  "size": "small",  
  "quantity": 10,  
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
