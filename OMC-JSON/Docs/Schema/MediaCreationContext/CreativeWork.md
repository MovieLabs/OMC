A uniquely identified production.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property             | Constraint     | Type                                                                                                | Description                                                                                                                        |
| -------------------- | -------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| entityType           | const required | `"CreativeWork"`                                                                                    | Declares the entity type.                                                                                                          |
| creativeWorkType     | enum           | [creativeWorkType](#creativeWorkType)                                                               | The specific type of creative work                                                                                                 |
| creativeWorkCategory | ctrlValue      | [creativeWorkCategory](#creativeWorkCategory)                                                       | The form of the creative work.                                                                                                     |
| seasonNumber         |                | string<br>number<br>null                                                                            |                                                                                                                                    |
| episodeSequence      |                | [&nbsp[episodeSequence](#episodeSequence)&nbsp]                                                     |                                                                                                                                    |
| creativeWorkTitle    |                | [&nbsp[creativeWorkTitle](#creativeWorkTitle)&nbsp]                                                 | The canonical title name or names for the creative work                                                                            |
| approximateLength    |                | [durationTime](../Utility/Utility.md#durationTime)                                                  | Should be formatted to comply with ISO 8601.                                                                                       |
| originalLanguage     |                | [ [language](../Utility/Utility.md#language) ]                                                      | A list of the primary languages used in the Creative Work.                                                                         |
| countryOfOrigin      |                | [ [country](../Utility/Utility.md#country) ]                                                        | The home country of the companies that had primary creative control of the creation of the Creative Work, generally the producers. |
| Context              | anyOf          | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]                      | Informs scope within the construction process of a Creative Work.                                                                  |
| Series               | anyOf          | [ [CreativeWork](./CreativeWork.md) <br>[identifier](../Utility/Utility.md#identifier) ]            | A series this Creative Work belongs to.                                                                                            |
| Season               | anyOf          | [ [CreativeWork](./CreativeWork.md) <br>[identifier](../Utility/Utility.md#identifier) ]            | A season this Creative Work belongs to.                                                                                            |
| Episiode             | anyOf          | [ [CreativeWork](./CreativeWork.md) <br>[identifier](../Utility/Utility.md#identifier) ]            | A set of Episodes this Creative Work contains.                                                                                     |
| ProductionCompany    | anyOf          | [ [Participant](../Participant/Participant.md) <br>[identifier](../Utility/Utility.md#identifier) ] | An Organization responsible for the development and production of a Creative Work.                                                 |


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
| titleType     | enum       | [titleType](#titleType)                    | The specific type of title |
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

| Value    | Description                                                                                                                                                                                                |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| internal | An internal title or code name, not used in commercial release.                                                                                                                                            |
| working  | Working title, used during the course of production.                                                                                                                                                       |
| regional | A title unique to a particular territory or otherwise used outside the work’s original home territory, such as local titles given to foreign imports. May be in the same language as the Release title(s). |
| release  | The original release title for the work.                                                                                                                                                                   |




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
}
```

