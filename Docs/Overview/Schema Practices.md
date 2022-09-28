# Schema Practices

## Schema Construction

### **Ambiguous naming**
We generally avoid ambiguous naming of properties.

Certain terms are often relevant in many different situations or uses, e.g. ``type, value``. In a large schema we feel it is important to be able to differentiate the 'type' or 'value' of what and explicitly identify what an attribute is describing.

To that end properties are generally named unambiguously. For example, even though dates share the same format their property name will describe the context of their use, ``createdOn, birthDate, shootDate``, etc.

The exception to this is when a property is not intrinsic to the entity. For example, many entities include ``name`` and ``description`` properties; these are used primarily to help humans identify the entity, and UI construction is simple if those two are common across all entities..

### **Plurals**
We avoid the use of plurals.

- It can create inconsistencies in naming, i.e. parties vs dates vs classes (ies, s, es). This can be hard for some people to remember, especially those for whom English is not a first language.
- When plurals are used to indicate a property can have multiple values, it can lead to confusion when there is only one. It can also complicate parsing of the data as it may not always be clear whether something should be in an array or not.
- If a schema is updated and a property that was originally singular is changed to allow multiple values, renaming is potentially  a breaking change.

### **Capitalization**
Properties are named using either camel case or upper camel case.

Camel case is the practice of not including spaces or punctuation in property names, but using capital letters to differentiate words.

The core entities themselves are named using upper camel case; Regular properties use the lower camel case (first letter is lower case).

Examples of entity naming (upper camel case)  Most uses of this (and all of the example given) represent top-level class definitions in the formal definition of OMC:
``NarrativeProp, Shot, Character``

Examples of property naming (lower camel case):
``characterName, shootDay, identifier``

### **Punctuation**
We avoid punctuation in all attribute terms and do not use hyphens, spaces, underscores, etc.. Some systems require these to be escaped or removed and there is variability across systems in how punctuation is treated as well as how it is sometimes represented on screen.

Avoid the use of additional symbols prepended or appended to names. For example, it is not uncommon to see $ prepended in JSON schemas ($id). However what is convention in one system rarely translates to other forms of serialization or databases. JSON schema itself uses this convention, which helps avoid confusion between the schema itself and the schema definition.

### **Multiple Values**
Where a property can contain a set of values the schema will specify an array, even if only a single value is present.

This helps simplify parsing the payload. Code can be written to expect that a value is iterable even when it contains a single value, allowing easy use of looping constructs.

For example, the commonly used identifier property is always an array, even if there is just one value.
```json
{
  "identifer": [
    {
      "identifierScope": "Movielabs",
      "identifierValue": "1234"
    }
  ]
}
```


### Required vs Non-Required fields
There is limited use of required properties, to allow for flexibility,

At this point we have adopted a philosophy of placing limited restraints on the use, inclusion and naming of properties. We are mindful that a schema with rigid constraints may be a barrier to adoption if someone feels they need to include some specific attribute that is not in the schema. In JSON schema the inclusion of additional properties is the default setting and instances will pass validation. The downside of this is that validation becomes weaker - if someone misspells a property 'filename', instead of 'fileName', it would still pass validation, but the receiving party would not parse the value correctly.

In addition, different languages will behave differently if they attempt to access non-existent properties. It is therefore the responsibility of the party parsing the data to catch and handle errors related to absent properties in the object.

It should be noted that the absence of a property does not mean that there is no value associated with it. It may just mean the sending party choose not to include it, or the requesting party did not explicitly request it. We therefore consider it good practice to set a property's value to ``null`` if you wish to specifically communicate the absence of a value.

## Extending the schema
Extensions and modifications to the schema can create compatibility problems; see [schema versioning](Schema-Version.md). The goal therefore is to be able to extend without introducing breaking changes.

To support this the JSON property of 'additionalProperties' is generally left in its default state of true. This means that if properties are added to a schema at a later date, validation will still pass for an instance that is validated with an older schema. Setting this value to false, would cause validation to fail if any additional properties were present.

This does mean that anyone adding their own properties is at risk of later conflicts if a schema introduces a property with the same name. We therefore do not recommend doing this in production environments.

To allow for bespoke extensions we include the ``customData`` property. Individual applications can include any data as a value for this. It is up to the sending and receiving parties to know how to interpret this field. We recommend that some sort of identifying key or namespace is used as an additional safeguard against collisions.

Custom data can be useful for including additional metadata directly in a payload. For example you may want to include additional fields from EXIF data as part of the structural characteristics of an image. In this case you might encode it like this:

```
"customData": {
	"exif": "<data>"
}
```

The data itself does not need to be JSON; other serialized formats could be used or something like base64 encoding.

This same mechanism works for application-specific custom data.

`"customData": {`
	`"PopularApplication": "<data>"`
`}`












