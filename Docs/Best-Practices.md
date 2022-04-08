# Best Practices



## Naming Conventions

**Ambiguous naming**

Generally ambiguous naming of attributes is be avoided. Certain terms can often be relevant in many different situations or uses, for example, lots of things have a 'name'. In large schema we feel it is important to be able to differentiate and explicitly identify what an attribute is describing.

Therefore the functional use of an attributes term should be encoded as part of the term, for example terms like 'date' or 'name' should be named birthDate or firstName.

The exception to this where an entity may include an arbitrary attribute, such as 'name', used primarily to help humans identify it. For example, an asset may be given an arbitrary name and description.

**Plurals**

Avoid the use of plurals.

- It creates inconsistencies in naming, i.e. parties vs dates vs classes (ies, s, es). This can be hard for some people, especially those for whom English is not a first language to remember.

- If plurals are used to indicate an attribute can have multiple values, it is then inconsistent if it only has one. Or if there is an update to a schema that takes an attribute that was singular to allow multiple values, the renaming would break the schema.

**Capitalization**

Capital letters for classes, lower case for properties.



** camel case



**Punctuation**
Punctuation should be avoided in all attribute terms, do not use hyphens, spaces, underscores, etc.. Some systems require these to be escaped or removed and there is variability across systems in how punctuation is treated as well as how it is sometimes represent ed on screen.

Avoid the use of additional symbols prepended or appended to names. For example, it is not uncommon to see $ prepended in JSON schemas ($id). However what is convention in one system rarely translates to other forms of serialization or databases. JSON schema itself uses this convention, this helps avoids any confusion between a the schema itself and the schema definition.





**Multiple Values**

If a property only has single value it may be represented with a single value or an array. Where multiple values then an array must be used.

 ** Convention is to use arrays where multiple values are likely

```json
"Identifer": {
	"id": "1234"
}
```



```
"Identifier": [
    {
        "id": "1234"
    },
    {"id": "5678"}
]


```





**Key Value Pairs**
Should use typed definition where applicable

// Preferred

    "creationDate": $ref Date

** This makes the use of non-ambiguous naming more important as a best practice



    {
      "participants": [
         {
          "type": "role",
          "value": "Editor
         },
        {
          "type": "organization",
          "value": "Super Duper Effects"
        }
      ]
    }

** This can work better when dealing with an array of things, such as people attached to a particular parts.


// Acceptable

    "creationDate": "string"


## Required vs Non-Required fields
With the exception of required fields the inclusion or exclusion of any given field in an instance is optional.





## Definitions

| Term     | Definition                                                   |
| -------- | ------------------------------------------------------------ |
| Entity   | A collection of Properties that together describe a fundamental building block of the model. Each instance of an Entity must have a unique Identifier that allows it to be related to other Entities. An Entity is typically analogous with one of the RDF classes in the ontology, or a complex type in GraphQL. |
| Property | Properties are <key><value> pairs that collectively create the structure and characteristics of an Entity. The value of a Property can be scalar type (string, number) or complex types (objects, arrays) or and Entity |
|          |                                                              |

Type: A property has an assigned type which defines it's structure and provide clear semantics



** Some examples for the above.









NEIM JSON LD/RDF/XML/Normalized

https://niem.github.io/NIEM-JSON-Spec/v5.0/niem-json-spec.html

https://github.com/NIEM/NIEM-JSON-Spec/wiki/NIEM-JSON-normalization

NEIM JSON Spec

https://github.com/NIEM/NIEM-JSON-Spec



