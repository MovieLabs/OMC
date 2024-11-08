Describes the form of an Asset along with the attributes specific to that asset's form.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property   | Operator          | Type                                                                           | Description               |
| ---------- | ----------------- | ------------------------------------------------------------------------------ | ------------------------- |
| entityType | const<br>required | `"AssetSC"`                                                                    | Declares the entity type. |
| Context    | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ] |                           |

## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "AssetSC",  
  "identifier": [  
    {  
      "identifierScope": "cg-example",  
      "identifierValue": "asc/669E728D-8393-4FD1-BF29-2BB7B9DE662C"  
    }  
  ],  
  "structuralType": "digital.structuredDocument",  
  "structuralProperties": {  
    "linkset": {  
      "recordType": "item",  
      "mediaType": "application/xml"  
    },  
    "fileDetails": {  
      "fileExtension": "mtlx",  
      "fileName": "TH_Castle_Bricks.mtlx",  
      "filePath": "/CG/materials/TH_Castle_Bricks/"  
    },  
    "purpose": "rendering"  
  }  
}
```