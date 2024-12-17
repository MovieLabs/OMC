# AssetSC
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
| DerivationOf     | oneOf      | [AssetSC](./AssetSC.md) <br>[identifier](../Utility/Utility.md#identifier)     | The AssetSC from which this one was Derived                                                                               |
| RepresentationOf | oneOf      | [AssetSC](./AssetSC.md) <br>[identifier](../Utility/Utility.md#identifier)     | The AssetSC which this AssetSC represents                                                                                 |
| RevisionOf       | oneOf      | [AssetSC](./AssetSC.md) <br>[identifier](../Utility/Utility.md#identifier)     | The AssetSC from which this one was Revised from                                                                          |
| Derivation       | anyOf      | [ [AssetSC](./AssetSC.md) <br>[identifier](../Utility/Utility.md#identifier) ] | A set of AssetSC's that are Derived from this one.                                                                        |
| Representation   | anyOf      | [ [AssetSC](./AssetSC.md) <br>[identifier](../Utility/Utility.md#identifier) ] | A set of AssetSC's that are Representations of this one.                                                                  |
| Revision         | anyOf      | [ [AssetSC](./AssetSC.md) <br>[identifier](../Utility/Utility.md#identifier) ] | A set of AssetSC's that are Revisions of this one.                                                                        |
| customData       |            | [customData](../Utility/Utility.md#customData)                                 | A user defined set of custom data in the payload of the instance, used where the formal schema lacks required properties. |

#### structuralProperties

| Property              | Constraint | Type                                                                 | Description                                                                                                           |
| --------------------- | ---------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| assetGroup            |            | [assetGroup](#assetGroup)                                            | Properties of the Asset Group.                                                                                        |
| audioBitRate          |            | integer, null                                                        | The number of bits in one second of sampled audio, expressed in Kbits per second.                                     |
| audioSampleRate       |            | integer, null                                                        | The average number of samples per second taken from the source audio input in KHz.                                    |
| audioSampleSize       |            | integer, null                                                        | The number of bits per audio sample.                                                                                  |
| codec                 |            | [codec](../Utility/Utility.md#codec)                                 | The specific codec used to encode the Asset.                                                                          |
| dimensions            |            | [dimensions](../Utility/Utility.md#dimensions)                       | Dimensions for an asset in a unit of measurement.                                                                     |
| boundingBox           |            | [boundingBox](../Utility/Utility.md#boundingBox)                     | The minimum axis-aligned right rectangular prism in the local space of the Geometry that fully encloses the Geometry. |
| coordinateOrientation |            | [coordinateOrientation](../Utility/Utility.md#coordinateOrientation) | The direction and handedness of the axes used in the geometry.                                                        |
| fileDetails           |            | [fileDetails](#fileDetails)                                          |                                                                                                                       |
| geometryType          | ctrlValue  | [geometryType](#geometryType)                                        | A description of the general underlying form of a three-dimensional shape.                                            |
| levelOfDetal          |            | [levelOfDetail](../Utility/Utility.md#levelOfDetail)                 | Percentage of the screen that an object can reasonably take up.                                                       |
| linkSet               |            | [linkSet](#linkSet)                                                  | Metadata used in resolving an identifier.                                                                             |
| materialType          | ctrlValue  | [materialType](../Utility/Utility.md#materialType)                   | A categorization of what the material is intended to simulate.                                                        |
| purpose               | ctrlValue  | [purpose](../Utility/Utility.md#purpose)                             | A suggested or intended use for the object in a pipeline.                                                             |
| scale                 |            | [scale](../Utility/Utility.md#scale)                                 | The number of “real” units represented by a single unit in the coordinate space of the Geometry.                      |

#### assetGroup
| Property  | Constraint | Type    | Description                                       |
| --------- | ---------- | ------- | ------------------------------------------------- |
| isOrdered |            | boolean | `true` if this should be treated as an ordered st |

#### fileDetails
| Property      | Constraint | Type         | Description                                                                                                       |
| ------------- | ---------- | ------------ | ----------------------------------------------------------------------------------------------------------------- |
| fileName      |            | string, null | A name that can be used for the file if stored to a file system.                                                  |
| filePath      |            | string, null | A directory path that can be used for the file if stored to a file system.                                        |
| fileExtension |            | string, null | A file extension, often 3-4 characters indicating the format of the file.                                         |
| mediaType     |            | string, null | A two-part identifier for file formats and content formats, often referred to as a MIME type and defined by IANA. |

#### linkSet
| Property   | Constraint | Type         | Description                                                                                                       |
| ---------- | ---------- | ------------ | ----------------------------------------------------------------------------------------------------------------- |
| recordType |            | string, null | A user generated categorization or description of the record.                                                     |
| mediaType  |            | string, null | A two-part identifier for file formats and content formats, often referred to as a MIME type and defined by IANA. |

### Controlled Values

#### structuralType
| Value                       | Description                                                                                           |
| --------------------------- | ----------------------------------------------------------------------------------------------------- |
| assetGroup                  | Signifies this Asset represents and Asset Group.                                                      |
| digital                     | Information that exists as digital data.                                                              |
| digital.audio               | A representation of sound.                                                                            |
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
| physical.audioVisual        | A Moving Image with Audio synchronized to the images.                                                 |
| physical.document           | A human readable object containing text and/or images.                                                |
| physical.image              | A two-dimensional visual representation.                                                              |
| physical.imageSequence      | A temporally ordered sequence of individual images which are the constituent parts of a Moving Image. |
| physical.movingImage        | A temporally ordered sequence of Images                                                               |
| physical.structuredDocument | A Document structured according to a set of rules which are used to parse or understand the document. |
#### geometryType
A description of the general underlying form of a three-dimensional shape.

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