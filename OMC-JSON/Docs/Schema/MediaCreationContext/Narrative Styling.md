Styling required to prepare an actor for their role.

| Property      | Operator        | Type                                                                               | Description |
| ------------- | --------------- | ---------------------------------------------------------------------------------- | ----------- |
|               |                 | [baseEntity](../core/baseEntity.md)                                                |             |
| entityType    | const, required | "NarrativeScene"                                                                   |             |
| narrativeType | enum            | [narrativeType](#narrativeType)                                                    |             |
| Context       | anyOf           | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]     |             |
| Depiction     | anyOf           | [ [Depiction](./Depiction.md) <br>[identifier](../Utility/Utility.md#identifier) ] |             |

### Controlled & Enumerated Values

#### narrativeType

| Value                | Description |
| -------------------- | ----------- |
| narrativeStyling     |             |
| narrativeHair        |             |
| narrativeMakeup      |             |
| narrativeProsthetics |             |
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
```
