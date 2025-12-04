# Composition
A set of Assets or other Compositions that can be combined to produce a new Asset.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property              | Constraint        | Type                                                                                                           | Description                                                                                               |
| --------------------- | ----------------- | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| entityType            | const<br>required | `"Depiction"`                                                                                                  | Declares the entity type.                                                                                 |
| version               |                   | [version](#version)                                                                                            | A particular form, variant, or representation of an Asset that differs in some way from its source Asset. |
| provenance            |                   | [provenance](../Utility/Utility.md#provenance)                                                                 | A record of when something was changed and by whom.                                                       |
| compositionType       | enum              | [compositionType](#compositionType)                                                                            | The specific type of composition.                                                                         |
| compositionProperties |                   | [compositionProperties](#compositionProperties)                                                                | Properties specific to this composition.                                                                  |
| includes              |                   | [includes](#includes)                                                                                          | The Assets, AssetSC's and Compositions that make up this Composition                                      |
| StartHere             | oneOf             | [Asset](../Asset/Asset.md)<br>[AssetSC](../Asset/AssetSC.md)<br>[identifier](../Utility/Utility.md#identifier) | Start point for assembling the Composition, the Asset that contains the instructions for the Composition. |
| Context               | anyOf             | [ [Context](../MediaCreationContext/Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]           | Informs scope within the construction process of a Creative Work.                                         |
### Object Properties

#### version
Includes properties from: [baseVersion](../core/baseVersion.md)

| Property     | Constraint | Type                                                                                   | Description                                                                                                               |
| ------------ | ---------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| DerivationOf | oneOf      | [Composition](./Composition.md) <br>[identifier](../Utility/Utility.md#identifier)     | The Composition from which this one was Derived                                                                           |
| RevisionOf   | oneOf      | [Composition](./Composition.md) <br>[identifier](../Utility/Utility.md#identifier)     | The Composition of which this is a Revision of                                                                            |
| VariantOf    | oneOf      | [Composition](./Composition.md) <br>[identifier](../Utility/Utility.md#identifier)     | The Composition of which this is a Variant of                                                                             |
| Alternative  | anyOf      | [ [Composition](./Composition.md) <br>[identifier](../Utility/Utility.md#identifier) ] | A set of Compositions that are Alternatives to this one.                                                                  |
| Derivation   | anyOf      | [ [Composition](./Composition.md) <br>[identifier](../Utility/Utility.md#identifier) ] | A set of Compositions that are Derived from this one.                                                                     |
| Revision     | anyOf      | [ [Composition](./Composition.md) <br>[identifier](../Utility/Utility.md#identifier) ] | A set of Compositions that are Revisions of this one.                                                                     |
| Variant      | anyOf      | [ [Composition](./Composition.md) <br>[identifier](../Utility/Utility.md#identifier) ] | A set of Compositions that are Variants of this one.                                                                      |
| customData   |            | [customData](../Utility/Utility.md#customData)                                         | A user defined set of custom data in the payload of the instance, used where the formal schema lacks required properties. |
#### compositionProperties

| Field Name            | Constraint | Type                                                        | Description                                                                                                           |
| --------------------- | ---------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| audioContent          |            | [ [audioContent](../Utility/Utility.md#audioContent) ]      | Classification of the content type in a particular Audio Asset.                                                       |
| boundingBox           |            | [boundingBox](./Utility.md#boundingBox)                     | The minimum axis-aligned right rectangular prism in the local space of the Geometry that fully encloses the Geometry. |
| coordinateOrientation |            | [coordinateOrientation](./Utility.md#coordinateOrientation) | The direction and handedness of the axes used in the geometry.                                                        |
| levelOfDetail         |            | [levelOfDetail](./Utility.md#levelOfDetail)                 | Percentage of the screen that an object can reasonably take up.                                                       |
| materialType          | ctrlValue  | [materialType](../Utility/Utility.md#materialType)          | A categorization of what the material is intended to simulate.                                                        |
| purpose               |            | [purpose](./Utility.md#purpose)                             | A suggested or intended use for the object in a pipeline.                                                             |
| scale                 |            | [scale](./Utility.md#scale)                                 | The number of “real” units represented by a single unit in the coordinate space of the Geometry.                      |
| soundfield            |            | [soundfield](../Utility/Utility.md#soundfield)              | The acoustical space created by simultaneously reproducing one or more Audio Channels.                                |

#### includes

| Field Name  | Constraint | Type                                                                                          | Description                                                                      |
| ----------- | ---------- | --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Asset       | anyOf      | [&nbsp[Asset](../Asset/Asset.md)<br>[identifier](../Utility/Utility.md#identifier)&nbsp]      | A set of Assets that are included in this Composition.                           |
| AssetSC     | anyOf      | [&nbsp[AssetSC](../Asset/AssetSC.md)<br>[identifier](../Utility/Utility.md#identifier)&nbsp]  | A set of Asset Structural Characteristics that are included in this Composition. |
| Composition | anyOf      | [&nbsp[Composition](./Composition.md)<br>[identifier](../Utility/Utility.md#identifier)&nbsp] | The set of Compositions that are included in this Composition.                   |


### Controlled & Enumerated Values

#### compositionType
| Value                    | Description                                                                                                                                     |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| audio                    | A Composition consisting of audio assets, Audio Compositions, and an Audio Session.                                                             |
| audio.bed                | The sum of non-object STEMs.                                                                                                                    |
| audio.preMix             | A collection of sound samples that have been processed for technical or creative review.                                                        |
| audio.printmaster        | The combination of STEMs for a particular soundfield at unity gain.                                                                             |
| audio.soundEditorialUnit | A collection of sound samples that have been selected in reference to the Creative Work or a portion of it.                                     |
| audio.stem               | Final processed Audio Assets and Compositions combined based on their Audio Classification, representing the final sound for the Creative Work. |
| cgAssembly               | A Composition that includes a collection of related CG Assets and CG Assemblies.                                                                |
| compositeMaterial        | A Material represented by a Composition.                                                                                                        |
| geometryAssembly         | A composition only containing geometry information.                                                                                             |
| sequence                 | An ordered collection of media used to organize units of work.                                                                                  |
| sequence.animation       | A unit of work made up of an ordered series of Animation shots.                                                                                 |
| sequence.color           | A sequence of shots with color grading characteristics linked to creative intent.                                                               |
| sequence.editorial       | A sequence of shots linked to creative intent.                                                                                                  |
| sequence.vfx             | A unit of work made up of an ordered series of VFX shots.                                                                                       |
| sequence.vfxImage        | An Image Sequence used in VFX work.                                                                                                             |

