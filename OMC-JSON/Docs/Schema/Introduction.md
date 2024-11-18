# Schema Introduction

## JSON
OMC-JSON is a specification for exchanging information between applications and workflows during the production and media based productions like movie and television shows.

OMC-JSON uses [JavaScript Object Notation](https://www.rfc-editor.org/info/rfc8259) to serialize information that can be exchanged or transmitted over multiple mechanisms including REST api's, graphQl, messaging systems or as files.

## JSON-Schema
OMC-JSON is written using the [JSON-Schema specification draft 2019-09](https://json-schema.org/draft/2019-09)

JSON Schema defines the structure, content, data types, and constraints of JSON documents. It's an IETF standard that helps ensure the consistency and integrity of JSON data across applications.

JSON documents may be validated using a [JSON-Schema validator](https://json-schema.org/tools) with a JSON Schema(which is itself a JSON document). There are many validators available in all of the major programming languages, At MovieLabs we have had success using [AJV]([Ajv JSON schema validator](https://ajv.js.org/)) for Javascript applications and [jsonschema]([jsonschema 4.23.1.dev47+g4e85551 documentation](https://python-jsonschema.readthedocs.io/en/latest/)) for Python.

MovieLabs also provides a validator for OMC-JSON. As well as performing basic validation (i.e. pass/fail), it implements additional checks that report and warn when best practices are not followed, such as not using controlled values or badly formed identifiers. A web based version is here https://omc-validator.mc.movielabs.com/, it is also available via an API and Docker container.
## Documentation

The documentation predominantly organized as a series of documents by entity. In addition there are descriptions of the core sub-schemas that describe the structure of the OMC-JSON but are not directly part of the broader ontology or data model. There are also a set of utility sub-schemas that are shared throughout.

#### Property
The property name, which is case sensitive
#### Constraint
Schema restraints place some sort of restriction or rule on the property value

| Constraint | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| required   | This property must be present and have a valid value to pass validation.<br><br>If a field is not explicitly **required** it can be considered optional.                                                                                                                                                                                                                                                                                                                 |
| const      | Must be set to the single value described in the **Type** column.                                                                                                                                                                                                                                                                                                                                                                                                        |
| enum       | Value must match one of the values of the enumerated list, the documentation may show those values in the **Type** column, or in a separate table if more space is required.                                                                                                                                                                                                                                                                                             |
| ctrlValue  | This is a special value that is not part of the JSON-Schema vocabulary. Controlled Values are part of the OMC ontology, they are considered best practice but are not enforced by the schemas, these terms are typically defined in by the schema and therefore can be universally recognized.<br><br>Using a value that is not a controlled value means parties consuming OMC-JSON may not understand the meaning of the value.<br><br>These values are case sensitive. |
| oneOf      | A choice of sub-schemas are available and data must validate against one and only one of the available options.                                                                                                                                                                                                                                                                                                                                                          |
| anyOf      | A choice of sub-schemas may be used and data can validate against any of the available options. This is often used where an property value is an array, each object in the array must independently be valid against one or more of the listed schemas.                                                                                                                                                                                                                  |
| pattern    | A regular expression (regEx) is used to validate the value.                                                                                                                                                                                                                                                                                                                                                                                                              |
*Notes:*
- *Additional explanation and examples are available in the JSON-Schema documentation linked above.*
- *Almost all sub-schemas are restricted from having additional properties, [customData](./Utility/Utility.md#customData) is provided for optional user data not covered by OMC *

#### Type
The type of value allowed, this may be a JSON privative such as 'string', 'number' or 'null', an OMC-JSON property or set of controlled values which will be linked in the Type field.
#### Description
A description of the property and what it represents in the ontology.

### Additional Notes
For those of you who spend time examining the schema you may find small technical discrepancies between its structure versus that presented in these documents. These should be functionally equivalent and are done to improve readability of the documentation.

In the schema some properties reference utility sub-schemas that only operate as constraints, i.e. they are a pattern property or have min/max. In these cases the Property column is omitted for clarity.

## root
The root of the schema definition is here [root](./core/root.md).
