The underlying systems and framework required for the production of the Creative Work; it is generally not specific to a particular Creative Work.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property         | Operator          | Type                                                                           | Description               |
| ---------------- | ----------------- | ------------------------------------------------------------------------------ | ------------------------- |
| entityType       | const<br>required | `"Infrastructure"`                                                             | Declares the entity type. |
| InfrastructureSC |                   |                                                                                |                           |
| infrastructureFC |                   |                                                                                |                           |
| Context          | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ] |                           |

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