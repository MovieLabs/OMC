
| Property      | Operator       | Type                                                             | Description                                                                                                                                  |
| ------------- | -------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| schemaVersion | enum, required | string                                                           | Describes the version of OMC-JSON schema that was used to create this instance.                                                              |
| identifier    | required       | [identifier](../Utility/Utility.md#identifier)                   |                                                                                                                                              |
| name          |                | string, null                                                     | A name for the entity, this is primarily for human consumption in things like user interfaces. It should not be considered a canonical name. |
| description   |                | string, null                                                     | A brief description of the entity, primarily for human consumption.                                                                          |
| customData    |                | [&nbsp[customData](../Utility/Utility.md#customData)&nbsp], null | A user defined set of custom data in the payload of the instance, used where the formal schema lacks required properties.                    |
| annotation    |                | [&nbsp[annotation](../Utility/Utility.md#annotation)&nbsp], null | Additional annotations about the entity.                                                                                                     |
| tag           |                | [ [tag](../Utility/Utility.md#tag) ], null                       | User defined tags for the entity.                                                                                                            |
| instanceInfo  |                | [instanceInfo](#instanceInfo), null                              | Properties that describe information about this particular instance of an entity.                                                            |

### Object Properties

#### instanceInfo

| Property      | Constraint | Type                                                                                            | Description                                                                                                               |
| ------------- | ---------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| createdOn     |            | [dateTime](../Utility/Utility.md#dateTime)                                                      |                                                                                                                           |
| CreatedBy     | oneOf      | [Participant](../Participant/Participant.md) <br>[identifier](../Utility/Utility.md#identifier) | The entities (people, organizations, and services) that are responsible for the production of the Creative Work.          |
| lastUpdatedOn |            | [dateTime](../Utility/Utility.md#dateTime)                                                      |                                                                                                                           |
| LastUpdatedBy | oneOf      | [Participant](../Participant/Participant.md) <br>[identifier](../Utility/Utility.md#identifier) | The entities (people, organizations, and services) that are responsible for the production of the Creative Work.          |
| customData    |            | [&nbsp[customData](../Utility/Utility.md#customData)&nbsp], null                                | A user defined set of custom data in the payload of the instance, used where the formal schema lacks required properties. |
