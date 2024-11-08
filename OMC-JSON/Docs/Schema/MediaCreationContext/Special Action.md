A performed action or set of actions that requires additional supervision, expertise, or equipment.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property          | Operator          | Type                                                                           | Description                         |
| ----------------- | ----------------- | ------------------------------------------------------------------------------ | ----------------------------------- |
| entityType        | const<br>required | `"SpecialAction"`                                                              | Declares the entity type.           |
| specialActionType | enum              | [specialActionType](#specialActionType)                                        | The specific type of special action |
| Context           | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ] |                                     |
### Controlled & Enumerated Values

#### specialActionType

| Value        | Description |
| ------------ | ----------- |
| stunt        |             |
| choreography |             |
| fight        |             |
## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "SpecialAction",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "chr/HNvHjXqJY9wv1IwjG-Hf1"  
    }  
  ],  
  "name": "A special Action",  
  "description": "Sven is hit by laser blast",  
  "specialActionType": "stunt",  
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
