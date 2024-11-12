Used to capture key identifying information about what is being recorded on any given setup and take.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property     | Constraint      | Type                                                                                                                                               | Description                                                                                                                                                                        |
| ------------ | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              |                 | [baseEntity](https://www.odwebp.svc.ms/core/baseEntity.md)                                                                                         |                                                                                                                                                                                    |
| entityType   | const, required | "Slate"                                                                                                                                            |                                                                                                                                                                                    |
| slateUID     |                 | string, null                                                                                                                                       | Slate Unique Identifier                                                                                                                                                            |
| cameraLabel  |                 | string, null                                                                                                                                       | Label for the Camera responsible for the Capture, usually related to the role and responsibility of the group operating it and usually a single upper-case letter starting with A. |
| cameraUnit   |                 | string, null                                                                                                                                       | A group of Participants responsible for shooting some element of a Scene, e.g., a Main Unit or Second Unit.                                                                        |
| cameraRoll   |                 | string, null                                                                                                                                       | Identifier for a group of events captured together on the same camera on the same media.                                                                                           |
| soundRoll    |                 | string, null                                                                                                                                       | Identifier for a group of audio events captured together on the same recording device and same media.                                                                              |
| shootDate    |                 |                                                                                                                                                    | The date of capture or creation                                                                                                                                                    |
| shootDay     |                 | number, string, null                                                                                                                               | The number of the day on the shooting schedule.                                                                                                                                    |
| recordingFPS |                 | number, null                                                                                                                                       | Frames per second recorded by the camera.                                                                                                                                          |
| Context      |                 | Context Entity                                                                                                                                     | Informs scope within the construction process of a Creative Work.                                                                                                                  |
| CreativeWork | oneOf           | [ [CreativeWork](https://www.odwebp.svc.ms/Creative%20Work.md)  <br>[identifier](https://www.odwebp.svc.ms/Utility/Utility.md#identifier) ]        |                                                                                                                                                                                    |
| Director     | anyOf           | [ [Participant](https://www.odwebp.svc.ms/Participant/Participant.md)  <br>[identifier](https://www.odwebp.svc.ms/Utility/Utility.md#identifier) ] |                                                                                                                                                                                    |


## Example JSON

```
{
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",
  "entityType": "Slate",
  "identifier": [
    {
      "identifierScope": "labkoat",
      "identifierValue": "slt/uOKge8nJKPQM9y9IVkDIz"
    }
  ],
  "slateUID": "2A-2",
  "cameraLabel": "A",
  "cameraUnit": "MaIn",
  "cameraRoll": "CRA",
  "soundRoll": "SRA",
  "shootDate": "2022-07-23",
  "shootDay": 1,
  "recordingFPS": 29.97,
  "CreativeWork": null,
  "Director": [
    {
      "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",
      "entityType": "Participant",
      "identifier": [
        {
          "identifierScope": "labkoat",
          "identifierValue": "ptc/3AE1ybCWJXJFxKhWhF0qd"
        }
      ],
      "name": "Herman Malinalli"
    }
  ],
  "Context": [
    {
      "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",
      "entityType": "Context",
      "identifier": [
        {
          "identifierScope": "labkoat",
          "identifierValue": "cxt/hlDwnZidsasQM3qOTyCWE"
        }
      ],
      "for": {
        "ProductionScene": [
          {
            "identifier": [
              {
                "identifierScope": "labkoat",
                "identifierValue": "pscn/Wu7bLX7wJoV0PbyqjidHz"
              }
            ]
          }
        ],
        "Asset": [
          {
            "identifier": [
              {
                "identifierScope": "labkoat",
                "identifierValue": "ast/MNfgKfj9wdSbXBOf5QbbY"
              }
            ]
          }
        ]
      }
    }
  ]
}
```