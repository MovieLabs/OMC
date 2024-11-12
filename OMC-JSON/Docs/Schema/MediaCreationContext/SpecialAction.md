A performed action or set of actions that requires additional supervision, expertise, or equipment.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property          | Constraint        | Type                                                                           | Description                                                       |
| ----------------- | ----------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| entityType        | const<br>required | `"SpecialAction"`                                                              | Declares the entity type.                                         |
| specialActionType | enum              | [specialActionType](#specialActionType)                                        | The specific type of special action                               |
| Context           | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ] | Informs scope within the construction process of a Creative Work. |
### Controlled & Enumerated Values

#### specialActionType
| Value | Description |
|-------|-------------|
| aerial | Anything involving work with equipment that flies.   |
| choreography | The creation, arrangement, and management of dance.  |
| fight | A fight is physical conflict between characters, in whatever number. Fights often have a Stunt component. |
| marine | Anything involving work on water or in water-borne craft.   |
| motionCapture | The recording of motion as a stream of digital data. |
| specialAction | Describes the use or purpose of an Asset within the production process. |
| stunt | Physical action described or implied in the narrative that would put an actor in some kind of danger and so requires a specialist to manage and coordinate.  |

### Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "SpecialAction",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "chr/HNvHjXqJY9wv1IwjG-Hf1"  
    }  
  ],  
  "name": "A special Action",  
  "description": "Sven is hit by laser blast",  
  "specialActionType": "stunt",  
  "Context": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "cxt/6RdTMezue-GZEDEB44_x7"  
        }  
      ]  
    }  
  ]  
}
```
