The combination of a Task and the Participant responsible for it.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property   | Constraint        | Type                  | Description               |
| ---------- | ----------------- | --------------------- | ------------------------- |
| entityType | const<br>required | `"Role"`              | Declares the entity type. |
| roleType   | ctrlValue         | [roleType](#roleType) |                           |

### ControlledValues

#### roleType


| Value | Description                               |
| ----- | ----------------------------------------- |
| actor | Person who plays the role of a character. |

## Examples

```JSON{  
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "Role",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "rol/7EdFxI0xaHHruB97KA9Ni"  
    }  
  ],  
  "roleType": "director"  
}
```
