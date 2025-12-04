# Infrastructure
The underlying systems and framework required for the production of the Creative Work; it is generally not specific to a particular Creative Work.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property         | Constraint        | Type                                                                                                 | Description                                                                                               |
| ---------------- | ----------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| entityType       | const<br>required | `"Infrastructure"`                                                                                   | Declares the entity type.                                                                                 |
| InfrastructureSC |                   | [InfrastructureSC](./Infrastructure.md)                                                              | Describes the form of the Infrastructure along with the attributes specific to that infrastructure's form |
| infrastructureFC |                   | [infrastructureFC](#infrastructureFC)                                                                | Describes the use or purpose of an Infrastructure within the production process                           |
| Context          | anyOf             | [ [Context](../MediaCreationContext/Context.md) <br>[identifier](../Utility/Utility.md#identifier) ] | Informs scope within the construction process of a Creative Work.                                         |

### Object Properties

#### infrastructureFC
Describes the use or purpose of an Infrastructure within the production process

| Property             | Constraint                                                       | Type         | Description                                                 |
| -------------------- | ---------------------------------------------------------------- | ------------ | ----------------------------------------------------------- |
| functionalType       |                                                                  | string, null | The use or purpose of a Task within the production process. |
| functionalProperties | additionalProperties: false                                      | object, null | A set of properties that describe the tasks functional use  |
| customData           | [&nbsp[customData](../Utility/Utility.md#customData)&nbsp], null |              |                                                             |


## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "Infrastructure",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "inf/7EdFxI0xaHHruB97KA9Ni"  
    }  
  ],  
  "InfrastructureSC": {  
    "identifier": [  
      {  
        "identifierScope": "labkoat",  
        "identifierValue": "infsc/7EdFxI0xaHHruB97KA9Ni"  
      }  
    ]  
  },  
  "infrastructureFC": {  
    "functionalType": "camera A",  
    "customData": null  
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