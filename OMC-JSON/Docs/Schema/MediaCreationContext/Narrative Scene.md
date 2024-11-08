Taken from the narrative itself and traditionally defined by creative intent and typically a unity of time, place, action, or theme.

| Property      | Operator        | Type                                                                           | Description |
| ------------- | --------------- | ------------------------------------------------------------------------------ | ----------- |
|               |                 | [baseEntity](../core/baseEntity.md)                                            |             |
| entityType    | const, required | "NarrativeScene"                                                               |             |
| narrativeType | enum            | [narrativeType](#narrativeType)                                                |             |
| sceneName     |                 | [sceneName](#sceneName)                                                        |             |
| sceneNumber   |                 | string, number, null                                                           |             |
| slugline      |                 | [ [annotation](../Utility/Utility.md#annotation) ]                             |             |
| Context       | anyOf           | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ] |             |

### Controlled & Enumerated Values

#### narrativeType

| Value          | Description                                                                                                                          |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| narrativeScene | Taken from the narrative itself and traditionally defined by creative intent and typically a unity of time, place, action, or theme. |
### Object Properties
#### sceneName

| Property | Operator | Type         | Description                                                                    |
| -------- | -------- | ------------ | ------------------------------------------------------------------------------ |
| fullName |          | string, null | A full descriptive name for the scene                                          |
| altName  |          |              | An alternate, often shorter, name used in applications to identify the scenes. |

## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "NarrativeScene",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "nscn/wz_MHOLYI3VwYx_0AX47Y"  
    }  
  ],  
  "name": "Jungle",  
  "description": "Title sequence with Sven bursting out of the jungle to the title sequence.",  
  "narrativeType": "narrativeScene",  
  "sceneName": {  
    "fullName": "Jungle",  
    "altName": "JGL"  
  },  
  "sceneNumber": "1",  
  "slugline": [  
    {  
      "title": "INT/EXT",  
      "text": "EXT"  
    },  
    {  
      "title": "time",  
      "text": "DAY"  
    }  
  ],  
  "Context": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "cxt/Yhk9Nqa9UvkoOmccdPEJf"  
        }  
      ]  
    }  
  ]  
}
```
