# Asset

| Attribute   | Type | Description | Required |
| ----------- | ---- | ----------- | --- |
| Identifier  | [Identifier](Identifier.md)   | A set of unique identifiers                   | Yes |
| name | string | | No |
| description | string | A brief description of the asset | No |
| StructuralCharacteristics | StructuralCharacteristics |  | Yes |
| FunctionalCharacteristics | FunctionalCharacteristics |  | Yes |
| Relationship | [Related](#Related) | Contexts and other entities the asset is related to | No |


## Related


| Predicate | Type  | Description |
| ---------- | ----------------- | ---- |
| hasProductionScene | [Production Scene](./ProductionScene) | |
| uses | Prop | Props the character uses |
| | | |




