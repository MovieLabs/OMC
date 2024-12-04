# Context
Informs scope within the construction process of a Creative Work.
### Properties

Includes properties from: [baseEntity](../core/baseEntity.md)

| Property          | Constraint        | Type                                                                           | Description                                                                        |
| ----------------- | ----------------- |--------------------------------------------------------------------------------| ---------------------------------------------------------------------------------- |
| entityType        | const<br>required | `"Context"`                                                                    | Declares the entity type.                                                          |
| contextType       | ctrlValue         | [contextType](#contextType)                                                    | The specific type of context                                                       |
| contextCategory   |                   | string<br>null                                                                 | Provides an additional level of categorization of the Context beyond it's type.    |
| contextProperties |                   | [contextProperties](#contextProperties)                                        | Properties specific to this composition                                            |
| For               |                   |                                                                                |                                                                                    |
| Context           | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ] | Informs scope within the construction process of a Creative Work.                  |
| contributor       |                   | [contributor](#contributor)                                                    | The person or organization making the contribution.                                |
| contributesTo     |                   | [contributesTo](#contributesTo)                                                | The creative work that the person or organization is contributing to.              |
| features          |                   | [features](#features)                                                          | Relates a narrative scene to other narrative entities.                             |
| featuresIn        |                   | [featuresIn](#featuresIn)                                                      | Relates a narrative entity to a narrative scene.                                   |
| for               |                   | [for](#for)                                                                    | Relates non-narrative entities, the inverse of has.                                |
| has               |                   | [has](#has)                                                                    | Relates non-narrative entities, the inverse of for.                                |
| neededBy          |                   | [neededBy](#neededBy)                                                          | Relates narrative entities, e.g. narrative prop, to a character, inverse of needs. |
| needs             |                   | [needs](#needs)                                                                | Relates a character to other narrative entities, inverse of neededBy.              |
| related           |                   | [related](#related)                                                            | A generic related entity.                                                          |
| represents        |                   | [represents](#represents)                                                      |                                                                                    |
| representedBy     |                   | [representedBy](#representedBy)                                                |                                                                                    |
| usedIn            |                   | [usedIn](#usedIn)                                                              |                                                                                    |
| uses              |                   | [uses](#uses)                                                                  |                                                                                    |

### Object Properties

#### contextProperties

| Property | Constraint | Type                  | Description                           |
| -------- | ---------- | --------------------- | ------------------------------------- |
| shootDay |            | [shootDay](#shootDay) | Details about the shoot day and date. |
#### contributor
| Property    | Constraint | Type                                                                                               | Description |
| ----------- | ---------- | -------------------------------------------------------------------------------------------------- | ----------- |
| Participant |            | [ [Participant](../Participant/Participant.md)<br>[identifier](../Utility/Utility.md#identifier) ] |             |
#### contributesTo
| Property     | Constraint | Type                                                                                    | Description |
| ------------ | ---------- | --------------------------------------------------------------------------------------- | ----------- |
| CreativeWork |            | [ [CreativeWork](./CreativeWork.md)<br>[identifier](../Utility/Utility.md#identifier) ] |             |
#### features
| Property          | Constraint | Type                                                                                              | Description |
| ----------------- | ---------- | ------------------------------------------------------------------------------------------------- | ----------- |
| Character         | anyOf      | [ [Character](./Character.md)<br>[identifier](../Utility/Utility.md#identifier) ]                 |             |
| Effect            | anyOf      | [ [Effect](./Effect.md)<br>[identifier](../Utility/Utility.md#identifier) ]                       |             |
| NarrativeAudio    | anyOf      | [ [NarrativeAudio](./NarrativeAudio.md)<br>[identifier](../Utility/Utility.md#identifier) ]       |             |
| NarrativeLocation | anyOf      | [ [NarrativeLocation](./NarrativeLocation.md)<br>[identifier](../Utility/Utility.md#identifier) ] |             |
| NarrativeObject   | anyOf      | [ [NarrativeObject](./NarrativeObject.md)<br>[identifier](../Utility/Utility.md#identifier) ]     |             |
| NarrativeStyling  | anyOf      | [ [NarrativeStyling](./NarrativeStyling.md)<br>[identifier](../Utility/Utility.md#identifier) ]   |             |
| NarrativeWardrobe | anyOf      | [ [NarrativeWardrobe](./NarrativeWardrobe.md)<br>[identifier](../Utility/Utility.md#identifier) ] |             |
| SpecialAction     | anyOf      | [ [SpecialAction](./SpecialAction.md)<br>[identifier](../Utility/Utility.md#identifier) ]         |             |

#### featuresIn
| Property       | Constraint | Type                                                                                        | Description |
| -------------- | ---------- | ------------------------------------------------------------------------------------------- | ----------- |
| NarrativeScene | anyOf      | [ [NarrativeScene](./NarrativeScene.md)<br>[identifier](../Utility/Utility.md#identifier) ] |             |

#### for
| Property        | Constraint | Type                                                                                           | Description |
| --------------- | ---------- | ---------------------------------------------------------------------------------------------- | ----------- |
| Asset           | anyOf      | [ [Asset](../Asset/Asset.md)<br>[identifier](../Utility/Utility.md#identifier) ]               |             |
| CreativeWork    | anyOf      | [ [CreativeWork](./CreativeWork.md)<br>[identifier](../Utility/Utility.md#identifier) ]        |             |
| NarrativeScene  | anyOf      | [ [NarrativeScene](./NarrativeScene.md)<br>[identifier](../Utility/Utility.md#identifier) ]    |             |
| ProductionScene | anyOf      | [ [ProductionScene](./ProductionScene.md)<br>[identifier](../Utility/Utility.md#identifier) ]  |             |
| Slate           | anyOf      | [ [Slate](./Slate.md)<br>[identifier](../Utility/Utility.md#identifier) ]                      |             |
| Composition     | anyOf      | [ [Composition](../Utility/Composition.md)<br>[identifier](../Utility/Utility.md#identifier) ] |             |
#### has
| Property          | Constraint | Type                                                                                                        | Description |
| ----------------- | ---------- | ----------------------------------------------------------------------------------------------------------- | ----------- |
| Asset             | anyOf      | [ [Asset](../Asset/Asset.md)<br>[identifier](../Utility/Utility.md#identifier) ]                            |             |
| Infrastructure    | anyOf      | [ [Infrastructure](../Infrastructure/Infrastructure.md)<br>[identifier](../Utility/Utility.md#identifier) ] |             |
| NarrativeLocation | anyOf      | [ [NarrativeLocation](./NarrativeLocation.md)<br>[identifier](../Utility/Utility.md#identifier) ]           |             |
| NarrativeScene    | anyOf      | [ [NarrativeScene](./NarrativeScene.md)<br>[identifier](../Utility/Utility.md#identifier) ]                 |             |
| Participant       | anyOf      | [ [Participant](../Participant/Participant.md)<br>[identifier](../Utility/Utility.md#identifier) ]          |             |
| ProductionScene   | anyOf      | [ [ProductionScene](./ProductionScene.md)<br>[identifier](../Utility/Utility.md#identifier) ]               |             |
| Slate             | anyOf      | [ [Slate](./Slate.md)<br>[identifier](../Utility/Utility.md#identifier) ]                                   |             |
| SpecialAction     | anyOf      | [ [SpecialAction](./SpecialAction.md)<br>[identifier](../Utility/Utility.md#identifier) ]                   |             |
#### neededBy
| Property  | Constraint | Type                                                                              | Description |
| --------- | ---------- | --------------------------------------------------------------------------------- | ----------- |
| Character | anyOf      | [ [Character](./Character.md)<br>[identifier](../Utility/Utility.md#identifier) ] |             |
#### needs
| Property          | Constraint | Type                                                                                              | Description |
| ----------------- | ---------- | ------------------------------------------------------------------------------------------------- | ----------- |
| Effect            | anyOf      | [ [Effect](./Effect.md)<br>[identifier](../Utility/Utility.md#identifier) ]                       |             |
| NarrativeAudio    | anyOf      | [ [NarrativeAudio](./NarrativeAudio.md)<br>[identifier](../Utility/Utility.md#identifier) ]       |             |
| NarrativeObject   | anyOf      | [ [NarrativeObject](./NarrativeObject.md)<br>[identifier](../Utility/Utility.md#identifier) ]     |             |
| NarrativeStyling  | anyOf      | [ [NarrativeStyling](./NarrativeStyling.md)<br>[identifier](../Utility/Utility.md#identifier) ]   |             |
| NarrativeWardrobe | anyOf      | [ [NarrativeWardrobe](./NarrativeWardrobe.md)<br>[identifier](../Utility/Utility.md#identifier) ] |             |
| SpecialAction     | anyOf      | [ [SpecialAction](./SpecialAction.md)<br>[identifier](../Utility/Utility.md#identifier) ]         |             |
#### related
| Property        | Constraint | Type                                                                                          | Description |
| --------------- | ---------- | --------------------------------------------------------------------------------------------- | ----------- |
| ProductionScene | anyOf      | [ [ProductionScene](./ProductionScene.md)<br>[identifier](../Utility/Utility.md#identifier) ] |             |

#### represents
| Property       | Constraint | Type                                                                                        | Description |
| -------------- | ---------- | ------------------------------------------------------------------------------------------- | ----------- |
| NarrativeScene | anyOf      | [ [NarrativeScene](./NarrativeScene.md)<br>[identifier](../Utility/Utility.md#identifier) ] |             |

#### representedBy
| Property        | Constraint | Type                                                                                          | Description |
| --------------- | ---------- | --------------------------------------------------------------------------------------------- | ----------- |
| Asset           | anyOf      | [ [Asset](../Asset/Asset.md)<br>[identifier](../Utility/Utility.md#identifier) ]              |             |
| ProductionScene | anyOf      | [ [ProductionScene](./ProductionScene.md)<br>[identifier](../Utility/Utility.md#identifier) ] |             |

#### usedIn
| Property           | Constraint | Type                                                                                                | Description |
| ------------------ | ---------- | --------------------------------------------------------------------------------------------------- | ----------- |
| ProductionLocation | anyOf      | [ [ProductionLocation](./ProductionLocation.md)<br>[identifier](../Utility/Utility.md#identifier) ] |             |
| ProductionScene    | anyOf      | [ [ProductionScene](./ProductionScene.md)<br>[identifier](../Utility/Utility.md#identifier) ]       |             |

#### uses
| Property           | Constraint | Type                                                                                                        | Description |
| ------------------ | ---------- | ----------------------------------------------------------------------------------------------------------- | ----------- |
| Asset              | anyOf      | [ [Asset](../Asset/Asset.md)<br>[identifier](../Utility/Utility.md#identifier) ]                            |             |
| Depiction          | anyOf      | [ [Depiction](./Depiction.md)<br>[identifier](../Utility/Utility.md#identifier) ]                           |             |
| Infrastructure     | anyOf      | [ [Infrastructure](../Infrastructure/Infrastructure.md)<br>[identifier](../Utility/Utility.md#identifier) ] |             |
| ProductionLocation | anyOf      | [ [ProductionLocation](./ProductionLocation.md)<br>[identifier](../Utility/Utility.md#identifier) ]         |             |
#### shootDay
Details about the shoot day and date.

| Property  | Constraint | Type                               | Description                                     |
| --------- | ---------- | ---------------------------------- | ----------------------------------------------- |
| shootDay  |            | string<br>number<br>null           | The number of the day on the shooting schedule. |
| shootDate |            | [date](../Utility/Utility.md#date) | The date of the shootDay                        |

### Controlled Values

#### contextType
| Value | Description |
|-------|-------------|
| concept | An exploratory representation of something from the narrative. |
| narrative | Informs scope for realizing the creative intent and aligns individual creative decisions within a Creative Work. |
| production | A real place that is used to depict the Narrative Location or used for creating the production. |
| shootDay | The number of the day on the shooting schedule. |
## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "Context",
  "contextType": "narrative",
  "contextCategory": "character.sven",
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "cxt/377RXIREHUj5MPzsl-Sba"  
    }  
  ],  
  "featuresIn": {  
    "NarrativeScene": [  
      {  
        "identifier": [  
          {  
            "identifierScope": "labkoat",  
            "identifierValue": "nscn/wz_MHOLYI3VwYx_0AX47Y"  
          }  
        ]  
      },  
      {  
        "identifier": [  
          {  
            "identifierScope": "labkoat",  
            "identifierValue": "nscn/zH9BzX8cjf-wY6N-HE6fg"  
          }  
        ]  
      }  
    ]  
  },  
  "needs": {  
    "NarrativeObject": [  
      {  
        "identifier": [  
          {  
            "identifierScope": "labkoat",  
            "identifierValue": "nprp/ozmg19-jNdhIlO1HwVP5G"  
          }  
        ]  
      },   
      {  
        "identifier": [  
          {  
            "identifierScope": "labkoat",  
            "identifierValue": "nprp/R7wfwv6cSPc6d1t1_glgJ"  
          }  
        ]  
      }  
    ],  
    "NarrativeWardrobe": null,  
    "SpecialAction": null  
  },  
  "has": {  
    "Asset": [  
      {  
        "identifier": [  
          {  
            "identifierScope": "labkoat",  
            "identifierValue": "asgp/6ijmAYmCMY86OQtX4cZ_y"  
          }  
        ]  
      }  
    ]  
  }  
}
```
