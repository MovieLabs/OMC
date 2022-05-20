# Best Practices

***[these are practices we follow, rather than practices people using the schema need, i think. i guess if they ad extension they should follow these, but maybe this should be renamed as 'Schema Practices' or some such]***

***[some of this overlaps with th e'covnetions' seciton of th eintroductory document, and we shoudl decide where they go]***

## Schema Construction

### **Ambiguous naming**

Generally ambiguous naming of properties is avoided. Certain terms can often be relevant in many different situations or uses, for example, lots of things have a 'name'. In large schema we feel it is important to be able to differentiate and explicitly identify what an attribute is describing.

To that end properties are generally named unambiguously. For example, even though dates will all share the same format their property name will describe the context of their use, createdOn, birthDate, shootDate, etc.

The exception to this is when a property is not intrinsic to the entity. We **sometimes** include a 'name' property that is used primarily to help humans identify it. For example, an asset may be given an arbitrary name and description.

***[for such properties, is it 'sometimes, 'usually, or 'always'?]***

### **Plurals**

***Avoid the use of plurals. [rephrase to 'We avoid the use of plurals', i think]'***

- It creates inconsistencies in naming, i.e. parties vs dates vs classes (ies, s, es). This can be hard for some people to remember, especially those for whom English is not a first language.

- If plurals are used to indicate a property can have multiple values, it is then becomes inconsistent if it only has one. Or if there is an update to a schema that takes an attribute that was singular to allow multiple values, the renaming would break the schema.

### **Capitalization**

Properties are named using either camel case or upper camel case. This is the practice of not including spaces or punctuation in property names, but using capital letters to differentiate words.

Entities are named used upper camel case, regular properties camel case (first letter is lower case).

##### Examples of entity naming:

NarrativeProp, Shot, StructuralCharacteristics

##### Examples of property naming:

characterName, shootDay, identifier

### **Punctuation**

Punctuation should be avoided in all attribute terms, do not use hyphens, spaces, underscores, etc.. Some systems require these to be escaped or removed and there is variability across systems in how punctuation is treated as well as how it is sometimes represent ed on screen.

Avoid the use of additional symbols prepended or appended to names. For example, it is not uncommon to see $ prepended in JSON schemas ($id). However what is convention in one system rarely translates to other forms of serialization or databases. JSON schema itself uses this convention, this helps avoids any confusion between a the schema itself and the schema definition.

### **Multiple Values**

If a property only has single value it may be represented with a single value or an array. Where multiple values then an array must be used.

##### Example 1:

Identifier is always an array, even if there is just one value. It saves having to check its type every time it parsed.

```json
"identifer": [{
	"identifierScope": "Movielabs",
    "identifierValue": "1234"
}]
```




### Required vs Non-Required fields
With the exception of required fields the inclusion or exclusion of any given field in an instance is optional.

Given that the inclusion of most properties are optional this can create some potential problems when parsing the data. Different languages will behave differently if they attempt to access non-existent property keys. It is therefore the responsibility of the party parsing the data to catch and handle an errors related to this.

It should be noted that the absence of property does not mean that there is no attribute associated with it. It may just mean the sending party choose not to include it, or a requesting party choose not to request it. 

We therefore consider it a best practice to include a 'null' value if you wish to specifically communicate the absence of a properties attribute



## Extending the schema

Extensions and modifications to the schema can create compatibility problems, see [schema versioning](./Schema-Version.md). The goal therefore is to be able to extend without breaking changes.

To this end the JSON property of 'additionalProperties' is generally left in its default state of true. This means that if properties are added to a schema at a later date, validation will still pass for an instance that is validated with an older schema. Setting this value to false, would cause validation to fail if any additional properties were present.

This does mean that anyone adding their own properties is at risk of later conflicts if a schema introduces a property with the same name. We therefore do not recommend doing this in production environments.

To allow for bespoke extensions we include the 'extension' property. Individual applications can include any data as the attribute. It is up to the sending and receiving parties to know how to interpret this field. We also recommend that some sort of identifying property name is used, just as an additional safeguard against collisions.

This field can be useful for including additional metadata directly in a payload, for example additional fields from EXIF data in the Structural Characteristics of an image Asset. In this case you might encode it in the following manner:

```
"extension": {
	"exif": "<data>"
}
```

The data itself could be more JSON, some other serialized format, or even something encoded in base64.












