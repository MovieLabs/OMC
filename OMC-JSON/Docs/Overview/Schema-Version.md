# Schema Versioning

In this section we address only the issues related to the versioning of the schema. The versioning of actual assets used in the production are addressed separately as that is specific to individual production workflows,  different types of assets, and so on. For more information see here: [Versions](../Tech-Notes/Versions.md)

## JSON Schema Version
The version of schema specification that this schema is using. This will be a version of JSON Schema. Currently we are using draft 7, specified here:

```
"$schema": "http://json-schema.org/draft-07/schema#",
```

*Note: A topic for consideration by the working group is to migrate to using JSON-Schema 2020-12. There is some additional functionality through extra keywords, and there is more formalized mechanism for bundling schemas (which would be useful). However there does seem to be less support in some of the tooling for 2020-12 over JSON-7*

## OMC Schema Version
Schema's present some specific considerations when dealing with schema advancement, as certain advancements can break validation, but still maintain compatibility with historical data.

The nature of OMC as set of independent, related entities, in a potentially widely distributed system requires that each entity express which version of the schema was used to encode it. It can be expected that systems are routinely managing and parsing entities created at different times with different versions of the schema. It is not practical to expect all systems to migrate simultaneously when an update is released.

When considering compatibilities between schema versions there is a difference between whether a change affects the validation step or whether it will impact parsing historical data. Adding a new property would cause a validation error if data created using a later version of the schema were validated with a previous version. However, data created with historical a schema can still be read and parsed with a new schema.

For those familiar with JSON-Schema we have taken the decision to generally set the ``additionalProperties`` directive to ``false``, this will have the effect of causing a validation error if property names are misspelled or custom fields are included. However, we feel this provides a level of discipline in ensuring payloads comply with the specification. For users who need to express information that is not covered in the ontology or schema we provide the ``customData`` property.

MovieLabs intends to version and carry out updates to the entire schema. This means that updates may only impact certain entities and not others, but will greatly simplify the management of versions.

**Major**
A major version update indicates that functionality has been added or removed that creates a breaking change with prior versions that will both impact both the validation of historical data and potentially the parsing of historical data not part of this major release.

Examples: Adding additional required fields, or changing the naming of existing properties or controlled vocabulary.

**Minor**
A minor update indicates that functionality has been added or updated, backward compatibility has been maintained with data, although some functionality may not be available. However attempts to validate data with a schema that is older than the schema used to create may result in a failure.

Example: A property can be deprecated, but not removed. Properties that are not required can be added.

### Schema Version
Each entity contains a required property ``schemaVersion``, that describes the schema used to encode that entity.

The version will take the form of a resolvable URL that can be used to retrieve the schema. For example ``https://movielabs.com/omc/json/schema/v1.0``.

It is worth noting that it is entirely possible entities, even in the same payload, could be encoded with a different version of the schema. The payload may have been constructed from data from multiple systems, or a database migration may not have been done.


### Implementation considerations:

**Parsing data**
The presumption is that on consuming some OMC-JSON this will need to be parsed and acted on by the receiving system. Although many entities share a set of common properties, each has a specific meaning and typically unique properties, therefore a system can be expected to need a parser of some sort to process each entity.

- With the exception of the limited set of required properties there should no expectation that the property will be in present in payload.
- The property field may be present, but set to ``null``.
- The parser for each entity will essentially be versioned to match the schema, i.e. it will be compatible with a specific schema major version, and prior minor versions.
- Parsers that encounter instances encoded with a later minor version may not be able to parse certain properties, because they were added later.
- Parsers that encounter instances encoded with an earlier minor version should be able to parse all the properties of the payload

**Validating data**
We consider it best practice to validate all data when it is produced and prior to sending to another party. In this case a specific version of the schema will be used and the ``schemaVersion`` property should be set to reflect this.

- If validating data on ingest, a schema with the same major version and at least the same as or greater than than the version declared in the instance should be used. Otherwise results can not be guarantied.



[Introducing SchemaVer for semantic versioning of schemas](https://snowplowanalytics.com/blog/2014/05/13/introducing-schemaver-for-semantic-versioning-of-schemas/)

