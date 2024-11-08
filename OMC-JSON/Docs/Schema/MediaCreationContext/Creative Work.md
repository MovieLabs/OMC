A uniquely identified production.

| Property                              | Constraints     | Type                                                                                                | Description                          |
| ------------------------------------- | --------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------ |
|                                       |                 | [baseEntity](../core/baseEntity.md)                                                                 |                                      |
| entityType                            | const, required | "CreativeWork"                                                                                      |                                      |
| [creativeWorkType](#creativeWorkType) | enum            | string, null                                                                                        |                                      |
| creativeWorkCategory                  | ctrlValue       | string, null                                                                                        | The type or form of a Creative Work. |
| seasonNumber                          |                 | string, number, null                                                                                |                                      |
| episodeSequence                       |                 | [ [episodeSequence](#episodeSequence) ]                                                             |                                      |
| creativeWorkTitle                     |                 | [ [creativeWorkTitle](#creativeWorkTitle) ]                                                         |                                      |
| approximateLength                     |                 |                                                                                                     |                                      |
| originalLanguage                      |                 |                                                                                                     |                                      |
| countryOfOrigin                       |                 |                                                                                                     |                                      |
| Context                               |                 | Context Entity                                                                                      |                                      |
| Series                                | anyOf           | [ [CreativeWork](./Creative%20Work%Entity.md) <br>[identifier](../Utility/Utility#identifier.md) ]  |                                      |
| Season                                | anyOf           | [ [CreativeWork](./Creative%20Work.md) <br>[identifier](../Utility/Utility.md#identifier) ]         |                                      |
| Episiode                              | anyOf           | [ [CreativeWork](./Creative%20Work.md) <br>[identifier](../Utility/Utility.md#identifier) ]         |                                      |
| ProductionCompany                     | anyOf           | [ [Participant](../Participant/Participant.md) <br>[identifier](../Utility/Utility.md#identifier) ] |                                      |

*For the entityType is this the best way to represent the value*

### Controlled Values

#### creativeWorkType

| Value        | Description                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------------------- |
| creativeWork | A uniquely identified production.                                                                                          |
| series       | A group of Creative Works with a common overarching title and a strong relationship between the individual Creative Works. |
| season       | A group of Episodes in a Series that are made or distributed together.                                                     |
| episode      | A single Creative Work that is part of Series or Season.                                                                   |

#### creativeWorkCategory

| Value        | Description                                                                                                                                                                                             |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| movie        | A feature film or other long-from motion picture that first appeared in theatrical exhibition or was released directly to video (home entertainment). If the duration is ≤ 40 minutes, then the record. |
| tv           | Content that first appeared via broadcast (terrestrial, satellite, cable, etc.). This includes telefilms, other one-off programs, and Episodes of television series.                                    |
| short        | A short program (≤ 40 minutes) that first appeared in theatrical exhibition or was released directly to video (home entertainment). If the duration is > 40 minutes, then the record is a Movie.        |
| supplemental | Material created to support some other work, such as a trailer, featurette, deleted scenes, gag reel, interviews, behind-the-scenes, etc.                                                               |

### Object Properties
#### episodeSequence

| Property           | Operator | Type                                          | Description                                                                        |
| ------------------ | -------- | --------------------------------------------- | ---------------------------------------------------------------------------------- |
| houseSequence      |          | string, number, null                          | The internal Episode number assigned by the producer or commissioning broadcaster. |
| distributionNumber |          | [ [distributionNumber](#distributionNumber) ] |                                                                                    |
#### distributionNumber

| Property | Operator | Type                 | Description |
| -------- | -------- | -------------------- | ----------- |
| value    |          | string, number, null |             |
| domain   |          | string, null         |             |
#### creativeWorkTitle

| Property      | Operator  | Type         | Description |
| ------------- | --------- | ------------ | ----------- |
| titleName     |           | string, null |             |
| titleType     | ctrlValue | string, null |             |
| titleLanguage |           | string, null |             |

## Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "CreativeWork",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "cw/hlDTz5s8IStbxWvdRVfSh"  
    }  
  ],  
  "creativeWorkType": "creativeWork",  
  "creativeWorkCategory": "short",  
  "creativeWorkTitle": [  
    {  
      "title": "Hyperspace Madness",  
      "titleType": "releaseTitle",  
      "titleLanguage": "en"  
    },  
    {  
      "title": "HSM",  
      "titleType": "internalTitle",  
      "titleLanguage": "en"  
    }  
  ],  
  "seasonNumber": 4,  
  "episodeSequence": {  
    "houseSequence": "4",  
    "distributionNumber": [  
      {  
        "value": 4,  
        "domain": "labkoat"  
      }  
    ]  
  },  
  "description": "Sven is a bumbling intergalactic repair man sent off to investigate a malfunctioning satellite.. He is quickly ambushed by the dreaded Killamari who have taken over the planet and plan to use it as a base to invade earth.",  
  "approximateLength": "PT5M",  
  "originalLanguage": [  
    "en"  
  ],  
  "countryOfOrigin": [  
    "US"  
  ],  
  "Series": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "cw/hlDTz5s8IStbx6jfjdo"  
        }  
      ]  
    }  
  ],  
  "Season": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "cw/h443258IStbx6jfjdo"  
        }  
      ]  
    }  
  ],  
  "Episode": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "cw/54gtrs8IStbx6jfjdo"  
        }  
      ]  
    }  
  ],  
  "ProductionCompany": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "cw/hlDTz5s8ISgdsre324"  
        }  
      ]  
    }  
  ],  
  "Context": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "cxt/6RdTMezue-GZEDEB44_x7"  
        }  
      ]  
    }  
  ],  
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
        "tagValue",  
        8  
      ]  
    }  
  ]  
},
```
