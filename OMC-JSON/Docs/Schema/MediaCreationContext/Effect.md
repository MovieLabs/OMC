A technique that creates or enhances visual elements in the finished work
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property   | Operator          | Type                                                                           | Description                 |
| ---------- | ----------------- | ------------------------------------------------------------------------------ | --------------------------- |
| entityType | const<br>required | `"Effect"`                                                                     | Declares the entity type.   |
| effectType | enum              | [effectType](#effectType)                                                      | The specific type of effect |
| Context    | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ] |                             |

### Controlled & Enumerated Values

#### effectType

| Value         | Description |     |
| ------------- | ----------- | --- |
| effect        |             |     |
| specialEffect |             |     |
| visualEffect  |             |     |
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
