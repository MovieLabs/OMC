A piece of work to be done and completed as a step in the production process.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property   | Operator          | Type                                                                           | Description               |
| ---------- | ----------------- | ------------------------------------------------------------------------------ | ------------------------- |
| entityType | const<br>required | `"Task"`                                                                       | Declares the entity type. |
| TaskSC     |                   |                                                                                |                           |
| taskFC     |                   |                                                                                |                           |
| Context    | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ] |                           |

## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "Task",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "tsk/7EdFxI0xaHHruB97KA9Ni"  
    }  
  ],  
  "TaskSC": {  
    "identifier": [  
      {  
        "identifierScope": "labkoat",  
        "identifierValue": "tsksc/7EdFxI0xaHHruB97KA9Ni"  
      }  
    ]  
  },  
  "taskFC": {  
    "functionalType": "transcode",  
    "customData": {  
      "taskType": "director"  
    }  
  },  
  "Context": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "cxt/hlDwnZidsasQM3qOTyCWE"  
        }  
      ]  
    }  
  ]  
}
```