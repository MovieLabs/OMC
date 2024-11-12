A uniquely identified production.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property             | Constraint     | Type                                                                                                | Description                                                                                                      |
| -------------------- | -------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| entityType           | const required | `"CreativeWork"`                                                                                    | Declares the entity type.                                                                                        |
| creativeWorkType     | enum           | [creativeWorkType](#creativeWorkType)                                                               | The specific type of creative work                                                                               |
| creativeWorkCategory | ctrlValue      | [creativeWorkCategory](#creativeWorkCategory)                                                       | The form of the creative work.                                                                                   |
| seasonNumber         |                | string, number, null                                                                                |                                                                                                                  |
| episodeSequence      |                | [&nbsp[episodeSequence](#episodeSequence)&nbsp]                                                     |                                                                                                                  |
| creativeWorkTitle    |                | [&nbsp[creativeWorkTitle](#creativeWorkTitle)&nbsp]                                                 | The canonical title name or names for the creative work                                                          |
| approximateLength    |                | [durationTime](../Utility/Utility.md#durationTime)                                                  | Should be formatted to comply with ISO 8601.                                                                     |
| originalLanguage     |                | [ [language](../Utility/Utility.md#language) ]                                                      | An IETF BCP 47 language code.                                                                                    |
| countryOfOrigin      |                | [ [country](../Utility/Utility.md#country) ]                                                        | The country, as an ISO 3166-1 alpha-2 country code.                                                              |
| Context              | anyOf          | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]                      | Informs scope within the construction process of a Creative Work.                                                |
| Series               | anyOf          | [ [CreativeWork](./CreativeWork.md) <br>[identifier](../Utility/Utility.md#identifier) ]            | A uniquely identified production.                                                                                |
| Season               | anyOf          | [ [CreativeWork](./CreativeWork.md) <br>[identifier](../Utility/Utility.md#identifier) ]            | A uniquely identified production.                                                                                |
| Episiode             | anyOf          | [ [CreativeWork](./CreativeWork.md) <br>[identifier](../Utility/Utility.md#identifier) ]            | A uniquely identified production.                                                                                |
| ProductionCompany    | anyOf          | [ [Participant](../Participant/Participant.md) <br>[identifier](../Utility/Utility.md#identifier) ] | The entities (people, organizations, and services) that are responsible for the production of the Creative Work. |


### Object Properties
#### episodeSequence

| Property           | Constraint | Type                                                  | Description                                                                                                                                                      |
| ------------------ | ---------- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| houseSequence      |            | string, number, null                                  | The internal Episode number assigned by the producer or commissioning broadcaster.                                                                               |
| distributionNumber |            | [&nbsp[distributionNumber](#distributionNumber)&nbsp] | The position number of the Episode within its parent Season (or parent Series, if the Episode is directly in a Series) during initial broadcast or distribution. |
#### distributionNumber
The position number of the Episode within its parent Season (or parent Series, if the Episode is directly in a Series) during initial broadcast or distribution.

| Property | Constraint | Type                 | Description |
| -------- | ---------- | -------------------- | ----------- |
| value    |            | string, number, null |             |
| domain   |            | string, null         |             |
#### creativeWorkTitle
The canonical title name for the creative work with type and language

| Property      | Constraint | Type                                       | Description                |
| ------------- | ---------- | ------------------------------------------ | -------------------------- |
| titleName     |            | string, null                               |                            |
| titleType     | ctrlValue  | [titleType](#titleType)                    | The specific type of title |
| titleLanguage |            | [language](../Utility/Utility.md#language) | The language of the title  |


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

##### titleType

| Value         | Description |
| ------------- | ----------- |
| internalTitle |             |
| workingTitle  |             |
| regionalTitle |             |
| releaseTitle  |             |




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

