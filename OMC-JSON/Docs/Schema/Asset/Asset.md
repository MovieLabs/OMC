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

| Property             | Constraint | Type                                           | Description                                                                                                               |
| -------------------- | ---------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| functionalType       | ctrlValue  | [functionalType](#functionalType)              | Describes the use or purpose of an Asset within the production process                                                    |
| functionalProperties |            | [functionalProperties](#functionalProperties)  | Properties that future describe an Asset function and use within the production process.                                  |
| customData           |            | [customData](../Utility/Utility.md#customData) | A user defined set of custom data in the payload of the instance, used where the formal schema lacks required properties. |

### functionalProperties
| Property              | Constraint | Type                                                   | Description                                                                            |
| --------------------- | ---------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| audioChannelName      | ctrlValue  | [ [audioChannelName](#audioChannelName) ]              | A formalization of the name of the loudspeaker the Audio Channel in intended to drive. |
| audioContent          |            | [ [audioContent](../Utility/Utility.md#audioContent) ] | Classification of the content type in a particular Audio Asset.                        |
| audioMixType          | ctrlValue  | [audioMixType](#audioMixType)                          | A description of the type or use for this mix.                                         |
| audioProcessingAction |            | string, null                                           | Indication of what was done to the audio in an Audio Session.                          |
| audioTrackName        |            | string, null                                           | Further differentiation for the Audio Track.                                           |
| mapFormat             | ctrlValue  | [mapFormat](#mapFormat)                                | The data layout of a Map                                                               |
| mapType               | ctrlValue  | [mapType](#mapType)                                    | Guidance about the intended use of a Map in a Material.                                |
| cameraMetadata        |            | [cameraMetadata](#cameraMetadata)                      | Capture-specific details and information about the Camera itself.                      |
| lensMetadata          |            | [lensMetadata](#lensMetadata)                          | Capture-specific details and information about the Lens itself.                        |
| recorderMetadata      |            | [recorderMetadata](#recorderMetadata)                  | Information about a Recorder and the recording media.                                  |
| isSelfContained       |            | [isSelfContained](#isSelfContained)                    | An Asset that does not depend on any other assets for a particular functional use.     |
| soundfield            | ctrlValue  | [soundfield](../Utility/Utility.md#soundfield)         | The acoustical space created by simultaneously reproducing one or more Audio Channels. |
| timing                |            | [timing](#timing)                                      | Timing data for a shot, indicating which frames of the shot are to be used.            |

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
An Asset that does not depend on any other assets for a particular functional use.

| Constraint | Type    | Description                                                                        |
| ---------- | ------- | ---------------------------------------------------------------------------------- |
|            | boolean | Indicates the Asset does not depend on other Assets to perform its functional use. |
#### timing
Timing data for a shot, indicating which frames of the shot are to be used.

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
| artwork                                  | Illustrations, photographs, or other materials that illustrate some aspect of a Creative Work.                                                                                                |
| artwork.animatedStoryboard               | A moving image produced from the individual images of a Storyboard.                                                                                                                           |
| artwork.conceptArt                       | Images that illustrate ideas for potential depictions of elements of the creative intent.                                                                                                     |
| artwork.storyboard                       | A series of images that forms a visual representation of some part of the narrative.                                                                                                          |
| audio                                    | A representation of sound.                                                                                                                                                                    |
| audio.channel                            | A distinct collection of sequenced audio samples that are intended for delivery to a single loudspeaker or other reproduction device.                                                         |
| audio.mix                                | A combination of multiple Audio Assets and Compositions into a particular format.                                                                                                             |
| audio.object                             | A segment of audio essence with associated metadata describing positional and other properties which may vary with time.                                                                      |
| audio.objectMetadata                     | A file containing metadata about the audio object.                                                                                                                                            |
| audio.track                              | A temporally continuous sequence of related samples.                                                                                                                                          |
| audioSession                             | An Asset that represents the state of the audio mixing and editing process.                                                                                                                   |
| cameraMetadata                           | Capture-specific details and information about the Camera itself.                                                                                                                             |
| capture                                  | The result of recording an event by any means                                                                                                                                                 |
| capture.calibration                      | Captured calibration data from a device.                                                                                                                                                      |
| capture.cameraProxy                      | A proxy directly generated by the camera.                                                                                                                                                     |
| capture.faceCamera                       | A capture of an actor's face, often used for motion capture.                                                                                                                                  |
| capture.lidar                            | Light Detecting and Ranging, a capture from a specialized scanning device that creates a point cloud.                                                                                         |
| capture.motionCapture                    | The recording of motion as a stream of digital data.                                                                                                                                          |
| capture.ocf                              | Original Captured Footage, A moving image captured from a camera.                                                                                                                             |
| capture.roll                             | Identifier for a group of events captured together on the same camera and recording media.                                                                                                    |
| capture.witnessCamera                    | A video capture not intended for the creative work, but as a record of related action, typically on-set.                                                                                      |
| cgModel                                  | A generic use for Geometry.                                                                                                                                                                   |
| color                                    | Asset containing information about color.                                                                                                                                                     |
| color.cdl                                | Color Decision List, describes suggested correct color for each shot.                                                                                                                         |
| color.colorSpace                         | A predefined encoding for communicating color appearance.                                                                                                                                     |
| color.lut                                | Look up table                                                                                                                                                                                 |
| configuration                            | Asset that contains information about the configuration of components of the workflow.                                                                                                        |
| configuration.colorSpace                 | A configuration file for a color management system.                                                                                                                                           |
| costume                                  | An Asset used to depict the Narrative Wardrobe of a Character.                                                                                                                                |
| creativeReferenceMaterial                | Images or other material used to inform the creation of a production element, to help convey a tone or look, etc.                                                                             |
| lensMetadata                             | Capture-specific details and information about the Lens itself.                                                                                                                               |
| map                                      | An image intended to drive or influence a behavior or value within a CG workflow.                                                                                                             |
| material                                 | Data values and relationships required to describe the look of a CG Asset.                                                                                                                    |
| productionCharacter                      | An Asset used in the portrayal of a Character.                                                                                                                                                |
| productionProp                           | A Depiction of the Narrative Prop.                                                                                                                                                            |
| productionProp.productionGreenery        | An Asset or Assets used to depict Narrative greenery in a Production Scene.                                                                                                                   |
| productionProp.productionVehicle         | An Asset used in the Depiction of a Narrative Vehicle                                                                                                                                         |
| productionSetDressing                    | Assets used in the depiction of Narrative Set Dressing.                                                                                                                                       |
| productionSetDressing.productionGreenery | An Asset or Assets used to depict Narrative greenery in a Production Scene.                                                                                                                   |
| productionSetDressing.productionVehicle  | An Asset used in the Depiction of a Narrative Vehicle                                                                                                                                         |
| proxy                                    | A lower quality representation of an Asset.                                                                                                                                                   |
| proxy.daily                              | A type of video proxy.                                                                                                                                                                        |
| proxy.editorial                          | A type of video proxy.                                                                                                                                                                        |
| recorderMetadata                         | Information about a Recorder and the recording media.                                                                                                                                         |
| script                                   | A Structured Document written as a blueprint to convey the creative intent for the Creative Work. Parsing the Script generates a guide to those things that are to be depicted in production. |
| sequenceChronologyDescriptor             | Describes how a series of Shots is used to generate a Sequence.                                                                                                                               |
| shot                                     | A discrete unit of visual narrative with a specified beginning and end.                                                                                                                       |
| shot.animation                           | A Shot that has been identified as requiring Animation work.                                                                                                                                  |
| shot.editorial                           | A shot that has been marked for editorial use.                                                                                                                                                |
| shot.vfx                                 | A Shot that has been identified as requiring VFX work.                                                                                                                                        |
| technicalReferenceMaterial               | Images and other material used to inform the execution of the production.                                                                                                                     |
#### audioChannelName
A formalization of the name of the loudspeaker the Audio Channel in intended to drive.

| Value | Description                        |
| ----- | ---------------------------------- |
| C     | Center channel                     |
| Ch    | Center Height channel              |
| Cs    | Center Surround channel            |
| HI    | Hearing Impaired channel           |
| L     | Left channel                       |
| Lc    | Left Center channel                |
| LFE   | Low Frequency Effects channel      |
| Lh    | Left Height channel                |
| Lrs   | Left Rear Surround channel         |
| Lrsh  | Left Rear Surround Height channel  |
| Ls    | Left Surround channel              |
| Lsh   | Left Surround Height channel       |
| Lss   | Left Side Surround channel         |
| Lssh  | Left Side Surround Height channel  |
| Lts   | Left Top Surround channel          |
| R     | Right channel                      |
| Rc    | Right Center channel               |
| Rh    | Right Height channel               |
| Rrs   | Right Rear Surround channel        |
| Rs    | Right Surround channel             |
| Rsh   | Right Surround Height channel      |
| Rss   | Right Surround Height channel      |
| Rssh  | Right Side Surround Height channel |
| Rts   | Right Top Surround channel         |
| Rtsh  | Right Rear Surround Height channel |
| Ts    | Top Surround channel               |
| VIN   | Visually Impaired channel          |

#### audioMixType
A description of the type or use for this mix.

| Value | Description |
|-------|-------------|
| finalDeliverable | Playable audio that can be packaged and distributed with a finished Creative Work. |
| finalMix | A Mix for distribution of the Creative Work. |
| onSetMix | A Mix of the on-set captured Audio. |
| printmaster | The combination of STEMs for a particular soundfield at unity gain. |
| temporaryMix | A non-final Mix used in the creative process, e.g. for review. |


#### mapType
Guidance about the intended use of a Map in a Material

| Value            |
| ---------------- |
| albedo           |
| ambientOcclusion |
| bump             |
| depthMap         |
| diffuse          |
| heightMap        |
| metalness        |
| normal           |
| opacity          |
| projectionMap    |
| roughness        |
| specular         |
| uvMap            |
| weightMap        |
#### mapFormat
The data layout of a Map.

| Value               | Description |
| ------------------- | ----------- |
| cubeFaceEnvironment | N/A         |
| cubeFaceShadow      | N/A         |
| latLongEnvironment  | N/A         |
| plainTexture        | N/A         |
| shadow              | N/A         |
| volumeShadow        | N/A         |
| volumeTexture       | N/A         |
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