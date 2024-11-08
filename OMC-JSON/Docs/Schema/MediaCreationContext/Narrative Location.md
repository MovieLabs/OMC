A location specified or implied by the narrative.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property      | Operator          | Type                                                                               | Description                             |
| ------------- | ----------------- | ---------------------------------------------------------------------------------- | --------------------------------------- |
| entityType    | const<br>required | `"NarrativeLocation"`                                                              | Declares the entity type.               |
| narrativeType | enum              | [narrativeType](#narrativeType)                                                    | The specific type of narrative location |
| Context       | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]     |                                         |
| Depiction     | anyOf             | [ [Depiction](./Depiction.md) <br>[identifier](../Utility/Utility.md#identifier) ] |                                         |

### Controlled & Enumerated Values

#### narrativeType

| Value             | Description                                       |
| ----------------- | ------------------------------------------------- |
| narrativeLocation | A location specified or implied by the narrative. |
## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "NarrativeLocation",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "loc/cnFSmIYdk0j5NhYkkcjnp"  
    }  
  ],  
  "name": "Headquarters",  
  "description": "The galactic federation home base of operations",  
  "narrativeType": "narrativeLocation",  
  "Location": {  
    "identifier": [  
      {  
        "identifierScope": "labkoat",  
        "identifierValue": "nloc/St_Hh-LxAQo4ICUAtbZ0v"  
      }  
    ]  
  },  
  "Context": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "cxt/34T8RjoQbKCl5lnyalkmr"  
        }  
      ]  
    }  
  ],  
  "Depiction": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "dep-HNvGRn9JY9wv1IwjG8Gff"  
        }  
      ]  
    }  
  ]  
}
```
