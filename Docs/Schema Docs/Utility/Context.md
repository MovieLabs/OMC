

### Character

| Domain    | Relationship        | Range             |
| --------- | ------------------- | ----------------- |
| Character | uses                | NarrativeProp     |
| Character | usesWardrobe (uses) | NarrativeWardrobe |
| Character | hasCostume          | Costume           |
| Character | appearsIn           | NarrativeScene    |
| Character | isPortrayedBy       | Participant       |
| Character | hasRelatedAsset     | Asset             |
|           |                     |                   |
|           |                     |                   |
|           |                     |                   |





### NarrativeProp

| Domain        | Relationship    | Range          |
| ------------- | --------------- | -------------- |
| NarrativeProp | isUsedBy        | Character      |
| NarrativeProp | appearsIn       | NarrativeScene |
| NarrativeProp | isDepictedBy    | ProductionProp |
|               | hasRelatedAsset | Asset          |
|               |                 |                |
|               |                 |                |
|               |                 |                |





### Production Prop

| Domain          | Relationship | Range     |
| --------------- | ------------ | --------- |
| Production Prop | isUsedBy     | Portrayal |
|                 |              |           |
|                 |              |           |
|                 |              |           |
|                 |              |           |
|                 |              |           |
|                 |              |           |
|                 |              |           |
|                 |              |           |

