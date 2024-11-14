# Asset
A physical or digital object or collection of objects specific to the creation of the Creative Work.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property   | Constraint        | Type                                                                                                     | Description                                                                                               |
| ---------- | ----------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| entityType | const<br>required | `"Asset"`                                                                                                | Declares the entity type.                                                                                 |
| version    |                   | [version](#version)                                                                                      | A particular form, variant, or representation of an Asset that differs in some way from its source Asset. |
| provenance |                   | [provenance](../Utility/Utility.md#provenance)                                                           | A record of when something was changed and by whom.                                                       |
| AssetSC    |                   |                                                                                                          | Describes the form of an Asset along with the attributes specific to that asset’s form.                   |
| assetFC    |                   | [assetFC](#assetFC)                                                                                      | Describes the use or purpose of an Asset within the production process                                    |
| Asset      | anyOf             | [ [Asset](./Asset.md) <br>[identifier](../Utility/Utility.md#identifier) ]                               | The set of Assets that make up an an asset group.                                                         |
| Context    | anyOf             | [ [Context](../MediaCreationContext/Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]     | Informs scope within the construction process of a Creative Work.                                         |
| Depiction  | anyOf             | [ [Depiction](../MediaCreationContext/Depiction.md) <br>[identifier](../Utility/Utility.md#identifier) ] | The set of entities this Asset depicts.                                                                   |

### Object Properties

#### version
Includes properties from: [baseVersion](../core/baseVersion.md)

| Property     | Constraint | Type                                                                       | Description                                                                                                               |
| ------------ | ---------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| DerivationOf | oneOf      | [Asset](./Asset.md) <br>[identifier](../Utility/Utility.md#identifier)     | The Asset from which this one was Derived                                                                                 |
| RevisionOf   | oneOf      | [Asset](./Asset.md) <br>[identifier](../Utility/Utility.md#identifier)     | The Asset of which this is a Revision of                                                                                  |
| VariantOf    | oneOf      | [Asset](./Asset.md) <br>[identifier](../Utility/Utility.md#identifier)     | The Asset of which this is a Variant of                                                                                   |
| Alternative  | anyOf      | [ [Asset](./Asset.md) <br>[identifier](../Utility/Utility.md#identifier) ] | A set of Assets that are Alternatives to this one.                                                                        |
| Derivation   | anyOf      | [ [Asset](./Asset.md) <br>[identifier](../Utility/Utility.md#identifier) ] | A set of Assets that are Derived from this one.                                                                           |
| Revision     | anyOf      | [ [Asset](./Asset.md) <br>[identifier](../Utility/Utility.md#identifier) ] | A set of Assets that are Revisions of this one.                                                                           |
| Variant      | anyOf      | [ [Asset](./Asset.md) <br>[identifier](../Utility/Utility.md#identifier) ] | A set of Assets that are Variants of this one.                                                                            |
| customData   |            | [customData](../Utility/Utility.md#customData)                             | A user defined set of custom data in the payload of the instance, used where the formal schema lacks required properties. |
#### assetFC
Describes the use or purpose of an Asset within the production process

| Property             | Constraint | Type                                                                                                                                                                                                                      | Description |
| -------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| functionalType       | ctrlValue  | string, number, null                                                                                                                                                                                                      |             |
| functionalProperties |            | [mapFormat](#mapFormat)<br>[mapType](#mapType)<br>[cameraMetadata](#cameraMetadata)<br>[lensMetadata](#lensMetadata)<br>[recorderMetadata](#recorderMetadata)<br>[isSelfContained](#isSelfContained)<br>[timing](#timing) |             |
| customData           |            |                                                                                                                                                                                                                           |             |
|                      |            |                                                                                                                                                                                                                           |             |
#### cameraMetadata
Capture-specific details and information about the Camera itself.

| Property                       | Constraint | Type         | Description                                                                                                                               |
| ------------------------------ | ---------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| activeSensorPhysicalDimensions |            | string, null | Height and width of the active area of the camera sensor                                                                                  |
| cameraLabel                    |            | string, null | Human readable ID assigned to each production camera.                                                                                     |
| cameraMake                     |            | string, null | The manufacturer or vendor of the camer                                                                                                   |
| cameraModel                    |            | string, null | The manufacturer's name for the camera model. For example, the name of the camera family followed by the name of the variant.             |
| cameraSerialNumber             |            | string, null | An alphanumeric code assigned by the manufacturer to a camera.                                                                            |
| cameraUID                      |            | string, null | An alphanumeric code that uniquely identifies the camera among all cameras from all vendors.                                              |
| captureRate                    |            | string, null | The number of individual images captured per second.                                                                                      |
| circleTake                     |            | string, null | Indicating whether a recorded sequence of images is considered a candidate for use.                                                       |
| exposureIndex                  |            | string, null | Exposure index is the ISO rating used to determine exposure when the recording was made.                                                  |
| fdlLink                        |            | string, null | Unique identifier of the FDL used by the camera                                                                                           |
| flipX                          |            | string, null | The flip-X factor indicates whether the image is flipped horizontally.                                                                    |
| flipY                          |            | string, null | The flip-Y factor indicates whether the image is flipped vertically.                                                                      |
| frameHeight                    |            | string, null | The height of the intended image in pixels. This may or may not be the height of the recorded image or the sensor                         |
| frameWidth                     |            | string, null | The width of the intended image in pixels. This may or may not be the width of the recorded image or the sensor                           |
| isoSpeed                       |            | string, null | Arithmetic ISO scale as defined in ISO 12232                                                                                              |
| lutUID                         |            | string, null | An alphanumeric code that uniquely identifies the LUT loaded into the camera and applied to the monitor output during shooting.           |
| pixelAspectRatio               |            | string, null | Describes how the pixels are to be interpreted to correctly display the image.                                                            |
| playbackRate                   |            | string, null | The number of individual images per second of the intended playback speed.                                                                |
| roll                           |            | string, null | The angle of the camera off of the roll axis, measured in degrees when the camera is level.                                               |
| shutterAngle                   |            | string, null | A measure of the exposure time of an image relative to the frame rate. 0 < shutter angle <= 360.                                          |
| tilt                           |            | string, null | The angle of a camera off its pitch axis, measured in degrees when the camera is level.                                                   |
| timecode                       |            | string, null | A linear sequence of numeric codes generated at a regular interview and usually recorded in the format: <hour>:<minute>:<second>:<frame>. |
| timecodeEnd                    |            | string, null | Timecode when recording stopped                                                                                                           |
| timecodeStart                  |            | string, null | Timecode when recording stopped                                                                                                           |
| tint                           |            | string, null | Defines the R/B white points against the green channel.                                                                                   |
| whiteBalance                   |            | string, null | The color temperature of white expressed in degrees Kelvin.                                                                               |

#### lensMetadata
Capture-specific details and information about the Lens itself.

| Property              | Constraint | Type         | Description                                                                                                                           |
| --------------------- | ---------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| tStop                 |            | string, null | The linear T-number of the lens, equal to the f-number of the lens divided by the square root of the transmittance of the lens.       |
| fStop                 |            | string, null | The linear f-number of the lens, equal to the focal length divided by the diameter of the entrance pupil.                             |
| entrancePupilPosition |            | string, null |                                                                                                                                       |
| focusPosition         |            | string, null | Focus distance/position of the lens.                                                                                                  |
| focalLength           |            | string, null | The actual focal length of the lens, in millimeters, when the image was captured. With a zoom lens this may be change frame by frame. |
| lensMake              |            | string, null | The lens manufacturer or vendor.                                                                                                      |
| lensModel             |            | string, null | The lens model identifier assigned by the lens manufacturer or vendor.                                                                |
| anamorphicSqueeze     |            | string, null | Nominal ratio of height to width of the image of an axis-aligned square captured by the camera sensor.                                |
| lensSerialNumber      |            | string, null | A number unique to each lens from the same manufacturer or vendor and of the same model.                                              |
| lensFirmwareVersion   |            | string, null | Version identifier for the firmware of the lens.                                                                                      |

#### recorderMetadata
Information about a Recorder and the recording media.

| Property                | Constraint | Type         | Description                                                                                                 |
| ----------------------- | ---------- | ------------ | ----------------------------------------------------------------------------------------------------------- |
| recorderFirmwareVersion |            | string, null | An alphanumeric code that identifies the firmware installed in the recorder at the time of recording.       |
| recorderMake            |            | string, null | The recorder manufacturer or vendor.                                                                        |
| recorderModel           |            | string, null | The recorder model identifier assigned by the lens manufacturer or vendor.                                  |
| recorderSerialNumber    |            | string, null | A number unique to each recorder from the same manufacturer or vendor and of the same model.                |
| storageMediaUID         |            | string, null | An alphanumeric code that uniquely identifies the storage media (i.e., mag) the footage was recorded on to. |
#### isSelfContained

| Property | Constraint | Type    | Description                                                                        |
| -------- | ---------- | ------- | ---------------------------------------------------------------------------------- |
|          |            | boolean | Indicates the Asset does not depend on other Assets to perform its functional use. |
#### timing

| Property    | Constraint | Type         | Description |
| ----------- | ---------- | ------------ | ----------- |
| sourceStart |            | string, null |             |
| sourceEnd   |            | string, null |             |
| recordStart |            | string, null |             |
| recordEnd   |            | string, null |             |
| duration    |            | string, null |             |


### Controlled Values

#### functionalType

| Value                                    | Description                                                                                                                                                                                   |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| artwork                                  | N/A                                                                                                                                                                                           |
| artwork.animatedStoryboard               | A moving image produced from the individual images of a Storyboard.                                                                                                                           |
| artwork.conceptArt                       | Images that illustrate ideas for potential depictions of elements of the creative intent.                                                                                                     |
| artwork.storyboard                       | A series of images that forms a visual representation of some part of the narrative.                                                                                                          |
| audio                                    | A representation of sound.                                                                                                                                                                    |
| audio.channel                            | N/A                                                                                                                                                                                           |
| audio.onSetMix                           | N/A                                                                                                                                                                                           |
| audio.track                              | N/A                                                                                                                                                                                           |
| cameraMetadata                           | Capture-specific details and information about the Camera itself.                                                                                                                             |
| capture                                  | The result of recording an event by any means                                                                                                                                                 |
| capture.audio                            | A representation of sound.                                                                                                                                                                    |
| capture.audio.wild                       | N/A                                                                                                                                                                                           |
| capture.calibration                      | N/A                                                                                                                                                                                           |
| capture.cameraProxy                      | N/A                                                                                                                                                                                           |
| capture.faceCamera                       | N/A                                                                                                                                                                                           |
| capture.lidar                            | N/A                                                                                                                                                                                           |
| capture.motionCapture                    | The recording of motion as a stream of digital data.                                                                                                                                          |
| capture.ocf                              | N/A                                                                                                                                                                                           |
| capture.roll                             | Identifier for a group of events captured together on the same camera and recording media.                                                                                                    |
| capture.witnessCamera                    | N/A                                                                                                                                                                                           |
| cgModel                                  | N/A                                                                                                                                                                                           |
| color                                    | N/A                                                                                                                                                                                           |
| color.cdl                                | N/A                                                                                                                                                                                           |
| color.colorSpace                         | A predefined encoding for communicating color appearance.                                                                                                                                     |
| color.lut                                | Look up table                                                                                                                                                                                 |
| configuration                            | N/A                                                                                                                                                                                           |
| configuration.colorSpace                 | A configuration file for a color management system.                                                                                                                                           |
| creativeReferenceMaterial                | Images or other material used to inform the creation of a production element, to help convey a tone or look, etc.                                                                             |
| lensMetadata                             | Capture-specific details and information about the Lens itself.                                                                                                                               |
| map                                      | An image intended to drive or influence a behavior or value within a CG workflow.                                                                                                             |
| material                                 | Data values and relationships required to describe the look of a CG Asset.                                                                                                                    |
| productionCharacter                      | N/A                                                                                                                                                                                           |
| productionProp                           | A Depiction of the Narrative Prop.                                                                                                                                                            |
| productionProp.productionGreenery        | An Asset or Assets used to depict Narrative greenery in a Production Scene.                                                                                                                   |
| productionProp.productionVehicle         | An Asset used in the Depiction of a Narrative Vehicle                                                                                                                                         |
| productionSetDressing                    | Assets used in the depiction of Narrative Set Dressing.                                                                                                                                       |
| productionSetDressing.productionGreenery | An Asset or Assets used to depict Narrative greenery in a Production Scene.                                                                                                                   |
| productionSetDressing.productionVehicle  | An Asset used in the Depiction of a Narrative Vehicle                                                                                                                                         |
| proxy                                    | N/A                                                                                                                                                                                           |
| proxy.daily                              | N/A                                                                                                                                                                                           |
| proxy.editorial                          | N/A                                                                                                                                                                                           |
| recorderMetadata                         | Information about a Recorder and the recording media.                                                                                                                                         |
| script                                   | A Structured Document written as a blueprint to convey the creative intent for the Creative Work. Parsing the Script generates a guide to those things that are to be depicted in production. |
| sequenceChronologyDescriptor             | Describes how a series of Shots is used to generate a Sequence.                                                                                                                               |
| shot                                     | A discrete unit of visual narrative with a specified beginning and end.                                                                                                                       |
| shot.animation                           | A Shot that has been identified as requiring Animation work.                                                                                                                                  |
| shot.editorial                           | N/A                                                                                                                                                                                           |
| shot.vfx                                 | A Shot that has been identified as requiring VFX work.                                                                                                                                        |
| technicalReferenceMaterial               | Images and other material used to inform the execution of the production.                                                                                                                     |
#### mapFormat
| Value               | Description |
| ------------------- | ----------- |
| cubeFaceEnvironment | N/A         |
| cubeFaceShadow      | N/A         |
| latLongEnvironment  | N/A         |
| plainTexture        | N/A         |
| shadow              | N/A         |
| volumeShadow        | N/A         |
| volumeTexture       | N/A         |
#### mapType
| Value            | Description |
| ---------------- | ----------- |
| albedo           | N/A         |
| ambientOcclusion | N/A         |
| bump             | N/A         |
| depthMap         | N/A         |
| diffuse          | N/A         |
| heightMap        | N/A         |
| metalness        | N/A         |
| normal           | N/A         |
| opacity          | N/A         |
| projectionMap    | N/A         |
| roughness        | N/A         |
| specular         | N/A         |
| uvMap            | N/A         |
| weightMap        | N/A         |

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