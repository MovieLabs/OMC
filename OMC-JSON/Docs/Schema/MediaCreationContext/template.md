A uniquely identified production.

| Property                              | Operator                       | Type                                                                           | Description |
| ------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------ | ----------- |
|                                       |                                | [baseEntity](../core/baseEntity.md)                                            |             |
| entityType                            | const, required                | "CreativeWork"                                                                 |             |
| [creativeWorkType](#creativeWorkType) | [ctrlValue](#creativeWorkType) | string, null                                                                   |             |
| creativeWorkTitle                     |                                | [ [creativeWorkTitle](#creativeWorkTitle) ]                                    |             |
| ProductionCompany                     | anyOf                          | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ] |             |



### Controlled & Enumerated Values

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