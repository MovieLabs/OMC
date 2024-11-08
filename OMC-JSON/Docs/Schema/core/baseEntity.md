
| Property      | Operator       | Type         | Description                                                                                                                                  |
| ------------- | -------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| schemaVersion | enum, required | string       | Describes the version of OMC-JSON schema that was used to create this instance.                                                              |
| identifier    | required       | [  ]         |                                                                                                                                              |
| name          |                | string, null | A name for the entity, this is primarily for human consumption in things like user interfaces. It should not be considered a canonical name. |
| description   |                | string, null | A brief description of the entity, primarily for human consumption.                                                                          |
| customData    |                |              |                                                                                                                                              |
| annotation    |                |              |                                                                                                                                              |
| tag           |                |              |                                                                                                                                              |
| instanceInfo  |                |              | Properties that describe information about this particular instance of an entity.                                                            |

