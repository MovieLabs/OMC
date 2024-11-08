The representation of something from a narrative entity by a production entity in the Creative Work, specified or implied by the Script.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property                        | Operator          | Type                                                                                                                                                                                                                                                     | Description                    |
| ------------------------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| entityType                      | const<br>required | `"Depiction"`                                                                                                                                                                                                                                            | Declares the entity type.      |
| [depictionType](#depictionType) | enum              | string, null                                                                                                                                                                                                                                             | The specific type of depiction |
| Depicts                         | oneOf             | [Character](./Character.md) <br>[NarrativeLocation](./NarrativeLocation)<br>[NarrativeStyling](./NarrativeStyling)<br>[NarrativeObject](./NarrativeObject)<br>[NarrativeWardrobe](./NarrativeWardrobe)<br>[identifier](../Utility/Utility.md#identifier) |                                |
| Depicter                        | oneOf             | [Asset](../Asset/Asset.md)<br>[Participant](../Participant/Participant.md)<br>[Composition](../Utility/Composition.md)<br>[identifier](../Utility/Utility.md#identifier)                                                                                 |                                |
| Context                         | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]                                                                                                                                                                           |                                |
### Controlled & Enumerated Values

#### depictionType

| Value     | Description |
| --------- | ----------- |
| depiction |             |
| portrayal |             |
## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "Depiction",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "dep-HNvGRn9JY9wv1IwjG8Gff"  
    }  
  ],  
  "depictionType": "portrayal",  
  "Depicts": {  
    "identifier": [  
      {  
        "identifierScope": "labkoat",  
        "identifierValue": "ptc/HynO3uE6KceCGhx-fkBWo"  
      }  
    ]  
  },  
  "Depicter": {  
    "identifier": [  
      {  
        "identifierScope": "labkoat",  
        "identifierValue": "ptc/HynO3uE6KceCGhx-fkBWo"  
      },  
      {  
        "identifierScope": "imdb",  
        "identifierValue": "nm0872514"  
      }  
    ]  
  }  
}
```