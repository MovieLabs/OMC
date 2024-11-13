A significant sound in the narrative.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property      | Constraint        | Type                                                                               | Description                                                       |
| ------------- | ----------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| entityType    | const<br>required | `"NarrativeAudio"`                                                                 | Declares the entity type.                                         |
| narrativeType | enum              | [narrativeType](#narrativeType)                                                    | The specific type of narrative audio                              |
| Context       | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]     | Informs scope within the construction process of a Creative Work. |
| Depiction     | anyOf             | [ [Depiction](./Depiction.md) <br>[identifier](../Utility/Utility.md#identifier) ] | A set of Depictions for this Narrative Entity                     |

### Controlled & Enumerated Values

#### narrativeType

| Value | Description |
|-------|-------------|
| narrativeAudio | A significant sound in the narrative. |
| narrativeMusic | Music that is implicitly or explicitly used to advance or support the narrative.  |
| narrativeSoundEffect | A sound that explicitly or implicitly advances or supports the narrative.   |
## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "NarrativeAudio",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "loc/cnFSmIYdk0j5NhYkkcjnp"  
    }  
  ],  
  "name": "Explosion",  
  "description": "Space ship explosion",  
  "narrativeType": "narrativeSoundEffect",  
  "Context": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "cxt/34T8RjoQbKCl5lnyalkmr"  
        }  
      ]  
    }  
  ],  
  "Depiction": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "dep-HNvGRn9JY9wv1IwjG8Gff"  
        }  
      ]  
    }  
  ]  
}
```
