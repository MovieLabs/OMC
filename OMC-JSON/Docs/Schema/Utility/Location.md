A particular place or position either in either the real world or the narrative world.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property    | Operator          | Type                                                                           | Description               |
| ----------- | ----------------- | ------------------------------------------------------------------------------ | ------------------------- |
| entityType  | const<br>required | `"Location"`                                                                   | Declares the entity type. |
| address     |                   |                                                                                |                           |
| coordinates |                   |                                                                                |                           |
| Context     | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ] |                           |


## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "Location",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "loc/CJXwmiWy3cXV802h-5fWI"  
    }  
  ],  
  "address": {  
    "street": "405 Av. Ogilvy B",  
    "locality": "Montréal",  
    "region": "Quebec",  
    "postalCode": "QC H3N 1M3",  
    "country": "CA"  
  },  
  "coordinates": {  
    "latitude": 45.53072,  
    "longitude": -73.62522  
  }  
}
```
