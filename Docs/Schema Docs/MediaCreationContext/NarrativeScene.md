
## Scene

### Narrative Scene
Taken from the narrative itself and traditionally defined by creative intent and various kinds of unity  (e.g., time,
place, action, or theme).


| Attribute   | Type | Description | Required |
| ----------- | ---- | ----------- | --- |
| Identifier  | [Identifier](Identifier.md)   | A set of unique identifiers                   | Yes |
| sceneHeader | string | A phrase used when referring to the Narrative Scene | Yes |
| description | string | A brief description of the scene | No |
| slugline    | sluglineComponent | A line in the script calling out specific information about a scene | No |
| Relationship | [Related](#Related) | Contexts and other entities the scene is related to



sluglineComponent {key: value}


## Related


| Predicate | Type  | Description |
| ---------- | ----------------- | ---- |
| isFromWork | [CreativeWork](CreativeWork.md) | Narrative scenes the character appears in |
| hasProductionScene | [Production Scene](ProductionScene.md) | |
| uses | Prop | Props the character uses |
| | | |




