# Best Practices

# Structuring schemas

The ontology provides an overriding data model, with a set of entities and the relationships that bind them together. However for practical purposes this model needs to be serialized, generally as either JSON or XML. The following document describes a set of best practices and guidelines when designing application or class specific schemas.



An object within a JSON document is composed of keys, each with a corresponding value ``<key>: <value>``

```
{
	"Slate": {
		"SlateUID":  "1234",
		"shootDay": 4
	}
}
```

The keys are always strings, the values can be a objects, arrays, or primitives such as strings, numbers or Booleans.

The following schema provides a set of conventions and definitions for building data representations using JSON. Schemas can be constructed from a set of components that can assembled together in a variety of ways to suit particular needs.



## Naming Conventions

**Ambiguous naming**
Avoid the use of names that can be ambiguous or apply to multiple types, key names like ‘date’ or ‘id’ should encode a specific reference to their type in the name ‘creationDate’, ‘distributionId’, etc.

** Identifiers that are part of an existing class (person) could be called ‘id’ or ‘identifier’?

**Plurals**
We should discuss, but this is my position.
** Avoid the use of plurals, it creates inconsistencies in naming i.e. parties vs dates vs classes.
** In the event a field name that initially only has a single entry is later updated to allow for multiple entries the field name itself should also be modified to reflect this, which potentially introduces a potential breaking change to people parsing the data.

**Capitalization**
** Should key names be capitalized or not, convention for XML but not JSON

Standardizing here between lower-cased first letter for JSON and upper-cased first letter for XML would also be acceptable in that it gives an easy conversion between the two if required.

**Punctuation**
Punctuation should be avoided in all naming, do not use hyphens, spaces, underscores, etc. Some database systems require these to be escaped and there is variability across systems in how punctuation is treated as well as how it is sometime represent on screen.

Avoid the use of additional symbols prepended or appended to names. For example, it is not uncommon to see $ prepended in JSON schemas ($id). However what is convention in one system rarely translates to other forms of serialization or databases.

**Reserved words**
A list of reserved keywords that define commonly recurring attribute types

    value
    attribute [attributes]
    language
    country
    date
    year
    name
    address
    type
    category [categories]: What is the universe of things this belongs in



Attributes as set of key value pairs, similar to XML


    {
      <valueName>: {
        "value": <value>,
        "attributes": {
          <attributeName1>: <value>,
          <attributeName2>: <value>,
        }
      }
    }



**Multiple Values**

If a property only has single value it may be represented with a single value or an array. Where multiple values then an array must be used.

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




**Typed Values**
For values that also require a type, the type should be explicitly stated in the declaration

// Preferred
Object with explicit type and value (XML would use attributes)

    "date": {
      "type": "creation",
      "value": "7/20/2020"
    }  


// Acceptable
Named key values

    "creationDate": "7/20/2020",
    "releaseDate": "7/20/2020"

// Bad

    "date": "7/20/2020"







## Definitions

Classes

Entities

Elements

Components

Properties: These represent a concept, idea or thing. It is defined by specific semantics and appears in the schema as name, key, tag or label for a field.

Type: A property has an assigned type which defines it's structure and provide clear semantics

Attributes: The values ascribed to a property when it is instantiated



Fields

Complex types

Literals





NEIM JSON LD/RDF/XML/Normalized

https://niem.github.io/NIEM-JSON-Spec/v5.0/niem-json-spec.html

https://github.com/NIEM/NIEM-JSON-Spec/wiki/NIEM-JSON-normalization

NEIM JSON Spec

https://github.com/NIEM/NIEM-JSON-Spec



## Versioning

The schema allows for versioning at several levels

JSON Schema: Defines the version number of the JSON schema specification

