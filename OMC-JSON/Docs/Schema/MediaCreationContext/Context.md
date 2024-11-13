Informs scope within the construction process of a Creative Work.
### Properties

Includes properties from: [baseEntity](../core/baseEntity.md)

| Property          | Constraint        | Type                                                                           | Description                                                                     |
| ----------------- | ----------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| entityType        | const<br>required | `"CreativeWork"`                                                               |                                                                                 |
| contextType       | ctrlValue         | [contextType](#contextType)                                                    | The specific type of context                                                    |
| contextCategory   |                   | string<br>null                                                                 | Provides an additional level of categorization of the Context beyond it's type. |
| contextProperties |                   | [contextProperties](#contextProperties)                                        | Properties specific to this composition                                         |
| For               |                   |                                                                                |                                                                                 |
| Context           | anyOf             | [ [Context](./Context.md) <br>[identifier](../Utility/Utility.md#identifier) ] | Informs scope within the construction process of a Creative Work.               |
| contributor       |                   |                                                                                |                                                                                 |
| contributesTo     |                   |                                                                                |                                                                                 |
| features          |                   |                                                                                |                                                                                 |
| featuresIn        |                   |                                                                                |                                                                                 |
| for               |                   |                                                                                |                                                                                 |
| has               |                   |                                                                                |                                                                                 |
| neededBy          |                   |                                                                                |                                                                                 |
| needs             |                   |                                                                                |                                                                                 |
| related           |                   |                                                                                |                                                                                 |
| represents        |                   |                                                                                |                                                                                 |
| representedBy     |                   |                                                                                |                                                                                 |
| usedIn            |                   |                                                                                |                                                                                 |
| uses              |                   |                                                                                |                                                                                 |




### Controlled Values

#### contextType


### Object Properties

#### contextProperties
## Examples

```JSON
{}
```