# NarrativeWardrobe
The clothing for a Character in the narrative.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property      | Constraint      | Type                                                                               | Description                                                       |
| ------------- | --------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| entityType    | const, required | `"NarrativeWardrobe"`                                                              | Declares the entity type.                                         |
| narrativeType | enum            | [narrativeType](#narrativeType)                                                    | The specific type of narrative wardrobe                           |
| Context       | anyOf           | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]     | Informs scope within the construction process of a Creative Work. |
| Depiction     | anyOf           | [ [Depiction](./Depiction.md) <br>[identifier](../Utility/Utility.md#identifier) ] | A set of Depictions for this Narrative Entity                     |

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
