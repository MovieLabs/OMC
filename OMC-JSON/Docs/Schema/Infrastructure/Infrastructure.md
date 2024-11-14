# Infrastructure
The underlying systems and framework required for the production of the Creative Work; it is generally not specific to a particular Creative Work.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property         | Constraint        | Type                                                                                                 | Description                                                       |
| ---------------- | ----------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| entityType       | const<br>required | `"Infrastructure"`                                                                                   | Declares the entity type.                                         |
| InfrastructureSC |                   | [InfrastructureSC](./Infrastructure.md)                                                              |                                                                   |
| infrastructureFC |                   | [infrastructureFC](#infrastructureFC)                                                                |                                                                   |
| Context          | anyOf             | [ [Context](../MediaCreationContext/Context.md) <br>[identifier](../Utility/Utility.md#identifier) ] | Informs scope within the construction process of a Creative Work. |

### Object Properties

#### infrastructureFC

| Property             | Constraint                  | Type         | Description |
| -------------------- | --------------------------- | ------------ | ----------- |
| functionalType       |                             | string, null |             |
| functionalProperties | additionalProperties: false | object, null |             |


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