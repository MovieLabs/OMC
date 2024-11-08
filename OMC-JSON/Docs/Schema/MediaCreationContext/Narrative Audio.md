A location specified or implied by the narrative.

| Property      | Operator        | Type                                                                               | Description |
| ------------- | --------------- | ---------------------------------------------------------------------------------- | ----------- |
|               |                 | [baseEntity](../core/baseEntity.md)                                                |             |
| entityType    | const, required | "NarrativeAudio"                                                                   |             |
| narrativeType | enum            | [narrativeType](#narrativeType)                                                    |             |
| Context       | anyOf           | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]     |             |
| Depiction     | anyOf           | [ [Depiction](./Depiction.md) <br>[identifier](../Utility/Utility.md#identifier) ] |             |

### Controlled & Enumerated Values

#### narrativeType

| Value                | Description |
| -------------------- | ----------- |
| narrativeAudio       |             |
| narrativeMusic       |             |
| narrativeSoundEffect |             |
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
