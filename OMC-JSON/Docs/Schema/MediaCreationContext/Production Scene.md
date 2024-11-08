Defined either by explicit divisions in the structure of the Script, e.g., by a Slugline, or by additional capture for use in the Creative Work that is not tied to any particular Scene in the Script.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property        | Operator          | Type                                                                           | Description                                                                                                                       |
| --------------- | ----------------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| entityType      | const<br>required | `"ProductionScene"`                                                            | Declares the entity type.                                                                                                         |
| sceneName       |                   | basicName                                                                      |                                                                                                                                   |
| sceneHeader     |                   | string, null                                                                   | Used when referring to the Production Scene. It is generally synonymous with Slugline and is used to divide a Script into scenes. |
| sceneDescriptor |                   | string, null                                                                   | An alphanumeric reference to a Production Scene.                                                                                  |
| sceneNumber     |                   | string, null                                                                   | A number tied to a Slugline when a Script is locked.                                                                              |
| Context         | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ] |                                                                                                                                   |
## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "ProductionScene",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "pscn/WdGf6FEyzRsudnquqVEAJ"  
    }  
  ],  
  "name": "Title Jungle",  
  "description": "Title sequence with Sven bursting out of the jungle to the title sequence.",  
  "sceneName": {  
    "fullName": "Title Jungle",  
    "altName": "TTL"  
  },  
  "sceneHeader": "Ext. Jungle - Day",  
  "sceneNumber": "1",  
  "sceneDescriptor": "TTL",  
  "Context": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "cxt/L75lHw74UVRtX5ldrr7xu"  
        }  
      ]  
    }  
  ]  
}
```
