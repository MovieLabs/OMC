A named object related to or interacting with characters that is implied or understood to be necessary for the narrative. Includes items like props, wardrobe, set dressing and vehicles.

| Property      | Operator             | Type                                                                               | Description |
| ------------- | -------------------- | ---------------------------------------------------------------------------------- | ----------- |
|               |                      | [baseEntity](../core/baseEntity.md)                                                |             |
| entityType    | const, required      | "NarrativeObject"                                                                  |             |
| narrativeType | enum                 | [narrativeType](#narrativeType)                                                    |             |
| quantity      | string, number, null |                                                                                    |             |
| size          | string, null         |                                                                                    |             |
| Context       | anyOf                | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]     |             |
| Depiction     | anyOf                | [ [Depiction](./Depiction.md) <br>[identifier](../Utility/Utility.md#identifier) ] |             |

### Controlled & Enumerated Values

#### narrativeType

| Value                | Description |
| -------------------- | ----------- |
| narrativeObject      |             |
| narrativeProp        |             |
| narrativeGreenery    |             |
| narrativeSetDressing |             |
| narrativeVehicle     |             |
## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "NarrativeObject",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "psd/CtrVXKgNDDME9aKy8EAqX"  
    }  
  ],  
  "name": "Beach rocks",  
  "description": "Various types of rocks that can be found on the beaches of SR 232",  
  "narrativeType": "narrativeSetDressing",  
  "size": "small",  
  "quantity": 10,  
  "Context": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "cxt/Q7RfaXCaI8fUyZuvddPFJ"  
        }  
      ]  
    }  
  ]  
}
```
