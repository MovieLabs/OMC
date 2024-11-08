The clothing for a Character in the narrative.

| Property      | Operator        | Type                                                                               | Description |
| ------------- | --------------- | ---------------------------------------------------------------------------------- | ----------- |
|               |                 | [baseEntity](../core/baseEntity.md)                                                |             |
| entityType    | const, required | "NarrativeScene"                                                                   |             |
| narrativeType | enum            | [narrativeType](#narrativeType)                                                    |             |
| Context       | anyOf           | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]     |             |
| Depiction     | anyOf           | [ [Depiction](./Depiction.md) <br>[identifier](../Utility/Utility.md#identifier) ] |             |

### Controlled & Enumerated Values

#### narrativeType

| Value             | Description                                    |
| ----------------- | ---------------------------------------------- |
| narrativeWardrobe | The clothing for a Character in the narrative. |
## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "NarrativeWardrobe",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "wrd/Ia7-FdhY1yBFyqG_2nYW8"  
    }  
  ],  
  "name": "Spacesuit",  
  "description": "RD-12 Envrionmental Protection Suit",  
  "narrativeType": "narrativeWardrobe",  
  "Context": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "cxt/wWz2OqsKDO7bTLZm9TdTJ"  
        }  
      ]  
    }  
  ]  
}
```
