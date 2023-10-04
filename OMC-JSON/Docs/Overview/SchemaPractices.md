# Schema Practices

In developing OMC-JSON we have made certain decisions about the structure and way certain things are expressed. Some of these are well trod discussions in the computer science field and some can invoke passionately held positions. Here we outline what our decisions were and the reasoning behind them.

## Property Naming

**Ambiguous naming**

We generally avoid ambiguous naming of properties.

Some commonly used terms are often relevant in many different situations or uses, e.g. terms like `type` or `value`. In a large schema we feel it is important to be able to differentiate what 'type' or 'value' and explicitly identify what a property is describing.

To that end, properties are generally named unambiguously. For example, even though dates share the same format their property name describes the context of their use, `createdOn, birthDate, shootDate`, etc.

The exception to this is when a property does not describe a canonical value. For example, most entities include a `name` and `description` properties; these are provided primarily to help humans identify the entity, they provide a consistent property name that can be used to store information that something like a user interface could use.

**Capitalization**

Properties are named using either camelCase (lower case first letter) or PascalCase (capitalized first letter). Camel case and Pascal case do not include spaces or punctuation in property names and use capital letters to differentiate words. In ‘camelCase’, the first word is not capitalized, and in ‘PascalCase’, the first word is capitalized, OMC-JSON uses the two conventions in specific circumstances.

Entities are named using Pascal case. Most uses of this (and all of the examples given) represent top-level class definitions in OMC-RDF. For example, `NarrativeObject`, `Shot`, `Character`

The properties of an entity use the following conventions:

- Properties that refer to another entity carry either a reference to that entity or embed some subset of its properties. The property name uses pascal case to indicate it is a reference. (`Context`, `Location`, `Depiction`).
- Properties that have a complex or primitive value (rather than a reference) are camel case. (`characterName`, `shootDay`, `identifier`)

**Punctuation**

We avoid punctuation in all property names and do not use hyphens, spaces, underscores, etc. Some systems require these to be escaped or removed and there is variability across systems in how punctuation is treated and sometimes how it is represented on screen. They can create extra work in URLs, where they need to be URL encoded and receiving parties must know to decode those URLs before use.

OMC-JSON does not use additional symbols prepended or appended to names. For example, it is not uncommon to see $ prepended in JSON schemas ($id). However, what is convention in one system rarely translates to other forms of serialization or database implementations.

**Plurals**

We avoid the use of plurals.

- It can create inconsistencies in naming, i.e., parties vs dates vs classes (ies, s, es). This can be hard for some people to remember.
- When plurals are used to indicate that a property can have multiple values, it can lead to confusion when there is only one. It can also complicate parsing of the data as it may not always be clear whether something should be in an array or not.
- If a schema is updated and a property that was originally singular is changed to allow multiple values, it would be a breaking change.

**Multiple Values**

Where a property can contain multiple values, the schema specifies an array, even when only a single value is present. Where a property should only ever contain a single instance, an object is used.

This practice helps simplify parsing the payload. A parser can be written to expect that a value is iterable even when it contains a single value, creating less need to type check everything.

For example, the commonly used identifier property is always an array, even if there is just one value.
```JSON
{
    "identifer": [{
        "identifierScope": "Movielabs",
        "identifierValue": "1234"
    }]
}
```

## Required vs Non-Required fields
There is limited use of required properties, to allow for flexibility. We allow applications to decide which properties of any given entity are relevant for their use case.

Different languages will behave differently if they attempt to access non-existent properties. It is therefore the responsibility of the consumer parsing the payload to catch and handle errors related to absent properties in the object.

It should be noted that the absence of a property does not mean that there is no value associated with it at all. It may just mean the producing party chose not to include it, or the requesting party did not explicitly request it.

We therefore consider it a good practice to set a property's value to `null`, if you wish to specifically communicate the absence of a value, the schema allows most properties to be set to null and is preferable to ambiguous values like “”, or 0 (unless you actually mean zero).

With the exception of identifier, arrays may be empty.

## Extending OMC-JSON
Extensions and modifications to OMC-JSON can create compatibility problems; see [Schema Versioning](./SchemaVersioning.md). The OMC-JSON schema generally sets the JSON-Schema keyword `additionalProperties` to ``false``, ensuring misspellings or custom properties will be rejected on validation.

This provides a level of safety in that only properties that have been described in the spec are included as part of the core payload. It also allows for new properties to be added and historical data to still be valid with versions equal to or greater than the version they were created with.

To allow for proprietary data or extensions we include the `customData` property. Individual applications can include any data as a value for this. It is up to the sending and receiving parties to know how to interpret this field. We recommend that some sort of identifying key or namespace is used as an additional safeguard against collisions.

The `customData` property can be useful for including additional metadata directly in a payload. For example, to include additional fields from an EXIF file as part of the structural characteristics of an image. In this case you might encode it like this:

```JSON
{
  "customData": {
    "exif": {
      "fieldName": <data>
    }
  }
}
```

The custom data itself does not need to be JSON; other serialized formats could be used, for example base64 or XML represented as a String.

This same mechanism works for application-specific custom data.
```JSON
{
    "customData": {
        "applicationName": <base64>
    }
}
```
