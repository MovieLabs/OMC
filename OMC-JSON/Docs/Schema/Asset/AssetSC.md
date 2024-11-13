Describes the form of an Asset along with the attributes specific to that asset's form.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property             | Constraint        | Type                                           | Description                                                                        |
| -------------------- | ----------------- | ---------------------------------------------- | ---------------------------------------------------------------------------------- |
| entityType           | const<br>required | `"AssetSC"`                                    | Declares the entity type.                                                          |
| version              |                   | [version](#version)                            |                                                                                    |
| provenance           |                   | [provenance](../Utility/Utility.md#provenance) | A record of when something was changed and by whom.                                |
| structuralType       | ctrlValue         | [structuralType](#structuralType)              | A canonical description of this assets form.                                       |
| structuralProperties |                   | [structuralProperties](#structuralProperties)  | A set of properties that describe the structural characteristics.                  |
| isAnalog             |                   | boolean                                        | True if the Asset is an Analog Asset.                                              |
| Carrier              |                   | [Carrier](../Infrastructure/Infrastructure.md) | For describing the physical storage device on which the digital essence is stored. |

### Object Properties

#### version
Includes properties from: [baseVersion](../core/baseVersion.md)

| Property         | Constraint | Type                                                                           | Description                                                                                                               |
| ---------------- | ---------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| DerivationOf     | oneOf      | [AssetSC](./AssetSC.md) <br>[identifier](../Utility/Utility.md#identifier)     | Describes the form of an Asset along with the attributes specific to that asset's form.                                   |
| RepresentationOf | oneOf      | [AssetSC](./AssetSC.md) <br>[identifier](../Utility/Utility.md#identifier)     | Describes the form of an Asset along with the attributes specific to that asset's form.                                   |
| RevisionOf       | oneOf      | [AssetSC](./AssetSC.md) <br>[identifier](../Utility/Utility.md#identifier)     | Describes the form of an Asset along with the attributes specific to that asset's form.                                   |
| Derivation       | anyOf      | [ [AssetSC](./AssetSC.md) <br>[identifier](../Utility/Utility.md#identifier) ] | Describes the form of an Asset along with the attributes specific to that asset's form.                                   |
| Representation   | anyOf      | [ [AssetSC](./AssetSC.md) <br>[identifier](../Utility/Utility.md#identifier) ] | Describes the form of an Asset along with the attributes specific to that asset's form.                                   |
| Revision         | anyOf      | [ [AssetSC](./AssetSC.md) <br>[identifier](../Utility/Utility.md#identifier) ] | Describes the form of an Asset along with the attributes specific to that asset's form.                                   |
| customData       |            | [customData](../Utility/Utility.md#customData)                                 | A user defined set of custom data in the payload of the instance, used where the formal schema lacks required properties. |

#### structuralProperties

| Property              | Constraint | Type                                                                 | Description |
| --------------------- | ---------- | -------------------------------------------------------------------- | ----------- |
| boundingBox           |            | [boundingBox](../Utility/Utility.md#boundingBox)                     |             |
| coordinateOrientation |            | [coordinateOrientation](../Utility/Utility.md#coordinateOrientation) |             |
| fileDetails           |            | [fileDetails](#fileDetails)                                          |             |
| geometryType          | ctrlValue  | [geometryType](#geometryType)                                        |             |
| levelOfDetal          |            | [levelOfDetail](../Utility/Utility.md#levelOfDetail)                 |             |
| linkSet               |            | [linkSet](#linkSet)                                                  |             |
| materialType          |            | [materialType](../Utility/Utility.md#materialType)                   |             |
| purpose               |            | [purpose](../Utility/Utility.md#purpose)                             |             |
| scale                 |            | [scale](../Utility/Utility.md#scale)                                 |             |

#### fileDetails
| Property      | Constraint | Type         | Description |
| ------------- | ---------- | ------------ | ----------- |
| fileName      |            | string, null |             |
| filePath      |            | string, null |             |
| fileExtension |            | string, null |             |
| mediaType     |            | string, null |             |

#### linkSet
| Property   | Constraint | Type         | Description |
| ---------- | ---------- | ------------ | ----------- |
| recordType |            | string, null |             |
| mediaType  |            | string, null |             |


### Controlled Values

#### structuralType
| Value                       | Description                                                                                           |
| --------------------------- | ----------------------------------------------------------------------------------------------------- |
| digital                     | Information that exists as digital data.                                                              |
| digital.audio               | A representation of sound.                                                                            |
| digital.audio.wild          | N/A                                                                                                   |
| digital.audioVisual         | A Moving Image with Audio synchronized to the images.                                                 |
| digital.data                | An Asset composed of digital data.                                                                    |
| digital.document            | A human readable object containing text and/or images.                                                |
| digital.image               | A two-dimensional visual representation.                                                              |
| digital.imageSequence       | A temporally ordered sequence of individual images which are the constituent parts of a Moving Image. |
| digital.movingImage         | A temporally ordered sequence of Images                                                               |
| digital.procedural          | An Asset that produces data that does not persist outside of its immediate use.                       |
| digital.structuredDocument  | A Document structured according to a set of rules which are used to parse or understand the document. |
| geometry                    | A shape defined in three dimensions.                                                                  |
| physical                    | A physical asset is one where the tangible reality of the Asset is its defining feature.              |
| physical.audio              | A representation of sound.                                                                            |
| physical.audio.wild         | N/A                                                                                                   |
| physical.audioVisual        | A Moving Image with Audio synchronized to the images.                                                 |
| physical.document           | A human readable object containing text and/or images.                                                |
| physical.image              | A two-dimensional visual representation.                                                              |
| physical.imageSequence      | A temporally ordered sequence of individual images which are the constituent parts of a Moving Image. |
| physical.movingImage        | A temporally ordered sequence of Images                                                               |
| physical.structuredDocument | A Document structured according to a set of rules which are used to parse or understand the document. |
#### geometryType

| Value        | Description |
| ------------ | ----------- |
| basisCurve   | N/A         |
| capsule      | N/A         |
| cone         | N/A         |
| cube         | N/A         |
| cylinder     | N/A         |
| mesh         | N/A         |
| nurbsCurve   | N/A         |
| nurbsSurface | N/A         |
| plane        | N/A         |
| teapot       | N/A         |
| torus        | N/A         |


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