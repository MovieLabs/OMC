A physical or digital object or collection of objects specific to the creation of the Creative Work.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property   | Operator          | Type                                                                           | Description               |
| ---------- | ----------------- | ------------------------------------------------------------------------------ | ------------------------- |
| entityType | const<br>required | `"Asset"`                                                                      | Declares the entity type. |
| AssetSC    |                   |                                                                                |                           |
| assetFC    |                   |                                                                                |                           |
| Context    | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ] |                           |
## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "Asset",  
  "identifier": [  
    {  
      "identifierScope": "cg-example",  
      "identifierValue": "ast/669E728D-8393-4FD1-BF29-2BB7B9DE662C"  
    }  
  ],  
  "name": "TH_Castle_Bricks",  
  "version": {  
    "versionNumber": "1.0",  
    "name": "TH_Castle_Bricks v1.0",  
    "description": "This is the first version of the TH_Castle_Bricks asset.",  
    "annotation": [  
      {  
        "author": "DML",  
        "title": "TH_Castle_Bricks v1.0",  
        "text": "Some text about the TH_Castle_Bricks asset."  
      }  
    ],  
    "DerivationOf": {  
      "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
      "entityType": "Asset",  
      "identifier": [  
        {  
          "identifierScope": "cg-example",  
          "identifierValue": "ast/669E728D-8393-4FD1-BF29-2BB7B9DE662C"  
        }  
      ]  
    },  
    "RevisionOf": {  
      "identifier": [  
        {  
          "identifierScope": "cg-example",  
          "identifierValue": "ast/669E728D-8393-4FD1-BF29-2BB7B9DE662C"  
        }  
      ]  
    },  
    "VariantOf": {  
      "identifier": [  
        {  
          "identifierScope": "cg-example",  
          "identifierValue": "ast/669E728D-8393-4FD1-BF29-2BB7B9DE662C"  
        }  
      ]  
    },  
    "Alternative": [  
      {  
        "identifier": [  
          {  
            "identifierScope": "cg-example",  
            "identifierValue": "ast/669E728D-8393-4FD1-BF29-2BB7B9DE662C"  
          }  
        ]  
      }  
    ],  
    "Derivation": [  
      {  
        "identifier": [  
          {  
            "identifierScope": "cg-example",  
            "identifierValue": "ast/669E728D-8393-4FD1-BF29-2BB7B9DE662C"  
          }  
        ]  
      }  
    ],  
    "Revision": [  
      {  
        "identifier": [  
          {  
            "identifierScope": "cg-example",  
            "identifierValue": "ast/669E728D-8393-4FD1-BF29-2BB7B9DE662C"  
          }  
        ]  
      }  
    ],  
    "Variant": [  
      {  
        "identifier": [  
          {  
            "identifierScope": "cg-example",  
            "identifierValue": "ast/669E728D-8393-4FD1-BF29-2BB7B9DE662C"  
          }  
        ]  
      }  
    ]  
  },  
  "provenance": {  
    "CreatedBy": {  
      "identifier": [  
        {  
          "identifierScope": "cg-example",  
          "identifierValue": "ast/669E728D-8393-4FD1-BF29-2BB7B9DE662C"  
        }  
      ]  
    },  
    "Role": {  
      "identifier": [  
        {  
          "identifierScope": "cg-example",  
          "identifierValue": "ast/669E728D-8393-4FD1-BF29-2BB7B9DE662C"  
        }  
      ]  
    },  
    "createdOn": "2021-01-01T00:00:00Z",  
    "Origin": {  
      "identifier": [  
        {  
          "identifierScope": "cg-example",  
          "identifierValue": "ast/669E728D-8393-4FD1-BF29-2BB7B9DE662C"  
        }  
      ]  
    },  
    "reason": "Initial creation of the TH_Castle_Bricks asset.",  
    "annotation": [  
      {  
        "author": "DML",  
        "title": "Note Title",  
        "text": "Note text."  
      }  
    ]  
  },  
  "assetFC": {  
    "functionalType": "material",  
    "functionalProperties": {  
      "materialType": "inorganic.stone.marble"  
    }  
  },  
  "AssetSC": {  
    "identifier": [  
      {  
        "identifierScope": "cg-example",  
        "identifierValue": "asc/669E728D-8393-4FD1-BF29-2BB7B9DE662C"  
      }  
    ]  
  },  
  "annotation": [  
    {  
      "title": "Note Title",  
      "text": "Note text."  
    }  
  ],  
  "tag": [  
    {  
      "domain": "tagType",  
      "value": [  
        "tagValue", 8  
      ]  
    }  
  ]  
}
```