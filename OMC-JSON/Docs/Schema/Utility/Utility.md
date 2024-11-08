
#### annotation

| Field Name | Operator | Type         | Description                         |
| ---------- | -------- | ------------ | ----------------------------------- |
| author     |          | string, null | Who wrote or added this annotation  |
| title      |          | string, null | A title for the note or annotation. |
| text       |          | string, null | The text of the note or annotation. |

#### identifier

| Field Name | Operator | Type                                  | Description                                                            |
| ---------- | -------- | ------------------------------------- | ---------------------------------------------------------------------- |
| identifier |          | [ [identifierItem](#identifierItem) ] | An identifier uniquely identifies an entity within a particular scope. |

#### identifierItem

| Field Name      | Operator | Type   | Description                                                                                              |
| --------------- | -------- | ------ | -------------------------------------------------------------------------------------------------------- |
| identifierScope | required | string | The universe within which an identifier is valid and unique.                                             |
| identifierValue | required | string | A string of characters that uniquely identifies an object within a particular scope.                     |
| combinedForm    |          | string | A combination of the Identifier Scope and Value that is useful for utilizing the identifier in a system. |
| url             |          | string | A URL or IRI that can be used for resolving the Identifier Value within the Identifier Scope.            |



#### country



| Field Name | Type         |     |
| ---------- | ------------ | --- |
|            | string, null |     |
|            |              |     |

## Reference

Description of reference