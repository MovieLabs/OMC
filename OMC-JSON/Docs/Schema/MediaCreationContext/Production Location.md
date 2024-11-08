A real place that is used to depict the Narrative Location or used for creating the production.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property     | Operator          | Type                                                                                 | Description                              |
| ------------ | ----------------- | ------------------------------------------------------------------------------------ | ---------------------------------------- |
| entityType   | const<br>required | `"ProductionLocation"`                                                               | Declares the entity type.                |
| locationType | enum              | [locationType](#locationType)                                                        | The specific type of production location |
| Context      | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]       |                                          |
| Location     | anyOf             | [Location](../Utility/Location.md)<br>[identifier](../Utility/Utility.md#identifier) |                                          |

### Controlled & Enumerated Values

#### locationType

| Value      | Description |     |
| ---------- | ----------- | --- |
| production |             |     |
| shooting   |             |     |
## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "ProductionLocation",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "loc/DBMKDFZ5G7PBwtgK2PXBG"  
    }  
  ],  
  "name": "Game On ",  
  "description": "Motion Capture Stage",  
  "locationType": "shooting",  
  "Location": {  
    "identifier": [  
      {  
        "identifierScope": "labkoat",  
        "identifierValue": "loc/CJXwmiWy3cXV802h-5fWI"  
      }  
    ]  
  },  
  "Context": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "cxt/74J6YVjYu7jTmhuoKCVx9"  
        }  
      ]  
    }  
  ]  
}
```
