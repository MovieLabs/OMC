A uniquely identified production.

| Property                              | Operator                       | Type                                                                                                  | Description |
| ------------------------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------- | ----------- |
|                                       |                                | [baseEntity](Schema/core/baseEntity)                                                                  |             |
| entityType                            | const, required                | "CreativeWork"                                                                                        |             |
| [creativeWorkType](#creativeWorkType) | [ctrlValue](#creativeWorkType) | string, null                                                                                          |             |
| creativeWorkTitle                     |                                | [ [creativeWorkTitle](#creativeWorkTitle) ]                                                           |             |
| ProductionCompany                     | anyOf                          | [ [Participant](Schema/Participant/Participant) <br>[identifier](Schema/Utility/Utility#identifier) ] |             |



### Controlled Values

#### creativeWorkType

### Object Properties
#### episodeSequence

| Property           | Operator | Type                                          | Description                                                                        |
| ------------------ | -------- | --------------------------------------------- | ---------------------------------------------------------------------------------- |
| houseSequence      |          | string, number, null                          | The internal Episode number assigned by the producer or commissioning broadcaster. |
| distributionNumber |          | [ [distributionNumber](#distributionNumber) ] |                                                                                    |

## Examples

```JSON
{}
```