# Schema Versioning

In this section we address issues related to the versioning of the schema itself. The versioning of Assets used in the production is addressed in a separate section. For more information see here: [OMC Versions](https://mc.movielabs.com/docs/ontology/assets/versions/introduction/)

## JSON-Schema Version

JSON-Schema itself is versioned, so any validator will need to know which version of the official JSON schema the OMC-JSON conforms to. This version is specified at the start of the schema and is currently draft-2019-09.


    "$schema": "https://json-schema.org/draft/2019-09/schema",


## OMC-JSON Schema Version

OMC-JSON schemas present some specific considerations when dealing with schema advancement, as certain changes can break validation but still maintain compatibility with historical data.

OMC is structured as a set of independent entities that are related to one another. This makes each instance of an entity an atomic unit that may be exchanged alone or with other entities in a larger payload. In a distributed system, there is no guarantee that all the sub-systems are using the same schema version, or that older historical data is not still in active use. Therefore, each entity must express which version of the schema was used to encode it. Systems consuming OMC-JSON can then either validate or parse an entity with the correct schema.

When considering compatibilities between schema versions, there is a difference between whether a change affects validation or whether it will impact parsing of the data. If a schema advancement adds a new property, a payload that utilizes that property would not validate against an older version. However, data created with an historical schema can still be read and parsed with a newer schema (e.g., where only the minor version has incremented).

We have decided to generally set the JSON-Schema `additionalProperties` directive to `false`. This will have the effect of causing a validation error if property names are misspelled or custom fields are included. This ensures payloads comply with the specification. For users who want to express information that is not covered by the ontology or schema, the `customData` property is provided, where any valid JSON may be used.

The schema as a whole carries a single version number which will apply to each sub-schema as well. The single version tracking simplifies the version management.

Although a single version number is used, we require each entity (as opposed to the JSON object as a whole) convey the version when defining a JSON instance. This will allow downstream consumers to use appropriate parsers at the entity level.

**Schema Version number**
Each entity contains a required property `schemaVersion`, that describes the schema used for that entity.

The `schemaVersion` is a resolvable URL that can be used to retrieve the schema. For example: `[https://movielabs.com/omc/json/schema/v2.0](https://movielabs.com/omc/json/schema/v2.0)`. We will use a 2-digit numbering system to indicate the specific version.

**Major**
An increase in a major version indicates that functionality has been added or removed that creates a breaking change with prior versions that will impact both the validation and parsing of historical data.

Examples: Adding additional required fields or changing the names of existing properties or controlled vocabulary.

**Minor**
An increase in the minor version indicates that functionality has been added or updated. Backward compatibility is maintained for historical data. However, attempts to validate data with a schema that is older than the schema used to create that data may result in a failure.

Example: A property can be deprecated, but not removed. Properties that are not required can be added.



## Implementation considerations

**Validating data**
We consider it best practice to validate all data when it is produced and prior to sending to consuming party. In this case, a specific version of the schema will be used when encoding and validating the entity and the `schemaVersion` property should be set to reflect this.

When consuming data it may be validated against a schema prior to parsing the payload. A schema with the same major version and at least the same as or greater minor version declared in the `schemaVersion` property of the instance should be used. Otherwise, validation results cannot be guaranteed.

*Note: It may not be possible to validate an entire document against a single schema, for example if a v3.x entity embeds a v2.x entity.*

**Parsing data**
The presumption is that clients consuming OMC-JSON will need to parse a payload to act on it appropriately, for example by mapping its property values to an internal data model. Although many entities share a set of common properties, each has specific meaning and typically unique properties. Therefore, the consumer should be expected to need a separate means to parse each entity type.


- With the exception of the limited set of required properties, there is no expectation that any specific property will be in present in payload.
- A property key may be present and set to `null`.
- A property that is an array, may have an empty array.
- Generally, the parser for each entity will be versioned to match a schema version:
    - For entities encoded with the same major and lower minor version, the parser should be successful, but it is possible expected properties are not present.
    - For entities encoded with the same major and higher minor version, properties may be present in the payload the parser is not familiar with.
    - For entities encoded with a different major version, the parsing results could be unpredictable.


