The entities (people, organizations, and services) that are responsible for the production of the Creative Work.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property      | Constraint        | Type                                                                                                                   | Description                                                                                        |
| ------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| entityType    | const<br>required | `"Participant"`                                                                                                        | Declares the entity type.                                                                          |
| ParticipantSC | oneOf             | [Person](./Person.md)<br>[Department](./Department.md)<br>[Organization](./Organization.md)<br>[Service](./Service.md) | Describes the form of a Participant along with the attributes specific to that Participant's form. |
| participantFC |                   | [participantFC](#participantFC)                                                                                        | The use or purpose of a Participant within the production process.                                 |
| Participant   |                   | [ [Participant](../Participant/Participant.md)<br>[identifier](../Utility/Utility.md#identifier) ]                     | A Participant composed of other Participants, where the assemblage is treated as a single unit.    |
| Context       |                   | [ [Context](../MediaCreationContext/Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]                   | Informs scope within the construction process of a Creative Work.                                  |
| Depiction     |                   | [ [Depiction](../MediaCreationContext/Depiction.md) <br>[identifier](../Utility/Utility.md#identifier) ]               | The set of entities this Participant depicts.                                                      |
### Object Properties

#### participantFC

| Property       | Constraint | Type                                           | Description                                                                                                                              |
| -------------- | ---------- | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| functionalType |            | string<br>null                                 |                                                                                                                                          |
| jobTitle       |            | string<br>null                                 | A formal name for the position a Person holds in relation to the production, usually associated with a specific set of responsibilities. |
| Role           |            | [ [Role](./Role.md) ]                          |                                                                                                                                          |
| customData     |            | [customData](../Utility/Utility.md#customData) | A user defined set of custom data in the payload of the instance, used where the formal schema lacks required properties.                |