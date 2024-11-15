# Character
A sentient entity (usually a person but not always) in the script whose specific identity is consequential to the narrative. A Character is generally identified by a specific name.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property      | Constraint        | Type                                                                               | Description                                              |
| ------------- | ----------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------- |
| entityType    | const<br>required | `"Character"`                                                                      | Declares the entity type.                                |
| characterType | enum              | [characterType](#characterType)                                                    | The specific type of character.                          |
| characterName |                   | [completeName](../Utility/Utility.md#completeName)                                 | The canonical name or names for the character.           |
| profile       |                   | [profile](#profile)                                                                | Specific details describing the character.               |
| quantity      |                   | string<br>number<br>null                                                           | Indicate the number of 'extra' characters when required. |
| Context       | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]     | A set of Contexts related to this Character              |
| Depiction     | anyOf             | [ [Depiction](./Depiction.md) <br>[identifier](../Utility/Utility.md#identifier) ] | A set of portrayls for this Character                    |
### Object Properties

#### profile
Specific details describing the character.

| Property                | Constraint | Type                                                | Description                                                   |
| ----------------------- | ---------- | --------------------------------------------------- | ------------------------------------------------------------- |
| physicalCharacteristics |            | [physicalCharacteristics](#physicalCharacteristics) | Description of a characters defining physical characteristics |
| gender                  |            | [gender](../Utility/Utility.md#gender)              | A gender for the character                                    |
| background              |            | [annotation](../Utility/Utility.md#annotation)      | Additional annotations on a character's background.           |
#### physicalCharacteristics
Description of a characters defining physical characteristics

| Property   | Constraint | Type                                                   | Description                                |
| ---------- | ---------- | ------------------------------------------------------ | ------------------------------------------ |
| species    |            | string<br>null                                         | A species to which this character belongs. |
| hairColor  |            | string<br>null                                         | The hair color of the character.           |
| hairLength |            | string<br>null                                         | The length of hair of the character.       |
| eyeColor   |            | string<br>null                                         | The color of the characters eyes.          |
| weight     |            | [weight](../Utility/Utility.md#weight)                 | The weight of the character.               |
| height     |            | [linearDistance](../Utility/Utility.md#linearDistance) | The height of the character.               |

### Controlled & Enumerated Values

#### characterType
The specific type of character

| Value     | Description                                                                                                                             |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| character | A sentient entity (usually a person but not always) in the script whose specific identity is consequential to the narrative.            |
| extra     | A sentient entity (usually a person, but not always) in the Script whose specific identity is minimally consequential to the narrative. |

### Examples

```JSON
{  
  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
  "entityType": "Character",  
  "identifier": [  
    {  
      "identifierScope": "labkoat",  
      "identifierValue": "chr/HNvHjXqJY9wv1IwjG-Hf1"  
    }  
  ],  
  "characterName": {  
    "fullName": "Sven",  
    "firstGivenName": "Sven",  
    "scriptName": "SVEN"  
  },  
  "profile": {  
    "physicalCharacteristics": {  
      "species": "Human",  
      "height": "1m90cm",  
      "weight": "80kg",  
      "hairColor": "Brown",  
      "hairLength": "Short",  
      "eyeColor": "Green"  
    },  
    "background": {  
      "likes": "Kiera, Space, Nature",  
      "dislikes": "War, Big space cities, Conflict",  
      "habits": "Sven is a bit of a sloth, happy to be far from prying eyes as he does his work at his pace. He is also a bit of a coward and has avoided the space navy at all cost. He is kind and patient and caring for the people in his life like Kiera.",  
      "traits": "Sven is a helpful unassuming character who likes to be alone. He connects with his handlers like Kiera but is happy to be engrossed in his work. He is generally scared of all things and not a hero."  
    },  
    "gender": {  
      "gender": "male",  
      "genderPronoun": "he/him"  
    }  
  },  
  "description": "Sven is an unassuming Satellite repair man. He spends his time alone in his ship traveling to remote planets on the outskirt of the galaxy maintaining a network of exploration satellites. He is more of a lover than a fighter.",  
  "Depiction": [  
    {  
      "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
      "entityType": "Depiction",  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "dep-HNvGRn9JY9wv1IwjG8Gff"  
        }  
      ]  
    }  
  ],  
  "Context": [  
    {  
      "identifier": [  
        {  
          "identifierScope": "labkoat",  
          "identifierValue": "cxt/377RXIREHUj5MPzsl-Sba"  
        }  
      ]  
    }  
  ]  
}
```
