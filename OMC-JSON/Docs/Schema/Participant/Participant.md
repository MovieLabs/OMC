The entities (people, organizations, and services) that are responsible for the production of the Creative Work.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property      | Operator          | Type            | Description               |
| ------------- | ----------------- | --------------- | ------------------------- |
| entityType    | const<br>required | `"Participant"` | Declares the entity type. |
| ParticipantSC |                   |                 |                           |
| participantFC |                   |                 |                           |
| contact       |                   | string, null    |                           |
| Participant   |                   |                 |                           |
| Context       |                   |                 |                           |
| Depiction     |                   |                 |                           |

#### Controlled Values

| creativeWorkType | Description                                                                                                                |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------- |
| creativeWork     | A uniquely identified production.                                                                                          |
| series           | A group of Creative Works with a common overarching title and a strong relationship between the individual Creative Works. |
| season           | A group of Episodes in a Series that are made or distributed together.                                                     |
| episode          | A single Creative Work that is part of Series or Season.                                                                   |
