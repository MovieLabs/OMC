The entities (people, organizations, and services) that are responsible for the production of the Creative Work.
### Properties
Includes properties from: [baseEntity](../core/baseEntity.md)

| Property      | Constraint        | Type                                                                                                                   | Description                                                                                                                              |
| ------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| entityType    | const<br>required | `"Participant"`                                                                                                        | Declares the entity type.                                                                                                                |
| ParticipantSC | oneOf             | [Person](./Person.md)<br>[Department](./Department.md)<br>[Organization](./Organization.md)<br>[Service](./Service.md) | Describes the form of a Participant along with the attributes specific to that Participant's form.                                       |
| participantFC |                   |                                                                                                                        | The use or purpose of a Participant within the production process.                                                                       |
| contact       |                   | [contact](../Utility/Utility.md#contact)                                                                               | Means by which the subject of an entity may be contacted in the production.                                                              |
| Participant   |                   | [ [Participant](../Participant/Participant.md)<br>[identifier](../Utility/Utility.md#identifier) ]                     | A Participant composed of other Participants, where the assemblage is treated as a single unit.                                          |
| Context       |                   | [ [Context](../MediaCreationContext/Context.md) <br>[identifier](../Utility/Utility.md#identifier) ]                   | Informs scope within the construction process of a Creative Work.                                                                        |
| Depiction     |                   | [ [Depiction](../MediaCreationContext/Depiction.md) <br>[identifier](../Utility/Utility.md#identifier) ]               | The representation of something from a narrative entity by a production entity in the Creative Work, specified or implied by the Script. |
|               |                   |                                                                                                                        |                                                                                                                                          |
### Object Properties

