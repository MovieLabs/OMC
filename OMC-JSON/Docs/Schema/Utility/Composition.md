A set of Assets or other Compositions that can be combined to produce a new Asset.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property              | Constraint        | Type                                                                                                            | Description                                                                                                                              |
| --------------------- | ----------------- | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| entityType            | const<br>required | `"Depiction"`                                                                                                   | Declares the entity type.                                                                                                                |
| version               |                   |                                                                                                                 |                                                                                                                                          |
| provenance            |                   | [provenance](../Utility/Utility.md#provenance)                                                                  | A record of when something was changed and by whom.                                                                                      |
| compositionType       | enum              | [compositionType](#compositionType)                                                                             | The specific type of composition                                                                                                         |
| compositionProperties |                   | [compositionProperties](#compositionProperties)                                                                 | Properties specific to this composition                                                                                                  |
| Asset                 | anyOf             | [&nbsp[Asset](../Asset/Asset.md)<br>[identifier](../Utility/Utility.md#identifier)&nbsp]                        | A set of Assets that are included in this Composition.                                                                                   |
| AssetSC               | anyOf             | [&nbsp[AssetSC](../Asset/AssetSC.md)<br>[identifier](../Utility/Utility.md#identifier)&nbsp]                    | A set of Asset Structural Characteristics that are included in this Composition.                                                         |
| Composition           | anyOf             | [&nbsp[Composition](./Composition.md)<br>[identifier](../Utility/Utility.md#identifier)&nbsp]                   | The set of Compositions that are included in this Composition.                                                                           |
| StartHere             | anyOf             | [Asset](../Asset/Asset.md)<br>[AssetSC](../Asset/AssetSC.md)<br>[identifier](../Utility/Utility.md#identifier)  | Start point for assembling the Composition, the Asset that contains the instructions for the Composition.                                |
| Depiction             | anyOf             | [&nbsp[Depiction](../MediaCreationContext/Depiction.md)<br>[identifier](../Utility/Utility.md#identifier)&nbsp] | The representation of something from a narrative entity by a production entity in the Creative Work, specified or implied by the Script. |
| Context               | anyOf             | [ [Context](../MediaCreationContext/Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]            | Informs scope within the construction process of a Creative Work.                                                                        |
### Controlled & Enumerated Values

#### compositionType

| Value              | Description                                                                       |
| ------------------ | --------------------------------------------------------------------------------- |
| cgAssembly         | A Composition that includes a collection of related CG Assets and CG Assemblies.  |
| compositeMaterial  | A Material represented by a Composition.                                          |
| geometryAssembly   | A composition only containing geometry information.                               |
| sequence           | An ordered collection of media used to organize units of work.                    |
| sequence.animation | A unit of work made up of an ordered series of Animation shots.                   |
| sequence.color     | A sequence of shots with color grading characteristics linked to creative intent. |
| sequence.editorial | A sequence of shots linked to creative intent.                                    |
| sequence.vfx       | A unit of work made up of an ordered series of VFX shots.                         |
| sequence.vfxImage  | An Image Sequence used in VFX work.                                               |
### Object Properties
#### compositionProperties

| Field Name            | Constraint | Type                                                        | Description                                                                                                           |
| --------------------- | ---------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| boundingBox           |            | [boundingBox](./Utility.md#boundingBox)                     | The minimum axis-aligned right rectangular prism in the local space of the Geometry that fully encloses the Geometry. |
| coordinateOrientation |            | [coordinateOrientation](./Utility.md#coordinateOrientation) | The direction and handedness of the axes used in the geometry.                                                        |
| levelOfDetail         |            | [levelOfDetail](./Utility.md#levelOfDetail)                 | Percentage of the screen that an object can reasonably take up.                                                       |
| purpose               |            | [purpose](./Utility.md#purpose)                             | A suggested or intended use for the object in a pipeline.                                                             |
| scale                 |            | [scale](./Utility.md#scale)                                 | The number of “real” units represented by a single unit in the coordinate space of the Geometry.                      |


## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "Composition",  
  "identifier": [  
    {  
      "identifierScope": "cg-example",  
      "identifierValue": "cmp/DE14F3DF-D929-45C3-B151-4CDE7147D220"  
    }  
  ],  
  "name": "schoolRoomAllBricks",  
  "compositionType": "cgAssembly",  
  "compositionProperties": {  
    "purpose": "general",  
    "levelOfDetail": 50,  
    "scale": "1m"  
  },  
  "Asset": [],  
  "AssetSC": [],  
  "Composition": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "cg-example",  
          "identifierValue": "cmp/2CD37C79-D1F4-49A6-84D8-49350B167B0F"  
        }  
      ]  
    }  
  ],  
  "StartHere": {  
    "identifier": [  
      {  
        "identifierScope": "cg-example",  
        "identifierValue": "ast/23B9E4AA-2BEA-466C-A3BE-3FA9C5E46B64"  
      }  
    ]  
  }  
}
```