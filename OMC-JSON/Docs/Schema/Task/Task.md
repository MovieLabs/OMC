# Task
A piece of work to be done and completed as a step in the production process.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property   | Constraint        | Type                                                                                                 | Description                                                                       |
| ---------- | ----------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| entityType | const<br>required | `"Task"`                                                                                             | Declares the entity type.                                                         |
| TaskSC     |                   | [TaskSC](./TaskSC.md)                                                                                | Describes the form of Task along with the attributes specific to that task’s form |
| taskFC     |                   | [taskFC](#taskFC)                                                                                    | Describes the purpose of the Task within the production process                   |
| Context    | anyOf             | [ [Context](../MediaCreationContext/Context.md) <br>[identifier](../Utility/Utility.md#identifier) ] | Informs scope within the construction process of a Creative Work.                 |
### Object Properties

#### taskFC
Describes the purpose of the Task within the production process.

| Property             | Constraint                                                       | Type         | Description                                                 |
| -------------------- | ---------------------------------------------------------------- | ------------ | ----------------------------------------------------------- |
| functionalType       | string, null                                                     | string, null | The use or purpose of a Task within the production process. |
| functionalProperties |                                                                  | object, null | A set of properties that describe the tasks functional use  |
| customData           | [&nbsp[customData](../Utility/Utility.md#customData)&nbsp], null |              |                                                             |


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