A technique that creates or enhances visual elements in the finished work
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property   | Constraint        | Type                                                                           | Description                                                       |
| ---------- | ----------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| entityType | const<br>required | `"Effect"`                                                                     | Declares the entity type.                                         |
| effectType | enum              | [effectType](#effectType)                                                      | The specific type of effect                                       |
| Context    | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ] | Informs scope within the construction process of a Creative Work. |

### Controlled & Enumerated Values

#### effectType

| Value         | Description                                                                                                                              |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| effect        | N/A                                                                                                                                      |
| specialEffect | Physically based effects, such as explosions, the use of mannequins, and the use of models, the results of which are captured on-camera. |
| visualEffect  | Effects created on or in the footage after it is captured.                                                                               |
## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "Effect",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "chr/HNvHjXqJY9wv1IwjG-Hf1"  
    }  
  ],  
  "name": "A special Action",  
  "description": "Sven is hit by laser blast",  
  "effectType": "specialEffect",  
  "Context": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "cxt/6RdTMezue-GZEDEB44_x7"  
        }  
      ]  
    }  
  ]  
}
```
